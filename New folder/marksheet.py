class BSmarksheetSystem():
    def compulsory(self):
        self.urdu =int(input("Enter your urdu marks: "))
        self.english =int(input("Enter your english marks: "))
        self.maths =int(input("Enter your maths marks: "))

    def artificial(self):
        self.machineLearning = int(input("Enter your Machine Learning marks: "))
        self.ict = int(input('Enter your ICT marks: '))
        self.datahandle = int(input("Enter your datahandle marks: "))
    def cybersecurity(self):
        self.ethicalHacking = int(input("Enter your ethical Hacking marks: "))
        self.scriptProgramming = int(input('Enter your scriptProgramming marks: '))
        self.cryptography = int(input("Enter your cryptography marks: "))
    def computerScience(self):
        self.discreatMath = int(input("Enter your Discreate Math marks: "))
        self.dataBase = int(input('Enter your dataBase marks: '))
        self.operatingSystem = int(input("Enter your Operating System  marks: "))
class BEmarksheetSystem(BSmarksheetSystem): 
    def architechture(self):
        self.autocad = int(input("Enter your Auto cad marks: "))
        self.twoDrawing = int(input("Enter your 2d Drwaing marks: "))
        self.interior= int(input("Enter your interior marks: "))
    def industrial(self):
        self.humanFactor = int(input("Enter your humanFactor marks:"))
        self.management = int(input("Enter your Management marks: "))
        self.materialHandling = int(input("Enter your materialHandling marks: "))
    def showRresult(self):
        # print("Machine Learning Marks : ", self.machineLearning)
        print(f"your AutoCad marks is {self.autocad}")
        print(f"your 2d Drawing marks is {self.twoDrawing}")
        print(f"your Interior is {self.interior}")
         
BE = BEmarksheetSystem()
BE.compulsory()
BE.architechture()
BE.showRresult()
 