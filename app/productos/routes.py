from flask import render_template, redirect, flash
from flask_login import login_required
from app.productos import productos
import app
import os
from .forms import NewProductForm, EditProductForm

@productos.route('/create', methods = ['GET', 'POST'])
@login_required
def crear():

    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #subir imagen a /imagenes
        #campo de imagen(filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + "/app/productos/imagen/" + p.imagen))
        flash("producto registrado correctamente")
        return redirect('/productos/listar')
    return render_template('new.html', form = form)

@productos.route('/listar')
def lista():
    #seleccionar los productos
    productos = app.models.Producto.query.all()
    return render_template("lista.html" ,
                           productos = productos)

@productos.route('/editar/<producto_id>',
                 methods = ['GET', 'POST'])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Producto Actualizado')
        return redirect('/productos/listar')
    return render_template("new.html" ,
                           form = form)

@productos.route('/eliminar/<producto_id>')
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Producto Eliminado')
    return redirect('/productos/listar')