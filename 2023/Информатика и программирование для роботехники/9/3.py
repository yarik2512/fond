class BattleField:
    def __init__(self, n):
        self.field = [[None for i in range(n)] for i in range(n)]
        self.n = n

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j] == 'x':
                    print('x', end=' ')
                elif self.field[i][j] != None:
                    self.field[i][j].print()
                else:
                    print('-', end=' ')
            print()

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('GO', end=' ')
    
    def add_to_field(self, field):
        field.field[self.x][self.y] = self

class Island(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('I', end=' ')
    
    def act(self, ship):
        ship.resources += self.value

class Mine(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('M', end=' ')
    
    def act(self, ship):
        ship.resources -= self.value

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resources = 100

    def add_ship(self, field):
        field.field[self.x][self.y] = self

    def print(self):
        print('S', end=' ')

    def move(self, field, x, y):
        if x != self.x and y != self.y:
            print('Ошибка! Такой ход сделать невозможно.')
            return
        while self.x != x:
            field.field[self.x][self.y] = 'x'
            self.x += 1
            if self.x >= field.n:
                self.x = 0
            if field.field[self.x][self.y] != None and field.field[self.x][self.y] != 'x':
                field.field[self.x][self.y].act(self)
            field.field[self.x][self.y] = self
        while self.y != y:
            field.field[self.x][self.y] = 'x'
            self.y += 1
            if self.y >= field.n:
                self.y = 0
            if field.field[self.x][self.y] != None and field.field[self.x][self.y] != 'x':
                field.field[self.x][self.y].act(self)
            field.field[self.x][self.y] = self
        field.field[self.x][self.y] = self

field = BattleField(10)
i1 = Island(2, 2, 10)
i2 = Island(1, 3, 20)
i3 = Island(4, 7, 30)
i4 = Island(3, 5, 40)
i1.add_to_field(field)
i2.add_to_field(field)
i3.add_to_field(field)
i4.add_to_field(field)
m1 = Mine(3, 1, 10)
m2 = Mine(1, 6, 20)
m3 = Mine(6, 1, 30)
m4 = Mine(7, 4, 10)
m5 = Mine(9, 3, 20)
m6 = Mine(0, 5, 30)
m1.add_to_field(field)
m2.add_to_field(field)
m3.add_to_field(field)
m4.add_to_field(field)
m5.add_to_field(field)
m6.add_to_field(field)
field.show()
x, y = [int(x)-1 for x in input().split(' ')]
ship = Ship(x, y)
ship.add_ship(field)
field.show()
target_x, target_y = 9, 9
while (x != target_x or y != target_y) and ship.resources > 0:
    s = input()
    if s == 'show':
        field.show()
        continue
    x, y = [int(x)-1 for x in s.split(' ')]
    ship.move(field, x, y)
field.show()

