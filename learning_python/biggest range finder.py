

def pali_check(string):
    string2 = ""

    for char in string:
        string2 = char + string2

    if string2 == string:
        print("This is a Palinundrome")
    else:
        print("nigger")
        

pali_check("racecar")