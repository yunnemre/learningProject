# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tedarikcikaytdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 311, 341))
        self.widget2.setObjectName("widget2")
        self.tedarikcilbl2 = QtWidgets.QLabel(self.widget2)
        self.tedarikcilbl2.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.tedarikcilbl2.setObjectName("tedarikcilbl2")
        self.tedarikcitxt2 = QtWidgets.QLineEdit(self.widget2)
        self.tedarikcitxt2.setGeometry(QtCore.QRect(10, 20, 281, 28))
        self.tedarikcitxt2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.tedarikcitxt2.setObjectName("tedarikcitxt2")
        self.adreslbl2 = QtWidgets.QLabel(self.widget2)
        self.adreslbl2.setGeometry(QtCore.QRect(10, 150, 41, 16))
        self.adreslbl2.setObjectName("adreslbl2")
        self.iltxt2 = QtWidgets.QLineEdit(self.widget2)
        self.iltxt2.setGeometry(QtCore.QRect(10, 120, 113, 20))
        self.iltxt2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.iltxt2.setObjectName("iltxt2")
        self.ilcetxt2 = QtWidgets.QLineEdit(self.widget2)
        self.ilcetxt2.setGeometry(QtCore.QRect(170, 120, 121, 20))
        self.ilcetxt2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.ilcetxt2.setObjectName("ilcetxt2")
        self.illbl2 = QtWidgets.QLabel(self.widget2)
        self.illbl2.setGeometry(QtCore.QRect(10, 100, 51, 20))
        self.illbl2.setObjectName("illbl2")
        self.ilcelbl2 = QtWidgets.QLabel(self.widget2)
        self.ilcelbl2.setGeometry(QtCore.QRect(170, 100, 41, 16))
        self.ilcelbl2.setObjectName("ilcelbl2")
        self.teltxt2 = QtWidgets.QLineEdit(self.widget2)
        self.teltxt2.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.teltxt2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.teltxt2.setObjectName("teltxt2")
        self.adrestxt2 = QtWidgets.QPlainTextEdit(self.widget2)
        self.adrestxt2.setGeometry(QtCore.QRect(10, 170, 281, 81))
        self.adrestxt2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.adrestxt2.setObjectName("adrestxt2")
        self.tellbl2 = QtWidgets.QLabel(self.widget2)
        self.tellbl2.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.tellbl2.setObjectName("tellbl2")
        self.emaillbl2 = QtWidgets.QLabel(self.widget2)
        self.emaillbl2.setGeometry(QtCore.QRect(170, 50, 47, 13))
        self.emaillbl2.setObjectName("emaillbl2")
        self.emailtxt2 = QtWidgets.QLineEdit(self.widget2)
        self.emailtxt2.setGeometry(QtCore.QRect(170, 70, 121, 20))
        self.emailtxt2.setStyleSheet("")
        self.emailtxt2.setObjectName("emailtxt2")
        self.tedarikcigirditmzlebtn = QtWidgets.QPushButton(self.widget2)
        self.tedarikcigirditmzlebtn.setGeometry(QtCore.QRect(60, 280, 75, 23))
        self.tedarikcigirditmzlebtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 85, 255);")
        self.tedarikcigirditmzlebtn.setObjectName("tedarikcigirditmzlebtn")
        self.tedarikcigirditmzlebtn.clicked.connect(self.temizlecliked)
        self.musterikydetbtn2 = QtWidgets.QPushButton(self.widget2)
        self.musterikydetbtn2.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.musterikydetbtn2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 85, 255);")
        self.musterikydetbtn2.setObjectName("musterikydetbtn2")
        self.musterikydetbtn2.clicked.connect(self.tkayt)
        self.kytinfolbl = QtWidgets.QLabel(self.widget2)
        self.kytinfolbl.setGeometry(QtCore.QRect(62, 255, 183, 20))
        self.kytinfolbl.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(0, 170, 0);")
        self.kytinfolbl.setObjectName("kytinfolbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TEDARİKÇİ EKLE"))
        self.tedarikcilbl2.setText(_translate("Dialog", "ŞİRKET ADI"))
        self.adreslbl2.setText(_translate("Dialog", "ADRES"))
        self.illbl2.setText(_translate("Dialog", "İL"))
        self.ilcelbl2.setText(_translate("Dialog", "İLÇE"))
        self.adrestxt2.setPlainText(_translate("Dialog", "\n"
""))
        self.tellbl2.setText(_translate("Dialog", "TELEFON"))
        self.emaillbl2.setText(_translate("Dialog", "EMAİL"))
        self.tedarikcigirditmzlebtn.setText(_translate("Dialog", "TEMİZLE"))
        self.musterikydetbtn2.setText(_translate("Dialog", "KAYDET"))



    def tkayt(self):
        _translate = QtCore.QCoreApplication.translate
        if self.tedarikcitxt2.text()=='' or self.teltxt2.text()=='' or self.emailtxt2.text()=='' or self.iltxt2.text()=='' or self.ilcetxt2.text()=='' or self.adrestxt2.toPlainText()=='':
            self.kytinfolbl.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255, 0, 0);")
            self.kytinfolbl.setText(_translate("Dialog", "Boş Alanlar var!"))
            self.kytinfolbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.kytinfolbl.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(0, 170, 0);")
            self.kytinfolbl.setText(_translate("Dialog", "Tedarikçi başarılı bir şekilde kayıt oldu."))
            db = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
            baglanti = db.cursor()
            tsa = self.tedarikcitxt2.text()
            ttel = self.teltxt2.text()
            temail = self.emailtxt2.text()
            til = self.iltxt2.text()
            tilce = self.ilcetxt2.text()
            tadres = self.adrestxt2.toPlainText()


            baglanti.execute(f"INSERT INTO tedarikci (TSA,TTel,TEmail,Til,Tilce,TAdres) VALUES ('{tsa}','{ttel}','{temail}','{til}','{tilce}','{tadres}')")

            db.commit()



    def temizlecliked(self):
        _translate = QtCore.QCoreApplication.translate
        self.kytinfolbl.setText(_translate("Dialog", ""))
        self.tedarikcitxt2.setText("")
        self.teltxt2.setText("")
        self.emailtxt2.setText("")
        self.iltxt2.setText("")
        self.ilcetxt2.setText("")
        self.adrestxt2.setPlainText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tkDialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(tkDialog)
    tkDialog.show()
    sys.exit(app.exec_())