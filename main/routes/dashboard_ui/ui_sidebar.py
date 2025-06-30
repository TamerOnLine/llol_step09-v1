from flask import render_template, request, redirect, url_for, flash
from main.models import db
from main.models.sidebar_link import SidebarLink
from . import ui_bp


# عرض وإضافة روابط الشريط الجانبي
@ui_bp.route("/sidebar", methods=["GET", "POST"])
def manage_sidebar():
    if request.method == "POST":
        label = request.form.get("label")
        endpoint = request.form.get("endpoint")
        icon = request.form.get("icon")
        order = request.form.get("order") or 0
        is_visible = True if request.form.get("is_visible") else False

        new_link = SidebarLink(
            label=label,
            endpoint=endpoint,
            icon=icon,
            order=order,
            is_visible=is_visible,
        )
        db.session.add(new_link)
        db.session.commit()
        flash("Sidebar link added successfully")
        return redirect(url_for("ui.manage_sidebar"))  # ✅ مصححة

    links = SidebarLink.query.order_by(SidebarLink.order).all()
    return render_template("sidebar/manage_sidebar.j2", links=links)


# حذف رابط من الشريط الجانبي
@ui_bp.route("/sidebar/delete/<int:link_id>")
def delete_sidebar_link(link_id):
    link = SidebarLink.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    flash("Sidebar link deleted successfully")
    return redirect(url_for("ui.manage_sidebar"))


# تعديل رابط موجود
@ui_bp.route("/sidebar/edit/<int:link_id>", methods=["GET", "POST"])
def edit_sidebar_link(link_id):
    link = SidebarLink.query.get_or_404(link_id)
    if request.method == "POST":
        link.label = request.form.get("label")
        link.endpoint = request.form.get("endpoint")
        link.icon = request.form.get("icon")
        link.order = request.form.get("order") or 0
        link.is_visible = True if request.form.get("is_visible") else False
        db.session.commit()
        flash("Sidebar link updated successfully")
        return redirect(url_for("ui.manage_sidebar"))  # ✅ مصححة

    return render_template("sidebar/edit_sidebar.j2", link=link)
