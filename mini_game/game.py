class Field:
    def __init__(self):
        self.fields = [[" " for _ in range(3)]for _ in range(3)]
    def filling(self,row,cell,symbol):
        try:
            if not (0 <= row < 3 and 0 <= cell < 3):
                raise ValueError("Число больше")
            if self.fields[row][cell] != ' ':
                raise ValueError("Поле занято")
            self.fields[row][cell] = symbol
        except ValueError as e:
            print("Ошибка",e)
            return False
        return True
    def display(self):
        for row in self.fields:
            print(" | ".join(row))
            print("-" * (3 * 4 - 3))
class Player:
    def __init__(self,symbol,field):
        self.symbol = symbol
        self.field = field
    def make_move(self):
        while True:
            try:
                row = int(input(f"Введите строку {self.symbol} (1-3): ")) - 1
                cell = int(input(f"Введите столбец {self.symbol} (1-3): ")) - 1
                if self.field.filling(row,cell,self.symbol):
                    break
            except ValueError:
                print("Ошибка")
import random
class Bot(Player):
    def make_move(self):
        while True:
            row = random.randint(0,2)
            cell = random.randint(0,2)
            if self.field.filling(row,cell,self.symbol):
                print(f"Бот {self.symbol} поставил в ({row + 1},{cell + 1})")
                break
class Checker:
    def __init__(self,field):
        self.field = field
    def check_win(self,player):
        s = player.symbol
        f = self.field.fields
        for row in f:
            if all(cell == s for cell in row):
                return True
        for col in range(3):
            if all(f[row][col] == s for row in range(3)):
                return True
        if f[0][0] == s and f[1][1] == s and f[2][2] == s:
            return True
        if f[0][2] == s and f[1][1] == s and f[2][0] == s:
            return True
        return False

    def draw(self):
        for row in self.field.fields:
            for cell in row:
                if cell == " ":
                    return False
        return True
class Game:
    def __init__(self):
        self.field = Field()
        self.checker = Checker(self.field)
    def main(self):
        user_input = input("Выберите режим: ")
        if user_input == "1":
            self.player1 = Player('x', self.field)
            self.player2 = Bot('o', self.field)
        elif user_input == "2":
            self.player1 = Player('x', self.field)
            self.player2 = Player('o', self.field)
        if user_input == "1" or user_input == "2":
            while True:
                self.player1.make_move()
                self.field.display()
                if self.checker.check_win(self.player1):
                    print("Игрок 1 победил")
                    break
                if self.checker.draw():
                    print("Ничья!")
                    break
                self.player2.make_move()
                self.field.display()
                if self.checker.check_win(self.player2):
                    print("Игрок 2 победил!")
                    break
                if self.checker.draw():
                    print("Ничья!")
                    break
        elif user_input == "exit":
            exit()
        else:
            print("\nНекорректный режим игры. Выберите 1 или 2\n")
            self.main()

field = Field()
player1 = Player('x', field)
player2 = Bot('o', field)

for _ in range(3):
    print("\n--->Игрок 1 (Его фигура: X)\n")
    player1.make_move()
    field.display()

    print("\n--->Бот (Его фигура: O)")
    player2.make_move()
    field.display()
