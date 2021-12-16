
class Cube:
    #===== write your code below =======
    def __init__(self, edge_length) -> None:
        self.edge_length = edge_length
    def volume(self):
        volume = pow(self.edge_length, 3)
        return volume
    def __str__(self) -> str:
        return (f"Edge Length: {self.edge_length} Volume: {self.volume()}")
if __name__ == '__main__':
    
    cube1 = Cube(edge_length=4)
    print(cube1.volume())
    print(cube1)