import sqlalchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

print(sqlalchemy.__version__)

engine = create_engine('sqlite:///value.sqlite', echo=True)
print(engine)

Base = declarative_base()

print(os.path.dirname(__file__))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
session = Session()
# once engine is available
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()

print(our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

ed_user.nickname = 'eddie'
print(session.dirty)

print(ed_user.id)

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)

dat = session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
print(type(dat))
print(dat)

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

from sqlalchemy.orm import aliased

user_alias = aliased(User, name='user_alias')

for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)
for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
query.all()

from sqlalchemy import func

data = session.query(func.count(User.name), User.name).group_by(User.name).all()
print(data)
