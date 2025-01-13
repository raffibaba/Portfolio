#Raffi Barber
#12/13/2024
#Mad Libs

#Init

#Functions
def story():
    print("Welcome to Mad Libs")
    name = input("name: ")
    animal = input("animal: ")
    bodyPart = input("body part: ")
    day = input("day of the week: ")
    place = input("place: ")
    print("On a cold " + day + " evening, " + name + " went to " + place + " and sat down to clear their head. Suddenly, the local " + animal + " showed up out of nowhere. " + name + " reached out their " + bodyPart + " to the " + animal + ", and it ripped " + name + "'s " + bodyPart + " off. The end")
#Main
story()
