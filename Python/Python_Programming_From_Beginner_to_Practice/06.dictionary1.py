"""    创建和使用字典   """

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

print("************************************************************")

"""    添加键值对   """
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("************************************************************")

"""    从空字典开始创建字典   """
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("************************************************************")

alien_0['color'] = 'green'
print(f"The alien is {alien_0['color']}.")

print("************************************************************")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("************************************************************")

del alien_0['points']
print(alien_0)

print("************************************************************")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("************************************************************")

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

print("************************************************************")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("************************************************************")

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

print("************************************************************")

for name in favorite_languages.keys():
    print(name.title())

print("************************************************************")

for name in favorite_languages:
    print(name.title())

print("************************************************************")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("************************************************************")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("************************************************************")

for language in set(favorite_languages.values()):
    print(language.title())