#veri modelleri
from pydantic import BaseModel
from typing import List,Dict

class TranslationRequest(BaseModel):  #çeviri talebi
    text=str
    languages=List[str]

class TaskResponse(BaseModel): #sonucu takip etmek için
    task_id=int

class TranslationStatus(BaseModel): #sonucu tutar
    task_id=int
    status=str
    translations=Dict[str,str]