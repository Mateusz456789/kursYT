import re
if re.match("^[A-Z][a-z]a*$", "Al"): # * moze wystepowac zmienna lub nie
    print("dopasowano")
else:
    print("nie dopasowano")
