# crud.py

from sqlalchemy.orm import Session
import models, schemas

# 獲取所有員工（改為回傳整個 ORM 對象）
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EmployeeORM).offset(skip).limit(limit).all()

# 獲取某位員工的資料（同樣改為整個 ORM 對象）
def get_employee(db: Session, employee_id: int):
    return db.query(models.EmployeeORM).filter(models.EmployeeORM.id == employee_id).first()

# 創建新員工
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.EmployeeORM(
        name=employee.name,
        department=employee.department,
        position=employee.position,
        phone=employee.phone,
        email=employee.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# 更新員工資料
def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.EmployeeORM).filter(models.EmployeeORM.id == employee_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.department = employee.department
        db_employee.position = employee.position
        db_employee.phone = employee.phone
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee

# 刪除員工
def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.EmployeeORM).filter(models.EmployeeORM.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
