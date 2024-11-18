DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "ecommerce",
}

DB_NAME = DB_CONFIG["database"]
TABLES = {
    "Customers": """
        CREATE TABLE IF NOT EXISTS Customers (
            Customer_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            Customer_Name VARCHAR(100) NOT NULL,
            State VARCHAR(50) NOT NULL,
            City VARCHAR(50) NOT NULL
        )
    """,

    "Categories": """
        CREATE TABLE IF NOT EXISTS Categories (
            Category_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            Category_Name VARCHAR(100) NOT NULL
        )
    """,
    "SubCategories": """
        CREATE TABLE IF NOT EXISTS SubCategories (
            SubCategory_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            SubCategory_Name VARCHAR(100) NOT NULL,
            Category_ID VARCHAR(10) NOT NULL,
            FOREIGN KEY (Category_ID) REFERENCES Categories(Category_ID)
        )
    """,

    "Orders": """
        CREATE TABLE IF NOT EXISTS Orders (
            Order_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            Order_Date DATE NOT NULL,
            Customer_ID VARCHAR(10) NOT NULL,
            FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
        )
    """,
    "OrderDetails": """
        CREATE TABLE IF NOT EXISTS OrderDetails (
            Detail_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            Order_ID VARCHAR(10) NOT NULL,
            Amount DECIMAL(10, 2) NOT NULL,
            Profit DECIMAL(10, 2) NOT NULL,
            Quantity INT NOT NULL,
            SubCategory_ID VARCHAR(10) NOT NULL,
            FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
            FOREIGN KEY (SubCategory_ID) REFERENCES SubCategories(SubCategory_ID)
        )
    """,

    "SalesTargets": """
        CREATE TABLE IF NOT EXISTS SalesTargets (
            Target_ID VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
            MonthOfOrderDate DATE NOT NULL,
            Category_ID VARCHAR(10) NOT NULL,
            Target DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (Category_ID) REFERENCES Categories(Category_ID)
        )
    """,
}
