bicycle = False
motorcycle = False
monthly_pass = True
delivery_guy = True

if monthly_pass == True:
    if bicycle == True:
        print("bicycle is allowed")
    elif motorcycle == True:
        print("motorcycle is allowed")
    else:
        print("four-wheeler is only allowed with delivery guys")

    if delivery_guy == True:
        print("delivery Guys are always allowed")

else:
    print("buy a monthly pass")
