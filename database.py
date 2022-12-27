import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome",
    database="airline_reservation_system"
)
c=c = mydb.cursor()

def show_tables():
    c.execute("SHOW TABLES")
    data1=c.fetchall()
    return data1

def view_airline_company():
    c.execute("SELECT * FROM AIRLINE_COMPANY")
    data2=c.fetchall()
    return data2

def view_airplane():
    c.execute("SELECT * FROM AIRPLANE")
    data3=c.fetchall()
    return data3

def view_airport():
    c.execute("SELECT * FROM AIRPORT")
    data4=c.fetchall()
    return data4

def view_traveller():
    c.execute("SELECT * FROM TRAVELLER")
    data5=c.fetchall()
    return data5

def view_traveller_i():
    c.execute("SELECT * FROM TRAVELLER_ITINERARY")
    data6=c.fetchall()
    return data6

def view_port_access():
    c.execute("SELECT * FROM PLANE_PORT_ACCESS")
    data7=c.fetchall()
    return data7

def view_flight_trip():
    c.execute("SELECT FLIGHT_TRIP_ID,DEPART_AIRPORT,DEPART_TIME,ARRIVAL_AIRPORT,ARRIVAL_TIME,USER_EMAIL,DISTANCE,AMOUNT,CURRENCY FROM FLIGHT_TRIP")
    data8=c.fetchall()
    return data8

def view_planes(From,To):
    c.execute(' SELECT AIRPLANE FROM PLANE_PORT_ACCESS WHERE AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}") AND AIRPLANE IN (SELECT AIRPLANE FROM PLANE_PORT_ACCESS WHERE AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}"));'.format(From,To))
    data11=c.fetchall()
    return data11

def add_traveller(fname,lname,phone,email):
    c.execute('INSERT INTO TRAVELLER(FNAME, LNAME, PHONE, EMAIL) VALUES (%s,%s,%s,%s)',(fname,lname,phone,email))
    mydb.commit()

def view_seats(plane,seat_type,depart_time,arrival_time):
    c.execute('SELECT SEAT_NO FROM SEAT WHERE AIRPLANE="{}" AND SEAT_CLASS="{}" AND AVAILABILITY = "YES" AND DEPART_TIME = "{}" AND ARRIVAL_TIME = "{}"'.format(plane,seat_type,depart_time,arrival_time))
    data12=c.fetchall()
    return data12

def get_airplane_time(list_of_planes,Depart,Arrive):
    list_of_planes1=tuple(list_of_planes)
    c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO IN {} AND DEPART_AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}") AND ARRIVAL_AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}");'.format(list_of_planes1,Depart,Arrive))
    data13=c.fetchall()
    return data13

def add_flight_trip(flight_trip_id,depart_airport,depart_time,arrival_airport,arrival_time,email,distance):
    c.execute('INSERT INTO FLIGHT_TRIP(FLIGHT_TRIP_ID,DEPART_AIRPORT,DEPART_TIME,ARRIVAL_AIRPORT,ARRIVAL_TIME,USER_EMAIL,DISTANCE) VALUES (%s,%s,%s,%s,%s,%s,%s)',(flight_trip_id,depart_airport,depart_time,arrival_airport,arrival_time,email,distance))
    mydb.commit()

def get_airplane_time_i(plane,Depart,Arrive):
    plane1=str(plane)
    c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO = "{}" AND DEPART_AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}") AND ARRIVAL_AIRPORT IN (SELECT AIRPORT_CODE FROM AIRPORT WHERE CITY="{}");'.format(plane,Depart,Arrive))
    data13=c.fetchall()
    return data13

def get_airplane_time_rdu(plane,Depart,Arrive):
    plane1=tuple(plane)
    if Depart == "Raleigh" and Arrive == "Charlotte":
        c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO IN ("AA751") AND DEPART_AIRPORT = "RDU" AND ARRIVAL_AIRPORT = "CLT"')
    elif Depart == "Raleigh" and Arrive == "Dallas":
        c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO IN ("AA751") AND DEPART_AIRPORT = "RDU" AND ARRIVAL_AIRPORT = "DFW"')
    elif Depart == "Dallas" and Arrive == "Raleigh":
        c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO IN ("AA751") AND DEPART_AIRPORT = "DFW" AND ARRIVAL_AIRPORT = "RDU"')
    elif Depart == "Charlotte" and Arrive == "Raleigh":
        c.execute('SELECT * FROM AIRPLANE_AVAILABILITY WHERE AIRPLANE_NO IN ("AA751") AND DEPART_AIRPORT = "CLT" AND ARRIVAL_AIRPORT = "RDU"')
    data13=c.fetchall()
    return data13

def add_flight_trip_i(flight_trip_id,idi,seat,plane):
    flight=str(flight_trip_id)
    idi=int(idi)
    plane=str(plane)
    seat=str(seat)
    c.execute('INSERT INTO TRAVELLER_ITINERARY(FLIGHT,ID,SEAT_NO,AIRPLANE) VALUES (%s,%s,%s,%s)',(flight,idi,seat,plane))
    mydb.commit()

def get_id(fname,lname,phone,email):
    c.execute('SELECT ID FROM TRAVELLER WHERE FNAME="{}" AND LNAME="{}" AND PHONE="{}" AND EMAIL="{}"'.format(fname,lname,phone,email))
    data14=c.fetchall()
    return data14

def update_seat(seat,plane):
    seat1=str(seat)
    c.execute('UPDATE SEAT SET AVAILABILITY = "NO" WHERE SEAT_NO = "{}" AND AIRPLANE = "{}"'.format(seat1,plane))
    mydb.commit()

def view_flight_trip_i(fti):
    c.execute("SELECT FLIGHT_TRIP_ID,DEPART_AIRPORT,DEPART_TIME,ARRIVAL_AIRPORT,ARRIVAL_TIME,USER_EMAIL,DISTANCE,AMOUNT,CURRENCY FROM FLIGHT_TRIP WHERE FLIGHT_TRIP_ID = '{}'".format(fti))
    data15=c.fetchall()
    return data15

def view_traveller_id(fti):
    c.execute('SELECT TI.FLIGHT,TI.ID,T.FNAME,T.LNAME,T.PHONE,T.EMAIL,TI.SEAT_NO,TI.AIRPLANE FROM TRAVELLER_ITINERARY AS TI,TRAVELLER AS T WHERE TI.ID=T.ID AND TI.FLIGHT="{}"'.format(fti))
    data16=c.fetchall()
    return data16

def delete_traveller(fti):
    c.execute('DELETE FROM TRAVELLER WHERE ID=(SELECT ID FROM TRAVELLER_ITINERARY WHERE FLIGHT="{}")'.format(fti))
    mydb.commit()
    
def delete_traveller_t(fti):
    c.execute('DELETE FROM TRAVELLER_ITINERARY WHERE FLIGHT="{}"'.format(fti))
    mydb.commit()

def delete_flight(fti):
    c.execute('DELETE FROM FLIGHT_TRIP WHERE FLIGHT_TRIP_ID="{}"'.format(fti))
    mydb.commit()

def view_traveller_iti(tid):
    tid1=int(tid)
    c.execute('SELECT * FROM TRAVELLER WHERE ID = {}'.format(tid1))
    data17=c.fetchall()
    return data17

def update_traveller(tid,new_first_name,new_last_name,new_phone,new_email):
    c.execute('UPDATE TRAVELLER SET FNAME = "{}" ,LNAME = "{}",PHONE = "{}",EMAIL= "{}" WHERE ID={}'.format(new_first_name,new_last_name,new_phone,new_email,tid))
    mydb.commit()

def update_flight(fti,email):
    c.execute('UPDATE FLIGHT_TRIP SET USER_EMAIL = "{}" WHERE FLIGHT_TRIP_ID = "{}"'.format(email,fti))
    mydb.commit()

def exec_custom_query(query):
    c.execute(query)
    data = c.fetchall()
    mydb.commit()
    return data

def no_of_seat_yes(airplane_no,depart_time,arrival_time):
    c.execute('select count(seat_no) from seat WHERE SEAT.AVAILABILITY="YES" AND AIRPLANE="{}" AND DEPART_TIME="{}" AND ARRIVAL_TIME="{}"'.format(airplane_no,depart_time,arrival_time))
    data = c.fetchall()
    return data

def no_of_seat_no(airplane_no,depart_time,arrival_time):
    c.execute('select count(seat_no) from seat WHERE SEAT.AVAILABILITY="NO" AND AIRPLANE="{}" AND DEPART_TIME="{}" AND ARRIVAL_TIME="{}"'.format(airplane_no,depart_time,arrival_time))
    data = c.fetchall()
    return data