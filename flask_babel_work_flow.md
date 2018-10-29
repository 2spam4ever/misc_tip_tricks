## Flask Babel

```sh
pip install Flask-Babel
```

in `config.py`

```python
BABEL_DEFAULT_LOCALE = 'vi'
BABEL_DEFAULT_TIMEZONE = 'UTC'
BABEL_TRANSLATION_DIRECTORIES = os.path.join(basedir, 'translations')
```

getter

```python
@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en'])

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
```

in `app/__init__.py`

```python
from flask_babel import Babel, gettext

app.config.from_object('config')
babel = Babel(app)
```

add `babel.cfg` in root directory

```cfg
[python: app/**.py]
[jinja2: app/templates/**/*.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

run

```sh
pybabel extract -F babel.cfg -o messages.pot .

pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
```

add translations

```
pybabel init -i messages.pot -d translations -l ja
```

import

```python
from flask_babel import gettext, ngettext, _
```

example

```python
msgid "This is team: <strong>%(name)s</strong> !"
```

compile

```sh
pybabel compile -d translations
```
