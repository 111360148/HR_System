from pydantic import BaseModel

# 共用欄位
class EmployeeBase(BaseModel):
    name: str
    department: str
    position: str
    phone: str
    email: str

# 用於創建時，不需要 id
class EmployeeCreate(EmployeeBase):
    pass

# 用於回傳資料時，需要有 id
class Employee(EmployeeBase):
    id: int  # ✅ 加上這一行

    class Config:
        from_attributes = True
