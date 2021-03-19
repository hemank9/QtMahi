import API.api_calls as my_api


def validateUserNumber(number):

    # usernum = str(number)
    if len(number) == 10:

        return True
    else :
        return False

def callLoginApi(number, passw):
    response = my_api.loginAPI(number, passw)
    return response



