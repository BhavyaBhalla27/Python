def greet(name = "stranger"):      # stranger is default parameter value
    p = print("Good day", name)
    
name = input("Enter your name:\n")
greet(name)                        # name will be taken as name entered by user 
greet()                            # name will be taken as default that is stranger def greet(name = "stranger"):