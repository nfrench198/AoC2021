my_file = open("ship2.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

print(content_list)

forwardlist = 0
aimlist = 0
depth = 0
for content in content_list:
    if "forward" in content:
        forward = content.lstrip("forward ")
        forward = int(forward)
        forwardlist = forwardlist + forward
        depth = aimlist * forward + depth
    if "up" in content:
        up = content.lstrip("up ")
        up = int(up)
        aimlist = aimlist - up
    if "down" in content:
        down = content.lstrip("down ")
        down = int(down)
        aimlist = aimlist + down

endresult = depth * forwardlist

print(f"Your aim is now equal to {aimlist}")
print(f"Your depth is now {depth}")
print(f"Your answer is {endresult}")