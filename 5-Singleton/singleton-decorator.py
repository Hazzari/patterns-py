def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self, name_db):
        print(f'Loading database {name_db}')
        self.name = name_db

    def __str__(self):
        return f'Database {self.name}'


if __name__ == '__main__':
    d1 = Database('NoSQL')
    d2 = Database('PostgresQL')
    print(d1 == d2)
    print(d2)

