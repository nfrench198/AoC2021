my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

greaterthanvalue = 0
lessthanvalue = 0
value2 = int(999)
for i in range(0 ,len(content_list) - 2):
    lastvalue = content_list[i+2]
    middlevalue = content_list[i +1]
    firstvalue = content_list[i]
    secondvalue = int(lastvalue) + int(middlevalue) + int(firstvalue)
    if secondvalue > value2:
        greaterthanvalue = greaterthanvalue + 1
        print(f"{secondvalue} is greather than {value2}")
    if value2 > secondvalue:
        lessthanvalue = lessthanvalue + 1
        print(f"{secondvalue} is less than {value2}")
    value2 = int(secondvalue)


print(f"\n\n The greather than value is {greaterthanvalue}, the less than value is {lessthanvalue}")