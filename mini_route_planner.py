cities = {
    "Distance":{
        "Ulaanbaatar": {
            "Erdenet": 400,
            "Darkhan": 224,
            "Zamiin-Uud": 656,
            "Terelj": 66,
            "Arvaikheer": 432
        },

        "Erdenet": {"Ulaanbaatar": 400},
        "Darkhan": {"Ulaanbaatar": 224},
        "Zamiin-Uud": {"Ulaanbaatar": 656},
        "Terelj": {"Ulaanbaatar": 66},
        "Arvaikheer": {"Ulaanbaatar": 432}
}}
    #Distances

city_id = {
    "id":{
        "1": "Ulaanbaatar",
        "2": "Erdenet",
        "3": "Darkhan",
        "4": "Zamiin-Uud",
        "5": "Terelj",
        "6": "Arvaikheer"
    }
}
    #id because idk, better ui?


def distance_finder(a, b):
    if b in cities["Distance"][a]:
        return cities["Distance"][a][b]
        #if the distance is already written, why not use it?
    
    elif b not in cities["Distance"][a]:
        for i in cities["Distance"]["Ulaanbaatar"]:
            if i == b:

                return cities["Distance"][a]["Ulaanbaatar"] + cities["Distance"]["Ulaanbaatar"][b]
        
        #it is literally just finding distance from ulaanbaatar to another city and combining the distance of a to ulaanbaatar and ulaanbaatar to b
            

def main():
    i = True

    while i:
        j = True
        print("""
    Mongolia Route Planner 0.1v
    ---------------------------
    Available cities
              
    1. Ulaanbaatar
    2. Erdenet
    3. Darkhan
    4. Zamiin-Uud
    5. Terelj
    6. Arvaikheer
""")
        
        city_depart_number = input("Departing city: ")
        city_arrival_number = input("Arrival city: ")

        if city_arrival_number not in ["1","2","3","4","5","6"] or city_depart_number not in ["1","2","3","4","5","6"] and city_arrival_number != city_depart_number:

            print("Choose the numbers from 1 to 6.")
        
        elif city_depart_number == city_arrival_number:

            print("Choose another city, it is literally the same city 😭😭😭, can we get a 5 booms for this, BOOM, BOOM, BOOM, BOOM, BOOM")
            # ok i have no clue why did i do this, maybe coding next to sicilian sea at 2 am is really hitting me huh hahah
            # I may remove some of these comments but honestly meh, idk, will i remember?

        elif int(city_depart_number) > 0 and int(city_depart_number) < 7 and int(city_arrival_number) > 0 and int(city_arrival_number) < 7 and int(city_arrival_number) != int(city_depart_number):

            city_depart = city_id["id"][city_depart_number]
            city_arrival = city_id["id"][city_arrival_number]
            distance = distance_finder(city_depart, city_arrival)
            
            print("Distance from", city_depart, "to", city_arrival, "is", str(distance)+"km")


        while j:
            exit_point = input("Would you like to quit this program?(Y,N): ")
            if exit_point == "Y":
                print("Well then, thank you for using my program. Bye!")
                i = False
                j = False
            elif exit_point == "N":
                print("Continuing")
                j = False
            else:
                print("What")



main()

#Excuse me the comments are there to make the code look longer hahah