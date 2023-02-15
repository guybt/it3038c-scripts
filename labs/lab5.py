import datetime

userBirthday = input("Please enter your birthday (MM-DD-YYYY): ")

#converts string to datetime object for calculation
birthdayDate = datetime.datetime.strptime(userBirthday, '%m-%d-%Y')

#calculates seconds from the datetime object
secondsOld = (datetime.datetime.now() - birthdayDate).total_seconds()
print("You are ", secondsOld, "seconds old!")