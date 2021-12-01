my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

my_file2 = open("input2.txt", "r")
content2 = my_file2.read()
content_list2 = content2.split("\n")
my_file2.close()

startnumber = 1

for i in range(0,len(content_list2)):
    if content_list2[i] > content_list[i]:
        startnumber = startnumber + 1
        print(f"{content_list2[i]} is greather than {content_list[i]}")

print(f"\n\n{startnumber}")
