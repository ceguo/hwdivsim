# Hardware division simulators for unsigned integers

## Quick start

Run the script in a terminal:
```
python3 restore.py 39 4
```

The script should start computing 39/4. The output is:
```
Initial status 0000000000100111
Remainder: 0000000000100111
Divisor:   00000100
Iteration 1
    Subtraction
      0000000001001110
    - 00000100
    Remainder < 0
    Remainder restored:
      0000000001001110
    Remainder after shifting:
      0000000010011100
Iteration 2
    Subtraction
      0000000010011100
    - 00000100
    Remainder < 0
    Remainder restored:
      0000000010011100
    Remainder after shifting:
      0000000100111000
Iteration 3
    Subtraction
      0000000100111000
    - 00000100
    Remainder < 0
    Remainder restored:
      0000000100111000
    Remainder after shifting:
      0000001001110000
Iteration 4
    Subtraction
      0000001001110000
    - 00000100
    Remainder < 0
    Remainder restored:
      0000001001110000
    Remainder after shifting:
      0000010011100000
Iteration 5
    Subtraction
      0000010011100000
    - 00000100
    Remainder >= 0
    Remainder before shifting:
      0000000011100000
    Remainder after shifting:
      0000000111000001
Iteration 6
    Subtraction
      0000000111000001
    - 00000100
    Remainder < 0
    Remainder restored:
      0000000111000001
    Remainder after shifting:
      0000001110000010
Iteration 7
    Subtraction
      0000001110000010
    - 00000100
    Remainder < 0
    Remainder restored:
      0000001110000010
    Remainder after shifting:
      0000011100000100
Iteration 8
    Subtraction
      0000011100000100
    - 00000100
    Remainder >= 0
    Remainder before shifting:
      0000001100000100
    Remainder after shifting:
      0000011000001001
Quotient (binary):   00001001
Remainder (binary):  00000011
Quotient (decimal):  9
Remainder (decimal):  3
```

## Usage
```
python3 restore.py [divident] [divisor]
```
Limits: '0 <= divident <= 255', '1 <= divisor <= 255'

## Other notes

Now the only algorithm supported is restoring division in Ex 3.2. This demo is for demonstration rather than efficient computation. It does not perform any input check. The code deliberately omits add-back procedure in the 'remainder < 0' branch for simplicity. The original remainder stays unchanged to simulate the add-back procedure in this branch.
