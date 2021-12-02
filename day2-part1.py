my_file = open("ship.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

print(content_list)

forwardlist = 0
uplist = 0
downlist = 0
for content in content_list:
    if "forward" in content:
        forward = content.lstrip("forward ")
        forward = int(forward)
        forwardlist = forwardlist + forward
    if "up" in content:
        up = content.lstrip("up ")
        up = int(up)
        uplist = uplist + up
    if "down" in content:
        down = content.lstrip("down ")
        down = int(down)
        downlist = downlist + down

totalposition = downlist - uplist

endresult = totalposition * forwardlist

print(f"You are now forward {forwardlist}")
print(f"Your total for up, which is really down {uplist}")
print(f"Your total for down, which is really up {downlist}")
print(f"Your height postion is now {totalposition}")
print(f"Your answer is {endresult}")