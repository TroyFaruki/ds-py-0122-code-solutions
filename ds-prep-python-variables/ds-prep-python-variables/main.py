first_name = 'Troy'
last_name = "Faruki"
full_name = first_name + " " + last_name
print(full_name)

height_in_inches_float = 73.2
print(height_in_inches_float)
print(type(height_in_inches_float))
height_in_meters = height_in_inches_float * 2.54 / 100
print(height_in_meters)

eats_plants = True
eats_animals = False
is_animal = eats_plants or eats_animals
is_omnivore = eats_plants and eats_animals
is_plant = not(is_animal)
print(eats_plants, is_animal, is_omnivore)


mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860
is_mean_height = height_in_meters == mean_height_in_meters
is_short = height_in_meters < short_threshold_in_meters
is_tall = height_in_meters >= tall_threshold_in_meters
is_normal_height = height_in_meters >= short_threshold_in_meters < tall_threshold_in_meters
print(is_mean_height, is_short, is_tall, is_normal_height)

nothing = None
print(nothing)
