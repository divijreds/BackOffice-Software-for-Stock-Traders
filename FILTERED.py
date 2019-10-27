# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:15:48 2019

@author: Divijreds
"""

from PyQt5 import uic, QtCore, QtGui, QtWidgets
import pandas as pd
import csv
import pdfkit as pdf

df=pd.DataFrame()

global user_id,exchange,client_id,symbol,option_type,strike_price,expiry_date,side,path
global s_user_id,s_exchange,s_client_id,s_symbol,s_expiry_date,s_strike_price,s_option_type,s_side

Flis=[]
Id_lis=[]

#remove duplicate
def remove_duplicate(lis):
    tempo=[]
    for x in lis:
        if x not in tempo:
            tempo.append(x)
    lis=tempo
    return lis

#search
def search1(temp,s_):
    temp=temp[s_]
    return temp

class CheckableComboBox(QtWidgets.QComboBox):
    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

    def checkedItems(self):
        self.one=[]
        for index in range(self.count()):
            item = self.model().item(index)
            if(item.checkState() == QtCore.Qt.Checked):
                self.one.append(str(item.text()))
                #print(self.one)
        return self.one

qtCreaterFile = "Backoffice_Layout.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreaterFile)
class Ui_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.user_id=[]
        self.exchange=[]
        self.client_id=[]
        self.symbol=[]
        self.expiry_date=[]
        self.strike_price=[]
        self.option_type=[]
        self.side=[]
        self.report=pd.DataFrame()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def loadData(self,Form):
        self.tableWidget.clearContents()
        t=self.temp1
        
        #user id
        s_user_id=self.comboBox_2.checkedItems()
        #print(s_user_id)
        if(s_user_id==None or s_user_id==[]):
            pass
        elif(s_user_id==['All']):
            #self.comboBox_2.setChecked(True)
            pass
        elif(s_user_id!=['']):
            Q_userid=t.UserID.isin(s_user_id)
            t=search1(t,Q_userid) 

        #exchange
        s_exchange=self.comboBox_3.checkedItems()
        #print(s_exchange)
        if(s_exchange==None or s_exchange==[]):
            pass
        elif(s_exchange==['All']):
            #self.CheckableComboBox.setChecked(True)
            pass
        elif(s_exchange!=['']):
            Q_exchange=t.Exchange.isin(s_exchange)
            t=search1(t,Q_exchange) 

        #client id
        s_client_id=self.comboBox_4.checkedItems()
        #print(s_exchange)
        if(s_client_id==None or s_client_id==[]):
            pass
        elif(s_client_id==['All']):
            pass
        elif(s_client_id!=['']):
            Q_clientid=t.ClientID.isin(s_client_id)
            t=search1(t,Q_clientid) 

        #symbol     
        s_symbol=self.comboBox_5.checkedItems()
        print(s_symbol)
        if(s_symbol==None or s_symbol==[]):
            pass
        elif(s_symbol==['All']):
            pass
        elif(s_symbol!=['']):
            Q_symbol=t.Symbol.isin(s_symbol)
            t=search1(t,Q_symbol)

        #print(t)
        
        #side    
        s_side=self.comboBox_6.checkedItems()
        print(s_side)
        if(s_side==None or s_side==[]):
            pass
        elif(s_side==['All']):
            pass
        elif(s_side!=['']):
            Q_side=t.Side.isin(s_side)
            t=search1(t,Q_side)        
        
        #exp date
        s_expiry_date=self.comboBox_7.checkedItems()
        if(s_expiry_date==None or s_expiry_date==[]):
            pass
        elif(s_expiry_date==['All']):
            pass
        elif(s_expiry_date!=['']):
            Q_exp=(t.ExpiryDate.isin(s_expiry_date))
            t=search1(t,Q_exp)
        
        #print(t)
            
        self.shape1=t.shape
        self.df_row=self.shape1[0]
        self.df_col=self.shape1[1]
        
        for i in range(self.df_row):
            for j in range(self.df_col):
                x = str(t.iloc[i,j])
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(x))
        self.report=t 
        print(self.report)
        
    def G_report(self, Form):
        #self.report= pd.read_csv('1.csv')
        usr=self.report["UserID"].unique()
        sym=[]
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=path_wkthmltopdf)
        inp=str(''' <html>
            <head><h1><center><b>TRADE REPORT</b></center></h1></head><body>''')
        for i in range(len(usr)):
            con=('''
            <h3> For User %s </h3>
            <table border="1" class="self.reportframe">
            <thead>
            <tr style="text-align: center;">
            <th>UserID:</th>
            <th>ClientID: </th>
            <th>Symbol: </th>
            <th>Exchange: </th>
            <th>ExpiryDate: </th>
            <th>Buy Quantity: </th>
            <th>Buy Average: </th>
            <th>Sell Quantity: </th>
            <th>Sell Average: </th>
            <th>Gross Profit: </th>
            <th>Brokerage: </th>
            <th>Net Profit </th>
            </tr>
            </thead>
            <tbody>
            '''%usr[i])
            inp=inp+con
            sym1=self.report.loc[self.report["UserID"]==usr[i],["Symbol"]]
            sym1=sym1["Symbol"].unique()
            sym.append(sym1)
            #print(sym)
            for j in range(len(sym[i])):
                #print(usr[i]+" "+sym[i][j])
                cli=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Symbol"]==sym[i][j])  ,["ClientID"]]
                cli=cli["ClientID"].unique()
                exc=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Symbol"]==sym[i][j]) ,["Exchange"]]
                exc=exc["Exchange"].unique()
                exp=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Symbol"]==sym[i][j]) ,["ExpiryDate"]]
                exp=exp["ExpiryDate"].unique()
                Bqut=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Side"]=="Buy") & (self.report["Symbol"]==sym[i][j]) ,["Quantity"]]
                Bqut=Bqut.sum()
                Bqut=Bqut[0]    
                Bpri=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Side"]=="Buy") & (self.report["Symbol"]==sym[i][j]) ,["Price"]]
                Bpri=Bpri.sum()
                Bpri=Bpri[0]
                Bavg=float(Bpri/Bqut)
                #print(str(Bpri)+" "+str(Bqut)+" "+str(Bavg))
                Squt=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Side"]=="Sell") & (self.report["Symbol"]==sym[i][j]) ,["Quantity"]]
                Squt=Squt.sum()
                Squt=Squt[0]
                Spri=self.report.loc[(self.report["UserID"]==usr[i]) & (self.report["Side"]=="Sell") & (self.report["Symbol"]==sym[i][j]) ,["Price"]]
                Spri=Spri.sum()
                Spri=Spri[0]
                Savg=float(Spri/Squt)
                Gpro=Spri-Bpri
                Brk=float(1)
                Npro=(Gpro-((Gpro*Brk)/100))
                #print(str(Spri)+" "+str(Squt)+" "+str(Savg))
                #print(str(Gpro)+" "+str(Npro))
                con=('''
                    <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%d</td>
                    <td>%.3f</td>
                    <td>%d</td>
                    <td>%.3f</td>
                    <td>%.3f</td>
                    <td>%.3f</td>
                    <td>%.3f</td>
                    </tr>
                    '''%(usr[i],cli,sym[i][j],exc,exp,Bqut,Bavg,Squt,Savg,Gpro,Brk,Npro))
                inp=inp+con
            inp=inp+('''</tbody></table>''')
        inp=inp+('''</body> </html>''')
        fname=("report.pdf")
        pdf.from_string(inp,fname,configuration=config)
   
        
    def getCSV(self, Form):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open file','C:/Users/admin/Desktop/Internship')
        if filePath != "":
            print("Address",filePath)
            df = pd.read_csv(str(filePath))
            self.temp1=pd.DataFrame()
            self.temp1=df
            self.label=self.temp1.columns.tolist()
            self.tableWidget.setHorizontalHeaderLabels(self.label)
            with open(str(filePath), 'r',encoding='utf-8',errors='ignore') as csvFile:
                reader = csv.reader(csvFile)
                next(reader)
                profit=float()
                for row in reader:
                    self.Id=row[1]+row[10]+row[22]+row[12]+row[15]+row[21]+row[13]
                    a=int(row[18])
                    b=float(row[20])
                    c=float(row[30])
                    if(row[16]=="Buy"):
                        profit=(-1*a*b*c)
                    else:
                        profit=(a*b*c)
                    if self.Id not in Id_lis:
                        Id_lis.append(self.Id)
                        self.user_id.append(row[1])
                        self.exchange.append(row[10])
                        self.client_id.append(row[22])
                        self.symbol.append(row[12])
                        self.option_type.append(row[15])
                        self.strike_price.append(row[21])
                        self.side.append(row[16])
                        self.expiry_date.append(row[13])
                        self.side.append(row[16])
                        Flis.append([self.Id,profit])
                    elif self.Id in Id_lis:
                        temp=Id_lis.index(self.Id)
                        profit=profit+(Flis[temp][1])
                        Flis[temp][1]=profit
                self.user_id=remove_duplicate(self.user_id)
                self.exchange=remove_duplicate(self.exchange)
                self.client_id=remove_duplicate(self.client_id)
                self.symbol=remove_duplicate(self.symbol)
                self.option_type=remove_duplicate(self.option_type)
                self.strike_price=remove_duplicate(self.strike_price)
                self.expiry_date=remove_duplicate(self.expiry_date)
                self.side=remove_duplicate(self.side)
                
                self.comboBox_2.addItem("All")
                for i in self.user_id:
                    self.comboBox_2.addItem(i)
                
                
                self.comboBox_3.addItem("All")
                for i in self.exchange:
                    self.comboBox_3.addItem(i)
                
                self.comboBox_4.addItem("All")
                for i in self.client_id:
                    self.comboBox_4.addItem(i)
                
                self.comboBox_5.addItem("All")
                for i in self.symbol:
                    self.comboBox_5.addItem(i)
                
                self.comboBox_6.addItem("All")                
                for i in self.side:
                    self.comboBox_6.addItem(i)
                
                self.comboBox_7.addItem("All")    
                for i in self.expiry_date:
                    self.comboBox_7.addItem(i)
                
    def setupUi(self, Form):
        Form.resize(847, 592)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 540, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.G_report)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 60, 181, 31))
        self.pushButton_2.clicked.connect(self.getCSV)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(400, 120, 51, 21))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 120, 51, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(520, 120, 51, 21))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = CheckableComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 120, 61, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = CheckableComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 120, 71, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = CheckableComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 120, 61, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = CheckableComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(440, 120, 71, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = CheckableComboBox(Form)
        self.comboBox_6.setGeometry(QtCore.QRect(550, 120, 51, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = CheckableComboBox(Form)
        self.comboBox_7.setGeometry(QtCore.QRect(680, 120, 81, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(610, 120, 61, 21))
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 791, 361))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(111)
        self.tableWidget.setColumnCount(38)
        self.tableWidget.setObjectName("tableWidget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Back Office Software"))
        self.pushButton.setText(_translate("Form", "Show Data"))
        self.pushButton_2.setText(_translate("Form", "Import CSV File"))
        self.pushButton_3.setText(_translate("Form", "Report"))
        self.label_6.setText(_translate("Form", "Symbol:"))
        self.label_5.setText(_translate("Form", "Client ID:"))
        self.label_3.setText(_translate("Form", "User ID:"))
        self.label_4.setText(_translate("Form", "Exchange:"))
        self.label_7.setText(_translate("Form", "Side:"))
        self.label_8.setText(_translate("Form", "Expiry Date:"))

if __name__ == "__main__":
    import sys
    user_id=[]
    exchange=[]
    client_id=[]
    symbol=[]
    expiry_date=[]
    strike_price=[]
    option_type=[]
    side=[]
    s_user_id=[]
    s_exchange=[]
    s_client_id=[]
    s_symbol=[]
    s_expiry_date=[]
    s_strike_price=[]
    s_option_type=[]
    s_side=[]
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
#                    User ID: %s </br>
#                Client ID: %s </br>
#                Symbol: %s </br>
#                Exchange: %s </br>
#                Expiry Date: %s </br>
#                Buy Quantity: %d </br>
#                Buy Average: %.3f </br>
#                Sell Quantity: %d </br>
#                Sell Average: %.3f </br>
#                Gross Profit: %.3f </br>
#                Brokerage: %.3f %% </br>
#                Net Profit: %.3f </br>