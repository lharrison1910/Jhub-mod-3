class Route:
    def __init__(self, file):
        self.file = f"Route00{file}.txt"
        self.movement
        self.path

        print(self.file)
        self.openFile 

    def openFile(self):
        with open(self.file) as file:
            self.movement = [line.strip() for line in file]

        if self.plotRoute() == "Error":
            print("Error: Route out of bounds")

    def plotRoute(self):
        self.path = [self.movement[0]-1,self.movement[1]-1]
        for i in range(2,self.movement.length()):
            if self.movement[i] == 'N':
                if self.validate(self.path[-1][0]+1):
                    self.path.append([self.path[-1][0]+1,self.path[-1][1]])
                    continue
                return "Error"
            elif self.movement[i] == 'S':
                if self.validate(self.path[-1][0]+1):
                    self.path.append([self.path[-1][0]-1,self.path[-1][1]])
                    continue
                return "Error"
            elif self.movement[i] == 'E':
                if self.validate(self.path[-1][0]+1):
                    self.path.append([self.path[-1][0],self.path[-1][1]+1])
                    continue
                return "Error"
            else:
                if self.validate(self.path[-1][0]+1):
                    self.path.append([self.path[-1][0]+1,self.path[-1][1]-1])
                    continue
                return "Error"
            
        return "Success"
    
    def validate(param):
        if 0<=param & param >=12:
            return True
        return False
    
    def printOut(self):
        out = {
            "0":"   :   :   :   :   :   :   :   :   :   :   :   :   :   ",
            "odd": "---:---:---:---:---:---:---:---:---:---:---:---:---:---",
            "even": f"  {row}:   :   :   :   :   :   :   :   :   :   :   :   :   "
            }
        row = 12
        
        for i in range(0,25):

            if i == 0:
                print(out["0"])
            
            if i % 2 == 1:
                print(out["odd"])
            else:
                for j in self.path:
                    if row in j[0]:
                        index = j[1]*5
                        result = out["even"][:index]+"x"+out["even"][index+1]
                        print(result)
                    else:
                        print(out["even"])
                        continue
                
        print("   : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 :10 :11 :12 :   ")

        print('Coordinates')
        for i in range(0,self.path.length()-1): 
            print(f"({self.path[i][0]},{self.path[i][1]})")


'''
   :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 12:   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 11:   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 10:   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 9 :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 8 :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 7 :   :   :   :   :   :   :   :   :   :   :   :   :  
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 6 :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 5 :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 4 :   :   :   :   :   :   :   :   :   :   :   :   :   
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 3 :   :   :   :   :   :   :   :   :   :   :   :   :
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 2 :   :   :   :   :   :   :   :   :   :   :   :   :
---:---:---:---:---:---:---:---:---:---:---:---:---:---
 1 :   :   :   :   :   :   :   :   :   :   :   :   :
---:---:---:---:---:---:---:---:---:---:---:---:---:---
   : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 :10 :11 :12 :

'''