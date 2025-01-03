import openai
from sqlalchemy.orm import Session
from crud import update_translation_task
from dotenv import load_dotenv
import os
load_dotenv()
OPEN_API_KEY=os.getenv("OPEN_API_KEY")

def perform_translation(task:int,text:str,languages:list,db:Session):
    translations={} #çevirileri içinde tutacak
    for lang in languages:
        try:
            response.openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role":"system", "content":f"You are a helpful assistant that translates text into {lang}"},#gptye iletilecek mesaj
                    {"role":"user","content":text} #çevrilecek metin
                ],
                max_tokens=1000 #max süre
            )
            translated_text=response["choices"][0]["message"]["content"].strip() #apiden dönen yanıt boşluksuz şekilde çekilecek
            translations[lang]=translated_text #translation listesine mesaj eklenecek
        except Exception as e:
            print(f"Error translating to {lang}:{e}")
            translations[lang]=f"Error:{e}" 
        except Exception as e:
            print(f"Unexpected error:{e}")
            translations[lang]=f"Unexpected error: {e}"
            update_translation_task(db,task_id,translations) #çeviri durumu güncellenecek