class Library:

    def main(self):
        print(""" Welcome to the library management system\n
        PRESS 1. IF YOU ARE A STUDENT
        PRESS 2. IF YOU ARE A TEACHER """)
        a = input("Enter Your Choice ")
        a = int(a)
        if a == 1:
            self.student()
        elif a == 2:
            self.teacher()
        else:
            print("\You submitted a wrong choice enter again")
            self.main()

    def student(self):
        t=2
        a = input("Press 1 if you are registered and if you are not registered simply press 2")
        if a == "2":
            self.register_student()
        elif a=="1":
            roll = input("Enter your roll no.")
            l = len(student_list)
            for i in range(l):
                student = student_list[i]
                if roll == student[0]:
                    b = input("Press 1 if you want to issue a book\nPress anything else if you want to return a book")
                    b = int(b)
                    if b == 1:
                        self.issue()
                    else:
                        self.return_book()
                    break
        else:
            print("it seems there was a mistake in your roll no.")
            again = input("""\n\n\nPress 1 to enter your roll no. again\nPress 2 to register yourself """)
            again = int(again)
            if again == 1:
                self.student()
            elif agian == 2:
                self.register_student()
            else:
                print("Please Enter correct choice")
                self.student()

    def teacher(self):
        a = input("\n\nPress 1 if you are registered and if you are not registered then press 2")
        a = int(a)
        if a == 2:
            self.register_teacher()
        elif a == 1:
            t_id = input("Enter your teacher ID")
            l = len(teacher_list)
            for i in range(l):
                teacher = teacher_list[i]
                if t_id == teacher[0]:
                    b = input("\n\nPress 1 if you want to add a book\nPress 2 if you want to remove a book\nPress 3 if you want to issue a book \nPress 4 if you want to return a book\nPress 5 to go to main menu")
                    b = int(b)
                    if b == 1:
                        self.add()
                    elif b == 2:
                        self.remove()
                    elif b == 3:
                        self.issue()
                    elif b==4:
                        self.return_book()
                    elif b == 5:
                        self.main()
                    else:
                        print("Enter a valid choice")
                    break
        else:
            print("Please enter a valid choice")
            self.teacher()

    def register_student(self):
        current = []
        print("Looks like you are not registered SO enter the following details")
        name = input("Enter Your Name")
        roll_no = input("Enter Your Roll no.")
        current.append(roll_no)
        current.append(name)
        global student_list
        student_list.append(current)
        print("You are now registered")
        self.student()

    def register_teacher(self):
        current = []
        print("Looks like you are not registered SO enter the following details")
        name = input("Enter Your Name")
        teacher_id = input("Enter Your Teacher Id")
        current.append(teacher_id)
        current.append(name)
        teacher_list.append(current)
        print("You are now registered")
        self.teacher()

    def manage(self):
        a = input("""PRESS 1 to add a book\nPRESS 2 to remove a book\nPRESS 3 to issue a book\nPRESS 4 to return a book\nPRESS 5 to exit""")
        a = int(a)
        if a == 1:
            self.add()
        elif a == 2:
            self.remove()
        elif a == 3:
            self.issue()
        elif a == 4:
            self.return_book()
        elif a == 5:
            exit()
        else:
            print("Please enter correct choice")
            self.manage()

    def add(self):
        book = []
        name = input("Enter name of the book")
        author = input("Enter the name of the author")
        quantity = input("Enter quantity of this book")
        book_id = input("Enter book ID")
        book.append(book_id)
        book.append(name)
        book.append(author)
        book.append(quantity)
        book_list.append(book)
        b = input("""You have succesfully added a book
                         PRESS 1 to enter again
                         PRESS anything else to go to the main menu""")
        if b == 1:
            self.add()
        else:
            self.manage()

    def remove(self):
        a = 2
        z = len(book_list)
        book_id = input("Enter the ID of the book you want to delete")
        for i in range(z):
            book = book_list[i]
            if book[0] == book_id:
                book_list.remove(book)
                a = 1
                break
        if a == 2:
            b = input("Book not found \n Press 1 to try again \n or else press anything else to go to main menu")
            b = int(b)
            if b == 1:
                self.remove()
            else:
                self.manage()

    def issue(self):
        a = 2
        l = len(book_list)
        for i in range(l):
            print(book_list(i))
        name = input("Now enter the name of the book you want to issue")
        for i in range(l):
            book = book_list[i]
            if book[1] == name:
                if book[3] >= 1:
                    book[3] = book[3] - 1
                    print("The book has been successfully issued")
                    a = 1
                    break
                else:
                    print("Not enough quantity of book available")
                    break
        if a == 2:
            b = input("Book not found \n Press 1 to try again \n or else press anything else to go to main menu")
            b = int(b)
            if b == 1:
                self.issue()
            else:
                self.manage()

    def return_book(self):
        a = 2
        name = input("Enter the name of the book you want to return")
        l = len(book_list)
        for i in range(l):
            book = book_list(i)
            if name == book[1]:
                book[3] = book[3] + 1
                print("Book has been succesfully returned")
                a = 1
                break
        if a == 1:
            print("book is not found, Please enter the correct name")
            self.return_book()


student_list = []
teacher_list = []
book_list = []
library = Library()
library.main()
