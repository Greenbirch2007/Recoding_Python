
# spam.py


import pkgutil

data = pkgutil.get_data(__package__,'tt.py').decode("utf8")
