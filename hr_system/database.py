from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 設定資料庫 URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 創建資料庫引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# 建立 SessionLocal，作為資料庫會話工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 定義 Base 類別，所有 ORM 模型都要繼承這個類別
Base = declarative_base()
