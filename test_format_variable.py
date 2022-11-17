import DataBase as db
import VitalityBooster as vb
logic_union = 'Группы конкурентов'
select = '''select *
                    from static.parsing_vk pv
                where pv.logic_union like '%{logic_union}%' '''
datalake = vb.MessengerSQL(db.PostgreSQL_Datalake())
datalake.connect()
df = datalake.send_command(select.format(logic_union=logic_union))
print(df)
