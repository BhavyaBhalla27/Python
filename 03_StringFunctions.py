story = "once upon a time Bhavya started Python Course from YouTube"
print(len(story))                # Gives the length of a string
print(story.endswith("YouTube")) # Boolean operation telling whether the story ends with that or not
print(story.count("o"))          # How many times the letter o occurs in the string
print(story.capitalize())        # Capitalize the first letter of the string
print(story.find("Bhavya"))      # Finds whether Bhavya is present or not. If not it returns -1.
print(story.find("Harry"))       # Returns -1 as Harry is not there in the string
print(story.replace("Bhavya","Mitu"))