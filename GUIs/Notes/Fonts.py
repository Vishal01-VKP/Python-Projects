from PyQt5 import QtCore, QtGui, QtWidgets, uic
import Notes


class Fonts(QtWidgets.QDialog, Notes.ui):
    def __init__(self, main_screen):
        super(Fonts, self).__init__()

        uic.loadUi("Notes-2.ui", self)

        self.colours_list = ["red","blue","green","yellow","white","black","orange","purple","gold","silver","violet","cyan","magenta","pink","indigo"]

        for i in self.colours_list:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)

        self.pushButton.clicked.connect(self.save_changes)

        self.color_data = main_screen.comboBox.currentText()

        self.show()


    def save_changes(self):
        text = Notes.Notes.textBox.toPlainText()
        text.setHtml(f"<div color={self.color_data}>{text}</div>")


app = QtWidgets.QApplication(sys.argv)
ui = Fonts()
app.exec_()