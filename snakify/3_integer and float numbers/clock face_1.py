# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60,
#  0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now.
# 1 2 6 ==> 31.05
h = int(input())
m = int(input())
s = int(input())
#angle_1hours = 360/12

angle = 360/12*(h+m/60+s/3600)
print(angle)
