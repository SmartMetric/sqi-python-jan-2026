
# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits = ["apple", "banana", "orange"]
print(0)

# Create a list called colors with items "red", "green", "blue".
#  Print the last item using negative indexing.
colors = [ "red", "green", "blue"]
print(colors[-1])

# Create a list called numbers with items from 1 to 10. 
# Print items from index 3 to index 7 (inclusive of index 3, exclusive of 8).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

# Create a list called alphabets with items "a", "b", "c", ..., "z". 
# Print a slice from index -3 to the end.

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", 
             "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]

print(alphabets[-3 :])


# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.

ages = [20, 30, 40]
ages[1] = 35
print(ages)

# Create a list called grades with items # Create a list called ages with items 20, 30, 40. 
# Replace the items from index 1 (inclusive) to index 3 (exclusive) with "X".

grades = [20, 30, 40]
grades[1] = "X"
print(grades)


# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.

cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)

# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruits = "apple", "banana", "cherry"
print(len(fruits))


# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.

prices = 10.5, 20.0, 15.75
print(type(prices))

# Create a list called mixed with items 10, "apple", True. Print the list.

mixed = [10, "apple", True]
print(mixed)

# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.

tuple_data = "a", "b", "c"
tuple_data = [tuple_data]
print(tuple_data)

# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.

books = ["Python", "Java"]
books.append("JavaScript")
print(books)


# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.

names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie" )
print(names)

# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students = ["Alice", "Bob"]
students2 = ("Charlie", "David")
students.extend(students2)
print(students)

# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
colour = ["red", "green", "blue"]
colour.remove("green")
print(colour)

# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.

numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

# ............................. ...............................................................................................
# Scenario: You are managing a guest list for a high-profile wedding. You have two lists: one for the 
# confirmed guests and another for the waitlisted guests. 
# The couple wants a simple wedding with close friends and family in attendance so there is room for only 10 guests. 
# Follow the instructions to manage the guest lists accordingly. Write the program in a file `wedding_guest_manager.py`.
# Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding 
# and are on the confirmed_guests list. The confirmed_guests list is full. New guests who accept the invitation will be 
# waitlisted.
# Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
# Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. 
# Put them on the waitlist.
# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. 
# Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has 
# asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. 
# Remove them from the confirmed_guests list. 
# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his 
# attendance. Remove him from the waitlist.
# The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional 
# arrangements for them. Get her this information.


# Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding and are on the confirmed_guests
#  list. The confirmed_guests list is full. New guests who accept the invitation will be waitlisted.

confirmed_guest = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist_guest = []
print(confirmed_guest)
print(waitlist_guest)

# Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.

waitlist_guest.extend(["Ken", "Jack", "Ivy"])
print(waitlist_guest)

# Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. 
# Put them on the waitlist.
waitlist_guest.extend(["Noah", "Oliver"])
print(waitlist_guest)

# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. 
# Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
confirmed_guest.remove("Alice")
confirmed_guest.append(waitlist_guest.pop(0))
print(confirmed_guest)
print(waitlist_guest)

# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make sure
#  he is on the guestlist. Check whether or not Charlie is on the guestlist.
print("Charlie" in confirmed_guest)

# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. 
# Remove them from the confirmed_guests list. 

confirmed_guest.remove("David")
confirmed_guest.remove("Eve")
print(confirmed_guest)

# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.

confirmed_guest.append(waitlist_guest.pop(0))
confirmed_guest.append(waitlist_guest.pop(0))
print(confirmed_guest)
print(waitlist_guest)

# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. 
# Remove him from the waitlist.
waitlist_guest.remove("Oliver")
print(waitlist_guest)

# The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them. 
# Get her this information.

print(confirmed_guest[-3:])

# The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move 
# 	waitlisted guest (Noah) into the confirmed_guests list.
confirmed_guest.append(waitlist_guest.pop(0))
print(confirmed_guest)
print(waitlist_guest)

# The event planner wants a report on the number of people who will be attending the wedding. Give her this information.
print(len(confirmed_guest))

# The event planner has also requested that you give her a list of all the names of the confirmed_guests. 
print(sorted(confirmed_guest))

# A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah 
# on the confirmed_guests list with Collins. Make sure you re-sort the list.
confirmed_guest.remove("Grace")
confirmed_guest.remove("Noah")
confirmed_guest.append("Collins")
print(sorted(confirmed_guest))

# # The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags 
# 	containing their food with their names on it. Give her a copy of the confirmed_guests list titled 
# 	guests_list_for_caterer`.
guests_list_for_caterer = confirmed_guest
print(guests_list_for_caterer)

# The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. 	Clear the 
# 	waitlist.
waitlist_guest.clear()
print(waitlist_guest)









