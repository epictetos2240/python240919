



def main():
    score = input("학점입력 > ")
    try:
        if not score.isdigit():
            raise
        
        if score > 4.5:
            raise
        if score < 0:
            raise
    except:
        exit()
    if score == 4.5:
        print("신")
    if 4.2 < score < 4.5:
        print("교수님의 사랑")
    if 3.5 < score < 4.2:
        print("현체제의 수호자")
    if 2.8 < score < 3.5:
        print("일반인")
    if 2.3 < score < 2.8:
        print("일탈을 꿈꾸는소시민")
    if 1.75 < score < 2.3:
        print("오락문화의 선구자")
    if 1.0 < score < 1.75:
        print("불가촉천민")
    if 0.5 < score < 1.0:
        print("자벌레")
    if 0 < score < 0.5:
        print("플랑크톤")
    if score == 0:
        print("시대를 앞서가는 혁명의 씨앗")



if __name__ == "__main__" :
    main()