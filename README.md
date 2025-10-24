# 🛍️ ShopNera

**ShopNera** is a smart local marketplace platform built for Pakistan.
It connects **nearby kiryana stores, restaurants, and riders** — making it easy for users to order anything from their area and get it delivered fast.

This is the **MVP (Minimum Viable Product)** version — designed to be lightweight, scalable, and AI-ready.
ShopNera consists of a **mobile app (Kivy)** for Android and a **backend (FastAPI)** with plans for AI recommendation, an admin dashboard, and an advanced search system.

---

## 🚀 Features (MVP Stage)

* 🏠 **Local Marketplace:** Browse and order from nearby stores & restaurants.
* 🤖 **AI Recommendations (Planned):** Personalized product suggestions based on user preferences and behavior.
* 🔍 **Smart Search Engine:** Filter by category, price, location, or shop type.
* 🚴 **Rider System:** Delivery handled by local riders (self or third-party).
* 🧑‍💼 **Admin Panel (Planned):** Manage shops, orders, and analytics.
* 📱 **Cross-Platform:** Currently focused on Android (Kivy), with plans for iOS later.

---

## 🧱 Project Structure

```
ShopNera/
│
├── backend/              # FastAPI backend (API, database, AI logic)
│   ├── api/              # API routes
│   ├── core/             # Config & database setup
│   ├── models/           # ORM models
│   ├── services/         # Business logic (orders, recommendations, etc.)
│   ├── ai/               # AI models (recommendation, search)
│   ├── admin_panel/      # Admin dashboard (future)
│   ├── utils/            # Helper functions
│   └── tests/            # Unit tests
│
├── mobile_app/           # Kivy-based Android app
│   ├── screens/          # App screens (Home, Shop, Cart, etc.)
│   ├── models/           # Data models
│   ├── services/         # API calls & logic
│   ├── utils/            # Helpers & constants
│   └── assets/           # Icons & logo
│
└── docs/                 # Documentation
    ├── README.md
    ├── API_DOCS.md
    ├── DATABASE_SCHEMA.md
    └── ROADMAP.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chaudhary-hadi27/ShopNera.git
cd ShopNera
```

### 2️⃣ Setup Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3️⃣ Setup Mobile App (Kivy)

```bash
cd ../mobile_app
pip install -r requirements.txt
python main.py
```

---

## 🧠 Tech Stack

| Component   | Technology                               |
| ----------- | ---------------------------------------- |
| Mobile App  | [Kivy](https://kivy.org/)                |
| Backend     | [FastAPI](https://fastapi.tiangolo.com/) |
| Database    | PostgreSQL / SQLite                      |
| AI System   | Scikit-learn / Transformers (future)     |
| Admin Panel | Streamlit / React (future)               |
| Deployment  | Docker + Render / Railway (planned)      |

---

## 🌐 Future Roadmap

* [ ] AI-based product recommendation system
* [ ] Admin dashboard for shop owners
* [ ] Rider tracking & delivery system
* [ ] Payment gateway integration (EasyPaisa, JazzCash)
* [ ] Push notifications for orders & offers
* [ ] iOS app version
* [ ] Multi-language support (Urdu + English)

---

## 💡 Vision

> “Empowering local shops and riders through AI — ShopNera connects communities and simplifies local commerce.”

---

## 👨‍💻 Author

**Chaudhary Hadi**
AI Developer & Founder of ShopNera
📧 Email: [chaudharyhadi27@gmail.com](mailto:chaudharyhadi27@gmail.com)
🌐 [GitHub](https://github.com/chaudhary-hadi27)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and build upon it.

---

## ❤️ Contributing

Contributions, ideas, and collaborations are welcome!
If you'd like to improve ShopNera, please fork the repo, make your changes, and submit a pull request.
