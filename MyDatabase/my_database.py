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
        conn.execute("DELETE FROM '" + constants.profile_table + "'")
        conn.execute("DELETE FROM '" + constants.health_calendar_table + "'")
        conn.execute("DELETE FROM '" + constants.login_table + "'")
        conn.execute("DELETE FROM '" + constants.completed_appointments_table + "'")
        conn.execute("DELETE FROM '" + constants.upcoming_appointments_table + "'")
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

def getHummData() :
    strResp = r'''{
    "status": true,
    "message": "Data loaded successfully",
    "total_records": 1313,
    "data": [
        {
            "Id": 1879,
            "Title": "Take care of your guts.",
            "SortDescription": ".",
            "Description": "One must take care of their intestines, we eat organic, and our intestines are home to numerous organisms, the presence of some might cause you pain. A mild pain that goes away in a day or two is nothing to worry about it could be gas, constipation, or indigestion. If the pain lasts longer or is frequently being felt, is a matter of concern, Read more about Diverticulitis, hernia and more.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0cb3426e31618742451272.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0cb3426e31618742451272.png",
            "Tags": 14,
            "DetailUrl": "https://www.healthline.com/health/pain-in-lower-left-abdomen",
            "PageType": 0,
            "Created_on": "2021-04-18 16:10:51",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1881,
            "Title": "Keep your heart happy, manage your anger.",
            "SortDescription": ".",
            "Description": "We adjust, we digest, but at times we are unable to control that hyperactivity bursting out that leads to angry you. Do you know apart from mental effects getting angry often can physically harm you? When you are angry your blood pressure increases, prolonged conditions can lead to heart diseases. It weakens your immune system. This video simply describes the self-awareness technique to be calm.  ",
            "MediaType": "1",
            "VideoType": 1,
            "VideoUrl": "https://youtu.be/BsVq5R_F6RA",
            "IsVideoUrl": "1",
            "VideoEmbededCode": "",
            "ImageName": "",
            "ThumbName": "",
            "Tags": 143,
            "DetailUrl": "",
            "PageType": 1,
            "Created_on": "2021-04-18 23:31:10",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1882,
            "Title": "Long term Snoring habit in your child could be linked to risky behavioral problems.",
            "SortDescription": ".",
            "Description": "Snoring in children could seem a bit odd, although normal if as a parent you have experienced you child snoring occasionally, but if they regularly do, might become a problem for future. Snoring affects the kid’s frontal lobe and prolonged snoring is linked to have complications of Hyperactivity, inattention, and sleep apnea. Read more on how such a condition could be resolved.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607d9d56c24fb1618845014796.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607d9d56c24fb1618845014796.png",
            "Tags": 4,
            "DetailUrl": "https://www.msn.com/en-in/health/medical/if-your-child-snores-he-may-be-at-risk-of-behavioural-problems-in-the-future-study/ar-BB1fFz5i?ocid=msedgdhp",
            "PageType": 0,
            "Created_on": "2021-04-19 20:40:14",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1883,
            "Title": "Mangoes are here, but don’t overeat them.",
            "SortDescription": ".",
            "Description": "Summertime and cold mango shake, or pudding is a great beverage. Mangoes are highly nutritious but overeating them could lead to adverse health conditions. Since they are high in sugar content especially fructose, &  packed with lots of fiber, Excessive consumption could result in high blood sugar levels which is not good for diabetic people, it may also cause diarrhoea. Swipe left to know more.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607d9e709a6ad1618845296633.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607d9e709a6ad1618845296633.png",
            "Tags": 14,
            "DetailUrl": "https://www.msn.com/en-in/health/nutrition/side-effects-of-over-eating-mangoes/ar-BB1fFmnI",
            "PageType": 0,
            "Created_on": "2021-04-20 10:59:59",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1884,
            "Title": "Why might you need an emergency C-section?",
            "SortDescription": ".",
            "Description": "An emergency C-section is a sign that your baby isn’t cooperating with the planned exit. It may also mean that your health is a concern and waiting for progress isn’t the right choice. The following are several reasons why this might happen: very long labour, If your baby is in breech or transverse position, tangled umbilical cord, placental problems, womb tear, a vaginal delivery isn't possible.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607d9ec27151e1618845378464.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607d9ec27151e1618845378464.png",
            "Tags": 42,
            "DetailUrl": "https://www.healthline.com/health/pregnancy/emergency-c-section#why-they-happen",
            "PageType": 0,
            "Created_on": "2021-04-19 20:46:18",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1885,
            "Title": "Read this before eating cheese during pregnanacy .",
            "SortDescription": ".",
            "Description": "Pregnant women are 10 times more likely to develop a serious infection called listeriosis caused by Listeria bacteria that can be found in raw, unpasteurized milk.one should avoid any cheeses or dairy products that are made using unpasteurized milk. Be careful and look for “pasteurized” cheese like cheddar, mozzarella, Parmesan, cream cheese, ricotta, etc",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607d9f061a6051618845446108.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607d9f061a6051618845446108.png",
            "Tags": 42,
            "DetailUrl": "https://www.healthline.com/health/pregnancy/cheese-pregnancy#safe-options",
            "PageType": 0,
            "Created_on": "2021-04-19 20:47:26",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 126,
            "IsSurvey": 2,
            "Question": "a zoonotic disease is an illness that…",
            "Options": [
                {
                    "option": 1,
                    "value": "A. Can be treated by a trained veterinarian",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "B. Requires animal products to eradicate",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 3,
                    "value": "C. Can be transmitted from animals to humans ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 4,
                    "value": "D. Threatens to wipe out a species",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                }
            ],
            "QuestionType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed_survey/607da0b890d811618845880593.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed_survey/thumb/607da0b890d811618845880593.png",
            "ImageType": 1,
            "CorrectOption": "3",
            "PageType": 5,
            "isUserSelectedOption": 0,
            "IsMedicineConfirmationSurvey": 0,
            "BackgroundColor": "",
            "MediaType": "",
            "Created_on": "2021-04-19 20:54:40",
            "FeedCategoryType": 2,
            "FontTextColor": ""
        },
        {
            "Id": 1886,
            "Title": "",
            "SortDescription": "",
            "Description": "",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607d9f67da1c81618845543893.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607d9f67da1c81618845543893.png",
            "Tags": 6,
            "DetailUrl": "https://www.mayoclinic.org/healthy-lifestyle/infant-and-toddler-health/expert-answers/air-travel-with-infant/faq-20058539",
            "PageType": 2,
            "Created_on": "2021-04-19 20:49:03",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1887,
            "Title": "Dads During Labor: How to Best Support a Laboring  mother",
            "SortDescription": ".",
            "Description": "We rounded up some advice to support your partner during labour and delivery. Firstly, learn about the phases of labour, what's happening to your partner's body. Help time her contractions. During early labour, remind your partner to stay hydrated and drink plenty of liquids. A person can become panicky during labour so show your support and help your partner to relax and cheer them on.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607da0187ca621618845720511.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607da0187ca621618845720511.png",
            "Tags": 6,
            "DetailUrl": "https://www.baby-chick.com/labor-day-for-dads/",
            "PageType": 0,
            "Created_on": "2021-04-19 20:52:00",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1870,
            "Title": "Holistic approach to measuring outcomes in children with autism spectrum disorder (ASD).",
            "SortDescription": ".",
            "Description": "A nervous system disorder that affects the cognitive, emotional, social, and physical development of an individual mostly in early childhood. It is estimated that 1 in every 54 kids in the US are on autism spectrum. The older approach based on the criteria of “Doing Well” does not completely satisfies the spectrum. Peer relationship and other skills are to be considered as well, read more.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b1f0aa40591618681610672.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b1f0aa40591618681610672.png",
            "Tags": 6,
            "DetailUrl": "https://www.medicalnewstoday.com/articles/autism-changing-the-narrative-to-recognize-growth",
            "PageType": 0,
            "Created_on": "2021-04-17 23:16:50",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1871,
            "Title": "A step closer to HIV Vaccine.",
            "SortDescription": ".",
            "Description": "Who estimated around 1.7 million new cases of HIV positive people in 2017 with a mortality rate 1/3? HIV requires a highly effective antiviral treatment, many people in poor countries do not have a adequate treatment facilities. Researchers from Washington university have come up with a potential development in treating HIV. Though very tough, but the phase I trials showed positive results.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b1f6f8799d1618681711555.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b1f6f8799d1618681711555.png",
            "Tags": 194,
            "DetailUrl": "https://www.medicalnewstoday.com/articles/clinical-trial-brings-an-effective-hiv-vaccine-a-step-closer",
            "PageType": 0,
            "Created_on": "2021-04-17 23:18:31",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1872,
            "Title": "5 Best yoga poses for PCOS treatment",
            "SortDescription": ".",
            "Description": "Polycystic ovarian syndrome (PCOS) is one health condition common in females of reproductive age caused by hormonal imbalance. Females diagnosed with PCOS often have raised the level of male hormones as well as insulin resistance and reduced levels of progesterone. Several of the general causes of PCOS include excessive stress, depression, anxiety, perennial tension or faulty lifestyle. ",
            "MediaType": "1",
            "VideoType": 1,
            "VideoUrl": "https://youtu.be/4xrDxxg5jv4",
            "IsVideoUrl": "1",
            "VideoEmbededCode": "",
            "ImageName": "",
            "ThumbName": "",
            "Tags": 14,
            "DetailUrl": "",
            "PageType": 1,
            "Created_on": "2021-04-17 23:22:02",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1874,
            "Title": "What Everyone Ought To Know About seborrheic dermatitis ?",
            "SortDescription": ".",
            "Description": "Cradle cap is the common term for seborrheic dermatitis (seb-eh-REE-ik dur-muh-TYE-tis) of the scalp in infants. It is also called seborrhea (seb-eh-REE-uh), can show up: on the forehead and face behind the ears. In the diaper area, armpits, and other skin folds and creases. Sometimes seborrheic dermatitis in the diaper area or skin folds can get infected. Contact the doctor if the rash gets worse.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0a81aedb81618741889716.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0a81aedb81618741889716.png",
            "Tags": 6,
            "DetailUrl": "https://kidshealth.org/en/parents/cradle-cap.htmll",
            "PageType": 0,
            "Created_on": "2021-04-18 16:01:29",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1875,
            "Title": "Hungry Kya, all the time, investigate the facts.",
            "SortDescription": ".",
            "Description": "This is the question of an individual’s metabolism and body’s efficiency in maintaining blood sugar levels. The articles show is the largest ongoing study, an effort of the research team from Kings College London and health science company ZOE. The study suggested that people who experienced big dips in their blood sugar levels tend to feel hungrier, Read more about an exclusive study on diet and health. ",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0af019b301618742000105.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0af019b301618742000105.png",
            "Tags": 14,
            "DetailUrl": "https://medicalxpress.com/news/2021-04-reveals-hungry.html",
            "PageType": 0,
            "Created_on": "2021-04-18 16:03:20",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1876,
            "Title": "Healthy comfort food, with soup.",
            "SortDescription": ".",
            "Description": "Soup is just the perfect solution for your healthy tummy cravings, served as a hot or warm liquid made by mixing vegetables and/or meat with milk, water, or tomato gravy. Although generally considered a healthful nutritious dish not all soups are healthy. The article suggests us the varieties of soups and their healthy quotient. Read more about what makes this item nutritious or junk food.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0b93f27f01618742163993.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0b93f27f01618742163993.png",
            "Tags": 14,
            "DetailUrl": "https://www.healthline.com/nutrition/is-soup-healthy",
            "PageType": 0,
            "Created_on": "2021-04-18 16:06:03",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1877,
            "Title": "When should one introduce their kids with butter in their diet?",
            "SortDescription": ".",
            "Description": "Fats are essential for kids; young age requires more energy. Concern over including butter in their diet is a very much important issue. One thing to keep in mind that if your kid is at risk of being overweight parents should avoid giving them butter. For others, 1-year-old kids require about 1000 calories/day, 50% of it should be covered by fats, it is not just butter other fatty food items too. ",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0beee6f2b1618742254946.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0beee6f2b1618742254946.png",
            "Tags": 14,
            "DetailUrl": "https://www.healthline.com/health/baby/butter-for-baby#benefits",
            "PageType": 0,
            "Created_on": "2021-04-19 11:28:36",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 125,
            "IsSurvey": 2,
            "Question": "What does AIDS stand for?",
            "Options": [
                {
                    "option": 1,
                    "value": "1 . Acquired Immune Deficiency Syndrome ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "2. Antiviral Immune disorder System",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 3,
                    "value": " 3. Auto Immune Disorder ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                }
            ],
            "QuestionType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed_survey/607c0d46105cc1618742598067.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed_survey/thumb/607c0d46105cc1618742598067.png",
            "ImageType": 1,
            "CorrectOption": "1",
            "PageType": 5,
            "isUserSelectedOption": 0,
            "IsMedicineConfirmationSurvey": 0,
            "BackgroundColor": "",
            "MediaType": "",
            "Created_on": "2021-04-18 16:13:18",
            "FeedCategoryType": 2,
            "FontTextColor": ""
        },
        {
            "Id": 1878,
            "Title": "Guide to Keep yourself Content, Work from home.",
            "SortDescription": ".",
            "Description": "The ambiguous nature of the current situation with covid has led people to work in an isolated environment. Although virtually connected, many might not adept at working this way. The article describes the right possibilities with the isolated work to a productive and healthy lifestyle during lockdowns. Foremost, building up a routine and creating a harmonious environment is essential, read more.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607c0c5707cb31618742359032.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607c0c5707cb31618742359032.png",
            "Tags": 14,
            "DetailUrl": "https://www.bbcgoodfood.com/howto/guide/mindfulness-tips-working-home",
            "PageType": 0,
            "Created_on": "2021-04-18 16:09:19",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1861,
            "Title": " Eliminate Your Fears And Doubts About TODDLERS LYING.",
            "SortDescription": ".",
            "Description": "Lying is part of normal childhood behaviour and development. They may begin to lie from age 2 and get better at it as they get older. Do not stress, it is a normal thing for them to do. A toddler lies for a number of reasons. They may be too young to know that it is right, to tell the truth, and wrong to lie. The lie expresses something they wish was true or want to avoid getting into trouble. ",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607979bcdb71b1618573756899.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607979bcdb71b1618573756899.png",
            "Tags": 5,
            "DetailUrl": "https://momlovesbest.com/toddler-tantrums#:~:text=1%20Offer%20a%20Hug.%20One%20way%20to%20deal,and%20understand%20what%20they%E2%80%99re%20trying%20to%20say.%20",
            "PageType": 0,
            "Created_on": "2021-04-16 17:19:16",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1862,
            "Title": "ARE YOU DEALING WITH ANGER MANAGEMENT ISSUES BEING A PARENT ?",
            "SortDescription": ".",
            "Description": "Raising children is an important job. It often involves balancing many different activities and one often loses patience and feel angry when things don’t go as planned. Parents can take steps to stop their anger from getting out of control. The first step is to notice the early signs. Once you do that you can do a few things to start calming down and set a good anger management example for children.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/60797b20d60a21618574112877.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/60797b20d60a21618574112877.png",
            "Tags": 5,
            "DetailUrl": "https://raisingchildren.net.au/guides/first-1000-days/looking-after-yourself/anger-management-for-parents",
            "PageType": 0,
            "Created_on": "2021-04-16 17:25:12",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1863,
            "Title": "How to swaddle your newborn baby",
            "SortDescription": ".",
            "Description": "The first time your baby visited the hospital nursery, she probably came back wrapped in a neat little package, with only her fuzzy little head poking out. \r\nSwaddling is an ancient method for wrapping newborns in a thin blanket. It’s adorable (who doesn’t love a baby burrito!), but it also serves the all-important purpose of helping your sweet pea stay calm and sleep more soundly. \r\n",
            "MediaType": "1",
            "VideoType": 1,
            "VideoUrl": "https://youtu.be/lQWWxWMLt-M",
            "IsVideoUrl": "1",
            "VideoEmbededCode": "",
            "ImageName": "",
            "ThumbName": "",
            "Tags": 5,
            "DetailUrl": "",
            "PageType": 1,
            "Created_on": "2021-04-16 17:28:29",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1865,
            "Title": "Being Cold Gives You a Cold Myth or a Fact?",
            "SortDescription": "-",
            "Description": "No matter what your grandma might've told you, spending too much time in the cold air doesn’t make you sick. One study found that healthy men who spent several hours in temperatures just above freezing had an increase in healthy, virus-fighting activity in their immune systems. In fact, you’re more likely to get sick indoors, where germs are easily passed.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/6079a719a19681618585369662.jpg",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/6079a719a19681618585369662.jpg",
            "Tags": 34,
            "DetailUrl": "",
            "PageType": 0,
            "Created_on": "2021-04-16 20:32:49",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1866,
            "Title": "THE INSIDER'S GUIDE TO STEAM EDUCATION ",
            "SortDescription": ".",
            "Description": "STEAM is the abbreviation for Science, Technology, Engineering, Art & Math. The integration of the arts into STEM learning has allowed educators to expand the benefits of hands-on education and collaboration in a variety of ways, promoting creativity and curiosity at the core . STEM is the need of the hour and the earlier children are introduced to it the better it will be for their future.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b179f4d7e11618679711317.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b179f4d7e11618679711317.png",
            "Tags": 5,
            "DetailUrl": "https://thestempedia.com/blog/benefits-of-stem-education-in-early-childhood/#:~:text=Early%20childhood%20education%20is%20the%20key%20to%20the%20betterment%20of%20society.&text=STEM%20education%20helps%20you%20better,than%20only%20reading%20about%20them.",
            "PageType": 0,
            "Created_on": "2021-04-17 22:45:11",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1867,
            "Title": "",
            "SortDescription": "",
            "Description": "",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b19087d3701618680072513.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b19087d3701618680072513.png",
            "Tags": 5,
            "DetailUrl": "https://www.verywellfamily.com/three-day-potty-training-tips-4071189",
            "PageType": 2,
            "Created_on": "2021-04-17 22:51:12",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1868,
            "Title": "What is CRADLE CAP ?",
            "SortDescription": ".",
            "Description": "A cradle cap causes crusty or oily scaly patches on a baby's scalp. When you see these rough patches on your baby’s head, you might worry that it’s something serious. It is common and harmless and is not painful or itchy. It’s the baby form of dandruff. This skin condition got its name because the most common place for the scaly patches to show up is on the head, where a baby would wear a cap.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b1a80a6bec1618680448683.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b1a80a6bec1618680448683.png",
            "Tags": 6,
            "DetailUrl": "https://www.seattlechildrens.org/conditions/a-z/cradle-cap/",
            "PageType": 0,
            "Created_on": "2021-04-17 22:57:28",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 1869,
            "Title": "WHAT CAUSES CRADLE CAP IN NEWBORN BABIES ?",
            "SortDescription": ".",
            "Description": "The exact cause of the cradle cap isn't known. It is probably caused by hormones from the mother. These hormones cross the placenta before birth. The hormones cause the oil glands in the skin to become overactive. They then release more oil than normal. Dead skin cells normally fall off. The extra oil causes these cells to \"stick\" to the skin. These cells form yellow crusts and scales on the scalp.",
            "MediaType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed/607b1d665e0051618681190385.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed/thumb/607b1d665e0051618681190385.png",
            "Tags": 6,
            "DetailUrl": "https://kidshealth.org/en/parents/cradle-cap.html",
            "PageType": 0,
            "Created_on": "2021-04-17 23:09:50",
            "IsSlider": "0",
            "Slider": [],
            "FeedCategoryType": 1
        },
        {
            "Id": 124,
            "IsSurvey": 2,
            "Question": "What is the average human body temperature?",
            "Options": [
                {
                    "option": 1,
                    "value": "1. 96.8 degrees F",
                    "AveragePercentage": 100,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "2. 98.6 degrees F ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 3,
                    "value": "3. 86.9 degrees F",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                }
            ],
            "QuestionType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed_survey/607b1fdc026e91618681820010.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed_survey/thumb/607b1fdc026e91618681820010.png",
            "ImageType": 1,
            "CorrectOption": "2",
            "PageType": 5,
            "isUserSelectedOption": 0,
            "IsMedicineConfirmationSurvey": 0,
            "BackgroundColor": "",
            "MediaType": "",
            "Created_on": "2021-04-17 23:20:20",
            "FeedCategoryType": 2,
            "FontTextColor": ""
        }
    ]
    }'''
    return strResp;



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
