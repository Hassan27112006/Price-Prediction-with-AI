import os
import re
import pickle
import pandas as pd
import speech_recognition as sr
import pyttsx3
import requests
import os
os.environ['OPENROUTER_API_KEY'] = "Bearer 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"


class NLPvoiceAssistant:
    def __init__(self, model_path='models/svm_model.pkl',
                 api_key=None, flash_model='google/gemini-flash-1.5-8b',
                 base_url="https://openrouter.ai/api/v1"):
        # Load price prediction model
        with open(model_path, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.scaler = data['scaler']
            self.columns = data['columns']

        # Voice engine
        self.tts = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        # Setup Gemini Flash endpoint
        self.flash_model = flash_model
        self.base_url = base_url
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OpenRouter API key required!")
    def prepare_df(self, area, bedrooms, bathrooms, location):
        df = pd.DataFrame({ 
            'area':[area], 'bedrooms':[bedrooms], 'bathrooms':[bathrooms],
            'location_Countryside':[1 if location=='Countryside' else 0],
            'location_Downtown':[1 if location=='Downtown' else 0],
            'location_Suburbs':[1 if location=='Suburbs' else 0] 
        })
        for col in self.columns:
            if col not in df.columns:
                df[col] = 0
        return self.scaler.transform(df[self.columns])

    def ask_flash(self, prompt: str) -> str:
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": self.api_key}
        payload = {
            "model": self.flash_model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            return res.json()["choices"][0]["message"]["content"]
        else:
            return f"Error {res.status_code}: {res.text}"

    def speak(self, text):
        print("🤖", text)
        self.tts.say(text)
        self.tts.runAndWait()

    def listen(self):
        with sr.Microphone() as mic:
            print("🎙️ Listening…")
            audio = self.recognizer.listen(mic)
        try:
            return self.recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return None
    def get_response(self, query):
                  
                 
        if not query:
                return "Please say that again."
        
        if any(w in query.lower() for w in ["price", "cost", "worth", "value"]):
                return self.get_price(query)
        else:
                 return self.ask_flash(query)


    def parse_inputs(self, query):
        try:
            area_match = re.search(r'(\d+)\s*(sqft|square)', query)
            area = int(area_match.group(1)) if area_match else 1500  # Default: 1500

            bedrooms_match = re.search(r'(\d+)\s*bed', query)
            bedrooms = int(bedrooms_match.group(1)) if bedrooms_match else 3  # Default: 3

            bathrooms_match = re.search(r'(\d+)\s*bath', query)
            bathrooms = int(bathrooms_match.group(1)) if bathrooms_match else 2  # Default: 2

            if 'downtown' in query:
               loc = 'Downtown'
            elif 'countryside' in query:
               loc = 'Countryside'
            else:
               loc = 'Suburbs'  # Default

            return area, bedrooms, bathrooms, loc

        except Exception as e:
            print(f"Error parsing input: {e}")
            return 1500, 3, 2, 'Suburbs'  # fallback defaults


    def get_price(self, query):
        inputs = self.parse_inputs(query)
        df_scaled = self.prepare_df(*inputs)
        price = self.model.predict(df_scaled)[0]
        return f"Estimated price: Rs{price:,.0f}"

    def run(self):
        self.speak("Hello, I'm your assistant. How can I help today?")
        while True:
            q = self.listen()
            if not q:
                self.speak("Please say that again.")
                continue
            if any(w in q for w in ["exit", "quit"]):
                self.speak("Goodbye!")
                break
            if "price" in q:
                resp = self.get_price(q)
            else:
                resp = self.ask_flash(q)
            self.speak(resp)
