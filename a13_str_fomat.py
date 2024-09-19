
def main():
    format_a = "{}만원".format(5000)
    format_b = "파이썬 열공해서 첫 연봉 {}만 원 만들기".format(5000)
    format_c = "{} {} {}".format(3000, 4000, 5000)
    format_d = "{} {} {}".format(1, "문자열", True)

    print(format_a)
    print(format_b)
    print(format_c)
    print(format_d)

if __name__ == "__main__" :
    main()
    