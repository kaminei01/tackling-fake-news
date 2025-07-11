#  Tackling Fake News – Real-time Detection Web App

A full-stack web application that detects fake news using a fine-tuned transformer model. Users can analyze claims, view results, and submit feedback — all in real time.

---

##  Features

-  Fake news detection using RoBERTa model
-  Real-time verdict updates via WebSocket (Socket.IO)
-  Light/Dark mode toggle
-  Chart.js visual statistics
-  Feedback form for user suggestions

---

##  Tech Stack

| Frontend            | Backend               | Database        | ML/AI Model         |
|---------------------|------------------------|------------------|---------------------|
| React.js + MUI      | FastAPI + Python Socket.IO | MongoDB (local) | RoBERTa (Transformers) |

---

## 📁 Project Structure

```
tackling-fake-news/
├── backend/
│   ├── api/             # FastAPI routes
│   ├── models/          # RoBERTa model
│   ├── analysis/        # Analyzer logic
│   ├── preprocessing/   # Text cleaning
│   ├── database/        # MongoDB connection
│   └── main.py          # FastAPI + Socket.IO app
├── frontend/
│   └── src/
│       ├── pages/       # Home, Analyze, Results, Feedback
│       ├── components/  # Chart, FAB, etc.
│       └── App.js       # Main app structure
```

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kaminei01/tackling-fake-news.git
cd tackling-fake-news
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```
⚠️ **Important:** The model files are too large to store on GitHub.

Instead, download the model files from the link below:

📦 **Model Download:** https://drive.google.com/drive/folders/18lm2d3k9htXQ5z89qI9OvY-hwZSCPRO6?usp=drive_link

After downloading:
- Extract the files (if zipped)
- Place the extracted folder inside:
  ```
  backend/models/Fake-News-Bert-Detect/
  ```

**Update the Model Path:**  
Open `backend/models/roberta_model.py` and update the model path variable to match the new location. For example:

```python
model_path = "backend/models/Fake-News-Bert-Detect"
```

Make sure MongoDB is running locally on `localhost:27017`.

Start FastAPI with Socket.IO:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Setup Frontend

```bash
cd frontend
npm install
npm start
```

---

##  Testing

Try submitting a fake/real claim from the Analyze page. The result will appear immediately in the Results page (thanks to WebSocket).

---

##  Feedback System

Users can submit feedback from the `/feedback` page. All feedback gets stored in the `feedback` collection in MongoDB.

---

##  Future Enhancements

-  Admin dashboard to review feedback
-  Browser extension for live news scanning
-  Multi-language support
-  Model retraining with active learning

---"# tackling-fake-news" 
