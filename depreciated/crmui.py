# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crmui.ui'
#
# Created: Sat Mar 16 17:05:52 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from table_def import *
from sqlalchemy import desc
rec_act=''
rec_client=''
#current_client=client combo box 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CRM_form(object):
    def setupUi(self, CRM_form):
        CRM_form.setObjectName(_fromUtf8("CRM_form"))
        CRM_form.resize(718, 624)
        CRM_form.setWindowOpacity(1.0)
        self.tableWidget = QtGui.QTableWidget(CRM_form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 681, 291))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget = QtGui.QTabWidget(CRM_form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 340, 411, 261))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Look_Up = QtGui.QWidget()
        self.Look_Up.setObjectName(_fromUtf8("Look_Up"))
        self.viewallrbutt = QtGui.QPushButton(self.Look_Up)
        self.viewallrbutt.setGeometry(QtCore.QRect(10, 20, 181, 41))
        self.viewallrbutt.setObjectName(_fromUtf8("viewallrbutt"))
        self.viewallcbutt = QtGui.QPushButton(self.Look_Up)
        self.viewallcbutt.setGeometry(QtCore.QRect(220, 20, 171, 41))
        self.viewallcbutt.setObjectName(_fromUtf8("viewallcbutt"))
        self.tabWidget.addTab(self.Look_Up, _fromUtf8(""))
        self.Add = QtGui.QWidget()
        self.Add.setObjectName(_fromUtf8("Add"))
        self.time_input = QtGui.QLineEdit(self.Add)
        self.time_input.setGeometry(QtCore.QRect(130, 50, 21, 21))
        self.time_input.setObjectName(_fromUtf8("time_input"))
        self.label_2 = QtGui.QLabel(self.Add)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dateEdit = QtGui.QDateEdit(self.Add)
        self.dateEdit.setGeometry(QtCore.QRect(10, 50, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        today = QtCore.QDate.currentDate()
        self.dateEdit.setDate(today)
        self.label_3 = QtGui.QLabel(self.Add)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.descript_cat_inut = QtGui.QComboBox(self.Add)
        self.descript_cat_inut.setGeometry(QtCore.QRect(160, 50, 111, 22))
        self.descript_cat_inut.setObjectName(_fromUtf8("descript_cat_inut"))
        self.descript_cat_inut.addItem(_fromUtf8(""))
        self.descript_cat_inut.addItem(_fromUtf8(""))
        self.descript_cat_inut.addItem(_fromUtf8(""))
        self.descript_cat_inut.addItem(_fromUtf8(""))
        self.descript_cat_inut.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.Add)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.addsql_submitt = QtGui.QPushButton(self.Add)
        self.addsql_submitt.setGeometry(QtCore.QRect(310, 200, 75, 23))
        self.addsql_submitt.setObjectName(_fromUtf8("addsql_submitt"))
        self.label_6 = QtGui.QLabel(self.Add)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.descpt_inout = QtGui.QPlainTextEdit(self.Add)
        self.descpt_inout.setGeometry(QtCore.QRect(10, 100, 381, 91))
        self.descpt_inout.setObjectName(_fromUtf8("descpt_inout"))
        self.tabWidget.addTab(self.Add, _fromUtf8(""))
        self.exitbutt = QtGui.QPushButton(CRM_form)
        self.exitbutt.setGeometry(QtCore.QRect(600, 570, 91, 31))
        self.exitbutt.setObjectName(_fromUtf8("exitbutt"))
        self.listWidget = QtGui.QListWidget(CRM_form)
        self.listWidget.setGeometry(QtCore.QRect(440, 360, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(CRM_form)
        self.label.setGeometry(QtCore.QRect(440, 330, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.actionTestaction = QtGui.QAction(CRM_form)
        self.actionTestaction.setObjectName(_fromUtf8("actionTestaction"))
        
        #populate the Client list
        self.popc()

        #populate the act list 
        self.popr()

        #Signals & Solts
        self.retranslateUi(CRM_form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.viewallrbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_querry_all_act)
        QtCore.QObject.connect(self.viewallcbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_querry_all_client)
        QtCore.QObject.connect(self.exitbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), CRM_form.close)
        #QtCore.QObject.connect(self.viewallrbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pyquerry1)
        #QtCore.QObject.connect(self.viewallcbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pyquerry1)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")),  self.c_activity)
        QtCore.QObject.connect(self.addsql_submitt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_sql_act)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.pyquerry1)
        QtCore.QObject.connect(self.descript_cat_inut, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.pyquerry1)
        QtCore.QObject.connect(self.time_input, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.pyquerry1)
        QtCore.QObject.connect(self.descpt_inout, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.pyquerry1)
        QtCore.QMetaObject.connectSlotsByName(CRM_form)

    def retranslateUi(self, CRM_form):
        CRM_form.setWindowTitle(_translate("CRM_form", "C & RM Activity Log", None))
        self.viewallrbutt.setText(_translate("CRM_form", "View All Activity Records", None))
        self.viewallcbutt.setText(_translate("CRM_form", "View All Client Records", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Look_Up), _translate("CRM_form", "Look Up", None))
        self.label_2.setText(_translate("CRM_form", "Date", None))
        self.label_3.setText(_translate("CRM_form", "Time", None))
        self.descript_cat_inut.setItemText(0, _translate("CRM_form", "Care Coordination", None))
        self.descript_cat_inut.setItemText(1, _translate("CRM_form", "Correspondence", None))
        self.descript_cat_inut.setItemText(2, _translate("CRM_form", "Onsite Hospital", None))
        self.descript_cat_inut.setItemText(3, _translate("CRM_form", "Phone Call Patient\n", None))
        self.descript_cat_inut.setItemText(4, _translate("CRM_form", "Medical Record Review\n", None))
        self.label_4.setText(_translate("CRM_form", "Category", None))
        self.label_5.setText(_translate("CRM_form", "Description of Activities", None))
        self.addsql_submitt.setText(_translate("CRM_form", "Submit", None))
        self.label_6.setText(_translate("CRM_form", "Add Activity to the Database:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add), _translate("CRM_form", "Add", None))
        self.exitbutt.setText(_translate("CRM_form", "Exit", None))
        self.label.setText(_translate("CRM_form", "Client Information", None))
        self.actionTestaction.setText(_translate("CRM_form", "Testaction", None))

    def pyquerry1(self):
        print"this is only a test"
    
    def pyquerry2(self, item):
        print"this is only a test"
        print item.text()
    
    def sql_connect(self):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
 
        engine = create_engine('sqlite:///CRM.sqlite', echo=False)
 
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
 
    def sqltotext_act(self,o,i):
        #for the act_log table
        #needs the o as an iterable, and the sqlachemy object i
        g={0:i.client_id,1:i.date, 2:i.descp_cat,3:i.time, 4:i.total}
        yu=g[o]
        item = QtGui.QTableWidgetItem()
        item.setText(str(yu))
        return item

    def sqltotext_client(self,o,i):
        #for the client table
        #needs the o as an iterable, and the sqlachemy object i
        g={0:i.client_id,1:i.first_name, 2:i.last_name,3:i.dob, 4:i.phone_number,5: i.account}
        yu=g[o]
        item = QtGui.QTableWidgetItem()
        item.setText(str(yu))
        return item
        
    def tableMain_build(self,res):
        #Setup our table 
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(5)

        #set headers
        for d in xrange(0,5):
            h={0:'Client Id',1:'Date', 2:'Description',3:'Time', 4:'Total'}
            header_item=h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_act(o,i))
    
    def sql_querry_all_act(self):
       #connect to the database
        session= self.sql_connect() 

        # how to do a SELECT * (i.e. all)
        res = session.query(act_log).order_by("Date desc").all()
        #build table
        self.tableMain_build(res)
    
        
    def sql_querry_all_client(self):
        """"putstuff here"""
        session=self.sql_connect()
 
        # how to do a SELECT * (i.e. all)
        res = session.query(client).all()

        #Setup our table 
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(6)

        #set main table headers
        for d in xrange(0,6):

            h={0:'Client Id',1:'First Name', 2:'Last Name',3:'D.O.B.', 4:'Phone number',5: 'Account'}
            header_item=h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate main table
        for e,i in enumerate(res):
            for o in xrange(0,6):
                self.tableWidget.setItem(e, o, self.sqltotext_client(o,i))

    
    def add_sql_act(self):
        import datetime
        #Connect to sever
        session= self.sql_connect()
        c=2 #client ID box doesnt exist yet
        u= 10 # unit price needs to be added
        raw_date=str(self.dateEdit.text())
        d=datetime.datetime.strptime(raw_date, "%m/%d/%Y")
        
        res_id=session.query(act_log).order_by('transaction_id desc').first()
        e=res_id.transaction_id
        e+=1
        d=datetime.date(2002,03,26)
        add_log = act_log(transaction_id=e, client_id=c, date=d, descp=str(self.descpt_inout.toPlainText()), descp_cat=str(self.descript_cat_inut.currentText()), time=float(self.time_input.text()
), unit_price=u, total=(u*float(self.time_input.text())))

        session.add(add_log)
        session.commit()
        rec_act=e
        #update main table
        res=session.query(act_log).filter(act_log.client_id==c).order_by("transaction_id desc").all()
        self.tableMain_build(res)
    
    def add_sql_c(self):
        res_id=session.query(client).order_by('client_id desc').first()
        e=res_id.client_id
        e+=1
        d=datetime.date(2002,03,26)
        add_c = client(client_id=e, first_name, last_name, dob, phone_number, account)

        session.add(add_c)
        session.commit()
        rec_client=e
        #update main table
        res=session.query(client).all()
        self.tableMain_build(res)

    def del_act(self):
        if rec_act!="":
            session.query(act_log).filter(act_log.transaction_id==rec_act).delete()

    def del_c(self):
        if rec_client!="":
            session.query(client).filter(client.client_id==rec_client).delete()

    def c_activity(self, item):
        #maybe make a combo button set to patients names and update it with  this self.descript_cat_inut.addItem(_fromUtf8(""))
        #maket his on click function set the value of that combo box and bring up activity to that patient. thus easy input
        import re
        session= self.sql_connect()
        
        item=item.text()
        s=re.split(", ", item)
        s0=str(s[0])
        s1=str(s[1])

        resc =session.query(client).filter(client.last_name==s1 and client.frist_name==s0)

        for i in resc:
            v=i.client_id
            
        
        res = session.query(act_log).filter(act_log.client_id==v).all()

        #build table
        self.tableMain_build(res)

    def popc(self):
        #populates the client list when the UI first init
        # connect to db
        session=self.sql_connect()
 
        # how to do a SELECT * (i.e. all)
        res = session.query(client).all()
        for e,i in enumerate(res):
            s=i.first_name
            s=s+", "+i.last_name
            item = QtGui.QListWidgetItem(s)
            self.listWidget.addItem(item)

    def popr(self):
        session=self.sql_connect()
        res = session.query(act_log).order_by("Date desc").limit(9)

        #Setup our table 
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(5)
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        #set headers
        for d in xrange(0,5):
            h={0:'Client Id',1:'Date', 2:'Description',3:'Time', 4:'Total'}
            header_item=h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_act(o,i))

    def open_referncefolder(self):
        import os
        os.startfile('C:\Users\Andrew\Documents\CRM\db Tests\Reference Forms') # opens explorer at C:\ drive

    def open_referncefile(self):
        import os
        os.startfile('C:\Users\Andrew\Documents\CRM\db Tests\Reference Forms/test.pdf')#opends pdf # this is windows only

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CRM_form = QtGui.QDialog()
    ui = Ui_CRM_form()
    ui.setupUi(CRM_form)
    CRM_form.show()
    sys.exit(app.exec_())

