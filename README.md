# 📧 Spam Mail Detector App

A lightweight, intelligent web app to detect spam emails using machine learning. This app is built with **Scikit-learn**, **Streamlit**.

---

## Features

- Detects whether a mail is **Spam** or **Not Spam**
- Built using **CountVectorizer + Multinomial Naive Bayes**
- Clean & interactive **Streamlit UI**
- Real-time predictions on input email text
- Easy to extend with **Gmail Inbox Scanner**

---

## Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Pipeline**: `CountVectorizer` for feature extraction → Naive Bayes classifier
- **Trained On**: CSV dataset with labeled email text
- **Saved Model**: `models/spam_model.pkl` using `joblib`

---

## 🌐 Try It Online

[Deployed on Streamlit](https://spam-email-detection-uctzxjslqym2v8kmanchnu.streamlit.app/)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/ParthSengar28/Spam-Email-Detection/issues).

---

## 🙋‍♂️ Author

**Parth Sengar**  
📧 sengarparth01@gmail.com  
🌐 [GitHub](https://github.com/ParthSengar28)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
