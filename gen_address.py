#!/usr/bin/python
import sys
from bip32utils import BIP32Key


class Account(object):

    def __init__(self, xpub):
        self.addresses = []
        self.transactions = []
        self.mask = 'm/1/0/'
        self.account = BIP32Key.fromExtendedKey(xpub)
        self.ext_node = self.account.ChildKey(0)

    def gen_new_address(self, order_id):
        addr_node = self.ext_node.ChildKey(order_id)
        address = addr_node.Address()
        return address


xpub = sys.argv[1]

acc = Account(xpub)
print acc.gen_new_address(2)