import firelink

choice =input("enter favourite website of(google or facebook or youtube) : ")
if choice in firelink.favourite_websites.keys():
        firelink.open_website(choice)
