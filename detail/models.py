from django.db import models

class BankDetails(models.Model):
    ifsc = models.CharField(max_length=15)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    def store(self,detaillist):
        self.ifsc = detaillist[0]
        self.bank_id = detaillist[1]
        self.branch = detaillist[2]
        self.address = detaillist[3]
        self.city = detaillist[4]
        self.district = detaillist[5]
        self.state = detaillist[6]
        self.bank_name = detaillist[7]

    def __str__(self):
        return self.bank_name + ' ' + self.city
