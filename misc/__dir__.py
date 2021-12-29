class DirTest:
    def __init__(self) -> None:
        self.name = "DirTest"
        self.value = 777
        print(self.__dir__())

dt = DirTest()
