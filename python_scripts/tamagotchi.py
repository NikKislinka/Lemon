class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.is_alive = True
    def feed(self):
        self.hunger -= 10
        self.happiness -= 5
        print(f"Вы покормили {self.name}. Счастье -5, Голод -10")
    def play(self):
        self.happiness += 15
        self.hunger += 5
        print(f"Вы поиграли с {self.name}. Счастье +15, голод +5")
    def live_one_day(self):
        self.hunger += 3
        self.happiness -= 3
    def check_status(self):
        if self.hunger >= 100:
            self.is_alive = False
            print(f"Ваш питомец {self.name} умер от голода!")
        elif self.happiness <= 0:
            self.is_alive = False
            print(f"Ваш питомец {self.name} умер от тоски!")
        elif self.hunger <= 0:
            self.is_alive = False
            print(f"Ваш питомец {self.name} умер от переедания!")
        elif self.happiness >= 100:
            self.is_alive = False
            print(f"Ваш питомец {self.name} умер от переутомления!")
    def __str__(self):
        return f"Информация о питомце:\n\nИмя: {self.name}\nГолод: {self.hunger}\nСчастье: {self.happiness}"

pet = Pet(input("Введите имя для питомца: "))

while pet.is_alive:
    print(pet)
    print("Меню:\n\n1 - покормить\n2 - поиграть\n0 - выход (ВНИМАНИЕ: Прогресс будет сброшен)")
    useract = input("Выберите действие: ")
    if useract == "1":
        pet.feed()
    elif useract == "2":
        pet.play()
    elif useract == "0":
        break
    pet.live_one_day()
    pet.check_status()
print("Игра окончена! До свидания!")
