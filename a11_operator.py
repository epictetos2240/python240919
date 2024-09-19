import math

def main():
    pi = 3.141592
    print(pi)
    print(math.pi)
    pi = math.pi
    r = 10
    print(f"원주율 = {pi}")
    print(f"반지름 =" , r)
    print(f"원의 둘레", 2*pi*r)
    print(f"원의 넓이=", pi*r**2)


if __name__ == "__main__" :
    main()
    