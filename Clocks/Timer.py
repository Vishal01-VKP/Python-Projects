from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys


class TimerWindow(QtWidgets.QDialog):
    def __init__(self):
        super(TimerWindow, self).__init__()

        uic.loadUi("Timer.ui", self)

        self.pause = True

        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.run_timer)
        timer.start(1000)

        self.pushButton.clicked.connect(self.set_timer)
        self.pushButton_2.clicked.connect(self.pause_timer)
        self.pushButton_3.clicked.connect(self.reset_timer)
        self.pushButton_4.clicked.connect(self.minute_plus)
        self.pushButton_5.clicked.connect(self.delete_all)

        self.show()


    def set_timer(self):
        self.pushButton.setDisabled(True)
        self.pause = False

        self.hours = self.spinBox.value()
        self.minutes = self.spinBox_2.value()
        self.seconds = self.spinBox_3.value()

        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")


    def run_timer(self):
        if self.pause == True:
            pass

        elif self.pause == False:
            if self.hours == self.minutes == self.seconds == 0:
                self.textBrowser.setText("00:00:00")

            else:
                if self.minutes == self.seconds == 0:
                    self.hours -= 1
                    self.minutes += 59
                    self.seconds += 59

                elif self.seconds == 0:
                    self.minutes -= 1
                    self.seconds += 59

                else:
                    self.seconds -= 1
                    
                self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")


    def pause_timer(self):
        if self.pause == False:
            self.pause = True
            self.pushButton_2.setText("Resume")

        else:
            self.pause = False
            self.pushButton_2.setText("Stop")


    def reset_timer(self):
        if self.pause == False:
            self.pause = True

        else:
            self.pause = False

        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.pushButton.setDisabled(False)

        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")
        self.pushButton_2.setText("Stop")


    def delete_all(self):
        self.reset_timer()

        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)


    def minute_plus(self):
        self.minutes += 1
        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TimerWindow()
    app.exec_()