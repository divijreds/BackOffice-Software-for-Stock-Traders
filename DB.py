import sqlite3
#sqlite3.connect(:memory:)
db = sqlite3.connect('e:\TradeBook') 
cursor = db.cursor()
cursor.execute('''create table tradebook(Server varchar(20), UserID varchar(20), ATINTradeID varchar(20), ATINOrderID varchar(20), OrderID varchar(20), ExchangeOrderNo varchar(20), ExchangeTradeID varchar(20), OrderTime varchar(20), ExchangeOrderTime varchar(20), ExchangeTradeTime varchar(20) ,Exchange varchar(20), SecurityID varchar(20), Symbol varchar(20), ExpiryDate varchar(20), SecurityType varchar(20), OptionType varchar(20), Side varchar(20), OrderType varchar(20), Quantity varchar(20), PendingQuantity varchar(20), Price varchar(20), Strikeprice varchar(20), ClientID varchar(20), ReferenceText varchar(20), ManagerID varchar(20), MemberID varchar(20), StrategyID varchar(20), CTCLID varchar(20), ProductType varchar(20), OpenClose varchar(20), Multiplier varchar(20), Pancard varchar(20), TerminalInfo varchar(20), AlgoID varchar(20), AlgoCategory varchar(20), ParticipantID varchar(20), Amount varchar(20), Id varchar(20))''')
db.commit()
print('New Table created...')