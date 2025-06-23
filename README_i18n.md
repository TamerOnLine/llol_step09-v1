
## 🌐 Internationalization Setup (i18n)

### 🔤 Installing Translation Dependencies

To enable automatic extraction and generation of translation files, make sure the following libraries are installed:

```bash
pip install flask-babel deep-translator polib
```

These libraries are used to:
- Extract translatable strings from your code and templates (`flask-babel`)
- Automatically translate messages to target languages (`deep-translator`)
- Manage `.po` translation files (`polib`)

### 🛠️ Running the Translation Script

Once installed, generate translation files by running:

```bash
py -m main.i18n_translate
```

This command will:
- Extract all `gettext` strings from templates and Python files
- Create or update `.po` files for all supported languages
- Optionally translate missing fields using Google Translate (via `deep-translator`)
- Generate a `.pot` template file under the `translations/` folder

### 📁 Output Structure

```bash
translations/
├── ar/
│   └── LC_MESSAGES/messages.po
├── de/
│   └── LC_MESSAGES/messages.po
└── messages.pot
```

### ✅ Notes

- If `translations/` doesn’t exist, it will be created automatically.
- You can add or remove supported languages by editing your language config (e.g., `LanguageOption` table).
- Make sure `polib` is installed to support `.po` file writing.
