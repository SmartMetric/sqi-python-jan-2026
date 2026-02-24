# 1. Given the string file_path = "/usr/local/bin/python",
#    use slicing to print:
#    a) The string "python"
#    b) The string "/usr/local"
#    Expected output:
#    python
#    /usr/local
 
file_path = "/usr/local/bin/python"  
print(file_path[-7:])
print(file_path[:11])


#
#
#
# 
#
#
#




# 2. Given the string headline = "Breaking News: Market Crash Today",
#    use slicing to print:
#    a) "Breaking News"
#    b) "Market Crash Today"
#    Expected output:
#    Breaking News
#    Market Crash Today
headline = "Breaking News: Market Crash Today"
print(headline[:13])
print(headline[13:33])


# 3. Given the string message = "System reboot required immediately",
#    use slicing to print the last 11 characters.
#    Expected output:
#    immediately
message = "System reboot required immediately"
print(message[-12:])

# 4. Given the string letters = "abcdefghijklmnopqrstuvwxyz",
#    use slicing to print:
#    a) Every second letter starting from index 0
#    b) Every third letter starting from index 1
#    Expected output:
#    acegikmoqsuwy
#    behknqtwz
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0::2])
print(letters[1::3])


# 5. Given the string palindrome = "racecar",
#    use slicing to reverse the string and print the result.
#    Expected output:
#    racecar
palindrome = "racecar"
print(palindrome[-7:])

# 6. Given the string description = "Slicing strings makes Python powerful",
#    use slicing to print:
#    a) Characters from index 8 to 15
#    b) Every second character from index 0 to 12
#    Expected output:
#    strings
#    Siigsrn
description = "Slicing strings makes Python powerful"
print(description[8:15])
print(description[0:13:2])

# 7. Given the string framework = "DjangoRestFramework",
#    use slicing to print:
#    a) The first 6 characters
#    b) The last 9 characters
#    Expected output:
#    Django
#    Framework
framework = "DjangoRestFramework"
print(framework[:6])
print(framework[-9:])


# 8. Given the string dataset = "UserActivityLogs",
#    use slicing to print the substring "Activity".
#    Expected output:
#    Activity
dataset = "UserActivityLogs"
print(dataset[4:12])

# 9. Given the string warning = "Unauthorized access detected!",
#    use slicing to print every second character.
#    Expected output:
#    Uatoie cesdtce!
warning = "Unauthorized access detected!"
print(warning[::2])


# 10. Given the string full_name = "Christopher",
#     use slicing to print the first 4 characters
#     concatenated with the last 4 characters.
#     Expected output:
#     Chripher
full_name = "Christopher"
print(full_name[:4]+full_name[-4:])
