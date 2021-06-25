import sqlite3
import constants
import json
import os.path

print(r"" + os.pardir + "\\MyDatabase\\" + constants.my_database_name)
conn = sqlite3.connect(constants.path + r"\QtMahi\MyDatabase\\" + constants.my_database_name)


def getUserID():
    try:
        if(isLogggedIn()):
            cursor = conn.execute("SELECT ID from '" + constants.login_table + "'")

            for row in cursor:
                print("ID = ", row[0])
                return str(row[0])

            return None
        else:
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
        if(isLogggedIn()):
            cursor = conn.execute("SELECT * from '" + constants.profile_table + "'")

            for row in cursor:
                print("ID = ", row[0])
                print("Response = ", row[1], "\n")
                return row[1]

            return None

        else:
            print("User Not logged in. Session not created")
            return None

    except Exception as e:
        print("Fetch profile details failed : ", e.__class__)
        return None

def updateProfile(user_id, userString):
    try:
        if(isLogggedIn()):
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
        else:
            print("User Not logged in. Session not created")
            return None

    except Exception as e:
        print("Update Profile in database failed : " + e.__class__)

def logoutUser():
    try:
        conn.execute("DROP TABLE '" + constants.profile_table + "'")
        conn.execute("DROP TABLE '" + constants.health_calendar_table + "'")
        conn.execute("DROP TABLE '" + constants.login_table + "'")
        conn.execute("DROP TABLE '" + constants.completed_appointments_table + "'")
        conn.execute("DROP TABLE '" + constants.upcoming_appointments_table + "'")
        conn.execute("DROP TABLE '" + constants.slot_timings + "'")
        conn.execute("DROP TABLE '" + constants.cylinder_table + "'")
        conn.execute("DROP TABLE '" + constants.dosage_status_table + "'")
        conn.execute("DROP TABLE '" + constants.med_time_table + "'")
        conn.execute("DROP TABLE '" + constants.extra_dosage_med_table + "'")
        conn.execute("DROP TABLE '" + constants.extra_dosage_cylinder_table + "'")
        conn.commit()
        print("Session cleared, user logout successful")

        return True

    except Exception as e:
        print("Logout user failed : ",e.__class__)
        return  False

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
        if(isLogggedIn()):
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
        else:
            print("User Not logged in. Session not created")
            return None

    except Exception as e:
        print("Update Health Calendar in database failed : " + e.__class__)
        return None

def getCalendarData():
    try:
        if isLogggedIn():
            cursor = conn.execute("SELECT COUNT(ID) from '" + constants.health_calendar_table + "'")
            row = cursor.fetchone()
            if (row[0] == 1):
                cursor = conn.execute("SELECT * from '" + constants.health_calendar_table + "'")
                row = cursor.fetchone()
                return row[1]
            else:
                print("No health calendar data available")
                return None
        else:
            print("User Not logged in. Session not created")
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

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.upcoming_appointments_table + ''' 
                               (ID TEXT PRIMARY KEY   NOT NULL,
                           APPO_JSON   TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.completed_appointments_table + ''' 
                               (ID TEXT PRIMARY KEY   NOT NULL,
                           APPO_JSON   TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.slot_timings_table + ''' 
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           SLOT_NAME TEXT NOT NULL, SLOT_TIME TEXT NOT NULL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.cylinder_table + ''' 
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           C_ID TEXT NOT NULL UNIQUE, C_COLORS TEXT, C_LOCK TEXT,
                           MED_FREQUENCY TEXT, MED_TIME_SLOT TEXT, MED_TIME_CHECK TEXT);''')

    # conn.execute("DROP TABLE "+constants.med_time_table)
    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.med_time_table + ''' 
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           MED_DATE TEXT NOT NULL, MED_TIME TEXT,CYLINDER_ID TEXT,
                            DOSAGE TEXT NOT NULL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.dosage_status_table + ''' 
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           DOSAGE_ID TEXT NOT NULL, MED_DATE TEXT, MED_TIME TEXT,
                            STATUS TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.extra_dosage_med_table + ''' 
                                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                              MED_DATE TEXT NOT NULL, MED_TIME TEXT,CYLINDER_ID TEXT,
                               DOSAGE TEXT NOT NULL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + constants.extra_dosage_cylinder_table + ''' 
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           C_ID TEXT NOT NULL UNIQUE, C_COLORS TEXT, C_LOCK TEXT,
                           MED_FREQUENCY TEXT, MED_TIME_SLOT TEXT, MED_TIME_CHECK TEXT);''')

    conn.commit()

def updateCompletedAppointments(user_id,appointments_string):
    try:

        if isLogggedIn():
            initTables()
            cursor = conn.execute("SELECT COUNT(ID) from '" + constants.completed_appointments_table + "'")
            row = cursor.fetchone()
            if (row[0] == 1):
                print("Completed Appointments data available")
                conn.execute(
                    "UPDATE " + constants.completed_appointments_table + " SET APPO_JSON='" + appointments_string + "' WHERE ID='" + user_id + "'")
                conn.commit()
                print("Update Completed appointments in database successful")
                return True
            else:
                print("No Completed appointments data available")
                query = "INSERT INTO '" + constants.completed_appointments_table + "' (ID, APPO_JSON) " \
                                                                            "VALUES ( '" + str(
                    user_id) + "', '" + str(appointments_string) + "' )"
                conn.execute(query)
                conn.commit()
                print("Completed Appointments added successfully")
                return True
        else:
            print("User Not logged in. Session not created")
            return None

    except Exception as e:
        print("Add/Update completed appointemnts failed : "+e.__class__)
        return False

def updateUpcomingAppointments(user_id,appointments_string):
    try:

        if isLogggedIn():
            initTables()
            cursor = conn.execute("SELECT COUNT(ID) from '" + constants.upcoming_appointments_table + "'")
            row = cursor.fetchone()
            if (row[0] == 1):
                print("upcoming Appointments data available")
                conn.execute(
                    "UPDATE " + constants.upcoming_appointments_table + " SET APPO_JSON='" + appointments_string + "' WHERE ID='" + user_id + "'")
                conn.commit()
                print("Update upcoming appointments in database successful")
                return True
            else:
                print("No upcoming appointments data available")
                query = "INSERT INTO '" + constants.upcoming_appointments_table + "' (ID, APPO_JSON) " \
                                                                            "VALUES ( '" + str(
                    user_id) + "', '" + str(appointments_string) + "' )"
                conn.execute(query)
                conn.commit()
                print("upcoming Appointments added successfully")
                return True
        else:
            print("User Not logged in. Session not created")
            return None

    except Exception as e:
        print("Add/Update upcoming appointemnts failed : "+e.__class__)
        return False

def setMedicationDB(response):

    conn.execute("DELETE FROM '" + constants.cylinder_table + "'")
    conn.execute("DELETE FROM '" + constants.med_time_table + "'")
    conn.execute("DELETE FROM '" + constants.dosage_status_table + "'")
    conn.execute("DELETE FROM '" + constants.extra_dosage_med_table + "'")
    conn.execute("DELETE FROM '" + constants.extra_dosage_cylinder_table + "'")

    # try:
    cylinder_data = response["data"]["medication_cylinder"]
    for cylinderId in constants.cylinders:
        cylinderData = cylinder_data[cylinderId]

        dosage_colors = str(cylinderData["dosage_color"])
        cylinder_lock = str(cylinderData["is_cylinder_lock"])
        med_time_slot = str(cylinderData["medicine_timing_name"])
        med_food_check = str(cylinderData["food_time_check"])
        med_frequency = str(cylinderData["med_frequency"])

        conn.execute("INSERT INTO '"+constants.cylinder_table+"' (C_ID,"
                  "C_COLORS, C_LOCK, MED_FREQUENCY, MED_TIME_SLOT, MED_TIME_CHECK) "
                  "VALUES (?,?,?,?,?,?)",(cylinderId,dosage_colors,cylinder_lock,med_frequency,
                  med_time_slot,med_food_check))


        time_slot = med_time_slot+"_"+med_food_check

        cursor = conn.execute("SELECT SLOT_TIME FROM '"+constants.slot_timings_table+"' "
                    "WHERE SLOT_NAME = '"+time_slot+"'")
        row = cursor.fetchone()
        dosage_time = str(row[0])
        for dose in cylinderData["dosages"]:
            med_date = str(dose["med_take_date"])
            dosage = str(dose["medicine_list"])

            conn.execute("INSERT INTO '"+constants.med_time_table+"' (MED_DATE,"
                      "MED_TIME,DOSAGE, CYLINDER_ID) VALUES(?,?,?,?)",
                         (med_date,dosage_time,dosage,cylinderId))

            temp = conn.execute("SELECT ID FROM '" + constants.med_time_table + "' ORDER BY ID DESC")
            dosageId = temp.fetchone()
            # print(dosageId[0])
            conn.execute("INSERT INTO '"+constants.dosage_status_table+"' (DOSAGE_ID,"
                      "MED_DATE,MED_TIME, STATUS) VALUES(?,?,?,?)",
                         (str(dosageId[0]),med_date,dosage_time, constants.dosage_available))

    print("Starting with extra dosage")
    extra_dosage_cylinder = response["data"]["extra_dosages_cylinder"]
    if len(extra_dosage_cylinder)>0:
        i = 0

        for extra_dose in extra_dosage_cylinder:
            dosage_colors = str(extra_dose["dosage_color"])
            cylinder_lock = str(extra_dose["is_cylinder_lock"])
            med_time_slot = str(extra_dose["medicine_timing_name"])
            med_food_check = str(extra_dose["food_time_check"])
            med_frequency = str(extra_dose["med_frequency"])

            conn.execute("INSERT INTO '"+constants.extra_dosage_cylinder_table+"' (C_ID,"
                      "C_COLORS, C_LOCK, MED_FREQUENCY, MED_TIME_SLOT, MED_TIME_CHECK) "
                      "VALUES (?,?,?,?,?,?)",(str(i),dosage_colors,cylinder_lock,med_frequency,
                      med_time_slot,med_food_check))

            time_slot = med_time_slot+"_"+med_food_check

            cursor = conn.execute("SELECT SLOT_TIME FROM '"+constants.slot_timings_table+"' "
                        "WHERE SLOT_NAME = '"+time_slot+"'")

            row = cursor.fetchone()
            dosage_time = str(row[0])
            for dose in extra_dose["dosages"]:
                med_date = str(dose["med_take_date"])
                dosage = str(dose["medicine_list"])

                conn.execute("INSERT INTO '"+constants.extra_dosage_med_table+"' (MED_DATE,"
                          "MED_TIME,DOSAGE, CYLINDER_ID) VALUES(?,?,?,?)",
                             (med_date,dosage_time,dosage,str(i)))

                # temp = conn.execute("SELECT ID FROM '" + constants.extra_dosage_med_table + "' ORDER BY ID DESC")
                # dosageId = temp.fetchone()
                # # print(dosageId[0])
                # conn.execute("INSERT INTO '"+constants.dosage_status_table+"' (DOSAGE_ID,"
                #           "MED_DATE,MED_TIME, STATUS) VALUES(?,?,?,?)",
                #              (str(dosageId[0]),med_date,dosage_time, constants.dosage_available))

            i = i+1

    conn.commit()
    # except:
    #     print("Set Medication DB : Something went wrong !")

def setSlotTimings(response):
    try:

        # if we get data from server
        if(response != None):
            try:
                common_timings = response["data"]["common_dosage_timing"]

                if len(common_timings)>0:

                    conn.execute("DELETE FROM '" + constants.slot_timings_table + "'")

                    for timing in common_timings:
                        med_timing_name = timing["med_timing_name"]

                        before_food_key = med_timing_name+"_before_food"
                        after_food_key = med_timing_name+"_after_food"

                        before_food_time = timing["before_food_time"]
                        after_food_time = timing["after_food_time"]

                        conn.execute("INSERT INTO '" + constants.slot_timings_table +
                                     "' (SLOT_NAME, SLOT_TIME) " \
                                    "VALUES (?,?)",(before_food_key,before_food_time))
                        conn.execute("INSERT INTO '" + constants.slot_timings_table +
                                     "' (SLOT_NAME, SLOT_TIME) " \
                                    "VALUES (?,?)",(after_food_key,after_food_time))

                    conn.commit()

                extra_dosage_timings = response["data"]["extra_dosage_timing"]

                if len(extra_dosage_timings) > 0:


                    for timing in extra_dosage_timings:
                        med_timing_name = timing["med_timing_name"]

                        before_food_key = med_timing_name + "_before_food"
                        after_food_key = med_timing_name + "_after_food"

                        before_food_time = timing["before_food_time"]
                        after_food_time = timing["after_food_time"]

                        conn.execute("INSERT INTO '" + constants.slot_timings_table +
                                     "' (SLOT_NAME, SLOT_TIME) " \
                                     "VALUES (?,?)", (before_food_key, before_food_time))
                        conn.execute("INSERT INTO '" + constants.slot_timings_table +
                                     "' (SLOT_NAME, SLOT_TIME) " \
                                     "VALUES (?,?)", (after_food_key, after_food_time))

                    conn.commit()


                else:
                    setSlotTimings(None)
            except Exception as e:
                print(e.__cause__)
                setSlotTimings(None)

        # else set up static slot timings
        else:

            conn.execute("DELETE FROM '"+constants.slot_timings_table+"'")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'morning_before_food', '08:00' )")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'morning_after_food', '09:00' )")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'noon_before_food', '12:00' )")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'noon_after_food', '13:00' )")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'evening_before_food', '19:00' )")

            conn.execute("INSERT INTO '" +constants.slot_timings_table + "' (SLOT_NAME, SLOT_TIME) " \
                    "VALUES ( 'evening_after_food', '21:00' )")

            conn.commit()

    except Exception as e:
        print("Something went wrong : Set Slot Timings "+str(e.__cause__))

def getSlotTimings():
    try:

        cursor = conn.execute("SELECT * from '" + constants.slot_timings_table + "'")

        for row in cursor:
            print(str(row))

    except Exception as e:
        print("Something went wrong : Get Slot Timings "+str(e.__cause__))

def getCylinderData():
    try:

        cursor = conn.execute("SELECT * from '" + constants.cylinder_table + "'")

        for row in cursor:
            print(str(row))

    except Exception as e:
        print("Something went wrong : Get Slot Timings "+str(e.__cause__))

def getDosages():
    try:

        cursor = conn.execute("SELECT * from '" + constants.med_time_table + "'")

        for row in cursor:
            print(str(row))

    except Exception as e:
        print("Something went wrong : Get Slot Timings "+str(e.__cause__))

def getDosagesStatus(type):
    try:


        cursor = None
        # Query to get latest entries for all doses
        if type == 1:

            query = "SELECT * from '" + constants.dosage_status_table +"' x "+\
                   "WHERE x.ID in (SELECT max(ID) FROM '"+constants.dosage_status_table+\
            "' y where y.DOSAGE_ID = x.DOSAGE_ID)"

            # Join medicine table and dosage status table
            cursor = conn.execute("SELECT * from '" + constants.med_time_table + "' c JOIN ("+
                     query+") y ON c.ID = y.DOSAGE_ID ORDER BY c.ID")


        # Query to get all entries for all doses
        elif type == 2:
            cursor = conn.execute("SELECT * from '" + constants.med_time_table + "' c JOIN '"+
                     constants.dosage_status_table+"' y ON c.ID = y.DOSAGE_ID JOIN '"+
                  constants.cylinder_table+"' z ON c.CYLINDER_ID = z.C_ID ORDER BY c.ID")

        if cursor!=None :
            # for row in cursor:
            #     print(str(row))
            return cursor
        else:
            return None

    except Exception as e:
        print("Something went wrong : Get Dosage Status "+str(e.__cause__))

def insertMissedMedicine():
    try:
        conn.execute("INSERT INTO '" + constants.dosage_status_table + "' (DOSAGE_ID,"
                   "MED_DATE,MED_TIME, STATUS) VALUES(?,?,?,?)",
                     ('345','2021-06-17', '13:15', constants.dosage_missed))
        conn.commit()
        cursor = conn.execute("SELECT * FROM '"+constants.dosage_status_table+
                  "'")
    except Exception as e:
        print(e.__cause__)

def getDosageCylinders():
    try:
        cursor = conn.execute("SELECT * from '" + constants.extra_dosage_cylinder_table + "'")

        for row in cursor:
            print(str(row))
    except Exception as e:
        print(e.__cause__)

def getExtraDosages():
    try:
        cursor = conn.execute("SELECT * from '" + constants.extra_dosage_med_table + "'")

        for row in cursor:
            print(str(row))
    except Exception as e:
        print(e.__cause__)


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
    # setSlotTimings(None)
    getSlotTimings()
    # getCylinderData()
    # getDosages()
    # getDosagesStatus(2)
    # insertMissedMedicine()

    # getDosageCylinders()
    # getExtraDosages()