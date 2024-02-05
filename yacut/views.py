import string
from random import choice

from flask import flash, redirect, render_template

from . import app, db
from .error_handlers import InvalidAPIUsage
from .forms import URLForm
from .models import URLMap


def get_unique_short_id(length=6, chars=string.ascii_letters + string.digits):
    short_id = ''.join([choice(chars) for i in range(length)])
    if URLMap.query.filter_by(short=short_id).first():
        short_id = get_unique_short_id()
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_id = form.custom_id.data
        if short_id is None or short_id == '':
            short_id = get_unique_short_id()
        else:
            if URLMap.query.filter_by(short=short_id).first():
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('add_url.html', form=form)
        url_in_db = URLMap(
            original=form.original_link.data,
            short=short_id
        )
        db.session.add(url_in_db)
        db.session.commit()
        return render_template('add_url.html', form=form, url_in_db=url_in_db)
    return render_template('add_url.html', form=form)


@app.route('/<short_id>')
def redirect_view(short_id):
    url_in_db = URLMap.query.filter_by(short=short_id).first()
    if url_in_db is None:
        raise InvalidAPIUsage('Указанный идентификатор не найден', 404)
    return redirect(url_in_db.original)
