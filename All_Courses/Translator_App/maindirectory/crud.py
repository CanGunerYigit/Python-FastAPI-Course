#veritabanı işlemleri için görev ekleme, commit etmme ve refreshleme
from sqlalchemy.orm import Session
import models

def create_translation_task(db:Session,text:str,Languages:list): #yeni çeviri görevi
    task=models.TranslationTask(text=text,Languages=Languages) #yeni nesne oluşturur
    db.add(task) #yeni taskı veritabanına ekler
    db.commit() #commit ederek kalıcı hale getirir
    db.refresh(task)
    return task

def get_translation_task(db:Session,task_id:int): #taskı id sine göre getirir
    return db.query(models.TranslationTask).filter(models.TranslationTask.id==task_id).first() #task idsine göre arama sorgusu

def update_translation_task(db:Session,task_id:int,translations:dict): #taskı güncelleme
    task=db.query(models.TranslationTask).filter(models.TranslationTask.id==task_id).first()
    task.translations = translations
    task.status="completed" #models.py deki defaultu completed olarak değiştirdik
    db.commit()
    db.refresh(task)
    return task

