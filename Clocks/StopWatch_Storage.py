from PyQt5 import QtCore, QtGui, QtWidgets, uic


class StopWatch_Storage(QtWidgets.QDialog):
    def __init__(self):
        super(StopWatch_Storage, self).__init__()

        uic.loadUi("StopWatch_Storage.ui", self)

        self.pushButton.clicked.connect(self.save_details)
        self.pushButton_2.clicked.connect(self.reset1)
        self.pushButton_3.clicked.connect(self.reset2)
        self.pushButton_4.clicked.connect(self.reset3)

        self.show()


    def reset1(self) : self.lineEdit.clear()


    def reset2(self) : self.lineEdit_2.clear()


    def reset3(self) : self.plainTextEdit.clear()


    def save_details(self):
        detail_id = self.lineEdit.text()
        time_taken = self.lineEdit_2.text()
        description = self.plainTextEdit.toPlainText()

        with open("TimeRecords.txt","a") as writer:
            writer.write(f"{'='*20} ID : {detail_id} {'='*20}\n\nTime Taken : {time_taken}\nDescription : {description}\n\n")