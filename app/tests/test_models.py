from django.db import transaction, models, IntegrityError
from django.test import TestCase
from app.models import UberTransactions, BoltTransactions



class UberTransactionsTests(TestCase):

    @transaction.atomic
    def create_spam(self):
        spam = UberTransactions(transaction_uuid='6a49c49a-eaee-5f24-aa4e-2a30eb81bfb6',
                                driver_uuid='cd725b41-9e47-4fd0-8a1f-3514ddf6238a',
                                driver_name='',
                                driver_second_name='',
                                trip_uuid='e54f97da-73a4-464f-8a32-af6f948165d9',
                                trip_description='',
                                organization_name='',
                                organization_nickname='',
                                transaction_time='',
                                paid_to_you=55.59,
                                your_earnings=55.59,
                                cash=0,
                                fare=0,
                                tax=0,
                                fare2=0,
                                service_tax=0,
                                wait_time=0,
                                transfered_to_bank=0,
                                peak_rate=0,
                                tips=0,
                                cancel_payment=0)
        spam.save()
        return True

    def test_integrity_error(self):
        # first one should work fine
        self.assertTrue(self.create_spam())
        # second time violates unique constraint
        self.assertRaises(IntegrityError, self.create_spam)
        # have we recovered?
        self.assertEquals(len(UberTransactions.objects.all()), 1)


class BoltTransactionsTests(TestCase):

    @transaction.atomic
    def create_spam(self):
        spam = BoltTransactions.objects.create(driver_name='Юрій Філіппов',
                                               driver_number='+380502428878',
                                               trip_date='2022-09-12',
                                               payment_confirmed='19:03',
                                               boarding='Івана Дяченка вулиця 13, Киев 02088',
                                               payment_method='Готівка',
                                               requsted_time='18:06',
                                               fare=283.00,
                                               payment_authorization=0.00,
                                               service_tax=0.00,
                                               cancel_payment=0.00,
                                               tips=0.00,
                                               order_status='Завершено',
                                               car='Renault Mégane',
                                               license_plate='KA6047EI')
        spam.save()
        return True

    def test_integrity_error(self):
        # first one should work fine
        self.assertTrue(self.create_spam())
        # second time violates unique constraint
        self.assertRaises(IntegrityError, self.create_spam)
        # have we recovered?
        self.assertEquals(len(BoltTransactions.objects.all()), 1)
