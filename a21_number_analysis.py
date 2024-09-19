# 사용자가 여러 숫자를 쉼표로 구분하여 입력을 받습니다
# ex) 10, 20, 30, abc
# 합계계산 , 평균계산, 최대값 계산, 최소값 계산
# 만약에 문자가 있으면 무시하고 계산을 진행하고 어떤 값이 무시되었는지 출력!
# 유효한 숫자가 없습니다. -> 
# format을 써서 자리수를 유효숫자 소수점 3번째 자리까지 출력


def main():
    a = input("값을 입력하세요")
    b = a.split(",")
    b = list(map(int,a))
    print(b)
    
    # sum_b = sum(b)
    # averge_b = sum(b)/len(b)
    # max_b = max(b)
    # min_b = min(b)

    # print("합계 : {}",sum_b)


    
   

if __name__ == "__main__" :
    main()