#Python3. Using function parameters example
#         Preparing and verifying of postal labels
#         Condition: post can be send to Arisona or California only
#         California is default

def prepare_addr(name, surname, apt, street, town, state = 'CA', code = 90044):
    lbl =   name + " " + surname + "\n" + str(apt) +","+street+" "+ "st." + \
            "\n" + state + " "+ str(code)
        
    if state == 'CA':
        if code < 90000 or code > 96163:
            return ">>>Bad zip code: " + lbl
    elif state == 'AZ':
        if code <  85000 or code > 86556:
            return ">>>Bad zip code: " + lbl
    else:
        return ">>>Bad state: " + lbl
    return lbl

def output_labels(lb):
    for l in lb:
        print(l+"\n")

adrs = []        
adrs.append(prepare_addr ("Georg", "Brown", "100", "Freedom", "Los Angeles"))
adrs.append(prepare_addr ("Amelia", "Bush", "55", "Green", "Sun Diego", "CA", 92039))
adrs.append(prepare_addr ("Johen", "Black", "222", "Helloween", "Anytown", "ZZ"))
output_labels(adrs)

