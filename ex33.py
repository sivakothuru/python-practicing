i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i 

print "The numbers:"

for num in numbers:
    print num

# using function
def while_loop(number):

    i = 0
    while i < number:
        print "At the top i is %d" % i
        numb.append(i)

        i += 1
        print "Numbers now: ", numb
        print "At the bottom i is %d" % i

num = input("Enter a number> ")

numb = []
while_loop(num)

# using for-loop
new_list = []
number = input("Enter a num: ")
for i in range(0, number):
    new_list.append(i)
    print "Current num is %d" % i
    print "current list is ", new_list