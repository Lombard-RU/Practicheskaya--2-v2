class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.cart = []  

    def add_to_cart(self, medicine):
        self.cart.append(medicine)
        print(f"Лекарство '{medicine.name}' добавлено в корзину.")

    def view_cart(self):
        if not self.cart:
            print("Корзина пуста.")
        else:
            print("Ваши лекарства в корзине:")
            for medicine in self.cart:
                print(medicine)


class Medicine:
    def __init__(self, name, dosage, price):
        self.name = name
        self.dosage = dosage  
        self.price = price  

    def __str__(self):
        return f"Название: {self.name}, Дозировка: {self.dosage} мг, Цена: {self.price} руб."


class PharmacySystem:
    def __init__(self):
        self.medicines = []  
        self.users = []  
        self.current_user = None  

    def register_user(self, username, password, role):
        user = User(username, password, role)
        self.users.append(user)

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True
        return False

    def add_medicine(self, name, dosage, price):
        medicine = Medicine(name, dosage, price)
        self.medicines.append(medicine)
        print(f"Лекарство '{name}' добавлено с ценой {price} руб.")

    def remove_medicine(self, name):
        for medicine in self.medicines:
            if medicine.name == name:
                self.medicines.remove(medicine)
                print(f"Лекарство '{name}' удалено.")
                return
        print(f"Лекарство '{name}' не найдено.")

    def search_medicine(self, name):
        for medicine in self.medicines:
            if medicine.name == name:
                print(f"Найдено: {medicine}")
                return
        print(f"Лекарство '{name}' не найдено.")

    def buy_medicine(self, name):
        for medicine in self.medicines:
            if medicine.name == name:
                self.current_user.add_to_cart(medicine)
                return
        print(f"Лекарство '{name}' не найдено.")

    def view_medicines(self):
        if not self.medicines:
            print("Список лекарств пуст.")
            return
        print("\nДоступные лекарства:")
        for medicine in self.medicines:
            print(medicine)

    def admin_menu(self):
        while True:
            print("\nМеню администратора:")
            print("1. Добавить лекарство")
            print("2. Удалить лекарство")
            print("3. Просмотреть все лекарства")
            print("4. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                name = input("Введите название лекарства: ")
                dosage = int(input("Введите дозировку (мг): "))
                price = float(input("Введите цену (руб.): "))
                self.add_medicine(name, dosage, price)
            elif choice == '2':
                name = input("Введите название лекарства для удаления: ")
                self.remove_medicine(name)
            elif choice == '3':
                self.view_medicines()
            elif choice == '4':
                print("Выход из меню администратора.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def user_menu(self):
        while True:
            print("\nМеню пользователя:")
            print("1. Просмотреть все лекарства")
            print("2. Поиск лекарства")
            print("3. Купить лекарство")
            print("4. Просмотреть корзину")
            print("5. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.view_medicines()
            elif choice == '2':
                name = input("Введите название лекарства для поиска: ")
                self.search_medicine(name)
            elif choice == '3':
                name = input("Введите название лекарства для покупки: ")
                self.buy_medicine(name)
            elif choice == '4':
                self.current_user.view_cart()
            elif choice == '5':
                print("Выход из меню пользователя.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def main_menu(self):
        while True:
            print("\nАвторизация")
            username = input("Логин: ")
            password = input("Пароль: ")

            if self.authenticate(username, password):
                print(f"Добро пожаловать, {self.current_user.username}!")
                if self.current_user.role == "admin":
                    self.admin_menu()
                else:
                    self.user_menu()
            else:
                print("Неверный логин или пароль.")


if __name__ == "__main__":
    pharmacy = PharmacySystem()
    
    pharmacy.register_user("admin", "adminpass", "admin")
    pharmacy.register_user("user", "userpass", "user")
    
    
    pharmacy.main_menu()
