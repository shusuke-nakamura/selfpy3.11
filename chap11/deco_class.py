def hoge_deco(cls):
    cls.hoge = 'ほげ'
    return cls


@hoge_deco
class MyClass:
    print


if __name__ == '__main__':
    print(MyClass.hoge)
