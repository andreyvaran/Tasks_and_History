class Transport:
    def __init__(self, num, type, speed, fuel_type):
        self.num = num
        self.type = type
        self.fuel_type = int(fuel_type)
        self.speed = int(speed)

    def reduce_speed(self):
        return self.speed

    def distance(self, time):
        return time * self.reduce_speed()


class Car(Transport):
    def __init__(self, id, type, speed, fuel_type):
        super().__init__(id, type, speed, fuel_type)

    def reduce_speed(self):
        if self.fuel_type == 95:
            return self.speed * 0.9
        if self.fuel_type == 92:
            return self.speed * 0.8
        return self.speed

    def distance(self, time):
        return time * self.reduce_speed()


class Moto(Transport):
    def __init__(self, id, type, speed, fuel_type):
        super().__init__(id, type, speed, fuel_type)

    def reduce_speed(self):
        if self.fuel_type == 95:
            return self.speed * 0.8
        if self.fuel_type == 92:
            return self.speed * 0.6
        return self.speed

    def distance(self, time):
        return time * self.reduce_speed()


class Truck(Transport):
    def __init__(self, id, type, speed, fuel_type=-1):
        super().__init__(id, type, speed, fuel_type)

    def reduce_speed(self):
        return self.speed

    def distance(self, time):
        return time * self.reduce_speed()


n, m, t = input().split()
n = int(n)
m = int(m)
t = int(t)
vehicles = []

for i in range(int(n)):
    args = input().split()
    Fuel_type = 0
    if len(args) > 3:
        Num, Type, Speed, Fuel_type = args
    else:
        Num, Type, Speed = args
        if Type == '1':
            vehicles.append(Car(Num, Type, Speed, Fuel_type))
        if Type == '2':
            vehicles.append(Moto(Num, Type, Speed, Fuel_type))
        if Type == '3':
            vehicles.append(Truck(Num, Type, Speed))

dist = int(vehicles[0].distance(t))
mindist = min ( m - dist % m ,dist % m )
ans = int(vehicles[0].num)

for i in range(n):
    new_dist = min(m - (int(vehicles[i].distance(t)) % m), abs((int(vehicles[i].distance(t)) % m)))
    if mindist >= new_dist:
        mindist = new_dist
        if ans > int(vehicles[i].num):
            ans = int(vehicles[i].num)

print(ans)