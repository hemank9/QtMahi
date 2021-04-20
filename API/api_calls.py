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
                    'action':constants. Action_PROFILE_REQUIRED_SETUP_CHECK,
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType}

            print("URL: "+myUrls.MAHI_CONTROLLER_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.PROFILE_URL, data=data)

            print("fetch profile response : "+r.text.strip())
            response = json.loads(r.text)

            if response['stat']:
                print("Fetch Profile Successful")
                myDB.updateProfile(myDB.getUserID(), r.text.strip())
                return r.text.strip()

            else:
                print(response['stat'])
                return None
        else:
            return None

    except Exception as e:
        print("Fail " + str(e.__class__))
        return None

def fetchHealthCalendarAPI(userNumber,userId,deviceId):
    try:

        data = {'user_id': userId,
                'mobile_no': userNumber,
                'device_id': deviceId,
                'stuff': constants.Stuff,
                'app_type': constants.AppType}

        print("Calendar URL: "+myUrls.HEALTH_CALENDAR_URL)
        utility.printParams(data)
        r = requests.post(url=myUrls.HEALTH_CALENDAR_URL, data=data)

        print("fetch Calendar response : "+r.text.strip())
        response = json.loads(r.text)

        if response['stat']:
            print("Fetch Calendar Successful")
            myDB.updateCalendarDB(userId,json.dumps(response))
            return response

        else:
            print(response['stat'])
            return None

    except Exception as e:
        print("Fail " + str(e.__class__))
        return None

def logoutUser(userId,deviceId,deviceToken):

    try:
        if(userId!=None):
            data = {'user_id': userId,
                    'device_token': deviceToken,
                    'device_id': deviceId,
                    'role': constants.RoleID,
                    'stuff': constants.Stuff,
                    'app_type': constants.AppType}

            print("logout URL: " + myUrls.HEALTH_CALENDAR_URL)
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
                'device_token': "mahi_token",
                'device_id': "mahi_id",
                'action': constants.ACTION_get_my_feeds,
                'stuff': constants.Stuff,
                'app_type': constants.AppType}

            print("HUMM Feeds URL: " + myUrls.HUMM_URL)
            utility.printParams(data)
            r = requests.post(url=myUrls.HUMM_URL, data=data)

            print("fetch HUMM Feeds response : " + r.text.strip())
            response = json.loads(r.text)

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
