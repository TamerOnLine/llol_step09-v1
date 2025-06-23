# Flask-Powered Tool for Structuring and Styling Multilingual Resumes with Live Control

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


---

## 📖 Overview

**This project** is the seventh milestone of an open-source dynamic resume builder aimed at empowering multilingual content creation, real-time editing, and customization. It's built for developers who need structured, localized, and exportable resume content managed through a Flask-based admin interface.

---

### 📦 Clone & Setup

Follow these steps to clone the repository and set up your development environment:

```bash
git clone https://github.com/TamerOnLine/llol_step09-v1.git  # Clone the repository from GitHub
cd llol_step09-v1                                             # Navigate into the project directory
py -m venv venv                                               # Create a virtual environment named 'venv'
.\venv\Scripts\Activate                                       # Activate the virtual environment (Windows CMD)
py -m pip install --upgrade pip                               # Upgrade pip to the latest version
pip install -r requirements.txt                               # Install all required dependencies
```

#### 💡 Tip
> If you're using PowerShell, replace the activation command with:
> ```powershell
> .\venv\Scripts\Activate.ps1
> ```

#### 🎬 Demo

<p align="center">
  <a href="screenshots/install.gif">
    <img src="screenshots/install.gif" alt="Quick install demo" width="600"/>
  </a>
</p>

> 📽️ The video above shows the complete setup process for the `llol_step09` repository, from cloning to installing dependencies.

---

## 🌐 Internationalization (i18n)

This project supports full multilingual content through dynamic extraction and translation of interface text.

### 🔤 Install Dependencies

Before generating translation files, install the required packages:

```bash
pip install flask-babel deep-translator polib
```

These are used to:
- Extract translatable strings (`flask-babel`)
- Auto-translate new entries (`deep-translator`)
- Manage `.po` files (`polib`)

---

### 🛠️ Generate Translation Files

Run the following command to extract and translate strings:

```bash
py -m main.i18n_translate  # auto-generate .po files
```

This will:
- Extract all `gettext` strings from Python and Jinja templates
- Create or update `.po` files per language
- Generate the `.pot` template file
- Optionally auto-translate missing entries

📁 Output structure:

```bash
translations/
├── ar/
│   └── LC_MESSAGES/messages.po
├── de/
│   └── LC_MESSAGES/messages.po
└── messages.pot
```

> 💡 If the `translations/` folder doesn't exist, it will be created automatically.

---

### 🎬 Demo

<p align="center">
  <a href="screenshots/i18n_translate.gif">
    <img src="screenshots/i18n_translate.gif" alt="i18n_translate in action" width="600"/>
  </a>
</p>

> 📽️ A complete i18n workflow in one command: extraction, translation, and file generation.

---

### ✅ Tips

- You can configure supported languages through your `LanguageOption` table in the admin panel.
- Re-run the script after modifying any text with `gettext()` or adding new templates.
- `polib` is required for proper `.po` file generation.


---

## 🌍 Features

- 🌐 Multi-language support using `Flask-Babel`
- 🔄 Automatic translation using `deep-translator`
- 🧾 Live editing of sections, paragraphs, and fields
- 🎛️ Admin dashboard for dynamic content management
- 🐘 PostgreSQL as the primary database
- 🎨 Ready for resume theming and customization

---

## 🧩 Database Schema

The resume structure is built dynamically using the following tables:

- `ResumeSection`: Top-level sections (e.g., Education, Work Experience)
- `ResumeParagraph`: Paragraphs under each section with `field_type`
- `ResumeField`: Key-value pairs inside each paragraph; supports multilingual content
- `Setting`: Stores design and display options as JSON
- `LanguageOption`: Manages supported languages
- `NavigationLink`: Handles sidebar/menu navigation

A ResumeSection contains multiple ResumeParagraphs, and each ResumeParagraph includes multiple ResumeFields.

---

### 🎨 Custom Styling via Settings

You can control the appearance of your resume using the admin panel:

- **Section Title Styling**: font-size, color, weight
- **Paragraph Styling**: font-size, color
- **Body Font**: custom font stack

These are stored as JSON in the `Setting` table and dynamically applied to your resume.

---

### 🗂️ Key Files

| File | Purpose |
|------|---------|
| `main_routes.py` | Public routes (home, index, language selector) |
| `admin_builder_routes.py` | Admin: section CRUD |
| `admin_paragraph.py` | Admin: paragraph CRUD |
| `admin_field.py` | Admin: field CRUD and reordering |
| `i18n_translate.py` | Auto translation and `.po` file generation |
| `run.py` | App bootstrap with DB creation |

---

### 🛠️ Database Setup & `.env` Configuration

Before running the app, you must create the target PostgreSQL database manually and configure environment variables for the connection.

#### ✅ Step 1: Create the `.env` file

In the root directory of the project, create a file named `.env` and add the following lines:

```env
DB_NAME=postgreslebenslauf
DB_USER=postgres
DB_PASSWORD=12345
DB_HOST=localhost
DB_PORT=5432
FLASK_DEBUG=True
```

Replace the values with your actual PostgreSQL credentials.

> 💡 **Note:** The database `postgreslebenslauf` must already exist on your PostgreSQL server. This project does **not** create the database itself — it only creates tables inside it.

---

#### ✅ Step 2: Create the PostgreSQL database (if not already created)

You can create the database using any method you prefer:

- **Using `psql` CLI**:
  ```bash
  createdb -U postgres postgreslebenslauf
  ```

- **Inside `psql` shell**:
  ```sql
  CREATE DATABASE postgreslebenslauf;
  ```

- **Using pgAdmin GUI**:
  - Open pgAdmin
  - Right-click on **Databases** → **Create** → **Database**
  - Set the name to `postgreslebenslauf` and save

---

After completing these steps, you can start the app with:

```bash
py -m run  # start the Flask app using the run.py bootstrap
```

This will:
- Connect to the PostgreSQL server using the credentials in `.env`.
- Expect the database `postgreslebenslauf` to already exist.
- Create required tables automatically if missing.
- Launch the Flask app in development mode with debugging enabled.

#### 🎬 Demo

<p align="center">
  <a href="screenshots/run.gif">
    <img src="screenshots/run.gif" alt="Flask app running with py -m run" width="600"/>
  </a>
</p>

> 📽️ The animation above shows how the application is launched and confirms successful connection to the database.

---

### 🧬 Database Migrations with `Flask-Migrate`

This project uses **Flask-Migrate** to manage database schema changes via Alembic.

#### ✅ Step 1: Initialize migrations folder

After installing requirements, initialize migration support:

```bash
flask db init  # initialize migrations folder (Alembic)
```

This creates a `migrations/` folder to track schema versions.

#### ✅ Step 2: Create migration script

After modifying your models, run:

```bash
flask db migrate -m "Initial migration"  # generate migration script from model changes
```

This generates a migration file under `migrations/versions/`.

#### ✅ Step 3: Apply the migration

Apply the changes to your connected PostgreSQL database:

```bash
flask db upgrade  # apply the migration to the database
```

> 📌 Make sure your `.env` file is configured and the target database exists before running migrations.

---

### 💡 Notes

- All migration scripts are tracked inside the `migrations/` folder.
- For production environments, always test migrations on a staging database before applying.

---

## 📂 Project Structure

```bash
📁 main/
├── 📁 config/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── db_initializer.py
│   └── settings.py
├── 📁 logic/
│   ├── __init__.py
│   └── builder.py
├── 📁 models/
│   ├── LanguageOption.py
│   ├── NavigationLink.py
│   ├── README.md
│   ├── Section.py
│   ├── __init__.py
│   ├── resume_field.py
│   ├── resume_paragraph.py
│   ├── resume_section.py
│   └── resume_setting.py
├── 📁 routes/
│   ├── 📁 admin/
│   │   ├── __init__.py
│   │   ├── admin_builder_routes.py
│   │   ├── admin_field.py
│   │   ├── admin_paragraph.py
│   │   └── admin_routes.py
│   ├── 📁 resume_templates/
│   │   ├── __init__.py
│   │   └── template01_routes.py
│   ├── README.md
│   ├── __init__.py
│   └── main_routes.py
├── 📁 static/
│   ├── 📁 css/
│   │   ├── 📁 resume_templates/
│   │   │   └── template01.css
│   │   └── resume.css
│   └── favicon.ico
├── 📁 templates/
│   ├── 📁 admin/
│   │   ├── paragraph_fields.html.j2
│   │   ├── resume_builder.html.j2
│   │   ├── sections.html.j2
│   │   ├── settings.html.j2
│   │   └── single_section_view.html.j2
│   ├── 📁 partials/
│   │   ├── flash_messages.html.j2
│   │   ├── footer.html.j2
│   │   └── navbar.html.j2
│   ├── 📁 resume_templates/
│   │   └── template01.j2
│   ├── base.html.j2
│   ├── home.html.j2
│   └── index.html.j2
├── 📁 tools/
│   ├── add_column_location.py
│   ├── check_data.py
│   └── init_db.py
├── 📁 translations/
│   ├── 📁 ar/
│   │   └── 📁 LC_MESSAGES/
│   │       └── messages.po
│   └── 📁 de/
│       └── 📁 LC_MESSAGES/
│           └── messages.po
├── __init__.py
├── babel.cfg
├── config.py
├── extensions.py
├── i18n.py
├── i18n_runtime.py
└── i18n_translate.py
```

---

## 🗺️ Roadmap

- ✅ **Step 01**: Initialize Flask app and basic routing structure (`flask`)
- ✅ **Step 03**: Integrate SQLAlchemy ORM for dynamic resume data modeling (`flask-sqlalchemy`)
- ✅ **Step 11**: Add multilingual support and auto-translation via Babel and Deep Translator (`flask-babel`, `deep_translator`)
- ✅ **Step 14 – Phase 05**: Set up environment-based configuration and PostgreSQL connection (`python-dotenv`, `psycopg2-binary`)
- ✅ **Step 14 – Phase 06**: Enable translation file parsing and editing using `polib`
- 🚧 **Step 14 – Phase 08**: Set up automated testing, coverage reports, and code quality checks (`pytest`, `pytest-cov`, `codecov`)
- 🔜 **Step 14 – Phase 09**: Enable database migration with `Flask-Migrate` and Alembic (`flask-migrate`)
- 📄 **Step 15**: Build resume export system to generate downloadable PDF files
- 🎨 **Step 16**: Fine-tune paragraph styling, typography, and custom design options
- 📚 **Step 17**: Generate and publish documentation with `mkdocs`, support for Git metadata and dynamic pages (`mkdocs-material`, etc.)
- 🚀 **Step 18**: Prepare deployment setup (Docker, Gunicorn, CI/CD) and make it production-ready
- 🔬 **Step 19**: Add resume preview templating and support for multiple themes
- 🧠 **Step 20**: AI-powered suggestions for resume content improvements (future scope)



---

## 🧰 Built With

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [PostgreSQL](https://www.postgresql.org/)
- [deep-translator](https://pypi.org/project/deep-translator/)

---

## 📚 Documentation & Tutorials

- [🔗 Official Project Wiki](https://github.com/TamerOnLine/llol_step09-v1/wiki) – Coming soon
- [▶️ YouTube Tutorials](https://www.youtube.com/@mystrotamer) – In-depth walkthroughs and lessons
- [📄 API Reference (if applicable)](docs/api.md)
- [📘 Blog Posts and Articles](#) – To be linked

> Want to suggest a tutorial or contribute documentation? Open an issue or PR!


---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it with attribution.  
Feel free to explore and build upon it!

---

## 👨‍💻 About the Author

This project is developed and maintained by [@TamerOnLine](https://github.com/TamerOnLine), a passionate software developer and educator focused on Python, Flask, PostgreSQL, and open-source learning tools.

🔹 Founder of **Flask University** – an initiative to create real-world, open-source Flask projects  
🔹 Creator of [@TamerOnPi](https://www.youtube.com/@mystrotamer) – a YouTube channel sharing tech, tutorials, and Pi Network insights  
🔹 Building tools that empower developers to learn by doing, one milestone at a time

Feel free to connect or contribute:

[![GitHub](https://img.shields.io/badge/GitHub-TamerOnLine-181717?style=flat&logo=github)](https://github.com/TamerOnLine)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tameronline/)
[![YouTube](https://img.shields.io/badge/YouTube-TamerOnPi-red?style=flat&logo=youtube)](https://www.youtube.com/@mystrotamer)

---

> 💡 **Got feedback or want to collaborate?**  
> Open an issue, fork the repo, or just say hi on LinkedIn!

