# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def updated_damages(damages):
  updated_damages = []
  for damage in damages: 
    if damage == "Damages not recorded": 
      updated_damages.append(damage)
    else: 
      if damage[-1] == "M":
        updated_damages.append(float(damage.strip("M"))* conversion["M"])
      if damage[-1] == "B": 
        updated_damages.append(float(damage.strip("B")) * conversion["B"])
  return updated_damages
updated_damages = updated_damages(damages)
# print(updated_damages)


# 2 
# Create a Table
def dictionary(name, month, year, max_wind_sustained, areas_affected, updated_damages, death):
  dictionary = {}
  for i in range(len(damages)):
    dictionary[name[i]] = {
      "Name": name[i],
      "Month": month[i],
      "Year": year[i],
      "Max Sustained Wind": max_wind_sustained[i],
      "Areas affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Deaths": deaths[i]
    }
  return(dictionary)
# Create and view the hurricanes dictionary
dictionary = dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(dictionary)



# 3
# Organizing by Year
def year_dictionary(dictionary):
  year_dictionary = {}
  for key, value in dictionary.items():
    current_year = dictionary[key]["Year"]
    if current_year not in year_dictionary: 
      year_dictionary[current_year] = [value]
    else: 
      year_dictionary[current_year].append(value)
  return year_dictionary
# print(year_dictionary(dictionary))


#4 Counting Damaged Areas
def damaged_areas_count(dictionary):
  damage_area_count = {}
  for key,value in dictionary.items():
    for area in dictionary[key]["Areas affected"]: 
      if area not in damage_area_count:
        damage_area_count[area] = 1
      else: 
        damage_area_count[area] +=1
  return damage_area_count

affected_area_dictionary = damaged_areas_count(dictionary)
# print(damaged_areas_count(dictionary))



# 5 
# Calculating Maximum Hurricane Count
def most_affected(affected_area_dict):
  hurricane_count = 0
  hurricane_area = ""
  for key, value in affected_area_dict.items():
    if value > hurricane_count: 
      hurricane_count = value 
      hurricane_area = key
    else: 
      continue
  print(f"The most affected area is {hurricane_area} with a hurricane count of {hurricane_count}.")
# most_affected(affected_area_dictionary)
# find most frequently affected area and the number of hurricanes involved in


#6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def deadliest_hurricane(dictionary):
  name_deadliest_hurricane = ''
  deaths_deadliest_hurricane = 0
  for key, value in dictionary.items():
    if dictionary[key]["Deaths"] > deaths_deadliest_hurricane:
      deaths_deadliest_hurricane  = dictionary[key]["Deaths"]
      name_deadliest_hurricane = key
    continue
  print(f"The deadliest hurricane is hurricane {name_deadliest_hurricane} with a total of {deaths_deadliest_hurricane} deaths.")
# deadliest_hurricane(dictionary)


# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def mortality_scaling(dictionary):
  mortality_scale_dictionary = {0: [] , 1: [], 2: [], 3: [], 4: []}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

  for key, value in dictionary.items():
    if dictionary[key]["Deaths"] == mortality_scale[0]:
      mortality_scale_dictionary[0].append(dictionary[key])
    elif dictionary[key]["Deaths"] <= mortality_scale[1]:
      mortality_scale_dictionary[1].append(dictionary[key])
    elif dictionary[key]["Deaths"] <= mortality_scale[2]:
      mortality_scale_dictionary[2].append(dictionary[key])
    elif dictionary[key]["Deaths"] <= mortality_scale[3]:
      mortality_scale_dictionary[3].append(dictionary[key])
    else: 
      mortality_scale_dictionary[4].append(dictionary[key])
  return mortality_scale_dictionary
# print(mortality_scaling(dictionary))

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def max_damage_cost(dictionary):
  most_damage_cost = 0 
  hurricane_name = ""
  for key,values in dictionary.items(): 
    if dictionary[key]["Damage"] != "Damages not recorded" and float(dictionary[key]["Damage"]) > most_damage_cost:
      most_damage_cost = float(dictionary[key]["Damage"])
      hurricane_name = key
    continue
  print(f"The hurricane that induced the most damage was Hurricane {hurricane_name} at a total cost of {most_damage_cost}.")
# max_damage_cost(dictionary)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def hurricane_damage_scaling(dictionary):
  hurricane_damage_scale = {
    0:[], 1:[], 2:[], 3:[], 4:[]
  }
  for key,value in dictionary.items():
    if dictionary[key]["Damage"] == "Damages not recorded":
      continue
    else:
      if float(dictionary[key]["Damage"]) == damage_scale[0]:
        hurricane_damage_scale[0].append(value)
      elif float(dictionary[key]["Damage"]) <= damage_scale[1]:
        hurricane_damage_scale[1].append(value)
      elif float(dictionary[key]["Damage"]) <= damage_scale[2]:
        hurricane_damage_scale[2].append(value)
      elif float(dictionary[key]["Damage"]) <= damage_scale[3]:
        hurricane_damage_scale[3].append(value)
      else: 
        hurricane_damage_scale[4].append(value)
  return hurricane_damage_scale

# print(hurricane_damage_scaling(dictionary))
  
# categorize hurricanes in new dictionary with damage severity as key
