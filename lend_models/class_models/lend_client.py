from decimal import Decimal

from datetime_utils.date_time import DateTime
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver


class LendClientSet(models.Model):
    name = models.CharField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class LendClient(models.Model):
    client = models.ForeignKey(LendClientSet, on_delete=models.CASCADE)
    created_date = models.DateField(default=DateTime.datenow)
    updated_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.client)


# @receiver(post_save, sender=LendClient)
# def add(sender, instance, created, **kwargs):
#     if created:
#         wallet = Wallet.objects.get(id=instance.wallet.id)
#         if wallet:
#             wallet.balance = wallet.balance - instance.amount
#         wallet.save()


@receiver(pre_save, sender=LendClient)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = DateTime.datenow()

# @receiver(post_delete, sender=LendClient)
# def delete(sender, instance, using, **kwargs):
#     wallet = Wallet.objects.get(id=instance.wallet.id)
#     print(instance.id)
#     if wallet:
#         # old_record = Expense.objects.get(id=instance.id)
#         # if old_record:
#         wallet.balance = wallet.balance + instance.amount
#     wallet.save()
