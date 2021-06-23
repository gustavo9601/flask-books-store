# Usando Manager para mejora la ejecucion del servidor
from flask_script import Manager, Server

from app import init_app
from config import config

# Get settings and pass to function config
settings = config['development']
app = init_app(settings)

manager = Manager(app)
# Add settings to config global manager
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

if __name__ == '__main__':
    """
    # Execute in console
    py manage.py runserver
    """
    manager.run()
