# HDWD - Hierarchical Deterministic Wallet Derivator

This is a simple *cli* tool to derive new accounts and seeds from a master seed. It is based on the BIP32, BIP39, BIP44, BIP84 and BIP85 standard. It allows you to have one backup seed for all mobile apps, lightning nodes, hardware wallets, etc...

It can be used on old raspberry pi's or old laptops which does not have GUI or browser available.

# Warning
Before using this tool, make sure you test it on a random seed first. 
Here are few online tools to verify you get same output:
* https://iancoleman.io/bip39/
* https://bitcoiner.guide/seed/

Never use this tool on an computer connected to the internet. 
Once you enter your master seed its recommended to either destroy the computer or make sure it will not be used for any other purpose. Another option is to boot Tails OS from a USB stick but is not as secure as destroying the computer.


# Installation
```
pip install -r requirements.txt
python main.py
```

## Manual
* Run `pip install hdwallet btc-hd-wallet`
* Copy contents of `main.py` to your computer
* Modify as needed


# Usage
```
$ python main.py

Select your mnemonic language:
    0) "english"
    1) "french"
    2) "italian"
    3) "chinese_simplified"
    4) "chinese_traditional"
    5) "japanese"
    6) "korean"
    7) "spanish"

:: Select [0-7]:
    
0

:: Enter mnemonic words (eg: 'citizen praise jealous element crash express match'): 
citizen praise jealous element crash express match bottom phone salad cattle total already edge among brand tumble across journey range vibrant script melt solid

:: Enter passphrase (eg: 'my supper dupper passphrase'): 
my supper duper passphrase

----------------------------------------

:: Select your command:
    0) Derive new mnemonic (BIP85)
    1) Account private key - Spendable address for whole account:
    2) Account public key - Watch-only address for whole account:
    3) Recieving addresses for account
    4) Exit

0

:: Enter account index: 
0
world energy equip clinic roast place illegal adapt amazing double today moral humble twenty sick benefit exercise give illness february allow place segment habit
```

# Tests
```
pytest .
```
