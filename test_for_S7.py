import sqlite3
import pandas as pd

con = sqlite3.connect(r'C:\Users\m.sentyabov\Desktop\mytest.db')
wb = pd.read_excel(r'C:\Users\m.sentyabov\Desktop\Книга2.xlsx')

wb.to_sql(name='tst_flights', con=con, if_exists='replace', index=True)
con.commit()
con.close()
