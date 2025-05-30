import os
os.environ["HF_HOME"] = "/home/username/transformers_cache"
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")  
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

def translate_text(text, lang):
    tokens = tokenizer(text, return_tensors="pt")
    output = model.generate(**tokens, forced_bos_token_id=tokenizer.get_lang_id(lang))
    return tokenizer.decode(output[0], skip_special_tokens=True)    

while True:
    text = input("Enter text to translate: ")
    language = input("Enter target language code: ")    
    print("Translated text:",translate_text(text, language))
    print()