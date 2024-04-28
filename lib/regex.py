import re

my_pattern = r"[^?!\n\s][A-Za-z'\s,]*day[A-Za-z'\s,]*[\.?]"
my_regex = re.compile(my_pattern)

