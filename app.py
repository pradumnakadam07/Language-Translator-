from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

app = Flask(__name__)
CORS(app)  

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    lang = data.get("lang")

    if not text or not lang:
        return jsonify({"error": "Missing text or language"}), 400

    tokens = tokenizer(text, return_tensors="pt")
    output = model.generate(**tokens, forced_bos_token_id=tokenizer.get_lang_id(lang))
    translated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
