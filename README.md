# E-Commerce Data Analytics System

The **E-Commerce Data Analytics System** is a tool designed to analyze and manage data related to online sales. In this case, we have an e-commerce sales dataset from India. This system helps you easily understand customer behavior, sales trends, and product performance by analyzing data from these files.

> **Data Source** - [E-Commerce Data](https://www.kaggle.com/datasets/benroshan/ecommerce-data?select=Sales+target.csv)

## Getting Started

### Installing

Install the required Python packages:

```sh
pip install pandas
pip install mysql-connector-python
pip install prettytable
pip install matplotlib
```

### Executing program

1. Set up the database by running the [setting.py](setting.py) script:

```sh
python setting.py
```

2. Open the Jupyter notebook to start the application:

```sh
jupyter notebook app.ipynb
```

3. The main menu will appear, allowing you to choose the desired option:

   - **1. Customer Details** - View customer details
   - **2. Purchase History** - View purchase history
   - **3. Monthly Sales Reports** - View monthly sales reports
   - **4. Manage Items** - Manage product items
   - **5. Backup** - Backup data
   - **e. Exit** - Exit the program

4. Select the desired menu by typing the corresponding number or letter, then press Enter.

### Customer Details

In this menu, you can view detailed information about customers, including their contact information and purchase history.

### Purchase History

This option allows you to view the purchase history of customers, providing insights into their buying patterns and preferences.

### Monthly Sales Reports

View detailed sales reports on a monthly basis. This helps in tracking sales performance and identifying trends over time.

### Manage Items

In the **Manage Items** menu, you can manage product categories with the following options:

- **\[C\]reate** - Create a new category
- **\[U\]pdate** - Edit the category name
- **\[D\]elete** - Delete a category
- **\[Q\]uit** - Return to the main menu

### Backup

This option allows you to backup the database to prevent data loss. It is recommended to perform regular backups to ensure data safety.

##

This system helps you analyze customer behavior, track sales performance, and manage product categories effectively.
