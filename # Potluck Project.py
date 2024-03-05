# Potluck Project 
# INMT 443
# Grant Cates

# Main method
def main():
    print("Let's have a potluck!")
    
    # Create a new potluck object for this potluck.
    thisPotluck = Potluck("", "", "", [])
    
    # Call getPotluckDetails to ask for title, location, date information for the potluck
    # Store the returned object back into thisPotluck
    thisPotluck.getPotluckDetails()
    
    # Create a list to store potluck attendees 
    attendeeList = []
    
    # Loop for adding new Attendees
    while True:
        userInput = input("Would you like to enter an Attendee? (Y/N): ")
        if userInput.upper() == "Y":
            # Create a new Attendee object
            newAttendee = Attendee("", "")
            # Call the enterNewAttendee() method and store the returned object
            newAttendee.enterNewAttendee()
            # Append the Attendee object to the list of potluck attendees
            attendeeList.append(newAttendee)
        elif userInput.upper() == "N":
            break
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
    
    # Save your list to your Potluck object
    thisPotluck.attendees = attendeeList
    
    # Call the printDetails() method for your Potluck object
    thisPotluck.printDetails()

# Class for Attendee objects
class Attendee:
    def __init__(self, name, contribution):
        self.name = name
        self.contribution = contribution

    # Method to ask user the Attendee's information and create a new Attendee object
    def enterNewAttendee(self):
        self.name = input("What is the attendee's name? ")
        self.contribution = input("What is the attendee bringing? ")
        return self

# Class for Potluck objects     
class Potluck:
    def __init__(self, title, date, location, attendees):
        self.title = title
        self.date = date
        self.location = location
        self.attendees = attendees

    # Method to ask user for potluck title, date, location
    def getPotluckDetails(self):
        self.title = input("What is the title of the potluck? ")
        self.date = input("What is the date of the potluck? ")
        self.location = input("Where is the potluck taking place? ")
        return self
    
    # Method to print the details of the potluck object
    def printDetails(self):
        print(f"You are invited to {self.title}!")
        print(f"Date: {self.date} Location: {self.location}")
        print("Here's what everyone is bringing:")
        for attendee in self.attendees:
            print(f"Name: {attendee.name} Contribution: {attendee.contribution}")






def main():
    # do some stuff
    print("Hello world!")

    addItem = True
    userInput = input("Do you want to add an item to your cart?")
    itemList = []

    # While Loop
    while addItem:
        if userInput == "Y":
            print("They said yes")
            itemList.append(addItemFunction())
            userInput = input("Do you want to add another item?")
        else:
            print("They said no")
            addItem = False
    else:
        print("The user is finished adding items to their list")

    for item in itemList:
        print(item)


def addItemFunction():
    newItem = input("What item do you want to add?")
    return newItem


# tell the program to call the main method at start
main()
