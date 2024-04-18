class Driver:
    def __init__(self, name, time, total_time = 0):
        self.name = name
        self.time = time
        self.total_time = sum(map(int, time.split()))

    def time_per_lapse(self, lap):
        return self.time[lap-1]
    
n, m = map(int, input().split())
mas = [0]*n
for i in range(n):
    driver = Driver(input(), input())
    mas[i] = driver

mas = sorted(mas, key=lambda driver: driver.total_time)
print(mas[0].name)
