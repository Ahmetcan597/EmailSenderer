import sys
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QCheckBox

#her şeyi ingilizce yap sözleşmeyi kaldır bu kadar

class Pencere(QtWidgets.QWidget):

     def __init__(self):

        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

     def baglanti_olustur(self):
         pass
        # baglanti = sqlite3.connect("mailuyg.db")
        # self.cursor = baglanti.cursor()

        # self.cursor.execute("Create table if not exists mailler (sender TEXT,senderpass TEXT,toemail TEXT,baslik TEXT,yazi TEXT,kac INT)")

        # baglanti.commit()

     def init_ui(self):

         self.sendermail = QtWidgets.QLineEdit()
         self.senderpass = QtWidgets.QLineEdit()
         self.senderpass.setEchoMode(QtWidgets.QLineEdit.Password)
         self.toemail = QtWidgets.QLineEdit()
         self.bilgi = QtWidgets.QLabel("First space:Your gmail adress\nSecond space:Your gmail password\nThird one:Who do you want to send email to?\nDon't forget this program only works gmails accounts\nBelow, The first one is the heading, the second one is the paragraph of your email.\nAhmetcan Temel")
         self.baslik = QtWidgets.QLineEdit()
         self.yazi = QtWidgets.QLineEdit()
         self.say = 0
         self.checkbox = QCheckBox("Confirmation is required")
         self.gönderilen = QtWidgets.QLabel("0 email was sent")
         self.buton1 = QtWidgets.QPushButton("send 1 email")
         self.buton10 = QtWidgets.QPushButton("send 10 email")
         self.buton20 = QtWidgets.QPushButton("send 20 email")
         self.buton30 = QtWidgets.QPushButton("send 30 email")
         self.buton50 = QtWidgets.QPushButton("send 50 email")
         self.buton100 = QtWidgets.QPushButton("send 100 email")
         self.buton1000 = QtWidgets.QPushButton("send 1000 email")

         v_box = QtWidgets.QVBoxLayout()

         v_box.addWidget(self.sendermail)
         v_box.addWidget(self.senderpass)
         v_box.addWidget(self.toemail)
         v_box.addWidget(self.bilgi)
         v_box.addWidget(self.baslik)
         v_box.addWidget(self.yazi)
         v_box.addWidget(self.checkbox)
         v_box.addWidget(self.gönderilen)
         v_box.addWidget(self.buton1)
         v_box.addWidget(self.buton10)
         v_box.addWidget(self.buton20)
         v_box.addWidget(self.buton30)
         v_box.addWidget(self.buton50)
         v_box.addWidget(self.buton100)
         v_box.addWidget(self.buton1000)

         h_box = QtWidgets.QHBoxLayout()
         h_box.addStretch()
         h_box.addLayout(v_box)
         h_box.addStretch()

         self.setLayout(h_box)
         self.setWindowTitle("EmailSenderer")
         self.setWindowIcon(QtGui.QIcon("download.jpg"))
         

         self.buton1.clicked.connect(self.mail_atan)
         self.buton10.clicked.connect(self.mail_patlat10)
         self.buton20.clicked.connect(self.mail_patlat20)
         self.buton30.clicked.connect(self.mail_patlat30)
         self.buton50.clicked.connect(self.mail_patlat50)
         self.buton100.clicked.connect(self.mail_patlat100)
         self.buton1000.clicked.connect(self.mail_patlat1000)



         self.show()


     def mail_atan(self):

         checkbox = self.checkbox.isChecked()
         if (self.checkbox.isChecked()):

                mesaj = MIMEMultipart()

                mesaj["From"] = self.sendermail.text()
                mesaj["To"] = self.toemail.text()
                mesaj["Subject"] = self.baslik.text()

                yazi = self.yazi.text()
                mesaj_govdesi = MIMEText(yazi,"plain")

                mesaj.attach(mesaj_govdesi)

                try:

                    mail = smtplib.SMTP("smtp.gmail.com",587)

                    mail.ehlo()

                    mail.starttls()

                    mail.login(self.sendermail.text(),self.senderpass.text())

                    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

                    print("email was sent")
                    self.say += 1
                    self.gönderilen.setText(self.toemail.text() + "to address" + str(self.say) + " times email was sent.")

                    mail.close()

                except:
                
                    sys.stderr.write("email wasn't sent")
                    sys.stderr.flush
         else:
             self.gönderilen.setText("you didn't click the confirmation")



     def mail_patlat10(self):
         i = 0
         x = 10
         while i < x:
             self.mail_atan()
             i += 1
     def mail_patlat20(self):
         i = 0
         x = 20
         while i < x:
             self.mail_atan()
             i += 1
     def mail_patlat30(self):
         i = 0
         x = 30
         while i < x:
             self.mail_atan()
             i += 1
     def mail_patlat50(self):
         i = 0
         x = 50
         while i < x:
             self.mail_atan()
             i += 1
     def mail_patlat100(self):
         i = 0
         x = 100
         while i < x:
             self.mail_atan()
             i += 1
     def mail_patlat1000(self):
         i = 0
         x = 1000
         while i < x:
             self.mail_atan()
             i += 1
              
        
app = QtWidgets.QApplication(sys.argv)


pencere = Pencere()

sys.exit(app.exec_())

