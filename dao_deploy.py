import pywaves as pw
import random
import os

NODE = "https://testnode1.wavesnodes.com"
CHAIN = "T"


def create_account():
    pw.setNode(NODE, CHAIN)
    seed = " ".join([random.choice(pw.wordList) for n in range(15)])
    account = pw.Address(seed=seed)
    return {
        "seed": account.seed,
        "address": account.address
    }


def read_scripts():
    dic = {
        "mem": "dao-membership.ride",
        "dis": "disruptive-grant.ride",
        "web": "web3-grant.ride",
        "int": "interhack-grant.ride",
    }

    keys = list(dic.keys())

    for k in keys:
        with open("smart-contracts/"+dic[k], encoding="utf-8") as f:
            dic[k] = f.read()

    return dic


def deploy(seed1):
    print(seed1)

    pw.setNode(NODE, CHAIN)

    a1 = pw.Address(seed=seed1)
    balance = a1.balance()

    print(balance)

    if balance < 4*10**6:
        raise("Top up the account balance using Waves Faucet")

    accs = [create_account() for n in range(3)]

    sponsor_amount = 10**6

    print(accs)

    for a in accs:
        a1.sendWaves(pw.Address(a["address"]), sponsor_amount, attachment="setting DAO", txFee=500000)

    scripts = read_scripts()

    a1.setScript(scripts["mem"], txFee=1400000)

    print("script #1 set")

    pw.Address(seed=accs[0]["seed"]).setScript(scripts["dis"], txFee=1000000)
    print("script #1 set")

    pw.Address(seed=accs[1]["seed"]).setScript(scripts["web"], txFee=1000000)
    print("script #2 set")

    pw.Address(seed=accs[2]["seed"]).setScript(scripts["int"], txFee=1000000)
    print("script #3 set")

    out = "membership;{};{}".format(a1.address, a1.seed) + \
          "\ndisruptive grants;{};{}".format(accs[0]["address"], accs[0]["seed"]) + \
          "\nweb 3.0 grants;{};{}".format(accs[1]["address"], accs[1]["seed"]) + \
          "\ninterhack grants;{};{}".format(accs[2]["address"], accs[2]["seed"])

    with open("credentials.csv", "w", encoding="utf-8") as f:
        f.write(out)

    print(out)


def main():
    deploy(os.environ["SEED"])


seed1 = "debate gravity oppose deposit turtle proud eye alley absurd bachelor coil excess dignity dune depart"


if __name__ == "__main__":
    main()

