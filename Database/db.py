import mysql.connector


class Db:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="python",
            password="mesh7a2olek",
            database="python",
            auth_plugin='mysql_native_password'
        )
        self.cur = self.mydb.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee ( id int PRIMARY KEY, full_name VARCHAR(50), email VARCHAR(50),salary INT, is_manager VARCHAR(5) )")
        self.mydb.commit()


    def get_all_employees(self):
        self.cur.execute("select * from employee")
        records = self.cur.fetchall()
        return records

    def get_employee(self, id):
        sql = "select * from employee where id = %s"
        val = (id,)
        self.cur.execute(sql, val)
        records = self.cur.fetchall()
        return records
    def insert_employee(self, emp):
        sql = "INSERT INTO employee (full_name,id, email, salary, is_manager) VALUES (%s, %s, %s, %s,%s)"
        val = (emp.full_name, emp.id, emp.email,emp.salary, emp.is_manager)
        self.cur.execute(sql, val)
        self.mydb.commit()
    def delete_employee(self, id):
        sql = "DELETE FROM employee where id= %s "
        val = (id,)
        self.cur.execute(sql, val)
        self.mydb.commit()