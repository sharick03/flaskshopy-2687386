from flask import render_template, redirect, flash
from app.clientes import clientes
import app
from .forms import NewClientForm, EditClientForm

@clientes.route('/create', methods = ['GET', 'POST'])
def crear():

    p = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("cliente registrado correctamente")
        return redirect('/clientes/listar')
    return render_template('crear.html', form = form)

@clientes.route('/listar')
def lista():
    clientes = app.models.Cliente.query.all()
    return render_template("listar.html" ,
                           clientes = clientes)

@clientes.route('/editar/<cliente_id>',
                 methods = ['GET', 'POST'])
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente Actualizado')
        return redirect('/clientes/listar')
    return render_template("crear.html" ,
                           form = form)

@clientes.route('/eliminar/<cliente_id>')
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Cliente Eliminado')
    return redirect('/clientes/listar')
    return render_template("crear.html" ,
                           form = form)