
# 🍽️ University Cafeteria Ordering System

This is a Django-based web application that allows university students to browse the cafeteria menu, place orders, and manage them efficiently. It includes user registration/login, category-based item listings, and an intuitive ordering system.

---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/university-cafeteria.git
   cd university-cafeteria
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Visit `http://127.0.0.1:8000/` in your browser.

---

## 🚀 Features Implemented

- 👤 User registration, login, and logout
- 📋 Menu page with categorized food items
- ➕ Add/remove item quantities
- 🛒 Place and preview orders
- 🖼️ Upload media (images for categories/items)
- 🗃️ Admin panel for managing data

---

## 📁 Project Structure

```
project/
├── cafeteria/           # App for cafeteria logic
├── users/               # User registration/login
├── static/              # Static CSS/JS files
├── media/               # Uploaded images
├── templates/           # HTML templates
├── uni_cafe/            # Main project config
├── manage.py            # Django entry point
└── db.sqlite3           # SQLite database
