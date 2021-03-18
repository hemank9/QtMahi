import sqlite3
import constants
import json
import os.path

print(r"" + os.pardir + "\\MyDatabase\\" + constants.my_database_name)
conn = sqlite3.connect(constants.path + r"\Mahi\MyDatabase\\" + constants.my_database_name)


def getUserID():
    try:
        cursor = conn.execute("SELECT ID from '" + constants.login_table + "'")

        for row in cursor:
            print("ID = ", row[0])
            return str(row[0])

        return None

    except Exception as e:
        print("Fetch profile details failed : ", e.__class__)
        return None


def createSession(user_id, userstring):
    try:
    # # send userdata json directly in this method when login is successful
    # # user_data = json.loads(userstring)

        initTables()

        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.login_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):

            print("Session available")
            conn.execute(
                "UPDATE " + constants.login_table + " SET LOGIN_JSON='" + userstring + "' WHERE ID='" + user_id + "'")
            conn.commit()
            print("Session Updated successfully")
        else:

            query = "INSERT INTO '" + constants.login_table + "' (ID, LOGIN_JSON) " \
                                                                "VALUES ( '" + str(user_id) + "', '" + userstring + "' )"
            conn.execute(query)

            conn.commit()
            print("Session created successfully")

    except Exception as e:
        print("create session failed : ", e.__class__)


def fetchProfileDetails():
    try:
        cursor = conn.execute("SELECT * from '" + constants.profile_table + "'")

        for row in cursor:
            print("ID = ", row[0])
            print("Response = ", row[1], "\n")
            return row[1]

        return None

    except Exception as e:
        print("Fetch profile details failed : ", e.__class__)
        return None


def updateProfile(user_id, userString):
    try:

        initTables()
        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.profile_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):
            conn.execute(
                "UPDATE " + constants.profile_table + " SET PROFILE_JSON='" + userString + "' WHERE ID='" + user_id + "'")
            conn.commit()
            print("Update profile in database successful")
        else:
            query = "INSERT INTO '" + constants.profile_table + "' (ID, PROFILE_JSON) " \
                                                              "VALUES ( '" + str(user_id) + "', '" + userString + "' )"
            conn.execute(query)

            conn.commit()
            print("Profile added successfully")

    except Exception as e:
        print("Update Profile in database failed : " + e.__class__)


def logoutUser():
    try:
        conn.execute("DELETE FROM '" + constants.profile_table + "'")
        conn.execute("DELETE FROM '" + constants.health_calendar_table + "'")
        conn.execute("DELETE FROM '" + constants.login_table + "'")
        conn.commit()
        print("Session cleared, user logout successful")

    except Exception as e:
        print("Logout user failed : ",e.__class__)


def isLogggedIn():
    try:
        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.login_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):
            print("User is Logged in")
            return True
        else:
            print("No login data available")
            return False

    except Exception as e:
        print("Fetch profile details failed : ", e.__class__)
        return False


def updateCalendarDB(user_id, calendar_json):
    try:
        initTables()

        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.health_calendar_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):
            print("Health calendar available")
            conn.execute(
                "UPDATE " + constants.health_calendar_table + " SET CALENDAR_JSON='" + calendar_json + "' WHERE ID='" + user_id + "'")
            conn.commit()
            print("Update Health calendar in database successful")
            return True
        else:
            print("No calendar data available")
            query = "INSERT INTO '" + constants.health_calendar_table + "' (ID, CALENDAR_JSON) " \
                                                                        "VALUES ( '" + str(
                user_id) + "', '" + str(calendar_json) + "' )"
            conn.execute(query)
            conn.commit()
            print("Calendar updated successfully")
            return True

    except Exception as e:
        print("Update Health Calendar in database failed : " + e.__class__)
        return None


def getCalendarData():
    try:
        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.health_calendar_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):
            cursor = conn.execute("SELECT * from '" + constants.health_calendar_table + "'")
            row = cursor.fetchone()
            return row[1]
        else:
            print("No health calendar data available")
            return None


    except Exception as e:
        print("Fetch Health Calendar from database failed : " + e.__class__)
        return None

def resetDatabase() :
    conn.close()
    os.remove(constants.my_database_name)
    reconnectDB()
    initTables()

def reconnectDB():
    global conn
    conn = sqlite3.connect(constants.path + r"\Mahi\MyDatabase\\" + constants.my_database_name)

def initTables():
    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.profile_table + ''' 
                       (ID TEXT PRIMARY KEY   NOT NULL,
                       PROFILE_JSON   TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.health_calendar_table + ''' 
                               (ID TEXT PRIMARY KEY   NOT NULL,
                           CALENDAR_JSON   TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.login_table + ''' 
                               (ID TEXT PRIMARY KEY   NOT NULL,
                           LOGIN_JSON   TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.appointments_table + ''' 
                               (ID TEXT PRIMARY KEY   NOT NULL,
                           APPO_JSON   TEXT);''')
    conn.commit()

def updateCompletedAppointments(user_id,appointments_string):
    try:
        initTables()
        cursor = conn.execute("SELECT COUNT(ID) from '" + constants.appointments_table + "'")
        row = cursor.fetchone()
        if (row[0] == 1):
            print("Appointments data available")
            conn.execute(
                "UPDATE " + constants.appointments_table + " SET APPO_JSON='" + appointments_string + "' WHERE ID='" + user_id + "'")
            conn.commit()
            print("Update appointments in database successful")
            return True
        else:
            print("No appointments data available")
            query = "INSERT INTO '" + constants.appointments_table + "' (ID, APPO_JSON) " \
                                                                        "VALUES ( '" + str(
                user_id) + "', '" + str(appointments_string) + "' )"
            conn.execute(query)
            conn.commit()
            print("Appointments added successfully")
            return True

    except Exception as e:
        print("Add/Update completed appointemnts failed : "+e.__class__)
        return False





if __name__ == "__main__":

    initTables()
    # createSession("46747",
    #               '{"user_img":"https:\/\/rc.mobihealth.in\/upload\/user_image\/46747_pp1609840465.jpg?363684491",'
    #               '"contact_num":"9131577259","firstname":"MAYUR","lastname":"","email":"mayur@fluvina.com","gender":"male",'
    #               '"address1":"anjali","address2":"","city":"Ahmedabad","dob":"12-11-2003","pincode":"390007","state":"Gujarat",'
    #               '"country":"India","age":17,"blood_group":""}'
    #               )

    # if isLogggedIn():
    #     fetchProfileDetails()
    # else:
    #     print("User is logged out !")
    # logoutUser()
    # getCalendarData()
    # resetDatabase()
