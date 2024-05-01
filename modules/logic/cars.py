def make_car(manufacturer:str, model:str, **car_details):
    car_details['manufacturer'] = manufacturer
    car_details['model'] = model
    return car_details

my_car = make_car('Honda', 'Jazz', colour='Black', reg='BK09 ZXY')

print(my_car)