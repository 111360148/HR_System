# 專案檔案結構
- code1.py：第一題反轉數字的程式碼。
- code2.py：第二題費氏數列的程式碼。
- hr_system 資料夾：員工管理系統的主程式。 


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
cd HR_System/hr_system
```

### 2. 使用 Docker Compose 啟動系統
```bash
docker-compose up --build
```

### 3. 開啟瀏覽器，訪問系統
- 前台網頁系統： http://127.0.0.1:8000
- FastAPI OpenAPI API 文件： http://127.0.0.1:8000/docs
