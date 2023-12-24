class animal:
    def animalName(self):
        self.tiger = input("Enter Animal Name 1 :")
        self.elephant = input("Enter Animal Name 2 :")
        self.monkey = input("Enter Animal Name 3")
    def showanimalName(self):
        print(f"There Is {self.tiger}")
        print(f"There is {self.elephant}")
        print(f"There is {self.monkey}")
        

class insects:
    def insectsName(self,aunt,cockrouch,mosqito):
        self.aunt = aunt
        self.cockrouch = cockrouch
        self.mosqito = mosqito

obj = animal()
for i in range(1,3):
    obj.animalName()
    obj.showanimalName()
    print("Please Next Student",i)
