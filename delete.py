# import module name
import sys #sys is a built-in module in python
import sqlite3 #sqlite3 is a built-in module in python 

# from top-level module.submodule import  element1, element2,  element3,.............
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

#return= module.method(actual argument)
conn  =  sqlite3.connect('./mydatabase.sqlite') # every function return something
cursor = conn.cursor() 

query = '''
            create table if not exists employees(
                id integer primary key autoincrement,
                name text not null,
                position text not null,
                salary real not null
            );
        '''

cursor.execute(query) # query is an actual  argument
conn.commit()


#ceo = ClassName()
#ceo = module.ClassName()
app =  QApplication([]) # [] is a list in python

#Create Widgets
name_label = QLabel('Name:')
name = QLineEdit()

position_label = QLabel('Position:')
position = QLineEdit()

salary_label = QLabel('Salary:')
salary = QLineEdit()

submit_button = QPushButton('Submit')
view_button = QPushButton('View')
show_employees = QPushButton('Show Employees')

# Global Variable
table = QTableWidget()

#1. funtion defination is a one time process
def deleteEmployee(row):
    #create a confirmation QMessageBox
    confirmation_box = QMessageBox()
    confirmation_box.setIcon(QMessageBox.Icon.Question)
    confirmation_box.setText("Do You want to proceed")
    confirmation_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    confirmation_box.setDefaultButton(QMessageBox.StandardButton.No)

    # Execute the confirmation dialog and get the result
    result = confirmation_box.exec()

    #check the result 
    if result == QMessageBox.StandardButton.Yes:

        print("user clicked yes , proceed with the action.")
        #Add your action here
        print(row)
        print(table.item(row,0).text())
        delid = table.item(row,0).text()
        # Build Query
        print("Before Typecasting")
        print(delid)
        print(type(delid))
        # Typecasting
        delid = int(delid)
        print("After Typecasting")
        print(delid)
        print(type(delid))
        print(f"delete  from employees where id={delid}")

        # Execute Query
        cursor.execute(f"delete  from employees where id={delid}")

        # Commit Query 
        conn.commit()
    else:
        print("User clicked no, cancel the action ")

#1. funtion defination is a one time process
def showEmployeeSlotFunction():
    print("Hello")
    # we can use globle variable inside function defination 
    #fetch data from the database 
    cursor.execute("select * from employees")
    data = cursor.fetchall()

    #ceo = ClassName()
    column_names = ['ID', 'Name', 'Position', 'Salary', 'Actions']
    table.setColumnCount(len(column_names)) #ceo.method()
    table.setHorizontalHeaderLabels(column_names)

    #set row count
    table.setRowCount(len(data))

    # populate the table with data 
    # for singular in plural
    for row_num, row_data in enumerate(data):
        for col_num, col_data in enumerate(row_data):
            item = QTableWidgetItem(str(col_data))
            table.setItem(row_num, col_num, item)
        # Add buttons foe each row
        #view_button = QPushButton('View')
        #edit_button = QPushButton('Edit')
        delete_button = QPushButton('Delete')

        button_layout = QVBoxLayout()
        #button_layout.addWidget(view_button)
        #button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.setContentsMargins(0, 0, 0, 0) # no margins

        buttons_widget = QWidget()
        buttons_widget.setLayout(button_layout)    
        table.setCellWidget(row_num, len(column_names)-1, buttons_widget)
                                   # lambda  fa1,    fa2    : expression
        delete_button.clicked.connect(lambda  _, row=row_num: deleteEmployee(row))

    # set horiontal header to stretch 
    table.show()
    pass

#1. funtion defination is a one time process
def myFunction():  # myFunction is writter in camelCase
    print("Hello Ranu")
    print(f"name={name.text()} position={position.text()} salary={salary.text()}  ")
    #query = "delete from employees;"
    #ceo .method(actual argument1)
    #cursor.execute(query)

    query = "insert into employees (name, position, salary) values (?, ?, ?);"
    # ceo = method(actual argument1, actual argument2)
    # ceo.method(string,tuple)
    cursor.execute(query, (name.text(), position.text(), salary.text()))
    conn.commit()

    msgBox = QMessageBox()
    msgBox.setText("Employee Saved Successfully")
    msgBox.exec()
    pass

submit_button.clicked.connect(myFunction)  #2. I Am Calling/Invoking the function
show_employees .clicked.connect(showEmployeeSlotFunction)  #2. I Am Calling/Invoking the function

# Set button color using style sheet
submit_button.setStyleSheet('background-color: green; color: white;') 
show_employees.setStyleSheet('background-color: blue; color: white;') 

# Set up layout
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name)
layout.addWidget(position_label)
layout.addWidget(position)
layout.addWidget(salary_label)
layout.addWidget(salary)
layout.addWidget(submit_button)
layout.addWidget(show_employees)
layout.addWidget(table)

# Set up window
window = QWidget()
window.setLayout(layout)
window.setWindowTitle('Employee Form')
#window.setGeometry(X,    Y,   W, H  )
#window.setGeometry(600, 200, 300, 200)


# Show the window
window.show()
sys.exit(app.exec())
