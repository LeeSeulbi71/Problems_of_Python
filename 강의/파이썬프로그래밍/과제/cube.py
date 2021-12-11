class Cube:
    #===== write your code below =======
    #초기 함수
    def __init__(self, edge_length):
        self.edge_length = edge_length
    #volume 계산 함수
    def volume(self):
        volume = pow(self.edge_length, 3)
        self.volume = volume
        return volume
    #인스턴스만 출력시
    def __str__(self) -> str:
        return "Edge Length: {}, Volume: {}".format(self.edge_length, self.volume())

if __name__ == '__main__':
    cube1 = Cube(edge_length=4)
    print(cube1.volume())
    print(cube1)