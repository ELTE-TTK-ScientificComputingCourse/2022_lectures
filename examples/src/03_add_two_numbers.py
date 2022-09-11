# Bash:
# echo $'10\n20' | python src/03_add_two_numbers.py
# cat data/03_input.txt | python src/03_sum_two_numbers.py

# Windows command line:
# type data/03_input.txt | python src/03_sum_two_numbers.py

import sys


reader = sys.stdin
a = int(next(reader))
b = int(next(reader))

result = a + b
print(result)
