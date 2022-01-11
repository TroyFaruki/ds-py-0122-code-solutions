# 1 bool_to_int
bool_to_int = lambda value : int(value)
print(bool_to_int(True))
print(bool_to_int(False))
#get_smaller
get_smaller = lambda a,b : min(a, b)
print(get_smaller(16, 31))
print(get_smaller(253, 223))
#3 Cube
def cube(cube):
  return cube ** 3

print(cube(2))
print(cube(5))

#4 absolute_difference

def absolute_difference(a, b):
  absolute_difference = abs(a-b)
  return(absolute_difference)

print(absolute_difference(14, 11))
print(absolute_difference(13, 40))

# 5 squared_difference

def squared_difference(a, b):
  squared_difference = (a-b)**2
  return(squared_difference)

print(squared_difference(14, 11))
print(squared_difference(13, 40))

#6 hours_to_minutes

def hours_to_minutes(hours):
  hours_to_minutes = hours * 60
  return(hours_to_minutes)

print(hours_to_minutes(hours = 3.5))
print(hours_to_minutes(hours = 12))

#7 get_circumference

def get_circumference(radius):
  get_circumference = radius ** 2 * 3.14
  return(get_circumference)

print(get_circumference(radius = 1))
print(get_circumference(radius = 9.2))

# 8 linear_transform

def linear_transform(x, slope, intercept):
  linear_transform = (slope * x) + intercept
  return(linear_transform)

print(linear_transform(x = 5.0, slope=3.0, intercept = -8.5))
print(linear_transform(slope = -2.1, intercept = 17.0, x = 2.5))

#9 standardize

def standardize(x, x_center, scale_size = abs):
  standardize = (x - x_center) / scale_size
  return(standardize)

print(standardize(x = 8.2, x_center= 13.8, scale_size = 4.83))
print(standardize(scale_size = 24.63, x = 2.89, x_center = -72.813))
