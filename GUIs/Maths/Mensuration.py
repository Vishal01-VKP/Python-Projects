"""
    Mensuration Formulae :

    1. Circle :

        Radius to Circumference : (44/7)*value
        Radius to Area : (22/7)*(value**2)
        Area to Radius : (value*7/22)**(1/2)
        Area to Circumference : (2*22*((value*7/22)**(1/2)))/7
        Circumference to Radius : (7/44)*value
        Circumference to Area : (((7/44)*value)**2)*22/7

    2. Square :

        Length to Perimeter : 4*value
        Length to Area : value**2
        Area to Length : value**0.5
        Area to Perimeter : (value**0.5)*4
        Perimeter to Length : value/4
        Perimeter to Area : (value/4)**2

"""


def circle(what_to_find, what_is_given, value):

    radius_to_circumference = (2*22*value)/7
    radius_to_area = (22*value*value)/7
    area_to_radius = (value*7/22)**0.5
    area_to_circumference = (2*22*area_to_radius)/7
    circumference_to_radius = (value*7)/44
    circumference_to_area = (circumference_to_radius**2)*22/7
    
    if what_is_given.lower() == "radius":

        if what_to_find.lower() == "circumference":
            print(f"Circumference : {radius_to_circumference}")

        elif what_to_find.lower() == "area":
            print(f"Area : {radius_to_area}")

        if what_to_find.lower() == "both":
            print(f"Circumference : {radius_to_circumference} , Area : {radius_to_area}")

    if what_is_given.lower() == "circumference":

        if what_to_find.lower() == "area":
            print(f"Area : {circumference_to_area}")

        elif what_to_find.lower() == "radius":
            print(f"Radius : {circumference_to_radius}")

        if what_to_find.lower() == "both":
            print(f"Area : {circumference_to_area} , Radius : {circumference_to_radius}")

    if what_is_given.lower() == "area":

        if what_to_find.lower() == "radius":
            print(f"Radius : {area_to_radius}")

        elif what_to_find.lower() == "circumference":
            print(f"Circumference : {area_to_circumference}")

        if what_to_find.lower() == "both":
            print(f"Radius : {area_to_radius} , Circumference : {area_to_circumference}")


def square(what_to_find, what_is_given, value):

    length_to_perimeter = 4*value
    length_to_area = value**2
    area_to_length = value**0.5
    area_to_perimeter = (value**0.5)*4
    perimeter_to_length = value/4
    perimeter_to_area = (value/4)**2
    
    if what_is_given.lower() == "length":

        if what_to_find.lower() == "perimeter":
            print(f"perimeter : {length_to_perimeter}")

        elif what_to_find.lower() == "area":
            print(f"Area : {length_to_area}")

        if what_to_find.lower() == "both":
            print(f"perimeter : {length_to_perimeter} , Area : {length_to_area}")

    if what_is_given.lower() == "perimeter":

        if what_to_find.lower() == "area":
            print(f"Area : {perimeter_to_area}")

        elif what_to_find.lower() == "length":
            print(f"length : {perimeter_to_length}")

        if what_to_find.lower() == "both":
            print(f"Area : {perimeter_to_area} , length : {perimeter_to_length}")

    if what_is_given.lower() == "area":

        if what_to_find.lower() == "length":
            print(f"length : {area_to_length}")

        elif what_to_find.lower() == "perimeter":
            print(f"perimeter : {area_to_perimeter}")

        if what_to_find.lower() == "both":
            print(f"length : {area_to_length} , perimeter : {area_to_perimeter}")


# while True:
#     asked = input("What to find ? : ")
#     given = input("What is given ? : ")
#     value = int(input("What's the value ? : "))

#     circle(asked, given, value)
            

