# city_functions.py

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result

# Call the function three ways
print(city_country("nairobi", "kenya"))
print(city_country("paris", "france", 2148000))
print(city_country("tokyo", "japan", 13929000, "Japanese"))
