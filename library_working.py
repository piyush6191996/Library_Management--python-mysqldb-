import pymysql.cursors
import pymysql
import time


class Library:

    def main(self):
        print(""" Welcome to the library management system\n
        PRESS 1. IF YOU ARE A STUDENT
        PRESS 2. IF YOU ARE A TEACHER """)
        a = int(input("Enter Your Choice "))
        if a == 1:
            global key
            key = 1
            self.student()
        elif a == 2:
            global key
            key = 2
            self.teacher()
        else:
            print("\You submitted a wrong choice enter again")
            self.main()

    def student(self):
        a = int(input("Press 1 if you are registered and if you are not registered simply press 2\n"
                      "Press 3 to go back in the menu"))
        if a == 2:
            self.register_student()
        elif a == 3:
            self.main()
        elif a == 1:
            roll = int(input("Enter your roll no."))
            sql = cur.execute("SELECT roll_no FROM student_list WHERE roll_no = {0}".format(int(roll)))
            if sql:
                sql = "SELECT name FROM student_list WHERE roll_no = {0}".format(int(roll))
                cur.execute(sql)
                name = cur.fetchall()
                print("Hello %s" % name)
                global value
                value = roll
                self.student_manage()
            else:
                print("Your Student number not found, Please try again")
                self.student()
        else:
            print("it seems there was a mistake in your roll no.")
            again = int(input("""\n\n\nPress 1 to enter your roll no. again\nPress 2 to register yourself """))
            if again == 1:
                self.student()
            elif again == 2:
                self.register_student()
            else:
                print("Please Enter correct choice")
                self.student()

    def teacher(self):
        a = int(input("\n\nPress 1 if you are registered and if you are not registered then press 2\n"
                      "Press 3 to go back in the menu"))
        if a == 2:
            self.register_teacher()
        elif a == 3:
            self.main()
        elif a == 1:
            t_id = int(input("Enter your teacher ID"))
            sql = cur.execute("SELECT teacher_list.teacher_id FROM teacher_list WHERE teacher_id = {0}"
                              .format(int(t_id)))
            if sql:
                sql = "SELECT name FROM student_list WHERE teacher_id = {0}".format(int(t_id))
                cur.execute(sql)
                name = cur.fetchall()
                print("Hello %s" % name)
                global value
                value = t_id
                self.student_manage()
            else:
                print("Your teacher ID not found, Please try again")
                self.teacher()
        else:
            print("Please enter a valid choice")
            self.teacher()

    def register_student(self):
        print("Looks like you are not registered So please enter the following details")
        name = input("Enter Your Name")
        roll_no = int(input("Enter Your Roll no."))
        year = int(input("Enter your year"))
        branch = (input("Enter your branch"))
        issued_book_id = "abc"
        global cur
        cur = conn.cursor()
        cur.execute("insert into student_list(roll_no, name, branch, year, book_issued) "
                    "VALUES ('{0}','{1}','{2}','{3}','{4}')".format(int(roll_no), name, branch, int(year),
                                                                    issued_book_id))
        conn.commit()
        sql = "SELECT * FROM student_list"
        cur.execute(sql)
        results = cur.fetchall()
        for r in results:
            print(r)
        print("You are now registered")
        global value
        value = roll_no
        self.student_manage()

    def student_manage(self):
        print("HELLO, WELCOME TO THE STUDENT SIDE OF LIBRARY MANAGEMENT")
        b = int(input("Press 1 if you want to issue a book\n"
                      "Press 2 if you want to return a book\n"
                      "Press 3 to view your details"""
                      "Press 4 to go back in the menu"))
        if b == 1:
            self.issue(key, value)
        elif b == 3:
            self.student_details(value)
        elif b == 2:
            self.return_book(key, value)
        elif b == 4:
            self.student()
        else:
            print("Enter the correct choice")
            self.student_manage()

    def register_teacher(self):
        print("Looks like you are not registered SO enter the following details")
        name = input("Enter Your Name")
        teacher_id = int(input("Enter Your Teacher Id"))
        issued_book_id = ""
        global cur
        cur = conn.cursor()
        cur.execute("insert into teacher_list(teacher_id, name, book_issued) "
                    "VALUES ('{0}','{1}','{2}')".format(int(teacher_id), name, issued_book_id))
        conn.commit()
        sql = "SELECT * FROM teacher_list"
        cur.execute(sql)
        results = cur.fetchall()
        for r in results:
            print(r)
        print("You are now registered")
        global value
        value = teacher_id
        self.manage()

    def manage(self):
        print("HELLO, WELCOME TO THE TEACHER SIDE OF LIBRARY MANAGEMENT")
        a = int(input("""   PRESS 1 to add a book\n
        PRESS 2 to remove a book\n
        PRESS 3 to issue a book\n
        PRESS 4 to return a book\n
        PRESS 5 to view personal details\n
        PRESS 6 to go to back in menu"""))
        if a == 1:
            self.add()
        elif a == 2:
            self.remove()
        elif a == 3:
            self.issue(key, value)
        elif a == 4:
            self.return_book(key, value)
        elif a == 5:
            self.teacher_details(value)
        elif a == 6:
            self.teacher()
        else:
            print("Please enter correct choice")
            self.manage()

    def issue(self, key, value):
        a = 2
        global cur
        cur = conn.cursor()
        sql_book_list = "SELECT * FROM book_list"
        cur.execute(sql_book_list)
        results = cur.fetchall()
        for r in results:
            print(r)
        book_idd = input(print("Now Enter The ID of the book you want...."))
        sql_book_name = "SELECT * FROM book_list WHERE book_id = {0}".format(int(book_idd))
        cur.execute(sql_book_name)
        ##sql_book_name = cur.execute("SELECT * FROM book_list WHERE name = '{0}'".format(book_name))
        if sql_book_name:
            sql = "SELECT quantity FROM book_list WHERE book_id = {0}".format(int(book_idd))
            cur.execute(sql)
            quantity = cur.fetchall()
            if quantity >= 1:
                a = 1
                print("Book has been found, and is being added to your account")
                quantity -= 1
                sql = "UPDATE book_list SET quantity = {0} WHERE name = {1}".format(int(quantity), book_name)
                cur.execute(sql)
                conn.commit()
                if key == 1:
                    sql = "SELECT book_id FROM book_list WHERE name = {0}".format(book_name)
                    cur.execute(sql)
                    book_id = cur.fetchall()
                    sql = "UPDATE student_list SET book_issued = {0} WHERE roll_no = {1}".format(int(book_id), value)
                    cur.execute(sql)
                    conn.commit()
                if key == 2:
                    sql = "SELECT book_id FROM book_list WHERE name = {0}".format(book_name)
                    cur.execute(sql)
                    book_id = cur.fetchall()
                    sql = "UPDATE teacher_list SET book_issued = {0} WHERE roll_no = {1}".format(int(book_id), value)
                    cur.execute(sql)
                    conn.commit()
            else:
                b = input("Not enough quantity of book available\nPress 1 to select another book\n"
                          "Press 2 to go back in menu")
                if b == 1:
                    self.issue(key, value)
                if b == 2:
                    if key == 1:
                        self.student_manage()
                    if key == 2:
                        self.manage()
        if a == 2:
            b = input("Book not found \n Press 1 to try again \n or else press anything else to go to main menu")
            b = int(b)
            if b == 1:
                self.issue(key, value)
            else:
                self.manage()

    def add(self):
        name = input("Enter name of the book")
        author = input("Enter the name of the author")
        quantity = int(input("Enter quantity of this book"))
        book_id = int(input("Enter book ID"))
        global cur
        cur = conn.cursor()
        cur.execute("insert into book_list(book_id, name, author, quantity) "
                    "VALUES ('{0}','{1}','{2}','{3}')".format(int(book_id), name, author, int(quantity)))
        conn.commit()
        sql = "SELECT * FROM book_list"
        cur.execute(sql)
        results = cur.fetchall()
        for r in results:
            print(r)
        b = int(input("""You have successfully added a book
                         PRESS 1 to enter again
                         PRESS anything else to go to back to manage menu"""))
        if b == 1:
            self.add()
        else:
            self.manage()

    def remove(self):
        a = 2
        book_name = input("Now Enter The name of the book you want....")
        sql_book_name = cur.execute("SELECT name FROM book_list WHERE name = {0}".book_name)
        if sql_book_name:
            print("The Book has been found and now is being removed")
            global cur
            cur = conn.cursor()
            cur.execute("DELETE FROM book_list WHERE name = {0}".format(book_name))
            conn.commit()
            time.sleep(2)
            a = 1
            print("The Book has been removed successfully")
            self.manage()
        if a == 2:
            b = int(input("Book not found \n Press 1 to try again \n or else press anything else to go to main menu"))
            if b == 1:
                self.remove()
            else:
                self.manage()

    def return_book(self, key, value):
        a = 2

        book_name = input(print("Now Enter The name of the book you want to raturn...."))
        sql_book_name = cur.execute("SELECT name FROM book_list WHERE name = {0}".format(book_name))
        if sql_book_name:
            sql = "SELECT quantity FROM book_list WHERE name = {0}".format(book_name)
            cur.execute(sql)
            quantity = cur.fetchall()
            quantity += 1
            print("Book has been found, and is being removed from your account")
            sql = "UPDATE book_list SET quantity = {0} WHERE name = {1}".format(int(quantity), book_name)
            cur.execute(sql)
            conn.commit()
            if key == 1:
                sql = "UPDATE student_list SET book_issued = {0} WHERE roll_no = {1}".format("", value)
                cur.execute(sql)
                conn.commit()
                a = 1
                print("Book has been Successfully removed")
                self.student_manage()
            if key == 2:
                sql = "UPDATE teacher_list SET book_issued = {0} WHERE roll_no = {1}".format("", value)
                cur.execute(sql)
                conn.commit()
                a = 1
                print("Book has been Successfully removed")
                self.manage()
        if a == 2:
            c = int(input("book is not found,\n""Press 1 to try again\n Press anything to go back to the menu"))
            if c == 1:
                    self.return_book(key, value)
            else:
                if key == 1:
                    self.student_manage()
                else:
                    self.manage()

    def student_details(self, value):
        global cur
        cur = conn.cursor()
        sql_book_list = "SELECT * FROM student_list WHERE roll_no = {0}".format(value)
        cur.execute(sql_book_list)
        results = cur.fetchall()
        for r in results:
            print(r)
            self.student_manage()

        '''print("Your details are as following")
        l = len(student_list)
        for i in range(l):
            list = student_list[i]
            if value == list[0]:
                break
        print("Roll No. : %s" % list[0])
        print("Name     : %s" % list[1])
        print("Branch   : %s" % list[2])
        print("Year     : %s" % list[3])
        if list[4]:
            print("Any book issued  : Yes")
            print("Issued Book ID   : %s" % list[4])
        else:
            print("Any book issued  : No")
        self.student_manage()'''

    def teacher_details(self,value):
        global cur
        cur = conn.cursor()
        sql_book_list = "SELECT * FROM teacher_list WHERE roll_no = {0}".format(value)
        cur.execute(sql_book_list)
        results = cur.fetchall()
        for r in results:
            print(r)

        '''print("Your details are as follows")
        l = len(teacher_list)
        for i in range(l):
            list_t = teacher_list[i]
            if value == int(list_t[0]):
                break
        print("Teacher ID : %d" % value)
        print("Name       : %s" % list_t[1])
        if list_t[2]:
            print("Any book issued  : Yes")
            print("Issued Book ID   : %s" % list_t[2])
        else:
            print("Any book issued  : No")
        self.manage()'''

config = {
  'user': 'root',
  'port': 3306,
  'password': 'Piyush@1996',
  'host': 'localhost',
  'database': 'library_management',
  #'raise_on_warnings': True
}
global key
global value
student_list = []
teacher_list = []
book_list = []
conn = pymysql.connect(**config)
cur = conn.cursor()
library = Library()
library.main()
