from btc_hd_wallet import BIP85DeterministicEntropy
from hdwallet import BIP32HDWallet, BIP84HDWallet, HDWallet, utils

LANGUAGES = ["english", "french", "italian", "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]


def get_account_private_key(words: str, language: str, passphrase: str, account: int) -> str:
    wallet = BIP84HDWallet("BTC").from_mnemonic(words, language, passphrase)
    wallet.clean_derivation()
    wallet.from_index(84, hardened=True)  # BIP84 - native segwit
    wallet.from_index(0, hardened=True)  # bitcoin mainnet
    wallet.from_index(account, hardened=True)  # account
    return wallet.xprivate_key() or "Error"


def get_account_public_key(words: str, language: str, passphrase: str, account: int) -> str:
    wallet = BIP84HDWallet("BTC").from_mnemonic(words, language, passphrase)
    wallet.clean_derivation()
    wallet.from_index(84, hardened=True)  # BIP84 - native segwit
    wallet.from_index(0, hardened=True)  # bitcoin mainnet
    wallet.from_index(1, hardened=True)  # account
    return wallet.xpublic_key() or "Error"


def get_receiving_addresses(words: str, language: str, passphrase: str, account: int, n: int) -> list[str]:
    addresses = []
    for i in range(n):
        xpublic_key = get_account_public_key(words, language, passphrase, account)
        pubwallet = HDWallet("BTC").from_xpublic_key(xpublic_key)
        pubwallet.from_index(0)  # change (external/internal)
        pubwallet.from_index(i)  # address_index
        addresses.append(pubwallet.p2wpkh_address())
    return addresses


def get_new_mnemonic(words: str, language: str, passphrase: str, index: int) -> str:
    wallet = BIP32HDWallet("BTC").from_mnemonic(words, language, passphrase)
    wallet.clean_derivation()
    bip85 = BIP85DeterministicEntropy.from_xprv(xprv=wallet.xprivate_key())
    return bip85.bip39_mnemonic(word_count=24, index=index)


def main():
    print("""
Select your mnemonic language:
    0) "english"
    1) "french"
    2) "italian"
    3) "chinese_simplified"
    4) "chinese_traditional"
    5) "japanese"
    6) "korean"
    7) "spanish"
\n:: Select [0-7]:
    """)
    language = LANGUAGES[int(input())]

    print("\n:: Enter mnemonic words (eg: 'citizen praise jealous element crash express match'): ")
    words = input()
    assert utils.is_mnemonic(words, language), "Invalid mnemonic words"

    print("\n:: Enter passphrase (eg: 'my supper dupper passphrase'): ")
    passphrase = input()

    while True:
        print("""
----------------------------------------
\n:: Select your command:
    0) Derive new mnemonic (BIP85)
    1) Account private key - Spendable address for whole account:
    2) Account public key - Watch-only address for whole account:
    3) Recieving addresses for account
    4) Exit
""")
        command = int(input())

        if command != 4:
            print("\n:: Enter account index: ")
            index = int(input())

        match command:
            case 0:
                print(get_new_mnemonic(words, language, passphrase, index))
            case 1:
                print(get_account_private_key(words, language, passphrase, index))
            case 2:
                print(get_account_public_key(words, language, passphrase, index))
            case 3:
                print("\n:: How many addresses would you like to generate: ")
                n = int(input())
                print(*get_receiving_addresses(words, language, passphrase, index, n), sep="\n")
            case _:
                break


if __name__ == '__main__':
    main()

