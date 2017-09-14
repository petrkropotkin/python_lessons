# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are greater than their neighbours above.
#1 7 9 0 ==> 2
# ---------------- my solution-----------------------------

first = int(input())
counter = 0


while first != 0:
    second = int(input())
    if first < second:
        counter += 1
    first = second
print(counter)

# -------------------Suggested solution------------------------

prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)
