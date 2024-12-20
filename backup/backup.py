import os
from datetime import datetime


def backup_db():
    while True:
        print("Do you want to backup database")
        print("\nOptions: [Y]es, [N]o")
        choice = input("Enter your choice: ").strip().lower()
        print()

        if choice == "y":
            current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"backup_{current_datetime}.txt"

            backup_folder = os.path.join(os.path.dirname(__file__), "myBackup")
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)
            backup_filepath = os.path.join(backup_folder, backup_filename)

            from db.get import fetch_data_from_db

            query = "SHOW TABLES"
            rows, columns = fetch_data_from_db(query)

            tables = [table[0] for table in rows]

            from db.conn import create_connection

            with create_connection() as conn:
                with conn.cursor() as cursor:
                    with open(backup_filepath, "w") as backup_file:

                        for table in tables:
                            cursor.execute(f"SHOW CREATE TABLE {table}")
                            create_table_query = cursor.fetchone()[1]
                            backup_file.write(f"-- Table: {table}\n")
                            backup_file.write(f"{create_table_query};\n\n")

                            query = f"SELECT * FROM {table}"
                            rows, columns = fetch_data_from_db(query)

                            for row in rows:
                                values = [
                                    str(value) if value is not None else "NULL"
                                    for value in row
                                ]
                                insert_query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                                backup_file.write(insert_query)

                            backup_file.write("\n\n")

            print(f"Backup saved to {backup_filename}")
            print()

            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break

        elif choice == "n":
            from adminMenu.admin_menu import adminMenu_display

            adminMenu_display()
            break

        else:
            print("Please try again.")
            print()
