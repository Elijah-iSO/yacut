from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):

    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Regexp(
                '^[a-zA-Z0-9]+$', message='используйте a-z, A-Z, 0-9'
            ),
            Length(max=16, message='до 16 символов'),
        ]
    )
    submit = SubmitField('Создать')
