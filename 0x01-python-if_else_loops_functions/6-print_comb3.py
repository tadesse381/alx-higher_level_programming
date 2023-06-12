#!/usr/bin/env python3

# Print all combinations of two digits in ascending order
print(', '.join(f"{i}{j}" for i in range(10) for j in range(i+1, 10)))
