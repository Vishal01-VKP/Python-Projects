from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Fonts(QtWidgets.QDialog):
    def __init__(self):
        super(Fonts, self).__init__()

        uic.loadUi("Notes-2.ui", self)

        self.colours_list = ["red","blue","green","yellow","white","black","orange","purple","gold","silver","violet","cyan","magenta","pink","indigo"]

        for i in self.colours_list:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)

        self.pushButton.clicked.connect(self.save_changes)

        self.show()


    def save_changes(self, object):
        with open("fonts_data.txt", "w") as writer:
            writer.write(f"{self.fontComboBox.currentText()}\n{self.spinBox.value()}\n{self.comboBox.currentText()}\n{self.comboBox_2.currentText()}")