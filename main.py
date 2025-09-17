# main.py
# Arithmetic Operations Project

from sum import add
from difference import subtract
from product import multiply
from division import divide

def main():
    a, b = 20, 5
    print("Arithmetic Operations")
    print(f"Sum of {a} and {b}: {add(a, b)}")
    print(f"Difference of {a} and {b}: {subtract(a, b)}")
    print(f"Product of {a} and {b}: {multiply(a, b)}")
    print(f"Division of {a} by {b}: {divide(a, b)}")

if __name__ == "__main__":
    main()
