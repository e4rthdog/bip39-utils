# Utilities for BIP39 phrase handling

Scripts to assist in handling the seed phrase

## bip39-word-converter.py

Converts a phrase to the respective number from the official BIP39 English word list.

- `bip39-word-converter.py -n` will convert sequence of numbers to words
- `bip39-word-converter.py -w` will convert sequence of words to numbers

## bip39-word-replace.py

Converts every number from a string of numbers to letters and vice versa given a specific word as base. The word should have more than 10 characters and non recurring.

- `bip39-word-replace.py -e abcdefghijklmnop '0256'` will give `acfg`
- `bip39-word-replace.py -d abcdefghijklmnop 'acfg'` will give `0256`
