def connect_db():
    try:
        connection = pymysql
    except:
        print("DB connection ")