# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepasswordpart1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
import UG,UM


db= pymysql.connect(host='127.0.0.1',
                    user='root',
                    password='',
                    db='test',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                    )
baglanti=db.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 168)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/wheat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.part1 = QtWidgets.QWidget(Dialog)
        self.part1.setGeometry(QtCore.QRect(10, 10, 251, 151))
        self.part1.setObjectName("part1")
        self.eskilbl = QtWidgets.QLabel(self.part1)
        self.eskilbl.setGeometry(QtCore.QRect(67, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eskilbl.setFont(font)
        self.eskilbl.setObjectName("eskilbl")
        self.oldpsswordtxt = QtWidgets.QLineEdit(self.part1)
        self.oldpsswordtxt.setGeometry(QtCore.QRect(71, 70, 111, 20))
        self.oldpsswordtxt.setToolTip("")
        self.oldpsswordtxt.setWhatsThis("")
        self.oldpsswordtxt.setText("")
        self.oldpsswordtxt.setFrame(True)
        self.oldpsswordtxt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldpsswordtxt.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.oldpsswordtxt.setClearButtonEnabled(True)
        self.oldpsswordtxt.setObjectName("oldpsswordtxt")
        self.ileributon = QtWidgets.QPushButton(self.part1)
        self.ileributon.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.ileributon.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 85, 255);")
        self.ileributon.setObjectName("ileributon")


        #############################################

        self.part2 = QtWidgets.QWidget(Dialog)
        self.part2.setGeometry(QtCore.QRect(10, 10, 261, 151))
        self.part2.setObjectName("part2")
        self.yenilbl = QtWidgets.QLabel(self.part2)
        self.yenilbl.setGeometry(QtCore.QRect(0, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yenilbl.setFont(font)
        self.yenilbl.setObjectName("yenilbl")
        self.newpasswordtxt = QtWidgets.QLineEdit(self.part2)
        self.newpasswordtxt.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.newpasswordtxt.setToolTip("")
        self.newpasswordtxt.setWhatsThis("")
        self.newpasswordtxt.setText("")
        self.newpasswordtxt.setFrame(True)
        self.newpasswordtxt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpasswordtxt.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.newpasswordtxt.setClearButtonEnabled(True)
        self.newpasswordtxt.setObjectName("newpasswordtxt")
        self.pswkydbtn = QtWidgets.QPushButton(self.part2)
        self.pswkydbtn.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.pswkydbtn.setStyleSheet("\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "alternate-background-color: rgb(0, 85, 255);")
        self.pswkydbtn.setObjectName("pswkydbtn")
        self.yenilbl2 = QtWidgets.QLabel(self.part2)
        self.yenilbl2.setGeometry(QtCore.QRect(0, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yenilbl2.setFont(font)
        self.yenilbl2.setObjectName("yenilbl2")
        self.newpaswordtxt2 = QtWidgets.QLineEdit(self.part2)
        self.newpaswordtxt2.setGeometry(QtCore.QRect(130, 52, 111, 20))
        self.newpaswordtxt2.setToolTip("")
        self.newpaswordtxt2.setWhatsThis("")
        self.newpaswordtxt2.setText("")
        self.newpaswordtxt2.setFrame(True)
        self.newpaswordtxt2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpaswordtxt2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.newpaswordtxt2.setClearButtonEnabled(True)
        self.newpaswordtxt2.setObjectName("newpaswordtxt2")

        self.falsesfrealert = QtWidgets.QLabel(self.part1)
        self.falsesfrealert.setGeometry(QtCore.QRect(60, 5, 141, 20))
        self.falsesfrealert.setStyleSheet("color: rgb(255, 0, 0);\n""font: 8pt \"MS Shell Dlg 2\";\n"
                                          "")
        self.falsesfrealert.setText("")
        self.falsesfrealert.setObjectName("falsesfrealert")

        self.falsesfrealert2 = QtWidgets.QLabel(self.part2)
        self.falsesfrealert2.setGeometry(QtCore.QRect(60, 125, 141, 20))
        self.falsesfrealert2.setStyleSheet("color: rgb(255, 0, 0);\n""font: 8pt \"MS Shell Dlg 2\";\n"
                                          "")
        self.falsesfrealert2.setText("")
        self.falsesfrealert2.setObjectName("falsesfrealert2")


        self.part2.hide()

        self.ileributon.clicked.connect(self.kontrolsfre)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Şifre Değiştirme"))
        self.eskilbl.setText(_translate("Dialog", "Eski Şifrenizi giriniz:"))
        self.oldpsswordtxt.setPlaceholderText(_translate("Dialog", "Şifrenizi giriniz"))
        self.ileributon.setText(_translate("Dialog", "İleri"))
        self.yenilbl.setText(_translate("Dialog", "Yeni Şifrenizi giriniz:"))
        self.newpasswordtxt.setPlaceholderText(_translate("Dialog", "Şifrenizi giriniz"))
        self.pswkydbtn.setText(_translate("Dialog", "Kaydet"))
        self.yenilbl2.setText(_translate("Dialog", "Tekrar giriniz:"))
        self.newpaswordtxt2.setPlaceholderText(_translate("Dialog", "Şifrenizi giriniz"))


    def kontrolsfre(self):

        baglanti.execute(f'SELECT Id FROM password WHERE Id="1" ')
        index = baglanti.fetchall()
        if len(index) == 1:
            baglanti.execute("SELECT * FROM password WHERE Id='1'")
            ss = baglanti.fetchall()
        if self.oldpsswordtxt.text() == str(ss[0]['psword']):
            self.part1.hide()
            self.part2.show()

        else:
            self.falsesfrealert.setText('!Yanlış şifre tekrar deneyiniz.')

        self.pswkydbtn.clicked.connect(self.changesql)

    def changesql(self):
        baglanti.execute(f'SELECT psword FROM password WHERE Id="1" ')
        index = baglanti.fetchall()


        if self.newpasswordtxt.text()==self.newpaswordtxt2.text() and self.newpasswordtxt.text()!=str(index[0]['psword']) and self.newpaswordtxt2.text()!=str(index[0]['psword']):

            baglanti.execute(f"UPDATE password SET psword='{self.newpasswordtxt.text()}' WHERE Id='1';")
            db.commit()
            self.falsesfrealert2.setStyleSheet("color: rgb(0, 170, 0);\n""font: 8pt \"MS Shell Dlg 2\";\n""")
            self.falsesfrealert2.setText('Şifre Değişimi başarılı.')
            self.falsesfrealert2.setAlignment(Qt.AlignCenter)
            return self.cksyap()
        elif self.newpasswordtxt.text()==str(index[0]['psword']) and self.newpaswordtxt2.text()==str(index[0]['psword']):

            self.falsesfrealert2.setText('Eski Şifre İle Aynı Olamaz !')
            self.falsesfrealert2.setAlignment(Qt.AlignCenter)
        else:

            self.falsesfrealert2.setText('Şifreler uyuşmuyor !')
            self.falsesfrealert2.setAlignment(Qt.AlignCenter)


    def cksyap(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Şifre Değişimi başarılı")
        msgBox.setWindowTitle("UYARI")
        msgBox.setWindowIcon(QtGui.QIcon("../Projeİcerik/icons/warning (1).png"))
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setStandardButtons(QMessageBox.Close)
        buttonc = msgBox.button(QMessageBox.Close)
        buttonc.setText("Kapat")
        returnValue = msgBox.exec()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cDialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(cDialog)
    cDialog.show()
    sys.exit(app.exec_())
