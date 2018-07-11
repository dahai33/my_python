# #!/usr/bin/python3
# #Author:刘海涛
# # --*-- coding: uft-8 --*--
# # @Time   : 16:26
# #is mysql
# import pymysql
# import appium
# db=pymysql.connect("localhost",port=3660,user="root",password="password",db="testDB",charset="utf8mb4")
# cursor=db.cursor()
# sql="""select * from stundet where name='tomcat';"""
# print(sql)
# cursor.execute(sql)
# db.commit()
# #insert
# # insert_sql="""insert into student ("name",age,"school","sex") vluses ("tome",12,"shangliu","man");"""
# # try:
# #     cursor.execute(insert_sql)
# #     db.commit()
# # except:
# #     db.rollback()
# # db.close()
#
# #db.close()
# inset_1="""insert into student values ("%d","%s","%s")"""
# cursor.execute(inset_1,[("1","2","3"),("3","4","5")])
# user_id=12
# user_name="liuhaitao"
# try:
#     cursor.execute("""insert into student values ("%d" ,"%s") %(user_id,user_name)""")
#     db.commit()
# except:
#     db.rollback()
# db.close()
# ####返回查询结果集
# select_sql="""select * from student  where id >'%d' % (100)"""
# try:
#     cursor.execute(select_sql)
# #接受所有返回的行
#     resout=cursor.fetchall()
# #如下返回的是一个结果集对象
#     resout_1=cursor.fetchone()
# #如下返回影响的行数
#     resout_2=cursor.rowcount()
#     if(resout!=None):
#         for row in cursor.fetchmany(resout_1)
#             print row
#
#     for row in resout:
#         fname=row[0]
#         fage=row[1]
#         fschool=row[2]
#         fsex=row[3]
#         print("fname=%s","fage=%d","fschool=%s","fsex=%s"(fname,fage,fschool,fsex))
# except:
#     print(Exception)
# finally:
#     db.close()