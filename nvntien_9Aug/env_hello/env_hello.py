import os


def env_hello():
    if os.environ['LANG'] == 'fr_FR':
        return('Bonjour!')
    else:
        return('Hello!')
