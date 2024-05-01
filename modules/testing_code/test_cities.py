
from city_fuctions import city_country

def test_city_county():
    city_country_result = city_country('santiago', 'chille', 50000)
    assert city_country_result == 'Santiago, Chille - population = 50000'
