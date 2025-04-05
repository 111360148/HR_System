from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmployeeORM(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # 姓名
    department = Column(String)        # 部門
    position = Column(String)          # 職稱
    phone = Column(String)             # 電話
    email = Column(String)             # 電子郵件
