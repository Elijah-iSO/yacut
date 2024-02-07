from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import CUSTOM_ID_FORM_VALIDATORS


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
                CUSTOM_ID_FORM_VALIDATORS['regexp'], message='используйте a-z, A-Z, 0-9'
            ),
            Length(
                max=CUSTOM_ID_FORM_VALIDATORS['length'], message='до 16 символов'
            ),
        ]
    )
    submit = SubmitField('Создать')
