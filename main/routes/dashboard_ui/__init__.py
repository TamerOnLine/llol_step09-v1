from flask import Blueprint

ui_bp = Blueprint("ui", __name__, url_prefix="/ui")  # ✅ عدل الاسم

from . import ui_sidebar  # ✅ استيراد مسارات الشريط الجانبي

__all__ = ["ui_bp"]
