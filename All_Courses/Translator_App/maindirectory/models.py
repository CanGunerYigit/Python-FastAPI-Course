from sqlalchemy import Column,Integer,String,Text,JSON

from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class TranslationTask(Base):
    __tablename__ = 'translation_task' #tablo ismi
    id=Column(Integer,primary_key=True,index=True) #tabloda int tipinde id sütununu oluşturduk
    text=Column(Text,nullable=False) #text sütunu
    languages=Column(JSON,nullable=False) #languages sütunu
    status=Column(String,default="in progress") #status sütunu
    translation=Column(JSON,default={})