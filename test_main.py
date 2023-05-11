from .main import (
    get_account_private_key,
    get_account_public_key,
    get_receiving_addresses,
    get_new_mnemonic,
    dump_root,
    get_account_44_public_key,
)

words = "citizen praise jealous element crash express match bottom phone salad cattle total already edge among brand tumble across journey range vibrant script melt solid"


def test_get_account_private_key():
    assert (
        get_account_private_key(words, "english", "my supper duper passphrase", 1)
        == "zprvAe1Rde28ww564yRnMYWocN8YuQEsvA2uFzVXMedtdqJ2JfoZ588wN6Agk"
        "knfh5UGP3W9HTzr6rSXNTxzru6rpBv1oK4NGy1j7AKWXSLv7hx"
    )


def test_get_account_public_key():
    assert (
        get_account_public_key(words, "english", "my supper duper passphrase", 1)
        == "zpub6rzn39Z2nJdPHTWFTa3oyW5HTS5NKckkdDR8A33WCAq1BU8hcfTButVAc"
        "4y5UCn3JwV6QbWRJa4YUZJkrJe5ctMAN5R1LLufm9qH2ApFpqH"
    )


def test_get_account_public_legacy_key():
    assert (
        get_account_44_public_key(words, "english", "my supper duper passphrase", 1)
        == "xpub6CAgQyfkj7JMMjatcJnfafoDA2epAsfU2CRbL9TRzDAULAxSWE8jbn"
        "TexNz1i3e5A81nMfQPLJmxeSaEBjYGecKzqd4Gw6UdYyoHJsX1FLT"
    )


def test_get_recieving_addresses():
    assert get_receiving_addresses(
        words, "english", "my supper duper passphrase", 1, 3
    ) == [
        "bc1qxkut448jdk3myexxlkhjhxgrlvh9m8g6u5snz8",
        "bc1qe8a2dgut8jss2j030l5t996t6cypnf4y3tvsvc",
        "bc1qd2wwgng5hymf7y5x97cxt5kk8lg2pmtccxh5f5",
    ]


def test_get_new_mnemonic():
    assert (
        get_new_mnemonic(words, "english", "my supper duper passphrase", 0)
        == "world energy equip clinic roast place illegal adapt amazing double today moral humble twenty sick benefit exercise give illness february allow place segment habit"
    )
    assert (
        get_new_mnemonic(words, "english", "my supper duper passphrase", 1)
        == "isolate jealous omit leaf bring screen oval illness elite verify fruit settle staff theme soap below arrange verify fantasy physical game seven tone negative"
    )


def test_dump_root():
    dump = dump_root(words, "english", "my supper duper passphrase")

    assert (
        dump["entropy"]
        == "295531de23d326a1a230d2a397c89172e0728c81f8d8ea4049e1d8ef378362ae"
    )
    assert (
        dump["root_xprivate_key"]
        == "xprv9s21ZrQH143K2gaup2sq8VrwrV5ygNawYB35ZHybn15wuWHjqkx87pBso7"
        "ER5Esk1EqJ336SaeKWwEKBP5xLhGXsWssxQ6VXMWr5RRc5Xyt"
    )
