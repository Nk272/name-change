import sqlite3
import pandas as pd
filename="Final Data for portal.xlsx"
dbname="parts"
con=sqlite3.connect(dbname+".db")
df=pd.read_excel(filename,sheet='Sheet1')
df.to_sql("Participants",con,index=False,if_exists="replace")
con.commit()
con.close()