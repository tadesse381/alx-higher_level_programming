#!/usr/bin/env python3

# Filter out 'q' and 'e'
filtered_alphabet = filter(lambda x: x != 'q' and x != 'e', ascii_lowercase)

# Print filtered lowercase alphabet
print(''.join(filtered_alphabet), end='')
