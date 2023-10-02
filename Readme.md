# About

This codebase is to test out implementation of python custom curve 25519 similar to the one used in bouncy castle.

# Prerequisites

## Fidelius CLI
Download Fidelius CLI from here and update the path of varaible `FIDELIUS_CLI_PATH` in `fildelius_encryption_util.py`.
https://github.com/mgrmtech/fidelius-cli/releases

## Python lib

`pip install git+https://github.com/dimagi/pyfidelius@mvp2`

# Test Code
Run the test using

` python -m unittest test_python_custom_curve.py`
