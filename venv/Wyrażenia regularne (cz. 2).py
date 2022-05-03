import re

if re.match("ko.", "kot"):
    print("dopasowano")
else:
    print("Nie dopasowao")

# chodzy jeden znka w kodzie to wyszuka:
#można tez dawać przedział A-Z lub stosować $ jako ogranicznik 
import re

if re.match("^[kk].", "kot"):
    print("dopasowano")
else:
    print("Nie dopasowao")