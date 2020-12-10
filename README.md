# CIE Checker

This is a program that i was creating with a Dominican partner called **RedSpoof**,this script contain 2 modules, one that use to check is a CIE is correct passing it through the luhn calc, and the other use the first module to generate CIE.

## What is CIE?

The Identity and Electoral Card (CIE) is the official identity document given by the Dominican state to all citizens, being the only way to verify the identity of the bearer. The document also serves as a basis for executing legal, electoral and bank transaction support activities.

## Requeriments

You need to have [pip](https://pip.pypa.io/en/stable/installing/) installed to be able to install the necessary packages to run the program

  - argparse
  - os
  - sys
  - random

## Running the program

### Help Menu

``` bash
$ python3 CIE.py -h
usage: CIE.py [-h] [-G] [-Q QUANTITY] [-C CHECK]

Dominican Cedula Checker and Generator

optional arguments:
  -h, --help            show this help message and exit
  -G, --generate        Generate random Dominican Cedula (10 Default)
  -Q QUANTITY, --quantity QUANTITY
                        Quantity of Cedula to generate
  -C CHECK, --check CHECK
                        Check Cedula

python3 CIE.py -C XXXXXXXXXXX

```

### Generate Cedula

```python
$ python3 CIE.py -G  

40230895009 : is valid
40230006701 : is not valid
40222103237 : is not valid
40204962020 : is not valid
40201206651 : is valid
40244565812 : is not valid
40245952944 : is valid
40211865811 : is not valid
40206564172 : is not valid
40243565690 : is valid

```

## License

This project is licensed under the GNU v3.0 License - see the [LICENSE.md](https://raw.githubusercontent.com/G4m30ver/CIE/main/LICENSE?token=ASBTTJLAZ2TGHLOCAFMYGRK72GG6S) file for details
