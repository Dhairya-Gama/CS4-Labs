import sys

#with open('barter.dat', 'r') as f:
#    lines = f.readlines()

lines = ["(1/1/1/1/1/1/0) - (0/0/0/0/0/0/1)",
"(1/0/0/0/0/0/1) - (1/1/0/0/0/0/0)", "(0/0/1/0/0/0/0) - (1/1/0/0/0/0/0)",
"(7/5/5/4/4/0/0) - (0/0/0/0/0/0/1)",
"(0/0/0/4/4/5/0) - (0/2/0/1/8/0/0)"]



for wow in range(len(lines)):


    new_line = lines[wow].split("-")

    user_line = new_line[0].split("/")
    vendor_line = new_line[1].split("/")

    user_line[0] = user_line[0][1:]
    vendor_line[0] = vendor_line[0][2:]

    user_line[6] = user_line[6][0:1]
    vendor_line[6] = vendor_line[6][0:1]

    

    user_val = 0
    vendor_val = 0

    list = [1, 3, 5, 6, 8, 9, 100]


    for i in range(7):
        user_val += ( int(user_line[i]) * list[i] )

    for x in range(7):
        vendor_val += ( int(vendor_line[x]) * list[x] )

    

    if (vendor_val > user_val):
        print(0)

    else:
        num_comb = 0

        max_water = int(user_line[0])
        max_clothing = int(user_line[1])
        max_battery = int(user_line[2])
        max_tool = int(user_line[3])
        max_fuel = int(user_line[4])
        max_food = int(user_line[5])
        max_livestock = int(user_line[6])
        
        for w in range(max_water + 1):
            for c in range(max_clothing + 1):
                for b in range(max_battery + 1):
                    for t in range(max_tool + 1):
                        for f in range(max_fuel + 1):
                            for fd in range(max_food + 1):
                                for l in range(max_livestock + 1):
                                    offer_value = (w * list[0] +
                                                c * list[1] +
                                                b * list[2] +
                                                t * list[3] +
                                                f * list[4] +
                                                fd * list[5] +
                                                l * list[6])
                                    if offer_value >= vendor_val:
                                        num_comb += 1

        print(num_comb)