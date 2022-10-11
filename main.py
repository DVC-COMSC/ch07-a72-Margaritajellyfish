
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
count = 0
for i in range(len(num2)):
    if num2[i] in num1:
        count += 1
if count == len(num2):
    print(True)
# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
