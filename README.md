# 🎵 MoodMuse

## 🚀 Basic Details

**Team Name:** Ignite  
**Team Members:** Anunanda M,Devika N N
**Track:** Music 
**Problem Statement:**  
In today’s emotionally demanding world, music is a powerful tool for mood regulation. However, existing platforms fail to understand and respond to a user's real-time emotions.

**💡 Solution:**  
MoodMuse is a browser-based AI-powered web application that detects user mood from text or selection and responds by either recommending Spotify tracks or generating personalized AI music using Magenta.js—right in the browser.

**🧠 Project Description:**  
MoodMuse is built for emotional expression and mental well-being. It offers:
- Song recommendations based on mood selected from a dropdown.
- AI-generated music based on free-form emotional text input, processed using rule-based NLP.
- Real-time melody generation in the browser using TensorFlow’s Magenta.js.

---

## 🛠️ Technical Details

### 🧰 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **AI Music Generation:** Magenta.js (TensorFlow.js)
- **Music Recommendations:** Predefined Spotify track mapping

### 📦 Libraries/Tools Used
- Flask
- Magenta.js
- CSS
- JSON / REST APIs (within Flask)

---

## 🧪 Implementation

1. **Section 1 - Mood-Based Spotify Recommendations:**
   - User selects mood from a dropdown.
   - Flask backend maps it to a predefined list of Spotify tracks.
   - Songs are rendered with clickable Spotify links.

2. **Section 2 - Emotion Detection from Text:**
   - User types how they feel.
   - Flask detects the mood using rule-based keyword matching.
   - Detected mood is sent back to the frontend.
   - Magenta.js generates a melody in-browser based on mood.

---

## ⚙️ Installation & Execution

### 🖥️ Requirements
- Python 3.10+
- pip (Python package manager)

### 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/moodmuse.git
   cd moodmuse

