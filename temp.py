# import mysql.connector

# # เชื่อมต่อฐานข้อมูล MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="your_database"
# )

# cursor = conn.cursor()

# # คำสั่ง LOAD DATA INFILE
# load_query = """
#     LOAD DATA INFILE 'C:/path/to/your/file.csv'
#     INTO TABLE your_table
#     FIELDS TERMINATED BY ',' 
#     ENCLOSED BY '"'
#     LINES TERMINATED BY '\n'
#     IGNORE 1 ROWS;
# """

# # รันคำสั่ง
# cursor.execute(load_query)
# conn.commit()

# # ปิดการเชื่อมต่อ
# cursor.close()
# conn.close()
