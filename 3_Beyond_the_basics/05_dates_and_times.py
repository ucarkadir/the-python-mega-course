# from datetime import datetime

# from dan sonra yazılan modül ismi
# import dan sonra yazılan obje ismi


from datetime import datetime
delta = datetime.now() - datetime(1900, 12, 31)
delta.days
delta.seconds
datetime.now() # datetime.datetime(2018,3,2,20,5,22,940778)

dir(datetime) 
now = datetime.now()
now

then = datetime(1900, 12,31, 20,12, 59,84845)
now
then - now
# datetime.timedelta(-43007, 70795, 272487) 

then = datetime(1900,12,31,20,12,59,83845)
now = datetime.now()
whenever = datetime.strptime("2017-12-31","%Y-%m-%d") # datetime.datetime(2017, 12, 31, 0, 0)
whenever = datetime.strptime("2017:12:31:20:59","%Y:%m:%d:%H:%M") # datetime.datetime(2017, 12, 31, 20, 59)

whenever.strftime("%Y") # Uyarı: yazım şekli farklı, '2017'
whenever.strftime("%Y-%m-%d %H:%M") # '2017-12-31 20:59'

whenever.month # 12
whenever.year # 2017
whenever.day # 31
