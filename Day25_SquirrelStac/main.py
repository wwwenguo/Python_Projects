import pandas

color_cat = {
    'Gray': 0,
    'Cinnamon': 0,
    'Black': 0,
}

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_color = data['Primary Fur Color']
# print(data_color)

for index in range(0, len(data_color)):
    if data_color[index] == 'Gray':
        color_cat['Gray'] += 1
    elif data_color[index] == 'Cinnamon':
        color_cat['Cinnamon'] += 1
    elif data_color[index] == 'White':
        color_cat['Black'] += 1

for key, val in color_cat.items():
    color_cat[key] = [str(val)]
print(color_cat)

d = pandas.DataFrame.from_dict(color_cat, orient='index')
d.to_csv('color.csv')
