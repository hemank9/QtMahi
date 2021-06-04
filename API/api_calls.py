import json
import requests
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import constants as constants
import MyDatabase.my_database as myDB
import Utility.MahiUtility as utility
import API.my_urls as myUrls

def loginAPI(user, passw):
    try:

        data = {'username': user,
                'password': passw,
                'regId': constants.RegID,
                'device_id': "1f2d998f83b22271",
                'device_token': "1f2d998f83b22271",
                'role': constants.RoleID,
                'myaction': constants.ACTION_DEVICE_SIGN_IN,
                'app_type': constants.AppType}

        print("URL: "+myUrls.MAHI_CONTROLLER_URL)
        utility.printParams(data)
        r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

        print("login response : "+r.text.strip())
        response = json.loads(r.text)

        if response['stat']:
            print("Login Successful")
            user_data = response['profile']
            user_id = response['userId']
            myDB.createSession(user_id, json.dumps(user_data))
            return response

        else:
            print("Login failed \nstat : " + str(response['stat']) + \
                  "\nmsg : " + response['msg'])
            return None


    except Exception as e:
        print("Login failed : "+str(e.__class__))
        return None

def fetchProfileDetailsAPI():
    try:

        if myDB.isLogggedIn():
            data = {'user_id': myDB.getUserID(),
                    'myaction':constants. Action_get_my_profile_info,
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType}

            print("URL: "+myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

            print("fetch profile response : "+r.text.strip())
            response = json.loads(r.text)

            if response['status']:
                print("Fetch Profile Successful")
                myDB.updateProfile(myDB.getUserID(), r.text.strip())
                return r.text.strip()

            else:
                print(response['status'])
                return None
        else:
            return None

    except Exception as e:
        print("Fail " + str(e.__class__))
        return None

# def fetchHealthCalendarAPI(userNumber,userId,deviceId):
#     try:
#
#         data = {'user_id': userId,
#                 'mobile_no': userNumber,
#                 'device_id': deviceId,
#                 'stuff': constants.Stuff,
#                 'app_type': constants.AppType}
#
#         print("Calendar URL: "+myUrls.HEALTH_CALENDAR_URL)
#         utility.printParams(data)
#         r = requests.post(url=myUrls.HEALTH_CALENDAR_URL, data=data)
#
#         print("fetch Calendar response : "+r.text.strip())
#         response = json.loads(r.text)
#
#         if response['stat']:
#             print("Fetch Calendar Successful")
#             myDB.updateCalendarDB(userId,json.dumps(response))
#             return response
#
#         else:
#             print(response['stat'])
#             return None
#
#     except Exception as e:
#         print("Fail " + str(e.__class__))
#         return None

def logoutUser(userId,deviceId,deviceToken):

    try:
        if(userId!=None):
            data = {'user_id': userId,
                    'device_token': deviceToken,
                    'device_id': deviceId,
                    'role': constants.RoleID,
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType}

            print("logout URL: " + myUrls.LOGOUT_API)
            utility.printParams(data)
            r = requests.post(url=myUrls.LOGOUT_API, data=data)

            print("logout response : " + r.text.strip())
            response = json.loads(r.text)

            if response['stat']:
                print(response["result"])
                myDB.logoutUser()
                return True
            else:
                print("Logout Unsuccessful, please try again.")
                return False
        else:
            print("Logout Unsuccessful : User ID cannot be None")
            return False

    except Exception as e:
        print(e.__class__)

def fetchAppointments(appo_type, page):
    try:

        if myDB.isLogggedIn():
            data = {'user_id': str(myDB.getUserID()),
                'doctor_id': "0", #0 for all
                'page': str(page),
                'check_in_flag': str(appo_type), # 0 for upcoming, 1 for completed
                'action': constants.ACTION_GET_MY_APPOINTMENT_LIST,
                'stuff': constants.Stuff,
                'app_type': constants.AppType}

            print("Appointments URL: " + myUrls.HEALTH_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.HEALTH_URL, data=data)

            print("fetch appointments response : " + r.text.strip())
            response = json.loads(r.text)

            if response['status']:
                print("Fetch appointments Successful")

                #if completed appointments called then update them and only for page 1
                if(str(page) == "1"):
                    if str(appo_type) == "1" :
                        myDB.updateCompletedAppointments(myDB.getUserID(),r.text.strip())
                    else:
                        myDB.updateUpcomingAppointments(myDB.getUserID(), r.text.strip())

                return response

            else:
                print(response['status'])
                return None
        else:
            print("Session not created, user not logged in")
            return None

    except Exception as e:
        print("Fail " + str(e.__class__))
        return None

def fetchHummFeeds(page, feed_read_json,fetch_updated_feeds):
    try:

        if myDB.isLogggedIn():
            data = {'user_id': str(myDB.getUserID()),
                'feed_read_json': feed_read_json, #0 for all
                'page': str(page),
                'fetch_updated_feeds': fetch_updated_feeds, # 1 for fetching more feeds; 0 for just sending read json
                'device_token': constants.device_token,
                'device_id': constants.device_id,
                'action': constants.ACTION_get_my_feeds,
                'stuff': constants.Stuff,
                'app_type': constants.AppType}

            print("HUMM Feeds URL: " + myUrls.HUMM_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.HUMM_URL, data=data)

            print("fetch HUMM Feeds response : " + r.text.strip())
            response = json.loads(r.text, strict=False)

            if response['status']:

                print("Fetch HUMM Feeds Successful")
                return response

            else:
                print(response['status'])
                return None
        else:
            print("Session not created, user not logged in")
            return None

    except Exception as e:
        print("Fail " + str(e.__class__))
        return None

def saveHummSurveyQuizAns(option, feedId):
    try:

        if myDB.isLogggedIn():
            data = {'user_id': str(myDB.getUserID()),
                    'device_token': constants.device_token,
                    'device_id': constants.device_id,
                    'survey_id': str(feedId),
                    'selected_option': str(option),
                    'action': constants.ACTION_USER_OPTION_SAVE,
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType}

            print("HUMM Survey/Quiz option save URL: " + myUrls.HUMM_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.SAVE_HUMM_FEED_ANSWER_URL, data=data)

            print("fetch Survey/Quiz option save response : " + r.text.strip())
            response = json.loads(r.text,strict=False)

            if response['status']:

                print("Survey/Quiz option save Successful")
                return response

            else:
                print(response['status'])
                return None
        else:
            print("User not logged in.")
            return None

    except Exception as e:
        print(e.__cause__)
        return None

def fetchHummFeedsDummy():
    responseStr = r'''{
    "status": true,
    "message": "Data loaded successfully",
    "total_records": 1323,
    "data": [{
            "Id": 127,
            "IsSurvey": 2,
            "Question": "High-density lipoprotein is ",
            "Options": [
                {
                    "option": 1,
                    "value": "A. A muscle-building nutrient  ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "B. Good cholesterol that reduces the risk of heart disease",
                    "AveragePercentage": 0,
                    "SelectedOption": 1
                },
                {
                    "option": 3,
                    "value": "C. A resilient cancer cell ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 4,
                    "value": "D. A molecule that makes hair shiny and healthy",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                }
            ],
            "QuestionType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed_survey/607eeb1ece89b1618930462846.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed_survey/thumb/607eeb1ece89b1618930462846.png",
            "ImageType": 1,
            "CorrectOption": "2",
            "PageType": 5,
            "isUserSelectedOption": 1,
            "IsMedicineConfirmationSurvey": 0,
            "BackgroundColor": "",
            "MediaType": "",
            "Created_on": "2021-04-20 20:24:22",
            "FeedCategoryType": 2,
            "FontTextColor": ""
        },{
            "Id": 126,
            "IsSurvey": 1,
            "Question": "a zoonotic disease is an illness that…",
            "Options": [
                {
                    "option": 1,
                    "value": "A. Can be treated by a trained veterinarian",
                    "AveragePercentage": 10,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "B. Requires animal products to eradicate",
                    "AveragePercentage": 20,
                    "SelectedOption": 0
                },
                {
                    "option": 3,
                    "value": "C. Can be transmitted from animals to humans ",
                    "AveragePercentage": 30,
                    "SelectedOption": 0
                },
                {
                    "option": 4,
                    "value": "D. Threatens to wipe out a species",
                    "AveragePercentage": 40,
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
        },{
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
        },{
            "Id": 127,
            "IsSurvey": 2,
            "Question": "High-density lipoprotein is ",
            "Options": [
                {
                    "option": 1,
                    "value": "A. A muscle-building nutrient  ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 2,
                    "value": "B. Good cholesterol that reduces the risk of heart disease",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 3,
                    "value": "C. A resilient cancer cell ",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                },
                {
                    "option": 4,
                    "value": "D. A molecule that makes hair shiny and healthy",
                    "AveragePercentage": 0,
                    "SelectedOption": 0
                }
            ],
            "QuestionType": "2",
            "VideoType": 0,
            "VideoUrl": "",
            "IsVideoUrl": "0",
            "VideoEmbededCode": "",
            "ImageName": "https://mobihealth.in//upload/health_feed_survey/607eeb1ece89b1618930462846.png",
            "ThumbName": "https://mobihealth.in//upload/health_feed_survey/thumb/607eeb1ece89b1618930462846.png",
            "ImageType": 1,
            "CorrectOption": "2",
            "PageType": 5,
            "isUserSelectedOption": 0,
            "IsMedicineConfirmationSurvey": 0,
            "BackgroundColor": "",
            "MediaType": "",
            "Created_on": "2021-04-20 20:24:22",
            "FeedCategoryType": 2,
            "FontTextColor": ""
        },{
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
        },{
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
        }
    ]
    }'''

    return json.loads(responseStr, strict=False)

def getDummyResponse():
    return '''{"status":true,"response":[
{"date":"2020-09-28","fileType":"3","file":"1601459107-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-Growth-and-development-Fine-motor-1.png","fileNote":"test 1","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459107-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-Growth-and-development-Fine-motor-1.png"},
{"date":"2020-09-30","fileType":"3","file":"1601459389-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-Growth-and-development-Fine-motor-1.png","fileNote":"test 2","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459389-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-Growth-and-development-Fine-motor-1.png"},
{"date":"2020-09-30","fileType":"3","file":"1605168988-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 3","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1605168988-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"},
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 4","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"}, 
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 5","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"},
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 6","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"},
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 7","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"},
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 8","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"},
{"date":"2020-10-01","fileType":"3","file":"1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png","fileNote":"test 9","medicalObservation":"test","hashtag":"test","created_by":"1311","file_extention":"png","file_url":"https:\/\/patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0.nyc3.digitaloceanspaces.com\/1601459595-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0-keval-the-name-is-enough.png"}
],"folder":"patient-65nZ6gSRUJOHnNrsMJbsOkSym8hrAJ4rKgk9S6j0","msg":"File Load Successfully"}'''

def fetchMedicalFiles(sortOrder, fileType):
    try:
        if myDB.isLogggedIn():
            data ={'user_id': str(myDB.getUserID()),
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType,
                    'myaction': constants.ACTION_my_medical_files,
                    'sort_order': sortOrder,
                    'search':"",
                    'file_type': str(fileType)
                   }

            print("Fetch Files URL: " + myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

            print("Fetch Files response : " + r.text.strip())
            response = json.loads(r.text, strict=False)
            # response = json.loads(getDummyResponse(), strict=False)
            if response['status']:

                print("Fetch Files Successful")
                return response

            else:
                print(response['status'])
                return None

        else:
            print("user not logged in")
            return None
    except Exception as e:
        print(e.__cause__)
        return None

def fetchMedicalFileTypes():
    try:
        if myDB.isLogggedIn():

            data ={'user_id': str(myDB.getUserID()),
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType,
                    'myaction': constants.ACTION_get_patient_file_type_list,
                   }

            print("Fetch File Types URL: " + myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

            print("Fetch File Types response : " + r.text.strip())
            response = json.loads(r.text, strict=False)
            if response['status']:

                print("Fetch File Types Successful")
                return response

            else:
                print(response['status'])
                return None

        else:
            print("user not logged in")
            return None
    except Exception as e:
        print(e.__cause__)
        return None

def fetchTermsAndCondtions():
    try:
        if myDB.isLogggedIn():

            data ={
                    'app_type': constants.AppType,
                    'myaction': constants.ACTION_terms_condition,
                   }

            print("Fetch T&C URL: " + myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

            print("Fetch T&C response : " + r.text.strip())
            response = json.loads(r.text, strict=False)
            if response['status']:

                print("Fetch T&C Successful")
                return response

            else:
                print(response['status'])
                return None

        else:
            print("user not logged in")
            return None
    except Exception as e:
        print(e.__cause__)
        return None

def fetchPrivacyPolicy():
    try:
        if myDB.isLogggedIn():

            data ={
                    'app_type': constants.AppType,
                    'myaction': constants.ACTION_privacy_policy,
                   }

            print("Fetch Privacy Policy URL: " + myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.MAHI_CONTROLLER_URL, data=data)

            print("Fetch Privacy Policy response : " + r.text.strip())
            response = json.loads(r.text, strict=False)
            if response['status']:

                print("Fetch Privacy Policy Successful")
                return response

            else:
                print(response['status'])
                return None

        else:
            print("user not logged in")
            return None
    except Exception as e:
        print(e.__cause__)
        return None


if __name__ == "__main__":
    print("API Calls Main Function")

    # response = fetchProfileDetailsAPI(myDB.getUserID())
    # response = fetchHealthCalendarAPI("9131577259","46747","dummy")
    #
    # loginAPI("9131577259", "admin")
    # myDB.getUserID()
    # logoutUser(myDB.getUserID(),"dsfasdfsdf","asdfsdafsdf")

    # if myDB.fetchProfileDetails()==None:
    #     print("No Profile data available")

    # if(myDB.isLogggedIn()):
    #     print("User Logged in")
    # else:
    #     print("User logged out")

    # fetchAppointments("0","1")
    # fetchTermsAndCondtions()
    # fetchPrivacyPolicy()