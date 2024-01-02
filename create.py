# import module name
import sys #sys is a built-in module in python
import sqlite3 #sqlite3 is a built-in module in python 

# from top-level module.submodule import  element1, element2,  element3,.............
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

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
# Set button color using style sheet
submit_button.setStyleSheet('background-color: green; color: white;')

#1. funtion defination is a one time process
def myFunction():  # myFunction is writter in camelCase
    print("Hello Ranu")
    print(f"name={name.text()} position={position.text()} salary={salary.text()}  ")
    #query = "delete from employees;"
    #  ceo .method(actual argument1)
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


# Set up layout
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name)
layout.addWidget(position_label)
layout.addWidget(position)
layout.addWidget(salary_label)
layout.addWidget(salary)
layout.addWidget(submit_button)

# Set up window
window = QWidget()
window.setLayout(layout)
window.setWindowTitle('Employee Form')
#window.setGeometry(X,    Y,   W, H  )
#window.setGeometry(600, 200, 300, 200)

# Show the window
window.show()
sys.exit(app.exec())



