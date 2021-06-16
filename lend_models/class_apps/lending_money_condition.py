from wallet_models.class_apps.balances.objects.object_base import SetObjectPk, SetObjectCondition
# from wallet_models.class_apps.wallets.wallet_income import WalletAccountIncome
from wallet_models.class_apps.wallets.wallet_outlet import WalletAccountOutlet


class LendingMoneyWithdraw:
    is_return = False
    is_withdraw = False
    pk = None
    amount = None

    def __init__(
            self,
            is_return=False,
            is_withdraw=False,
            pk=None,
            amount=None
    ):
        self.is_return = is_return
        self.is_withdraw = is_withdraw
        self.pk = pk
        self.amount = amount

    def withdraw_money(self):
        if self.is_withdraw:
            WalletAccountOutlet.outlet_account(
                self.amount, self.pk
            )
        if self.is_return:
            WalletAccountOutlet.refund_outlet_account(
                self.amount, self.pk
            )


class LendingMoneyReturn:
    is_return = False
    is_withdraw = False
    pk = None
    amount = None

    def __init__(
            self,
            is_return=False,
            is_withdraw=False,
            pk=None,
            amount=None
    ):
        self.is_return = is_return
        self.is_withdraw = is_withdraw
        self.pk = pk
        self.amount = amount

    def return_money(self):
        if self.is_return:
            WalletAccountOutlet.refund_outlet_account(self.amount, self.pk)
    # update
    # def _update_outlet_account_same_pk(self, current_amount, last_amount):
    #     if self.current_condition:
    #         if self.last_condition:
    #             WalletAccountOutlet.update_outlet_account(
    #                 current_amount, last_amount,
    #                 self.current_pk
    #             )
    #             # print("update amount")
    #         else:
    #             WalletAccountOutlet.outlet_account(
    #                 current_amount,
    #                 self.current_pk
    #             )
    #     else:
    #         if self.last_condition:
    #             WalletAccountOutlet.refund_outlet_account(last_amount, self.last_pk)
    #
    # def _update_outlet_account_different_pk(self, current_amount, last_amount):
    #     if self.current_condition:
    #         if self.last_condition:
    #             # return stock
    #             WalletAccountOutlet.refund_outlet_account(last_amount, self.last_pk)
    #             # add new stock
    #             WalletAccountOutlet.outlet_account(current_amount, self.current_pk)
    #             print('update not workings')
    #         else:
    #             WalletAccountOutlet.outlet_account(current_amount, self.current_pk)
    #     else:
    #         if self.last_condition:
    #             WalletAccountOutlet.refund_outlet_account(last_amount, self.last_pk)
    #
    # def update_outlet_account(self, last_condition, last_amount, last_pk):
    #     if self.pk == last_pk:
    #         self._update_outlet_account_same_pk(self.amount, last_amount)
    #         print('update same pk: {}'.format(self.pk))
    #         print('update current condition: {}'.format(self.is_withdraw))
    #         print('update last return: {}'.format(last_condition))
    #         print('update last withdraw: {}'.format(self.last_condition))
    #     else:
    #         self._update_outlet_account_different_pk(current_amount, last_amount)
    #         print('update different pk: {}'.format(self.last_pk))
    #         print('update current condition: {}'.format(self.current_condition))
    #         print('update last condition: {}'.format(self.last_condition))
    #

# lending_money_condition = LendingMoneyCondition()
