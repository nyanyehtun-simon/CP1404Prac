COLORS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc",
    "AntiqueWhite3": "#cdc0b0",
    "AntiqueWhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": " #f0ffff"
}

color_name = None

while color_name != '':
    color_name = input('Enter color name: ')

    if color_name in COLORS.keys():
        print("{} is {}".format(color_name, COLORS[color_name]))
    else:
        print("The color {} is not in the list".format(color_name))



