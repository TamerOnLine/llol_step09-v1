# 🌍 Dynamic Multilingual Resume Builder – `llol_step09-v1`

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)
[![i18n](https://img.shields.io/badge/i18n-Multilingual-yellow)](https://www.transifex.com/)

[![Build](https://github.com/TamerOnLine/llol_step08/actions/workflows/main.yml/badge.svg)](https://github.com/TamerOnLine/llol_step08/actions/workflows/main.yml)
[![PostgreSQL Status](https://github.com/TamerOnLine/llol_step08/actions/workflows/postgres-check.yml/badge.svg)](https://github.com/TamerOnLine/llol_step08/actions/workflows/postgres-check.yml)
[![Tests](https://github.com/TamerOnLine/llol_step08/actions/workflows/test.yml/badge.svg)](https://github.com/TamerOnLine/llol_step08/actions/workflows/test.yml)
[![Coverage](https://codecov.io/gh/TamerOnLine/llol_step08/branch/main/graph/badge.svg)](https://codecov.io/gh/TamerOnLine/llol_step08)
[![Last Commit](https://img.shields.io/github/last-commit/TamerOnLine/llol_step08)](https://github.com/TamerOnLine/llol_step08)

[![Release](https://img.shields.io/github/v/release/TamerOnLine/llol_step08?include_prereleases)](https://github.com/TamerOnLine/llol_step08/releases)
[![License](https://img.shields.io/github/license/TamerOnLine/llol_step08)](https://github.com/TamerOnLine/llol_step08)

[![Status](https://img.shields.io/badge/status-stable-brightgreen)]()
[![Maintained](https://img.shields.io/badge/maintained-yes-success.svg)]()
[![Open Issues](https://img.shields.io/github/issues/TamerOnLine/llol_step08)](https://github.com/TamerOnLine/llol_step08/issues)
[![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/TamerOnLine/llol_step08/pulls)

[![Stars](https://img.shields.io/github/stars/TamerOnLine/llol_step08)](https://github.com/TamerOnLine/llol_step08)
[![Forks](https://img.shields.io/github/forks/TamerOnLine/llol_step08)](https://github.com/TamerOnLine/llol_step08)


A powerful open-source platform for building **dynamic, multilingual, and fully customizable resumes** with smart admin control and real-time translation.

---

## ✅ Features

- 🌐 **Multilingual Support**: Arabic, English, and German via `Flask-Babel` + `deep-translator`.
- 🎛️ **Smart Admin Panel**: Add, edit, hide, sort sections/paragraphs/fields dynamically.
- 🧾 **Flexible JSON Storage**: All texts support inline translation (e.g. `title_translations`).
- 🎨 **Live Styling Panel**: Customize font size, colors, and layout via admin settings.
- 🐘 **PostgreSQL + SQLAlchemy**: Scalable and professional database support.
- 🔧 **Built-in Tools**: Auto database creation, translation generation, data inspection.
- 🧩 **Clean Structure**: Organized folders – `models`, `routes`, `templates`, `tools`.

---

## 🧱 Database Structure

```
ResumeSection ──┬── ResumeParagraph ──┬── ResumeField
                │                     │
                │                     └─ field_type, translations
                └─ title_translations, is_visible
```

Each level (section, paragraph, field) supports sorting, visibility, and multilingual content.

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/TamerOnLine/llol_step09-v1
cd llol_step09-v1
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Create `.env`:

```env
DB_NAME=postgreslebenslauf
DB_USER=postgres
DB_PASSWORD=12345
DB_HOST=localhost
DB_PORT=5432
FLASK_DEBUG=True
```

### Run the app:

```bash
python run.py
```

---

## 🌍 Translation System (i18n)

- Extracts and translates strings from `.py` and `.j2` files using:

```bash
python -m main.i18n_translate
```

- Translation files stored at:  
  `main/translations/{ar,de}/LC_MESSAGES/messages.po`

---

## 🧩 Admin Routes

| Route | Purpose |
|-------|---------|
| `/admin/resume_builder` | Control resume layout |
| `/admin/sections` | Manage section names and visibility |
| `/admin/paragraphs` | Manage paragraphs under sections |
| `/admin/fields` | Control fields inside paragraphs |

---

## 🛠️ CLI Tools

| File | Function |
|------|----------|
| `init_db.py` | Initialize the database |
| `check_data.py` | Inspect and verify data integrity |
| `add_column_location.py` | Add new columns to tables |
| `i18n_translate.py` | Auto generate and translate `.po` files |

---

## 🧭 Roadmap

| Step | Feature |
|------|---------|
| Step 15 | Export resume as PDF |
| Step 16 | Design and typography improvements |
| Step 17 | Documentation with MkDocs |
| Step 18 | Docker + CI/CD deployment |
| Step 19 | Multiple themes support |
| Step 20 | AI-enhanced content suggestions |

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it with attribution.  
Feel free to explore and build upon it!

## 🔗 Useful Links

- 📄 [License](./LICENSE)

---

## 👨‍💻 About the Author

🎯 **Tamer OnLine – Developer & Architect**  
A dedicated software engineer and educator with a focus on building multilingual, modular, and open-source applications using Python, Flask, and PostgreSQL.

🔹 Founder of **Flask University** – an initiative to create real-world, open-source Flask projects  
🔹 Creator of [@TamerOnPi](https://www.youtube.com/@mystrotamer) – a YouTube channel sharing tech, tutorials, and Pi Network insights  
🔹 Passionate about helping developers learn by building, one milestone at a time

Connect or contribute:

[![GitHub](https://img.shields.io/badge/GitHub-TamerOnLine-181717?style=flat&logo=github)](https://github.com/TamerOnLine)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tameronline/)  
[![YouTube](https://img.shields.io/badge/YouTube-TamerOnPi-red?style=flat&logo=youtube)](https://www.youtube.com/@mystrotamer)

---

> “Build your resume like code: modular, scalable, and future-ready.”