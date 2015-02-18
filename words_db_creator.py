from sqlalchemy import create_engine, Column, Integer, CHAR, VARCHAR, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('sqlite:///words.sqlite')
engine.echo = False
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Words(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    c0 = Column(CHAR, default=".", index=True)
    c1 = Column(CHAR, default=".", index=True)
    c2 = Column(CHAR, default=".", index=True)
    c3 = Column(CHAR, default=".", index=True)
    c4 = Column(CHAR, default=".", index=True)
    c5 = Column(CHAR, default=".", index=True)
    c6 = Column(CHAR, default=".", index=True)
    c7 = Column(CHAR, default=".", index=True)
    c8 = Column(CHAR, default=".", index=True)
    c9 = Column(CHAR, default=".", index=True)
    c10 = Column(CHAR, default=".", index=True)
    c11 = Column(CHAR, default=".", index=True)
    c12 = Column(CHAR, default=".", index=True)
    c13 = Column(CHAR, default=".", index=True)
    c14 = Column(CHAR, default=".", index=True)
    c15 = Column(CHAR, default=".", index=True)
    c16 = Column(CHAR, default=".", index=True)
    c17 = Column(CHAR, default=".", index=True)
    c18 = Column(CHAR, default=".", index=True)
    c19 = Column(CHAR, default=".", index=True)
    c20 = Column(CHAR, default=".", index=True)
    c21 = Column(CHAR, default=".", index=True)
    c22 = Column(CHAR, default=".", index=True)
    c23 = Column(CHAR, default=".", index=True)
    c24 = Column(CHAR, default=".", index=True)
    c25 = Column(CHAR, default=".", index=True)
    c26 = Column(CHAR, default=".", index=True)
    c27 = Column(CHAR, default=".", index=True)
    c28 = Column(CHAR, default=".", index=True)
    c29 = Column(CHAR, default=".", index=True)
    word = Column(VARCHAR(30), unique=True, default="", index=True)
    length = Column(Integer, default=0, index=True)

Base.metadata.create_all(engine)

count = 0
for i in range(52):
    for j in range(28):
        count += 1
        sys.stdout.write("\r processing(%d/%d)..." % (count, 52*28))
        sys.stdout.flush()
        with open("words\words" + str(i) + "x" + str(j) + ".txt", "r") as words_file:
            count1 = 0
            for each_line in words_file:
                word = each_line.strip().lower()
                present_word = session.query(Words).filter_by(word=word).first()
                if present_word is not None:
                    continue
                justified_word = word.ljust(30, '.')
                word = Words(
                    c0=justified_word[0],
                    c1=justified_word[1],
                    c2=justified_word[2],
                    c3=justified_word[3],
                    c4=justified_word[4],
                    c5=justified_word[5],
                    c6=justified_word[6],
                    c7=justified_word[7],
                    c8=justified_word[8],
                    c9=justified_word[9],
                    c10=justified_word[10],
                    c11=justified_word[11],
                    c12=justified_word[12],
                    c13=justified_word[13],
                    c14=justified_word[14],
                    c15=justified_word[15],
                    c16=justified_word[16],
                    c17=justified_word[17],
                    c18=justified_word[18],
                    c19=justified_word[19],
                    c20=justified_word[20],
                    c21=justified_word[21],
                    c22=justified_word[22],
                    c23=justified_word[23],
                    c24=justified_word[24],
                    c25=justified_word[25],
                    c26=justified_word[26],
                    c27=justified_word[27],
                    c28=justified_word[28],
                    c29=justified_word[29],
                    word=word,
                    length=len(word),
                )
                session.add(word)
            session.commit()