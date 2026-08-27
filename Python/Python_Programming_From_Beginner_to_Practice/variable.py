name = "ada lovelace"
print(name)
print(name.title())
print(name.upper())
print(name)

name = name.upper()
print(name)
print(name.lower())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!!!")

favorite_language = "  python  "
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())

nostarch_url = 'https://www.baidu.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print(nostarch_url.removesuffix('.com'))