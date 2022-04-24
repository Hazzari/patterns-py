class Database:
    _instance = None

    # Проблема в том что инициализатор вызывается 2 раза, и это 2 разных объекта

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)