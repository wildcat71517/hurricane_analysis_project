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
def convert_damages_data(damages):
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
#print(updated_damages)


#Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value.

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def dictionary_by_year(dictionary):
  year_dict = {}
  for year in years:
    year_dict[year] = [hurricane for hurricane in hurricanes.values() if hurricane["Year"]==year]
  return year_dict

hurricanes_by_year = dictionary_by_year(hurricanes)
#print(hurricanes_by_year)




# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def areas_dict(dict):
  freq = {}
  for hurricane in hurricanes.values():
    for area in hurricane["Areas Affected"]:
      if area in freq.keys():
        freq[area] += 1 
      else:
        freq[area]=1
        
  return freq
  

affected_areas_count = areas_dict(hurricanes)
#print(areas_affected_count)




# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_hurricanes(dict):
  max_area = ''
  max_area_count = 0
  for key, value in dict.items():
    if value > max_area_count:
      max_area_count = value
      max_area = key
    return "The area affected by the most hurricanes is " + max_area + " with " + str(max_area_count) + " hurricanes."
  
most_affected_area = most_hurricanes(affected_areas_count)
#print(most_affected_area)
# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def greatest_num_deaths(dict):
    max_death = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Deaths'] > max_death:
            max_death = dict[name]['Deaths']
            hurricane_name = name
    return hurricane_name, max_death

deadliest_hurricane = greatest_num_deaths(hurricanes)
#print(deadliest_hurricane)

# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(dict):
    hurricane_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    for name in dict:
        if dict[name]['Deaths'] == mortality_scale[0]:
            hurricane_mortality[0].append(name)
        elif mortality_scale[0] < dict[name]['Deaths'] <= mortality_scale[1]:
            hurricane_mortality[1].append(name)
        elif mortality_scale[1] < dict[name]['Deaths'] <= mortality_scale[2]:
            hurricane_mortality[2].append(name)
        elif mortality_scale[2] < dict[name]['Deaths'] <= mortality_scale[3]:
            hurricane_mortality[3].append(name)
        elif mortality_scale[3] < dict[name]['Deaths'] <= mortality_scale[4]:
            hurricane_mortality[4].append(name)
        else:
            hurricane_mortality[5].append(name)
    return hurricane_mortality


#print(categorize_by_mortality(hurricanes))

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def max_damage(dict):
  max_damage_cane = ''
  max_damage = 0
  for name in dict:
      if dict[name]['Damage'] > max_damage:
          max_damage = dict[name]['Damage']
          max_damage_cane = name
  return max_damage_cane, max_damage

deadliest_hurricane = greatest_num_deaths(hurricanes)
#print(deadliest_hurricane)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_scaled(hurricanes):

    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}

    for hurricane in hurricanes:

        rate = 0
        damage = hurricanes[hurricane]['Damage']

        if damage == 'Damages not recorded':
            continue
        elif damage < 100000000:
            rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in damage_scale:
            damage_scale[rate] = hurricanes[hurricane]
        else:
            damage_scale[rate].append(hurricanes[hurricane])

    return damage_scale

damage_scale = damage_scaled(hurricanes)
print(damage_scale)
