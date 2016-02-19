from settings import RECIPIENTS, STARTTIME, DAYCOUNT
from database import login_info
import email, datetime
import mysql.connector as msc


def emailJOTD(address, date, msgid):
    """
    Create an e-mail 
    """
    msg = email.message_from_string("This is a test message.")
    msg['Date'] = date.strftime("%Y-%m-%d")
    msg['From'] = "website@example.com"
    msg['To'] = address
    msg['Message-Id'] = msgid
    return msg

def sqlJOTD(daycount):
    """
    Same to table messages.
    DANGER: any messages table will be deleted.
    mysql -h sql -u prefalo -p prefalo
    """
    
    TBLDEF = """\
    CREATE TABLE messages (
     ID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgDate DATETIME,
     msgText LONGTEXT
    ) ENGINE = MYISAM"""
    
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS messages")
    curs.execute(TBLDEF)
    
    for address in RECIPIENTS:
        date = STARTTIME 
        for mid in range(1, daycount + 1):                         
            msg = emailJOTD(address[1], date, str(mid))
            text = msg.as_string()
            datestr = msg['Date']
            print(datestr, text)
            curs.execute("INSERT INTO messages (msgDate, msgText) VALUES (%s, %s)", (datestr, text))  
            date = date + datetime.timedelta(days=1)         
    conn.close()

if __name__=="__main__":
    for n in range(3):
        print(emailJOTD(RECIPIENTS[n][1], STARTTIME, "1"))
    sqlJOTD(DAYCOUNT[0])