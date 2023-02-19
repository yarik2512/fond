class TresureIsland:
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

    def tresures_count(self):
        cnt = 0
        for r in self.field:
            for x in r:
                if x.__class__ == Treasure:
                    cnt += 1
        return cnt

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('GO', end=' ')
    
    def add_to_field(self, field):
        field.field[self.x][self.y] = self

class Treasure(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('Tr', end=' ')
    
    def act(self, pirate):
        pirate.money += self.value

class Snare(GameObject):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value
    
    def print(self):
        print('S ', end=' ')
    
    def act(self, player):
        player.money -= self.value

class Pirate:
    def __init__(self, x, y, money):
        self.x = x
        self.y = y
        self.money = money

    def add_pirate(self, field):
        field.field[self.x][self.y] = self

    def print(self):
        print('P ', end=' ')

    def move(self, field, x, y):
        if x != self.x and y != self.y:
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
        return

island = TresureIsland(10)
tr1 = Treasure(2, 2, 10)
tr2 = Treasure(1, 3, 20)
tr3 = Treasure(4, 7, 30)
tr4 = Treasure(3, 5, 40)
tr1.add_to_field(island)
tr2.add_to_field(island)
tr3.add_to_field(island)
tr4.add_to_field(island)
s1 = Snare(3, 1, 10)
s2 = Snare(1, 6, 20)
s3 = Snare(6, 1, 30)
s4 = Snare(7, 4, 10)
s5 = Snare(9, 3, 20)
s6 = Snare(0, 5, 30)
s1.add_to_field(island)
s2.add_to_field(island)
s3.add_to_field(island)
s4.add_to_field(island)
s5.add_to_field(island)
s6.add_to_field(island)
island.show()
x, y, m = [int(x) for x in input().split(' ')]
x -= 1
y -= 1
pirate = Pirate(x, y, m)
pirate.add_pirate(island)
island.show()
target_x, target_y = 9, 9
while island.tresures_count() > 0 and pirate.money > 0:
    s = input()
    if s == 'show':
        island.show()
        continue
    x, y = [int(x)-1 for x in s.split(' ')]
    pirate.move(island, x, y)
island.show()
