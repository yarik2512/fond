class Field:
    def __init__(self, n):
        self.field = [[None for i in range(n)] for i in range(n)]
        self.n = n

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j] == 'x':
                    print('x ', end=' ')
                elif self.field[i][j] != None:
                    self.field[i][j].print()
                else:
                    print('--', end=' ')
            print()

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, direction, field):
        field.field[self.x][self.y] = None
        old_x, old_y = self.x, self.y
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        field.field[self.x][self.y] = self
        print(f'Объект был перемещен из клетки ({old_x}, {old_y}) в клетку ({self.x}, {self.y}).')

    def print(self):
        print('GO', end=' ')
    
    def add_to_field(self, field):
        field.field[self.x][self.y] = self

class BonusObject(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('BO', end=' ')
    
    def act(self, player):
        player.health += self.value

class CurseObject(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('CO', end=' ')
    
    def act(self, player):
        player.health -= self.value

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def add_player(self, field):
        field.field[self.x][self.y] = self

    def print(self):
        print('P ', end=' ')

    def move(self, field, x, y, cnt):
        if x != self.x and y != self.y:
            print('Ошибка! Такой ход сделать невозможно.')
            return cnt
        c = cnt
        while self.x != x:
            field.field[self.x][self.y] = 'x'
            self.x += 1
            if self.x >= field.n:
                self.x = 0
            if field.field[self.x][self.y] != None and field.field[self.x][self.y] != 'x':
                field.field[self.x][self.y].act(self)
            c += 1
            field.field[self.x][self.y] = self
            if c % 5 == 0:
                field.show()
        while self.y != y:
            field.field[self.x][self.y] = 'x'
            self.y += 1
            if self.y >= field.n:
                self.y = 0
            if field.field[self.x][self.y] != None and field.field[self.x][self.y] != 'x':
                field.field[self.x][self.y].act(self)
            c += 1
            field.field[self.x][self.y] = self
            if c % 5 == 0:
                field.show()
        field.field[self.x][self.y] = self
        return c

field = Field(10)
bo1 = BonusObject(2, 2, 10)
bo2 = BonusObject(1, 3, 20)
bo3 = BonusObject(4, 7, 30)
bo4 = BonusObject(3, 5, 40)
bo1.add_to_field(field)
bo2.add_to_field(field)
bo3.add_to_field(field)
bo4.add_to_field(field)
co1 = CurseObject(3, 1, 10)
co2 = CurseObject(1, 6, 20)
co3 = CurseObject(6, 1, 30)
co4 = CurseObject(7, 4, 10)
co5 = CurseObject(9, 3, 20)
co6 = CurseObject(0, 5, 30)
co1.add_to_field(field)
co2.add_to_field(field)
co3.add_to_field(field)
co4.add_to_field(field)
co5.add_to_field(field)
co6.add_to_field(field)
field.show()
x, y = [int(x)-1 for x in input().split(' ')]
player = Player(x, y)
player.add_player(field)
field.show()
target_x, target_y = 9, 9
c = 0
while (x != target_x or y != target_y) and player.health > 0:
    x, y = [int(x)-1 for x in input().split(' ')]
    c = player.move(field, x, y, c)
field.show()
