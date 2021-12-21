from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sys
import os
import sqlite3 as sql
from kullanicikayit import Ui_MainWindow

global id, name, surname, number, mail, city

os.system('python Connection.py')
os.system('python createTable.py')

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.formLoad()
        self.ui.btnSAVE.clicked.connect(self.btnSaveClick)
        self.ui.btnUPDATE.clicked.connect(self.btnUpdateClick)
        self.ui.tblLISTED.clicked.connect(self.listedClick)
        self.ui.btnDELETE.clicked.connect(self.btnDeleteClick)

    def formLoad(self):
        self.ui.tblLISTED.clear()
        self.ui.tblLISTED.setColumnCount(6)
        self.ui.tblLISTED.setHorizontalHeaderLabels(('ID','NAME','SURNAME','NUMBER','MAIL','CITY'))
        self.ui.tblLISTED.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect("kullanicikayit.db")
        cur = db.cursor()
        sorgu = "Select * from User"
        cur.execute(sorgu)
        rows = cur.fetchall()
        self.ui.tblLISTED.setRowCount(len(rows))   
        for rowIndex , rowData in enumerate(rows):
            for colIndex, colData in enumerate(rowData):
                self.ui.tblLISTED.setItem(rowIndex,colIndex,QTableWidgetItem(str(colData)))

    def btnSaveClick(self):
        id = self.ui.txtID.text()
        name = self.ui.txtNAME.text()
        surname = self.ui.txtSURNAME.text()
        number = self.ui.txtNUMBER.text()
        mail = self.ui.txtMAIL.text()
        city = self.ui.txtCITY.text()
        try:
            self.conntection = sql.connect("kullanicikayit.db")
            self.c = self.conntection.cursor()
            self.c.execute("Insert into user Values(?,?,?,?,?,?)",(id,name,surname,number,mail,city))
            self.conntection.commit()
            self.c.close()
            self.conntection.close()
            print("saved success")
        except Exception:
            print("Could not save")
        self.btnClear()
        self.formLoad()

    def btnUpdateClick(self):
        id = self.ui.txtID.text()
        name = self.ui.txtNAME.text()
        surname = self.ui.txtSURNAME.text()
        number = self.ui.txtNUMBER.text()
        mail = self.ui.txtMAIL.text()
        city = self.ui.txtCITY.text()
        try:
            self.conntection = sql.connect("kullanicikayit.db")
            self.c = self.conntection.cursor()
            self.c.execute("UPDATE user set name = ?, surname = ?, number = ?, mail = ?, city = ? where id = ?",(name, surname,number,mail,city,id))
            self.conntection.commit()
            self.c.close()
            self.conntection.close()
            print("Update Success")           
        except Exception:
            print("Could not update")
        self.btnClear()
        self.formLoad()
        
    def listedClick(self):
        self.ui.txtID.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,0).text())
        self.ui.txtNAME.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,1).text())
        self.ui.txtSURNAME.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,2).text())
        self.ui.txtNUMBER.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,3).text())
        self.ui.txtMAIL.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,4).text())
        self.ui.txtCITY.setText(self.ui.tblLISTED.item(self.ui.tblLISTED.currentRow() ,5).text())

    def btnDeleteClick(self):
        id = self.ui.txtID.text()
        try:
            self.conntection = sql.connect("kullanicikayit.db")
            self.c = self.conntection.cursor()
            self.c.execute("DELETE from user where id = ?", (id,))
            self.conntection.commit()
            self.c.close()
            self.conntection.close()
            print("Delete Success")           
        except Exception:
            print("Could not delete")
        self.btnClear()
        self.formLoad()

    

    def btnClear(self):
        self.ui.txtID.clear()
        self.ui.txtNAME.clear()
        self.ui.txtSURNAME.clear()
        self.ui.txtCITY.clear()
        self.ui.txtNUMBER.clear()
        self.ui.txtMAIL.clear()

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

App()