# Author: CRS 9/29/21
points = input("Please input the points scored.")
if int(points) < 9:
    print("You did not earn a medal.")
else:
    if int(points) <= 11:
        print("You earned a bronze medal.")
    else:
        if int(points) <= 14:
            print("You earned a silver medal.")
        else:
            if int(points) >= 15:
                print("You earned a gold medal.")
