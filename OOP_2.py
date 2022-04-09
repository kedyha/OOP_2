class Human:
    default_name = "no_name"
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age

        self.__money = money = 0
        self.__house = house = None

    def info(self):
        print(f"имя {self.name}")
        print(f"возраст {self.age}")
        print(f" финансы{self.__money}")
        print(f" дом{self.__house}")

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_name)

        print(Human.default_age)

    def earn_money(self, earn:int):
        self.earn = earn
        self.__money += earn
        print(self.earn, self.__money)

if __name__ == "__main__":
    Human.default_info()

    pers = Human("алексан", 30)

    print(pers.info())

    pers.earn_money(200)

    print(pers.info())



