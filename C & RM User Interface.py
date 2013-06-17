#Catastrophic and Rehabilitative Management Gui
#Copy-write Andrew Conti 2013

from PyQt4 import QtCore, QtGui
from table_def import client, act_log, contact
rec_act = ''
rec_client = ''


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
        '''
        this function sets up our Gui with all of our specified paramaters. 

        Ie. widget size, buttons, displays ect. 
        '''
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
        self.viewallcontactsbutt = QtGui.QPushButton(self.Look_Up)
        self.viewallcontactsbutt.setGeometry(QtCore.QRect(10, 80, 181, 41))
        self.viewallcontactsbutt.setObjectName(_fromUtf8("viewallcontactsbutt"))
        self.viewallreferncebutt = QtGui.QPushButton(self.Look_Up)
        self.viewallreferncebutt.setGeometry(QtCore.QRect(220, 80, 171, 41))
        self.viewallreferncebutt.setObjectName(_fromUtf8("viewallreferncebutt"))
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
        self.dateEdit.setGeometry(QtCore.QRect(10, 50, 78, 21))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_3 = QtGui.QLabel(self.Add)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 31, 16))
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
        self.label_4.setGeometry(QtCore.QRect(160, 30, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.addsql_submitt = QtGui.QPushButton(self.Add)
        self.addsql_submitt.setGeometry(QtCore.QRect(340, 200, 51, 31))
        self.addsql_submitt.setObjectName(_fromUtf8("addsql_submitt"))
        self.label_6 = QtGui.QLabel(self.Add)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.descpt_inout = QtGui.QPlainTextEdit(self.Add)
        self.descpt_inout.setGeometry(QtCore.QRect(10, 100, 381, 91))
        self.descpt_inout.setObjectName(_fromUtf8("descpt_inout"))
        self.clientcombo = QtGui.QComboBox(self.Add)
        self.clientcombo.setGeometry(QtCore.QRect(280, 50, 111, 21))
        self.clientcombo.setObjectName(_fromUtf8("clientcombo"))
        self.label_7 = QtGui.QLabel(self.Add)
        self.label_7.setGeometry(QtCore.QRect(280, 30, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.clientcontacts = QtGui.QPushButton(self.Add)
        self.clientcontacts.setGeometry(QtCore.QRect(130, 200, 91, 31))
        self.clientcontacts.setToolTip(_fromUtf8(""))
        self.clientcontacts.setObjectName(_fromUtf8("clientcontacts"))
        self.clientreffernceform = QtGui.QPushButton(self.Add)
        self.clientreffernceform.setGeometry(QtCore.QRect(10, 200, 111, 31))
        self.clientreffernceform.setToolTip(_fromUtf8(""))
        self.clientreffernceform.setObjectName(_fromUtf8("clientreffernceform"))
        self.actdelete = QtGui.QPushButton(self.Add)
        self.actdelete.setGeometry(QtCore.QRect(230, 200, 101, 31))
        self.actdelete.setObjectName(_fromUtf8("actdelete"))
        self.label_12 = QtGui.QLabel(self.Add)
        self.label_12.setGeometry(QtCore.QRect(96, 30, 37, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.unit_price = QtGui.QLineEdit(self.Add)
        self.unit_price.setGeometry(QtCore.QRect(96, 50, 26, 21))
        self.unit_price.setPlaceholderText(_fromUtf8(""))
        self.unit_price.setObjectName(_fromUtf8("unit_price"))
        self.tabWidget.addTab(self.Add, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.caddfistname = QtGui.QLineEdit(self.tab)
        self.caddfistname.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.caddfistname.setObjectName(_fromUtf8("caddfistname"))
        self.caddlastname = QtGui.QLineEdit(self.tab)
        self.caddlastname.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.caddlastname.setObjectName(_fromUtf8("caddlastname"))
        self.phonelineEdit_3 = QtGui.QLineEdit(self.tab)
        self.phonelineEdit_3.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.phonelineEdit_3.setObjectName(_fromUtf8("phonelineEdit_3"))
        self.cadddateEdit_2 = QtGui.QDateEdit(self.tab)
        self.cadddateEdit_2.setGeometry(QtCore.QRect(20, 160, 110, 22))
        self.cadddateEdit_2.setObjectName(_fromUtf8("cadddateEdit_2"))
        self.caddaccount = QtGui.QLineEdit(self.tab)
        self.caddaccount.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.caddaccount.setObjectName(_fromUtf8("caddaccount"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(150, 80, 46, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(120, 20, 71, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.caddsumbit = QtGui.QPushButton(self.tab)
        self.caddsumbit.setGeometry(QtCore.QRect(130, 190, 81, 31))
        self.caddsumbit.setObjectName(_fromUtf8("caddsumbit"))
        self.cdelete = QtGui.QPushButton(self.tab)
        self.cdelete.setGeometry(QtCore.QRect(20, 190, 101, 31))
        self.cdelete.setObjectName(_fromUtf8("cdelete"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
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

        #set current client
        #current_client=str(self.clientcombo.currentText())
        
        #set gui date as today's date and formats it 
        today = QtCore.QDate.currentDate()
        self.dateEdit.setDate(today)
        self.dateEdit.setDisplayFormat("MM.dd.yyyy")
        self.cadddateEdit_2.setDate(today)
        self.cadddateEdit_2.setDisplayFormat("MM.dd.yyyy")
        
        #populate the Client list from our client table
        self.populate_clients()

        #populate the activity log list from our activity log table 
        self.populate_activity_log()

        # slots and signals
        # these lines below, call the methods in our gui when an event happens. ie a button is clicked ect. 
        self.retranslateUi(CRM_form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.viewallrbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_query_all_act)
        QtCore.QObject.connect(self.viewallcbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_query_all_client)
        QtCore.QObject.connect(self.exitbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), CRM_form.close)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.c_activity)
        QtCore.QObject.connect(self.addsql_submitt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_sql_act)
        QtCore.QObject.connect(self.clientcontacts, QtCore.SIGNAL(_fromUtf8("clicked()")), self.populate_contact_list)
        QtCore.QObject.connect(self.clientreffernceform, QtCore.SIGNAL(_fromUtf8("clicked()")), self.open_referncefile)
        QtCore.QObject.connect(self.clientcombo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.c_activity)
        QtCore.QObject.connect(self.viewallcontactsbutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.populate_contact_list)
        QtCore.QObject.connect(self.viewallreferncebutt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.open_referncefolder)
        QtCore.QObject.connect(self.caddsumbit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_sql_c)
        QtCore.QObject.connect(self.cdelete, QtCore.SIGNAL(_fromUtf8("clicked()")), self.del_c)
        QtCore.QObject.connect(self.actdelete, QtCore.SIGNAL(_fromUtf8("clicked()")), self.del_act)
        QtCore.QMetaObject.connectSlotsByName(CRM_form)

    def retranslateUi(self, CRM_form):
        CRM_form.setWindowTitle(_translate("CRM_form", "C & RM Activity Log", None))
        self.viewallrbutt.setText(_translate("CRM_form", "View All Activity Records", None))
        self.viewallcbutt.setText(_translate("CRM_form", "View All Client Records", None))
        self.viewallcontactsbutt.setText(_translate("CRM_form", "View All Contacts", None))
        self.viewallreferncebutt.setText(_translate("CRM_form", "View Reference All Forms", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Look_Up), _translate("CRM_form", "Look Up", None))
        self.time_input.setText(_translate("CRM_form", ".2", None))
        self.time_input.setPlaceholderText(_translate("CRM_form", ".2", None))
        self.label_2.setText(_translate("CRM_form", "Date:", None))
        self.label_3.setText(_translate("CRM_form", "Time:", None))
        self.descript_cat_inut.setItemText(0, _translate("CRM_form", "Care Coordination", None))
        self.descript_cat_inut.setItemText(1, _translate("CRM_form", "Correspondence", None))
        self.descript_cat_inut.setItemText(2, _translate("CRM_form", "Onsite Hospital", None))
        self.descript_cat_inut.setItemText(3, _translate("CRM_form", "Phone Call Patient", None))
        self.descript_cat_inut.setItemText(4, _translate("CRM_form", "Medical Record Review", None))
        self.label_4.setText(_translate("CRM_form", "Category:", None))
        self.label_5.setText(_translate("CRM_form", "Description of Activities:", None))
        self.addsql_submitt.setText(_translate("CRM_form", "Submit", None))
        self.label_6.setText(_translate("CRM_form", "Add Activity to the Database:", None))
        self.label_7.setText(_translate("CRM_form", "Client:", None))
        self.clientcontacts.setText(_translate("CRM_form", "Client Contacts", None))
        self.clientreffernceform.setText(_translate("CRM_form", "Client Refrence Form", None))
        self.actdelete.setText(_translate("CRM_form", "Delete Last Entry", None))
        self.label_12.setText(_translate("CRM_form", "Price:", None))
        self.unit_price.setText(_translate("CRM_form", "100", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add), _translate("CRM_form", "Add Activity", None))
        self.label_8.setText(_translate("CRM_form", "First Name:", None))
        self.label_9.setText(_translate("CRM_form", "Last Name:", None))
        self.label_10.setText(_translate("CRM_form", "Phone Number:", None))
        self.label_11.setText(_translate("CRM_form", "Date of Birth:", None))
        self.caddsumbit.setText(_translate("CRM_form", "Submit", None))
        self.cdelete.setText(_translate("CRM_form", "Delete Last Entry", None))
        self.label_13.setText(_translate("CRM_form", "Account:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CRM_form", "Add Client", None))
        self.exitbutt.setText(_translate("CRM_form", "Exit", None))
        self.label.setText(_translate("CRM_form", "Client Information", None))
        self.actionTestaction.setText(_translate("CRM_form", "Testaction", None))

    def place_holder(self):
        '''
        Simple place holder function
        '''
        pass
        #print"This is only a test.\n This functionality has not been implemented yet. But it will be soon .... "
    
    def sql_connect(self):
        '''
        Connects to your SQLlite data base and returns the session object
        '''
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        #database = 'index.db'
        #conn = sqlite3.connect(database)
        #instantiate our engine #C:\Users\Andrew\Documents\CRM\db Tests\
        engine = create_engine('sqlite:///CRM.sqlite', echo=False)
 
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        return session
 
    def sqltotext_act(self,o,i):
        '''

        '''
        #for the act_log table
        #needs the o as an iterable, and the sqlachemy object i
        # needs to deal with characters like \ and suchbefore the start of a decrpt ect.
        g = {0:i.client_id, 1:i.date, 2:i.descp_cat, 3:i.time, 4:i.total, 5:i.descp}
        y = g[o]
  
        item = QtGui.QTableWidgetItem()
        item.setText(str(y))
        return item
    
    def sqltotext_contact(self,o,i):
        '''

        '''
        #for the act_log table
        #needs the o as an iterable, and the sqlachemy object i
        # needs to deal with characters like \ and suchbefore the start of a decrpt ect.
        g = {0:'PROVIDER_NAME',1:'SPECIALITY', 2:'PHONE',3:'ADDRESS', 4:'Miles'}
        y = g[o]
  
        item = QtGui.QTableWidgetItem()
        item.setText(str(y))
        return item

    def sqltotext_client(self,o,i):
        '''
        returns a SQL querry result from the client table as a QtGui item so it can be 
        populated in a QtGui listWidget.
        '''
        #for the client table
        #needs the o as an iterable, and the sqlachemy object i
        # needs to deal with characters like \ and suchbefore the start of a decrpt ect.
        g = {0 : i.client_id, 1 : i.first_name, 2 : i.last_name, 3 : i.dob, 4 : i.phone_number, 5 : i.account}
        y = g[o]
        item = QtGui.QTableWidgetItem()
        item.setText(str(y))
        return item
        
    def clienttable_build(self, res):
        '''
        Creates and fills the client table in our Gui
        '''
        
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(6)

        #set main table headers
        for d in xrange(0,6):

            h = {0:'Client Id',1:'First Name', 2:'Last Name',3:'D.O.B.', 4:'Phone number',5: 'Account'}
            header_item = h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate main table
        for e,i in enumerate(res):
            for o in xrange(0,6):
                self.tableWidget.setItem(e, o, self.sqltotext_client(o,i))
   
    def tableMain_build_act(self,res):
        '''
        etup our table for displaying activity log info
        '''
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(5)

        #set headers
        for d in xrange(0,5):
            h = {0:'Client Id',1:'Date', 2:'Description',3:'Time', 4:'Total'} 
            header_item = h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_act(o,i))
    
    def tableMain_build_contact(self,res):
        '''
        Setup our table for displaying contacts
        '''
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(5)

        #set headers
        for d in xrange(0,5):
            h = {0:'PROVIDER_NAME',1:'SPECIALITY', 2:'PHONE',3:'ADDRESS', 4:'Miles'} 
            header_item = h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_act(o,i))

    def sql_query_all_act(self):
        '''
        queries all activities in database
        '''
        #connect to the database
        session = self.sql_connect() 

        # how to do a SELECT * (i.e. all)
        res = session.query(act_log).order_by("Date desc").all()
        #build table
        self.tableMain_build_act(res)
    
        
    def sql_query_all_client(self):
        '''
        queries all clients
        '''
        #connect to database
        session = self.sql_connect()
 
        # how to do a SELECT * (i.e. all)
        res = session.query(client).all()
        #build table
        self.clienttable_build(res)


    
    def add_sql_act(self):
        '''
        adds activity and repopulates table
        '''
        import datetime
        #Connect to sever
        session = self.sql_connect()
        
        c = self.clientcombo.currentText()
        c = self.c_activity(c)
        print c # debug
        u = self.unit_price.text()

        raw_date = str(self.dateEdit.text()) 
        d = datetime.datetime.strptime(raw_date, "%m.%d.%Y")
        
        #get and incriment primary key
        res_id = session.query(act_log).order_by('transaction_id desc').first()
        e = res_id.transaction_id
        e += 1


        add_log = act_log(
                            transaction_id=e, client_id=str(c), date=d, 
                            descp=str(self.descpt_inout.toPlainText()), 
                            descp_cat=str(self.descript_cat_inut.currentText()), 
                            time=float(self.time_input.text()), unit_price=str(u), 
                            total=(int(u)*float(self.time_input.text()))
                            )

        session.add(add_log)
        session.commit()
        rec_act = e
        #update main table
        res = session.query(act_log).filter(act_log.client_id == str(c)).order_by("transaction_id desc").all()
        self.tableMain_build_act(res)
    
    def add_sql_c(self):
        '''
        adds client and repopulates table
        '''
        import datetime
        
        session = self.sql_connect()

        res_id = session.query(client).order_by('client_id desc').first()
        e = int(res_id.client_id)
        e += 1

        d = str(self.cadddateEdit_2.text())
        d = datetime.datetime.strptime(d, "%m.%d.%Y")
    
        add_c = client(
                        client_id=e, first_name=str(self.caddfistname.text()), 
                        last_name=str(self.caddlastname.text()), dob=d, 
                        phone_number=str(self.phonelineEdit_3.text()), 
                        account=str(self.caddaccount.text())
                        )

        session.add(add_c)
        session.commit()
        rec_client = e
       
        #update main table
        self.populate_clients()

        res = session.query(client).all()

        self.clienttable_build(res)


    def del_act(self):
        '''
        deletes addded activity
        '''
        print "test"
        #connect to the database
        #  session=self.sql_connect()        
        # # if not(rec_act ==""):
        #  session.query(act_log).filter(act_log.transaction_id==rec_act).delete()
        #  res=session.query(act_log).order_by("Date desc").all()
        #  self.tableMain_build_act(res)

    def del_c(self):
        '''
        deletes added contact
        '''
        print "test"
        #connect to the database
        # session=self.sql_connect()
        # session.query(client).filter(client.client_id==rec_client).delete()
        # res=session.query(client).all()
        # self.clienttable_build(res)


    def c_activity(self, item):
        '''
        dynamically populates the main table based on which contact is clicked on the list widget
        '''
        #maket his on click function set the value of that combo box and bring up activity to that patient. thus easy input
        import re
        session = self.sql_connect()
        
        if type(item) == QtCore.QString:
            item = str(item)
            s = re.split(", ", item)
            s0 = s[0]
            s1 = s[1]
            #current_client=s0+" "+s1
        
        if type(item) == QtGui.QListWidgetItem:
            item = item.text()
            s = re.split(", ", item)
            s0 = str(s[0])
            s1 = str(s[1])
            #current_client=s0+" "+s1

         
        resc =session.query(client).filter((client.last_name == s1) and (client.frist_name == s0))

        for i in resc:
            v = i.client_id
            print v  
        
        res = session.query(act_log).filter(act_log.client_id == v).all()

        #build table
        self.tableMain_build_act(res)

        return v


    def populate_clients(self):
        '''
        populates the client list when the UI first init
        '''
        # connect to db
        session = self.sql_connect()
        #Clears list for clean refreses
        self.listWidget.clear()
        self.clientcombo.clear()
        # how to do a SELECT * (i.e. all)
        res = session.query(client).all()
        for e,i in enumerate(res):
            s = i.first_name
            s = s + ", " + i.last_name
            item = QtGui.QListWidgetItem(s)
            self.listWidget.addItem(item)
            self.clientcombo.addItem(str(item.text()))
       

    def populate_activity_log(self):
        '''
        Populates the activity log results when the UI first INIT
        '''
        session = self.sql_connect()
        
        res = session.query(act_log).order_by("Date desc").limit(9)

        #Setup our table 
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(5)
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        #set headers
        for d in xrange(0,5):
            h = {0:'Client Id',1:'Date', 2:'Description',3:'Time', 4:'Total'}
            header_item = h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_act(o,i))
    
    def populate_contact_list(self):
        '''
        Populates the client contact list
        '''
        session = self.sql_connect()
        #session.query(contact).filter(contact.client_id == rec_client)
        res = session.query(contact).limit(9)

        #Setup our table 
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(5)
        #self.tableWidget = QtGui.QTableWidget(CRM_form) 
        #set headers
        for d in xrange(0,5):
            h = {0:'PROVIDER_NAME',1:'SPECIALITY', 2:'PHONE',3:'ADDRESS', 4:'Miles'}
            header_item = h[d]
            self.tableWidget.setHorizontalHeaderItem(d,QtGui.QTableWidgetItem(header_item))

        #populate table
        for e,i in enumerate(res):
            for o in xrange(0,5):
                self.tableWidget.setItem(e, o, self.sqltotext_contact(o, i)(o,i))
    
    def open_referncefolder(self):
        '''
        opens reference form pdf folder.
        '''
        import os
        os.startfile('C:\Users\Andrew\Documents\CRM\db Tests\Reference Forms') # opens explorer at C:\ drive

    def open_referncefile(self):
        ''''
        opens reference form pdf file. 
        '''
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

