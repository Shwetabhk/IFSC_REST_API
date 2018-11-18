from django_cron import CronJobBase, Schedule
from details.models import Bank
import os
import csv


class DataImport(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Branches.data'

    def do(self):
        try:
            with open("data.csv", 'r') as data:
                reader = csv.DictReader(data)
                for row in reader:
                    bank_object, flag = Bank.objects.get_or_create(
                        ifsc=row["ifsc"],
                        bank_id=int(row["bank_id"]),
                        branch=row["branch"],
                        address=row["address"],
                        city=row["city"],
                        district=row["district"],
                        state=row["state"],
                        bank_name=row["bank_name"]
                    )
                    print(bank_object, flag)
        except Exception as e:
            print(e)
