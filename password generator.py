#Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be, and how many letters and numbers they want in their password.
import random
import string
lowercaseletters = list(string.ascii_lowercase) #creates a list of lowercase letters
uppercaseletters = list(string.ascii_uppercase) #creates a list of uppercase letters
symbols = list(string.punctuation) #creates a list of punctuation
abc = lowercaseletters + uppercaseletters + symbols #combines the three lists together
onetwothree = list(range(100)) #creates a list of numbers

password_numbers = int(input("How many numbers in the password?")) #asks for user input - numbers
password_letters = int(input("How many letters in the password?")) #asks for user input - letters

if password_letters + password_numbers < 7: #if the users asks for a password lower than 6 characters
    print('pick a longer password') #this message will be displayed
else: #if the password is longer than 6 characters the algorithm will continue
    numbers = random.sample(onetwothree,  password_numbers) #Selects numbers from the list onetwothree at random. Password_number instructs how many numbers need to be picked
    print(numbers)
    letters = random.sample(abc, password_letters) #Selects numbers from the list abc at random. Password_letters instructs how many letters need to be picked
    print(letters)
    password = str(letters + numbers) #creates the password by combining the random letters and numbers
    print('here is your password', password)
    print(str(password.strip('[] ,'))) #removes brackers from password

