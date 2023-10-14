from pyswip import Prolog
prolog = Prolog()
prolog.assertz("father(john, jim)")  # Sample query to check if pyswip is working
list(prolog.query("father(john, X)"))  # Should return [{'X': 'jim'}]
