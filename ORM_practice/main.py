import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from ORM_practice.models import Book, Publisher, Shop, Sale, Stock, create_table
from ORM_practice.config import user, password, host, port, database

DSN = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open('test_data.json', 'r') as fd:
    data = json.load(fd)
for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()


def search_publisher():
    search_pub = input("введите название или id издателя:")
    try:
        if type(int(search_pub)) == int:
            for elem in session.query(Publisher).filter(Publisher.id == int(search_pub)).all():
                print(elem)
    except ValueError:
        for elem in session.query(Publisher).filter(Publisher.name == search_pub).all():
            print(elem)


def search_shop():
    what_shop = input('Введите название книги:')

    for v in session.query(Shop).join(Stock).join(Book).filter(Book.title == what_shop).all():
        print('ваша книга продаётся в магазинах ниже:')
        print(v)


if __name__ == "__main__":
    search_publisher()
    search_shop()
session.close()
