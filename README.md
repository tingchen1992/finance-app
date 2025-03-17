# 個人財務管理工具

這個專案是一個基於 Python 的簡單財務管理工具，使用 Flask 框架、SQLAlchemy 和 WTForms 實現。它可以讓使用者記錄日常的收入與支出，並且能夠按月分類顯示交易紀錄。

## 功能

- 記錄收入與支出
- 支援多種類別（例如：薪水、食物、交通等）
- 支援編輯與刪除交易紀錄
- 支援根據月份顯示交易紀錄

## 安裝與運行

### 步驟 1: 建立虛擬環境
首先，確保你的系統已經安裝了 Python 3.x 和 `pip`。
然後，創建並啟動一個虛擬環境：
`python3 -m venv venv`
`source venv/bin/activate`
# 如果是 Windows 系統，使用 venv\Scripts\activate

### 步驟 2: 安裝依賴
在虛擬環境中，安裝專案所需的依賴：
`pip install -r requirements.txt`

### 步驟 3: 設定資料庫
此專案使用 SQLAlchemy 作為 ORM 來管理資料庫。執行以下命令來建立資料庫：
`flask db init`
`flask db migrate`
`flask db upgrade`

### 步驟 4: 啟動應用程式
啟動 Flask 開發伺服器，進行本地測試：
`flask run`

可以通過瀏覽器訪問 http://127.0.0.1:5000


###如何使用

在首頁，你可以輸入並新增一筆收入或支出。
交易會顯示在表格中，包含類型、分類、金額和日期。
你可以選擇編輯或刪除已有的交易紀錄。
可以按月份來查看分類過的交易紀錄。

###主要技術

Flask: Web 框架
SQLAlchemy: ORM，用於處理資料庫
WTForms: 用於處理表單驗證
Bootstrap: 用於前端樣式
