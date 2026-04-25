import os
from dotenv import load_dotenv
from mysql.connector import *

load_dotenv()

def getConnection():
    return connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )
    
def offerNewCard(**kwargs):
    number = kwargs.get("number")
    name = kwargs.get("name")
    cvv = kwargs.get("cvv")
    bal = kwargs.get("bal")
    con = getConnection()
    cursor = con.cursor()
    qry = "insert into creditcard(cardnumber,holdername,cvv,balance) values(%s,%s,%s,%s)"
    cursor.execute(qry,(number,name,cvv,bal))
    con.commit()
    con.close()
    print("Card created")

def getTransactionByCard(cardid):
    con = getConnection()
    cursor = con.cursor(dictionary=True)
    qry = "select t.TransactionID, c.HolderName, m.MerchantName, t.Amount, t.Date from Transactions t inner join creditcard c on t.CardID = c.CardID inner join Merchant m on t.MerchantID = m.MerchantID where c.CardID = %s"
    cursor.execute(qry,(cardid,))
    data = cursor.fetchall()
    con.close()
    return data
print(getTransactionByCard(2))
# offerNewCard(number=567876567,name="Rajeshwari",cvv=988,bal=200000)