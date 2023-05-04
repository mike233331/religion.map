from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Session

sqlite_database = "sqlite:///mikka.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass



class church(Base):
    __tablename__ = "church"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    City = Column(String)
    coordinates = Column(String)
    description = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))
    religion_id = Column(Integer, ForeignKey("religion.id"))
    date_of_construction = Column(Integer)
    country = relationship("Country", back_populates="users")
    relig = relationship("religion", back_populates="user")



class religion(Base):
    __tablename__ = "religion"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user = relationship("church", back_populates="relig")


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("church", back_populates="country")



Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    #Создаем все религии
    Christianity = religion(name="Christianity")
    Islam = religion(name="Islam")
    Hinduism = religion(name="Hinduism")
    Buddhism = religion(name="Buddhism")
    Chinese_traditional_religion = religion(name="Chinese traditional religion")
    African_traditional_religions = religion(name="African traditional religions")
    # создаем компании
    Georgia = Country(name="Georgia")
    Egypt = Country(name="Egypt")
    Belarus = Country(name="Belarus")
    bolgaria = Country(name="bolgaria")
    Serbia = Country(name="Serbia")
    Greece = Country(name="Greece")
    Romania = Country(name="Romania")
    Ukraine = Country(name="Ukraine")
    Ethiopia = Country(name="ethiopia")
    Russia = Country(name="Russia")
    # создаем пользователей
    q1 = church(name="Cathedral of St. Sophia", City="Novgorod", date_of_construction=1045, coordinates="58° 31′ 18″ N, 31° 16′ 34″ E", description="The Cathedral of Holy Wisdom (the Holy Wisdom of God) in Veliky Novgorod is the cathedral church of the Metropolitan of Novgorod and the mother church of the Novgorodian Eparchy" )
    q2 = church(name="Anchiskhati Basilica", City="Tbilisi", date_of_construction=522, coordinates="41° 41′ 44″ N, 44° 48′ 25″ E", description="The Anchiskhati Basilica of St Mary (Georgian: ანჩისხატი) is the oldest surviving church in Tbilisi, Georgia. It belongs to the Georgian Orthodox Church and dates from the sixth century")
    q3 = church(name="Saint Sophia Cathedral", City="Polotsk", date_of_construction="1030", coordinates="55° 29′ 10″ N, 28° 45′ 31.4″ E", description="first mentioned in the Voskresenskaia Chronicle under the year 1056) and 1066. It stands at the confluence of the Polota River and Western Dvina River on the eastern side of the city and is probably the oldest church in Belarus.")
    # устанавливаем для компаний списки пользователей
    Russia.users = [q1]
    Georgia.users = [q2]
    Belarus.users = [q3]
    Christianity.user = [q1, q2, q3]
    # добавляем компании в базу данных, и вместе с ними добавляются пользователи
    db.add_all([Georgia, Egypt, Belarus, bolgaria, Serbia, Greece, Romania, Ukraine, Ethiopia, Russia])
    db.add_all([Christianity, Islam, Hinduism, Buddhism, Chinese_traditional_religion, African_traditional_religions])
    db.commit()