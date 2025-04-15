#acp
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    city = input("The place you are staying")
    if city=="chandigarh":
        return 134
    elif city=="paris":
        return 5000
    elif city=="jaipur":
        return 456
    

def rental_car(days):
    days = input("The number of days")
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
    


