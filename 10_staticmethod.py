class Employee:
    company = "google"
    @staticmethod
    def greet():                       # We dont have to pass self parameter as static method is used
        print("Good evening, Sir")

bhavya = Employee()
bhavya.greet()