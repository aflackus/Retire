def getFloat(message):
    while True:
        try:
            userNumber = float(input(message))
            return userNumber
        except ValueError:
            print("You must enter a number")

def getInt(message):
    while True:
        try:
            userNumber = input(message)
            if not userNumber:
                return 1
            else:

                return int(userNumber)
        except ValueError:
            print("You must enter a number")
            
