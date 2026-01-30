# Ask the user to enter the current temperature in Celsius
temperature = int(input("Enter the temperature in Celsius: "))

# Check the temperature and print the appropriate message
if temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")
# Create a list of integers from 1 to 20
numbers = list(range(1, 21))

# Loop through the list and find numbers divisible by 3
for number in numbers:
    if number % 3 == 0:
        print(number)    