# 使用官方 Python 映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔和程式碼
COPY requirements.txt .
COPY . .

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放 FastAPI 預設埠
EXPOSE 8000

# 啟動 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
