# Основные импорты
from flask import Flask


# Импорт блюпринтов
from main.views import main_blueprint
from api.views import api_blueprint


app = Flask(__name__)

# Для нормального отображения в любом браузере json
app.config['JSON_AS_ASCII'] = False

# Регистрация блюпринта
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == ('__main__'):
    app.run(debug=True)
