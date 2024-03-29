AppType = "user_app"
AppType2 = "health_machine"
Stuff = "stuff"
RoleID = "4"
RegID = "XXXXX"

# API Actions
Action_get_my_profile_info = "get_my_profile_info"
ACTION_GET_MY_APPOINTMENT_LIST = "GET_MY_APPOINTMENT_LIST"
ACTION_DEVICE_SIGN_IN = "device_sign_in"
ACTION_my_health_calendar = "my_health_calendar"
ACTION_get_my_feeds = "get_my-feeds"
ACTION_USER_OPTION_SAVE = "USEROPTIONSAVE"
ACTION_get_patient_file_type_list = "get_patient_file_type_list"
ACTION_my_medical_files = "my_medical_files"
ACTION_terms_condition = "terms_condition"
ACTION_privacy_policy = "privacy_policy"
ACTION_get_cylinder_data = "get_cylinder_data"
ACTION_device_register = "device_register"
ACTION_device_logout = "device_logout"
ACTION_book_cylinder_refill_request = "book_cylinder_refill_request"
ACTION_default_medication_timing = "default_medication_timing"
ACTION_GET_MY_PRESCRIPTION_LIST= "GET_MY_PRESCRIPTION_LIST"
ACTION_getVitalLastFiveData= "getVitalLastFiveData"
ACTION_update_vitals_data= "update_vitals_data"
ACTION_listing_of_all_my_vitals_at_rx= "listing_of_all_my_vitals_at_rx"
ACTION_getUserVitalData= "getUserVitalData"
ACTION_click_on_this_vital_id= "click_on_this_vital_id"


# Database Connection Settings

# Tables
my_database_name = "mahi.db"
login_table = "LOGIN_TABLE"
profile_table = "MY_PROFILE"
health_calendar_table = "CALENDAR"
upcoming_appointments_table = "UP_APPOINTMENTS"
completed_appointments_table = "COMPLETED_APPOINTMENTS"
slot_timings_table = "SLOT_TIMINGS"
cylinder_table = "CYLINDER"
med_time_table = "MEDICINE_TIME"
dosage_status_table = "DOSAGE_STATUS"
extra_dosage_med_table = "EXTRA_DOSAGE_MEDS"
extra_dosage_cylinder_table = "EXTRA_DOSAGE_CYLINDER"
change_time_sync_table = "CHANGE_TIME_SYNC"

device_id = "mahi_id"
device_token = "mahi_token"

MORNING_KEY = "morning"
NOON_KEY = "noon"
EVENING_KEY = "evening"
EARLY_MORNING_KEY = "early_morning"
LATE_NIGHT_KEY = "late_night"
MID_NIGHT_KEY = "mid_night"
BEFORE_FOOD_KEY = "before_food"
AFTER_FOOD_KEY = "after_food"


#One must always be commented
path = r"C:\Users\Dell\PycharmProjects\\" #Hemank Path to project
# path = r"D:\Projects\Fluvina\MAHI\\" #Swapnil Path to project
#
#Humm Pagetypes
HUMM_IMAGE_TEXT = 0
HUMM_FULL_IMAGE = 2
HUMM_IMAGE_QUIZ_SURVEY = 5
HUMM_FULL_TEXT = 4
HUMM_FULL_TEXT_SURVEY = 7
# static cylinder IDs
cylinders = ["blue","darkblue","darkgreen", "darkpink", "green", "lightblue", "lightpink", "pink"]


# Cylinder Dosage Status
dosage_available = "available"
dosage_missed = "missed"
dosage_taken = "taken"

#colors
color_transparent = "#00FFFFFF"
color_red = "#FF0000"