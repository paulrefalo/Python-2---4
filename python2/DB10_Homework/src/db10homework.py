""" SELECT from tables animal and food
and check to be sure all animals feed column is not NULL

mysql -h sql -u prefalo -p prefalo
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("""
                SELECT name, family, feed FROM animal
                LEFT JOIN food ON animal.id=food.id;
                """)

animalJoinFood = cursor.fetchall()
#print(animalJoinFood)

def hungry(animalJoinFood):
    for feed in animalJoinFood:
        if (feed == None):
            return 'true'
        else:
            return 'false'
        
print("At least one animal is hungry") if hungry(animalJoinFood) else print("All are fed")
        
"""       
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name=table2.column_name;

SELECT name, family, feed FROM animal
                JOIN food ON animal.id=food.anid;
"""