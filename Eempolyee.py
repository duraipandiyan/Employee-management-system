import sqlite3
class database:
    def __init__(self,db):
      try:
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        sql=""" create table Employee(id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age VARCHAR(100) NOT NULL,
        address VARCHAR(100) NOT NULL,
        DOB VARCHAR(100) NOT NULL,
        gender VARCHAR(100) NOT NULL,
        contact VARCHAR(100) NOT NULL,
        mail_id VARCHAR(100) NOT NULL);"""

        self.cur.execute(sql)
        self.con.commit()
      except Exception as e:
          print(e)

    def insert(self,id,name,age,address,DOB,gender,contact,mail_id):
        try:
            sql=""" insert into Employee values(?,?,?,?,?,?,?,?)"""
            self.cur.execute(sql,(id,name,age,address,DOB,gender,contact,mail_id))
            self.con.commit()
        except Exception as e:
            print(e)

        else:
            print("sucess")
    def fetch(self):
        try:
            sql="""select * from Employee;"""
            self.cur.execute(sql)
            data=self.cur.fetchall()
            return data
        except Exception as e:
            print(e)
        else:
           print("sucessfully")


    def update(self,id,name,age,address,DOB,gender,contact,mail_id):
     try:
        sql=""" update Employee
        set name=?,
        age=?,
        address=?,
        DOB=?,
        contact=?,
        gender=?,
        mail_id=?
        where id=?;
        """

        self.cur.execute(sql,(name,age,address,DOB,gender,contact,mail_id,id))
        self.con.commit()

     except Exception as e:
         print(e)
     else:
        print("vectory")

    def delete(self,id):
      try:
        sql="""delete from Employee
        where id=?
        """
        self.cur.execute(sql,(id,))
        self.con.commit()
      except Exception as e:
          print(e)

      else:
          print("record deleted")

#obj=create("student1.db")
#obj.insert(104,"praveen",19,"tirvl",8798567483,"python","praveen@gmail.com")
#obj.fetch()
#obj.update()
#obj.delete()