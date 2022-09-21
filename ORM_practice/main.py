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

if __name__ == "__main__":

    find_pub = input("введите название или id издателя:")
    try:
        if type(int(find_pub)) == int:
            for v in session.query(Publisher).filter(Publisher.id == int(find_pub)).all():
                print(v)
    except ValueError:
        for v in session.query(Publisher).filter(Publisher.name == find_pub).all():
            print(v)

session.close()
