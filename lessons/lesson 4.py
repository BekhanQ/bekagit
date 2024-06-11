class InterestBearingItem:    pass
class Asset:
    pass
class InsurableItem:    pass
class BankAccount(Asset):
    pass
class SavingAccount(BankAccount):    pass
class CheckingAccount(BankAccount):
    pass
class RealEstate(Asset, InsurableItem):    pass
class Security(Asset):
    pass
class Stock(Security, InterestBearingItem):
    pass
class Bond(Security, InterestBearingItem):    pass

