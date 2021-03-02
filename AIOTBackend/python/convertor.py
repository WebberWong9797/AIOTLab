import mysql.connector
from mysql.connector import Error
def insertVariblesIntoTable(avg_temp, avg_humid, avg_ph, date, hour, dataCount, SN):
    try:
        connection = mysql.connector.connect(host='10.0.0.70',
                                         database='AIoT_Farming',
                                         user='webber',
                                         password='webber')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO avg_data (avg_temp, avg_humid, avg_ph, date, hour, dataCount, SN) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s) """

        recordTuple = (avg_temp, avg_humid, avg_ph, date, hour, dataCount, SN)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
try:
    connection = mysql.connector.connect(host='10.0.0.70',
                                         database='AIoT_Farming',
                                         user='webber',
                                         password='webber')

    sql_select_Query = "select * from sensors"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in sensors is: ", cursor.rowcount)

    print("\nPrinting each sensors record")
    prevHour = 0
    sum_h = 0
    sum_t = 0
    sum_p = 0
    count = 1
    newlist = list()
    for row in records:
        currHour = row[2].hour
        if(prevHour != currHour):
            newlist.append(sum_h/count)
            insertVariblesIntoTable(round(sum_t/count,2), round(sum_h/count,2), round(sum_p/count,2), row[2], prevHour, count, row[3])
            print(row[0], prevHour, round(sum_h/count,2), round(sum_t/count,2), round(sum_p/count,2), count)
            prevHour = currHour
            sum_h = 0
            sum_t = 0
            sum_p = 0
            count = 0
        sum_h = sum_h + row[4]
        sum_t = sum_t + row[5]
        sum_p = sum_p + row[6]
        count = count + 1
    newlist.append(sum_h/count)
    print(row[0], prevHour, sum_h/count, sum_t/count, sum_p/count, count)
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


