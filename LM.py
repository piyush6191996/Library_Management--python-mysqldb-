import time


class LM:

    def add_books(self):
        print('You are in add books')
        time.sleep(2)
        self.menu()

    def remove_books(self):
        print('you are in remove books')
        time.sleep(2)
        self.menu()

    def add_members(self):
        print('you are in add members')
        time.sleep(2)
        self.menu()

    def remove_members(self):
        print('you are in remove members')
        time.sleep(2)
        self.menu()

    def allocate_books(self):
        print('you are in allocate books')
        time.sleep(2)
        self.menu()

    def deallocate_books(self):
        print('You are in deallocate books')
        time.sleep(2)
        self.menu()

    def menu(self):
        print('Choose what you want to do from the given options')
        print('1.    ADD BOOKS \n2.    REMOVE BOOKS \n3.    ADD MEMBERS \n4.    REMOVE MEMBERS \n5.    ALLOCATE BOOKS TO MEMBERS  \n6.    DEALLOCATE BOOKS FROM MEMBERS \n7.    EXIT')
        ch = input('Enter your choice')
        if ch == '1':
            self.add_books()
        elif ch == '2':
            self.remove_books()
        elif ch == '3':
            self.add_members()
        elif ch == '4':
            self.remove_members()
        elif ch == '5':
            self.allocate_books()
        elif ch == '6':
            self.deallocate_books()
        elif ch == '7':
            exit()
        else:
            print('Plese Enter The Correct Choice')
            time.sleep(2)
            self.menu()


print(' Welcome to your Library Management System')
time.sleep(2)
print(' \n\n ***************************************************** \n\n')
library = LM()
library.menu()
