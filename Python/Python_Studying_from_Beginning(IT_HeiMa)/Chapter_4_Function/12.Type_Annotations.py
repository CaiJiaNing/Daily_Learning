a: int = 5
b: float = 3.14
c: str = "Hello"
d: bool = True
pic: None = None

names: list[str] = ["Alice", "Bob", "Charlie"]
phone_numbers: set[str] = {"123-456-7890", "987-654-3210"}
options: dict[str, str] = {"color": "red", "size": "M"}
goods: tuple[str, float, int] = ("item1", 1000.0, 3)

names.append(True)

print(names)
