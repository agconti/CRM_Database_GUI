# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crmui.ui'
#
# Created: Sat Mar 16 17:05:52 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from table_def import *
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

        self.retranslateUi(CRM_form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.viewallrbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_querry_all_act)
        QtCore.QObject.connect(self.viewallcbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_querry_all_client)
        QtCore.QObject.connect(self.exitbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), CRM_form.close)
        #QtCore.QObject.connect(self.viewallrbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pyquerry1)
        #QtCore.QObject.connect(self.viewallcbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pyquerry1)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")),  self.sql_querry_all_client)
        #QtCore.QObject.connect(self.addsql_submitt, QtCore.SIGNAL(_fromUtf8("clicked()")), CRM_form.pyqeurry2)
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
        
        
    def sql_querry_all_act(self):
       #connect to the database
        session= self.sql_connect() 

        # how to do a SELECT * (i.e. all)
        res = session.query(act_log).all()
        
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
    
        
    def sql_querry_all_client(self):
        """"putstuff here"""
        session=self.sql_connect()
 
        # how to do a SELECT * (i.e. all)
        res = session.query(client).all()

        #Setup our table 
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(6)

        #set headers
        for d in xrange(0,6):

            h={0:'Client Id',1:'First Name', 2:'Last Name',3:'D.O.B.', 4:'Phone number',5: 'Account'}
            header_item=h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,6):
                self.tableWidget.setItem(e, o, self.sqltotext_client(o,i))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CRM_form = QtGui.QDialog()
    ui = Ui_CRM_form()
    ui.setupUi(CRM_form)
    CRM_form.show()
    sys.exit(app.exec_())

