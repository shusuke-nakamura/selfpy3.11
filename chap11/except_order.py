try:
    data = 5 / 0
except Exception:
    print('Exception')
except ArithmeticError:
    print('AirthmeticRoor')
except OverflowError:
    print('OverflowError')
