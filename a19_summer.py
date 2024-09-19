# datetime을 활용해서 month 데이터를 얻어와서
# 조건문으로 3 -5 포함해서 봄
# 6-8포함 까지 여름
# 9-11포함 까지 가을
# 나머지 겨울을 출력하는 프로그램 작성


import datetime

def main():
    now = datetime.datetime.now()
    # month = now.month
    month = 7
    if month >= 3 and month <= 5:
        print("봄입니다")
    elif month >= 6 and month <= 8:
        print("여름입니다")
    elif month >= 9 and month <= 11:
        print("가을입니다")
    else :
        print("겨울입니다")
  
if __name__ == "__main__" :
    main()