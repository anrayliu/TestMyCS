import sys 
sys.path.insert(0, "/var/www/test-my-cs")

activate = "/var/www/test-my-cs/.venv/bin/activate"
with open(activate) as f:
    exect(f.read(), dict_(__file__=activate))

from main import app as application