class Car:

    """一次模拟汽车的简单尝试"""

    def __init__(self, manufacturer, model, year):
        """初始化描述汽车的属性"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """模拟给汽车加油"""
        print("This car needs a gas tank!")

class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=100):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, manufacturer, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(manufacturer, model, year)
        self.battery_size = 75
        self.battery = Battery()  # 创建一个Battery实例作为属性

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()  # 调用Battery实例的方法
my_leaf.battery.get_range()  # 调用Battery实例的get_range方法