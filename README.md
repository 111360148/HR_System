# 員工管理系統 (Employee Management System)

## 專案簡介
本系統為員工管理系統，使用者可以透過網頁介面進行：
- 查詢所有員工資料
- 新增、編輯、刪除員工資訊
- 上傳 Excel 匯入員工資料
- 下載 Excel 檔案，方便使用者一次性修改資料

## 技術歷程
- **前端**：HTML + Bootstrap
- **後端**：FastAPI (含 OpenAPI 文件)
- **資料庫**：SQLite
- **容器化**：Docker + Docker Compose

## 部署步驟

### 1. 將程式從 GitHub 克隆下來
```bash
git clone https://github.com/111360148/HR_System.git
cd HR_System
```

### 2. 使用 Docker Compose 啟動系統
```bash
docker-compose up --build
```

### 3. 開啟瀏覽器，訪問系統
- 前台網頁系統： http://localhost:8501
- FastAPI OpenAPI API 文件：http://localhost:8000/docs
