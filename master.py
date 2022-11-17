import DataBase as dbase
import VitalityBooster as vb
import datetime
import pandas as pd
date_list = []
get_days = '''select *
                   from location_address_accesses_daytime laad
               where address_access_id='b8a65b99-f05f-4c9f-bdad-6454dc7d6d63';'''

get_data = '''select laa.name,
                     laa.address,
                     laa.email,
                     laa.is_send_email,
                     laa.phone,
                     laa.is_call_before_day,
                     laa.call_in_hour,
                     laa.call_time_from,
                     laa.call_time_to
                    from location_address_accesses laa
                where laa.id='b8a65b99-f05f-4c9f-bdad-6454dc7d6d63';'''
if __name__ == '__main__':
    datalake = vb.MessengerSQL(dbase.PostgreSQL_Master())
    datalake.connect()

    week_schedule = datalake.send_command(get_days)
    main_data = datalake.send_command(get_data)
    print(week_schedule['time_from'], week_schedule['time_to'])
    for i in range(7):
        # from_obj = datetime.datetime.strptime(str(week_schedule.iloc[i]['time_from']), "%d-%b-%Y %H:%M:%S").time()
        # to_obj = datetime.datetime.strptime(str(week_schedule.iloc[i]['time_to']), "%d-%b-%Y %H:%M:%S").time()
        date_list.append(pd.to_datetime(week_schedule.iloc[i]['time_from']))
        date_list.append(pd.to_datetime(week_schedule.iloc[i]['time_to']))
    print()
    print(date_list, len(date_list))
    main_data[["monday_from", "monday_to", "tuesday_from", "tuesday_to", "wednesday_from", "wednesday_to",
               "thursday_from", "thursday_to", "friday_from", "friday_to", "saturday_from", "saturday_to",
               "sunday_from", "sunday_to"]] = date_list
    print(main_data)
