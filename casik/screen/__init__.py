import importlib.util
from os import listdir

start_screen = 'main.py'
for filename in listdir('./screen/'):
    if filename[0] == '_': continue
    spec = importlib.util.spec_from_file_location(filename.split('.')[0], f'./screen/{filename}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if start_screen == filename:
        start_screen = module.main
