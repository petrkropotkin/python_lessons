# As a future athlete you just started your practice for an upcoming event.
# Given that on the first day you run x miles, and by the event you must be able to run y miles.
# Calculate the number of days required for you to finally reach the required distance for the event,
# if you increases your distance each day by 10% from the previous day.
#
# Print one integer representing the number of days to reach the required distance.

x = int(input())
y = int(input())
counter = 1
while x < y :
    x *= 1.1
    counter += 1
print(counter)

