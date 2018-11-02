#Python-3 if-elif-else example

print("\n*** Age adviser. ***\n")

print("Enter your age:")
age = int(input())

if age < 0:
	print("Please wate for you be borned")
elif age < 4:
	print("Hello baby! It is time to sleep!")
elif age < 12:
	print("It is time to learn Python!")
elif age < 20:
	print("Your still are not senior programer? Why?")
elif age < 40:
	print("Time to buy house, yacht, airplane")
elif age < 80:
	print("Do you plan to build submarine or space shuttle?")
elif age < 120:
	print("It is time to refresh your Python knowlage")
else:
	print("Are you tortoise?")

