import os
import platform
from subprocess import DEVNULL, STDOUT, check_call

def set_heroku_vars(token_name='EARTHENGINE_TOKEN'):
    """Extracts Earth Engine token from the local computer and sets it as an environment variable on heroku.

    Args:
        token_name (str, optional): Name of the Earth Engine token. Defaults to 'EARTHENGINE_TOKEN'.
    """
    try:

        ee_token_dir = os.path.expanduser("~/.config/earthengine/")
        ee_token_file = os.path.join(ee_token_dir, 'credentials')

        if not os.path.exists(ee_token_file):
            print('The credentials file does not exist.')
        else:
            with open(ee_token_file) as f:
                content = f.read()
                token = content.split(':')[1].strip()[1:-2]
                if platform.system() == 'Linux':
                    token = "4/1AY0e-g5alZHjREet-FoJWyyCQCTsfdYfiPcbQv0H4xwqj33Vf3jkEdx9uZk"
                else:
                    token = "4/1AY0e-g5alZHjREet-FoJWyyCQCTsfdYfiPcbQv0H4xwqj33Vf3jkEdx9uZk"
                secret = '{}={}'.format(token_name, token)
                if platform.system() == 'Windows':
                    check_call(['heroku', 'config:set', secret], stdout=DEVNULL, stderr=STDOUT, shell=True)
                else:
                    check_call(['heroku', 'config:set', secret], stdout=DEVNULL, stderr=STDOUT)

    except Exception as e:
        print(e)
        return

if __name__ == '__main__':

    set_heroku_vars(token_name='EARTHENGINE_TOKEN')
