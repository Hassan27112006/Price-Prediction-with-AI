# Price-Prediction-with-AI
# 🏠 Real Estate Price Prediction App with Voice Assistant

An intelligent and interactive web application built using **Streamlit** and **Machine Learning** to predict real estate prices based on user-provided features. Includes a fully functional **Voice Assistant** powered by `speechrecognition` and `pyttsx3` for audio-based interaction.

## ✅ Features

- 🔮 Predict property price using inputs like area, bedrooms, bathrooms, and location
- 🧠 Use a pre-trained **SVR (Support Vector Regression)** model with real housing data
- 📊 Integrated **EDA**: Data summaries, univariate and bivariate analysis
- 🎤 Voice-based assistant to answer queries and take voice commands
- 🧱 Clean, modular codebase using OOP and Streamlit best practices
- 💾 Model is saved with scaler and feature columns for real-world prediction

## 🧠 How It Works

1. User enters property details manually OR speaks using the microphone.
2. Input is cleaned, encoded, and scaled to match training data.
3. The **SVR model** makes a prediction.
4. A voice assistant can also explain or answer related questions.

## 🗂️ File Structure

real_estate_app/
│
├── app.py
├── model/
│ └── svm_model.pkl
├── core/
│ ├── model_utils.py
│ ├── input_handler.py
│ └── voice_handler.py
├── ui/
│ ├── sidebar.py
│ └── layout.py
├── voice/
│ └── NLPvoiceAssistant.py
└── README.md

bash
Copy
Edit

## 📥 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-estate-app.git
cd real-estate-app
2. Create and Activate a Virtual Environment (Optional)
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Application
bash
Copy
Edit
streamlit run app.py
📦 Key File Descriptions
File	Description
app.py	Main Streamlit script that brings together the UI and logic
model_utils.py	Loads the trained ML model and related preprocessor
input_handler.py	Transforms user input into model-ready data
voice_handler.py	Initializes the voice assistant
sidebar.py	Creates sidebar components like sliders and dropdowns
layout.py	Shows prediction, recognized voice input, assistant responses
svm_model.pkl	Pre-trained SVR model and scaler (saved via pickle)
NLPvoiceAssistant.py	Custom logic for listening to and responding to voice

🎤 Voice Assistant Info
Uses speechrecognition to listen and convert voice to text

Uses pyttsx3 to respond verbally to the user

Wraps logic in a custom NLPvoiceAssistant class

Integrated into Streamlit for full voice-based prediction experience

🛠️ Technologies Used
Python 3.10+

Streamlit

scikit-learn

pandas

numpy

seaborn

matplotlib

speechrecognition

pyttsx3

📸 Screenshots
scss
Copy
Edit
![Sidebar Input](screenshots/sidebar.png)
![Prediction Output](screenshots/output.png)
![Voice Assistant](screenshots/voice.png)
🙌 Credits
Created by: Muneeb Hassan
Structured and documented by: ChatGPT

📜 License
This project is licensed under the MIT License.

⭐ Support
If you found this helpful, give the repository a ⭐ on GitHub.

Copy
Edit







You said:
give all these in one file dont make structures just give give me one time copy paste do evreything in text


ChatGPT said:
markdown
Copy
Edit
# 🏠 Real Estate Price Prediction App with Voice Assistant

An intelligent and interactive web application built using **Streamlit** and **Machine Learning** to predict real estate prices based on user-provided features. Includes a fully functional **Voice Assistant** powered by `speechrecognition` and `pyttsx3` for audio-based interaction.

## ✅ Features

- 🔮 Predict property price using inputs like area, bedrooms, bathrooms, and location
- 🧠 Use a pre-trained **SVR (Support Vector Regression)** model with real housing data
- 📊 Integrated **EDA**: Data summaries, univariate and bivariate analysis
- 🎤 Voice-based assistant to answer queries and take voice commands
- 🧱 Clean, modular codebase using OOP and Streamlit best practices
- 💾 Model is saved with scaler and feature columns for real-world prediction

## 🧠 How It Works

1. User enters property details manually OR speaks using the microphone.
2. Input is cleaned, encoded, and scaled to match training data.
3. The **SVR model** makes a prediction.
4. A voice assistant can also explain or answer related questions.

## 🗂️ File Structure

app.py - Main Streamlit entry point  
model/svm_model.pkl - Trained SVR model with scaler and column names  
core/model_utils.py - Loads model, scaler, and feature columns  
core/input_handler.py - Builds and scales input for prediction  
core/voice_handler.py - Initializes the voice assistant  
ui/sidebar.py - Streamlit sidebar inputs for user  
ui/layout.py - Displays titles, outputs, and results  
voice/NLPvoiceAssistant.py - Contains the voice assistant logic  
README.md - Project documentation  

## 📥 Setup Instructions

1. Clone the Repository  
git clone https://github.com/your-username/real-estate-app.git
cd real-estate-app

mathematica
Copy
Edit

2. Create and Activate a Virtual Environment (optional but recommended)  
python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

markdown
Copy
Edit

3. Install Required Packages  
pip install -r requirements.txt

mathematica
Copy
Edit

4. Run the Application  
streamlit run app.py

pgsql
Copy
Edit

## 📦 Key File Descriptions

app.py – The main file that runs the Streamlit app  
model_utils.py – Loads the pre-trained model, scaler, and feature list  
input_handler.py – Builds a feature vector from user input  
voice_handler.py – Loads and initializes the voice assistant  
sidebar.py – Streamlit sidebar with sliders and dropdowns  
layout.py – Displays UI elements such as titles and predictions  
svm_model.pkl – Trained SVR model with preprocessing objects  
NLPvoiceAssistant.py – Contains logic for voice interaction  

## 🎤 Voice Assistant Info

- Uses `speechrecognition` to convert voice to text  
- Uses `pyttsx3` for speech output  
- The `NLPvoiceAssistant` class listens to user input, processes the query, responds through text and voice, and interacts with the ML model when needed  
- Activated via a "🎤 Ask via Voice" button in the Streamlit app  

## 🛠️ Technologies Used

- Python 3.10+  
- Streamlit  
- scikit-learn  
- pandas  
- numpy  
- seaborn  
- matplotlib  
- speechrecognition  
- pyttsx3  

## 📸 Screenshots

(You can include images like the following if available)  
![Sidebar Input](screenshots/sidebar.png)  
![Prediction Output](screenshots/output.png)  
![Voice Assistant](screenshots/voice.png)

## 🙌 Credits

Created by: **Muneeb Hassan**  
Documentation and Structuring by: [ChatGPT](https://openai.com/chatgpt)

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and build upon it.

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.