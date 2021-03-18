

class ProfileModel:
    "Profile Details"

    def __init__(self, id, first_name, last_name, contact_num, email, gender, address, user_image,
                 city, dob, pincode, state, country, age, bloodgroup):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num
        self.email = email
        self.gender = gender
        self.address = address
        self.user_image = user_image
        self.city = city
        self.dob = dob
        self.pincode = pincode
        self.state = state
        self.country = country
        self.age = age
        self.bloodgroup = bloodgroup


    def getId(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getFirstName(self):
        return self.first_name

    def setFirstName(self, first_name):
        self.first_name = first_name

    def getLastName(self):
        return self.last_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def getLastName(self):
        return self.last_name

    def setLastName(self, last_name):
        self.last_name = last_name




