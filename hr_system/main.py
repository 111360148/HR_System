from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import pandas as pd
from io import BytesIO
import io

app = FastAPI()

# 確保資料表創建
models.Base.metadata.create_all(bind=engine)

# 設定資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 靜態文件夾設定，提供 HTML 檔案和其他靜態資源
app.mount("/static", StaticFiles(directory="static"), name="static")

# 讀取根目錄，提供 index.html 頁面
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, status_code=200)

# 取得所有員工資料，支持分頁
@app.get("/employees", response_model=list[schemas.Employee])
def read_employees(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

# 取得單個員工資料
@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# 新增員工資料
@app.post("/employees", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

# 更新員工資料
@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# 刪除員工資料
@app.delete("/employees/{employee_id}", response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

from fastapi import Form

# 批量上傳員工資料，處理 Excel 檔案
@app.post("/upload_excel")
async def upload_excel(
    file: UploadFile = File(...),
    mode: str = Form("add"),  # 新增一個 mode 欄位：add 或 overwrite
    db: Session = Depends(get_db)
):
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
        raise HTTPException(status_code=400, detail="只接受 Excel 檔案（.xlsx 或 .xls）")

    contents = await file.read()
    df = pd.read_excel(BytesIO(contents), engine="openpyxl")

    for _, row in df.iterrows():
        # 讀取欄位
        name = row['姓名']
        department = row['部門']
        position = row['職稱']
        phone = row['電話']
        email = row['電子郵件']

        if mode == "overwrite":
            # 1. 清空資料庫現有員工資料
            db.query(models.EmployeeORM).delete()
            db.commit()

            # 2. 將 Excel 裡的資料全部新增
            for _, row in df.iterrows():
                name = row['姓名']
                department = row['部門']
                position = row['職稱']
                phone = row['電話']
                email = str(row['電子郵件']).strip().lower()

                new_emp = models.EmployeeORM(
                    name=name,
                    department=department,
                    position=position,
                    phone=phone,
                    email=email
                )
                db.add(new_emp)

            db.commit()

        else:
            # 僅新增，不判斷重複
            employee = schemas.EmployeeCreate(
                name=name,
                department=department,
                position=position,
                phone=phone,
                email=email
            )
            crud.create_employee(db=db, employee=employee)

    db.commit()
    return {"message": f"Excel 上傳完成（模式：{mode}）"}

@app.get("/backup_excel")
def backup_excel(db: Session = Depends(get_db)):
    employees = crud.get_all_employees(db)
    data = [{
        "姓名": emp.name,
        "部門": emp.department,
        "職稱": emp.position,
        "電話": emp.phone,
        "電子郵件": emp.email
    } for emp in employees]

    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename="employee_backup.xlsx"'}
    )