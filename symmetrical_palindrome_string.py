# Program to check if the string is symmetrical and a palindrome

s = 'madam'
half = int(len(s) / 2)
if len(s) % 2 == 0:
    first_str = s[:half]
    second_str = s[half:]
else: 
    first_str = s[:half]
    second_str = s[half+1:]
 
# symmetric
if first_str == second_str:
    print(s, 'string is symmertical')
else:
    print(s, 'string is not symmertical')

rev_string=s[::-1]
if s==rev_string:
    print("Its a palindrome")
else:
    print("Not a palindrome")
