from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from wallet_models.class_apps.balances.outlets.balance_outlet import BalanceOutlet, BalanceUpdate, BalanceRefund
from wallet_models.class_models.wallet import Wallet

from lends.class_models.lend import Lend


class LendAmount(models.Model):
    account = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    lend = models.ForeignKey(Lend, on_delete=models.CASCADE)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        blank=True,
        null=True
    )
    # interest = models.DecimalField(
    #     max_digits=20,
    #     decimal_places=2,
    #     default=Decimal(0.00),
    #     blank=True,
    #     null=True,
    #     verbose_name='Interest %'
    # )
    note = models.CharField(max_length=250, blank=True, null=True)
    is_return = models.BooleanField(
        default=False,
    )
    return_date = models.DateField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # LendAmount.objects.filter(id=self.id).exists()
    #     if not self.id:
    #         self.is_return = False
    #     super(LendAmount, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.lend)


@receiver(post_save, sender=LendAmount)
def add(sender, instance, created, **kwargs):
    if created:
        # account
        BalanceOutlet(
            current_condition=instance.is_return,
            current_instance=instance,
            current_amount=instance.amount
        ).outlet()


@receiver(pre_save, sender=LendAmount)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = LendAmount.objects.get(id=instance.id)
        # account
        BalanceUpdate(
            current_condition=instance.is_return,
            current_instance=instance,
            current_amount=instance.amount,
            last_condition=old_value.is_return,
            last_instance=old_value,
            last_amount=old_value.amount
        ).update()


@receiver(pre_delete, sender=LendAmount)
def delete(sender, instance, using, **kwargs):
    old_value = LendAmount.objects.get(id=instance.id)
    BalanceRefund(
        last_condition=old_value.is_return,
        last_instance=old_value,
        last_amount=old_value.amount
    ).refund()
