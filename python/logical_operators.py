for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")


temp = 30
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("Outdoor event is scheduled")

is_sunny = True

if temp >=28 and is_sunny:
    print("It is hot outside and it is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside and it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside and it is sunny")
elif not is_sunny:
    print("It is cloudy")