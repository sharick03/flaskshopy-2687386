from flask import render_template, redirect, flash
from flask_login import login_required
from app.clientes import clientes
import app
from .forms import NewClientForm, EditClientForm

@clientes.route('/createC', methods = ['GET', 'POST'])
@login_required
def crear():

    p = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("cliente registrado correctamente")
        return redirect('/clientes/listarC')
    return render_template('newC.html', form = form)

@clientes.route('/listarC')
def lista():
    clientes = app.models.Cliente.query.all()
    return render_template("listar.html" ,
                           clientes = clientes)

@clientes.route('/editarC/<cliente_id>',
                 methods = ['GET', 'POST'])
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente Actualizado')
        return redirect('/clientes/listarC')
    return render_template("newC.html" ,
                           form = form)

@clientes.route('/eliminarC/<cliente_id>')
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Cliente Eliminado')
    return redirect('/clientes/listarC')