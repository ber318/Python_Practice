names = ['Brian', 'Scarlett', 'Monica', 'Richard']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print("Hello, " + names[1] + "!") 
print("Hello, " + names[2] + "!")
print("Hello, " + names[3] + "!")  

cars = ['Lamborghini', 'Ferrari', 'Maserati']
print("The " + cars[0] + " Aventador is my favorite car.")

people = ['Lebron James', 'Dwyane Wade', 'Pat Riley']
print(people[0] + " would you like to come to dinner tomorrow?")
print(people[1] + " would you like to come to dinner tomorrow?")
print(people[2] + " would you like to come to dinner tomorrow?")

print(people[0] + " can not make it")
del people[0]
people.insert(0, 'Donald Trump')
print(people[0] + " would you like to come to dinner tomorrow?")
print(people[1] + " would you like to come to dinner tomorrow?")
print(people[2] + " would you like to come to dinner tomorrow?")

print("I have found a bigger table")
people.insert(0, 'Justise Winslow')
people.insert(2, 'Zion Williamson')
people.append('Richard Remer')
print(people[0] + " would you like to come to dinner tomorrow?")
print(people[1] + " would you like to come to dinner tomorrow?")
print(people[2] + " would you like to come to dinner tomorrow?")
print(people[3] + " would you like to come to dinner tomorrow?")
print(people[4] + " would you like to come to dinner tomorrow?")
print(people[5] + " would you like to come to dinner tomorrow?")

print("I apparently can only invite two people to dinner")
hello = people.pop()
print(hello + ", I am sorry, you cannot come to dinner.")
hello = people.pop()
print(hello + ", I am sorry, you cannot come to dinner.")
hello = people.pop()
print(hello + ", I am sorry, you cannot come to dinner.")
hello = people.pop()
print(hello + ", I am sorry, you cannot come to dinner.")

print(people[0] + ", you are still invited to dinner.")
print(people[1] + ", you are still invited to dinner.")
print(len(people))
del people[1]
del people[0]

places = ['London', 'Paris', 'Miami', 'New York', 'Los Angeles']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)


