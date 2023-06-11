class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f'{metacls}: __prepare__')
        return {'hoge': 'ほげ'}

    def __new__(metacls, name, bases, disc, **kwargs):
        print(f'{metacls}: __new__')
        return super().__new__(metacls, name, bases, disc)

    def __init__(cls, name, bases, disc, **kwargs):
        print(f'{cls}: __init__')
        super().__init__(name, bases, disc)

    def __call__(cls, *args, **kwargs):
        print(f'{cls}: __call__')
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    pass


if __name__ == '__main__':
    c = MyClass()
    print(MyClass.hoge)
