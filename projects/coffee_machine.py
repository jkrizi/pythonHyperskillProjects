class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water_stored = water
        self.milk_stored = milk
        self.beans_stored = beans
        self.cups_stored = cups
        self.money_collected = money
        self.state = 'starting'

    def set_machine_ready(self):
        print()
        print('Write action (buy, fill, take, remaining, exit):')
        self.state = 'ready'

    def gui(self, user_input):
        if self.state == 'ready':
            self.start_program(user_input)
        elif self.state == 'buying':
            self.buy(user_input)
        elif 'filling' in self.state:
            self.fill(int(user_input))

    def start_program(self, pressed_button):
        if pressed_button == 'buy':
            print()
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            self.state = 'buying'
        elif pressed_button == 'fill':
            print()
            print('Write how many ml of water do you want to add:')
            self.state = 'filling water'
        elif pressed_button == 'take':
            self.take()
        elif pressed_button == 'remaining':
            self.print_status()
        elif pressed_button == 'exit':
            self.state = 'exiting'
        else:
            print('Unknown program started!')

    def fill(self, volume):
        if 'water' in self.state:
            self.water_stored += volume
            self.state = 'filling milk'
            print('Write how many ml of milk do you want to add:')
        elif 'milk' in self.state:
            self.milk_stored += volume
            self.state = 'filling beans'
            print('Write how many grams of coffee beans do you want to add:')
        elif 'beans' in self.state:
            self.beans_stored += volume
            self.state = 'filling cups'
            print('Write how many disposable cups of coffee do you want to add:')
        else:
            self.cups_stored += volume
            self.set_machine_ready()

    def take(self):
        print()
        print('I gave you $' + str(self.money_collected))
        self.money_collected = 0
        self.set_machine_ready()

    def print_status(self):
        print()
        print('The coffee machine has:')
        print(self.water_stored, 'of water')
        print(self.milk_stored, 'of milk')
        print(self.beans_stored, 'of coffee beans')
        print(self.cups_stored, 'of disposable cups')
        print(self.money_collected, 'of money')
        self.set_machine_ready()

    def buy(self, coffee):
        if coffee == '1':
            self.make_coffee(250, 0, 16, 4)
        elif coffee == '2':
            self.make_coffee(350, 75, 20, 7)
        elif coffee == '3':
            self.make_coffee(200, 100, 12, 6)
        self.set_machine_ready()

    def make_coffee(self, water, milk, beans, price):
        if self.check_storage(water, milk, beans):
            self.water_stored -= water
            self.milk_stored -= milk
            self.beans_stored -= beans
            self.cups_stored -= 1
            self.money_collected += price

    def check_storage(self, water, milk, beans):
        if self.water_stored < water:
            print('Sorry, not enough water!')
        elif self.milk_stored < milk:
            print('Sorry, not enough milk!')
        elif self.beans_stored < beans:
            print('Sorry, not enough coffee beans!')
        elif self.cups_stored == 0:
            print('Sorry, not enough disposable coffee cups!')
        else:
            print('I have enough resources, making you a coffee!')
            return True
        return False


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.set_machine_ready()
while coffee_machine.state != 'exiting':
    coffee_machine.gui(input())

