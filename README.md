# 🎓 AI-Based Learning Style Predictor

An interactive Streamlit web application that helps users identify their **dominant learning style** — **Visual**, **Auditory**, or **Kinesthetic** — through a short quiz powered by Machine Learning.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-%23FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-ML-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Deployed-brightgreen?style=for-the-badge"/>
</div>

---

## 📌 Try It Out

👉 [Click here to launch the app on Streamlit Cloud](https://ai-based-learning-style-predictor-kgqy7zfx4dmnpcwxdyqddy.streamlit.app/)

---

## 🧠 About the Project

This project aims to make learning **personalized** by helping users discover how they learn best:

- 📊 Uses a trained Machine Learning model built on ML algorithm i.e., **Random Forest Classifier**.
- 📝 Takes inputs from a custom-designed **15-question** quiz.
- 🧑‍🏫 Predicts if the user is a **Visual, Auditory, or Kinesthetic learner**.
- 💡 Offers **in-depth explanations**, **study tips**, and **useful learning resources** for each style.

---

## 💻 Tech Stack

| Technology     | Purpose                             |
|----------------|-------------------------------------|
| `Python`       | Core programming language           |
| `scikit-learn` | Model training and prediction       |
| `Streamlit`    | Web app frontend                    |
| `joblib`       | Model serialization                 |
| `JSON`         | Question handling                   |
| `GitHub`       | Code hosting and version control    |
| `Streamlit Cloud` | App deployment                   |

---

## 📂 Project Structure

```bash
├── app.py                    
├── learning_style_model.pkl   # Trained ML model 
├── questions.json             # Quiz questions 
├── learning_style_dataset.csv # Dataset used for training 
```
---

## 🔍 Learning Styles Explained

| Learning Style | Description |
|----------------|-------------|
| 👁️ **Visual**   | Learns best with images, diagrams, color codes |
| 🎧 **Auditory** | Learns best through listening, speaking aloud |
| 🤸 **Kinesthetic** | Learns by doing, movement, and hands-on activities |

---

## 🛠 How to Run Locally

1. **Clone the repogit:**
   ```bash
      git clone https://github.com/RohithReddyGK/AI-Based-Learning-Style-Predictor.git
   ```
2. **Install dependencies:**
   ```bash
      pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
      streamlit run app.py
   ```
---

### 🙋‍♂️ Author 
Made with ❤️ by **Rohith Reddy.G.K**

🔗 Github: [@RohithReddyGK](https://github.com/RohithReddyGK)  
🔗 LinkedIn: [@rohithreddygk](https://linkedin.com/in/rohithreddygk)

### Show your support
Give a ⭐️ if you like this project!
