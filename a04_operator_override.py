class Abc():
    def __add__(self,bb):
        return "rusult of add"

def main() :
    a = Abc()
    b = Abc()
    c = a + b 
    print(c)
    
# 

if __name__ == "__ main__":
    main()

