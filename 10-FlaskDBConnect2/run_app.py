import os

from database_app_template_conditional import app


if __name__ == '__main__':
    app.debug = False
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
