# Hour hand turned by --α-- degrees since the midnight. Determine
# the angle by which minute hand turned since the start of the current hour.
# Input and output in this problems are floating-point numbers.
# 190 ==> 120

#------------Solution------------------------------
# The hour hand turns by 30 degrees for each hour.
# So the total amount mod(%) 30 gives you the degrees
# it has moved since the start of the hour.
# For instance at 190° it has gone for 6 hours (6*30 = 180) + 10°:
# 190 % 30==> 10
# The minute hand moves 12° for every 1° the hour hand moves:
# 10*12 ==> 120

# час для часовой стрелки == 30 градусов
# час для минутной стрелки == 360 градусов

alpha = float(input())
print(alpha%30*12)