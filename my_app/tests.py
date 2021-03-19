from django.test import TestCase
from my_app.models import Sample
from django.db import IntegrityError

class SampleModelTests(TestCase):
    def test_create_with_null(self):
        try:
            Sample.objects.create()
            Sample.objects.create()
            Sample.objects.create()
        except IntegrityError:
            self.fail('Unexpected Integrity Error')

    def test_create_with_uniuqe_together(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        with self.assertRaises(IntegrityError):    
            Sample.objects.create(filed_x='A',filed_y='B')

    def test_multi_object_returned_with_get(self):
        Sample.objects.create(filed_x='A')
        Sample.objects.create(filed_x='A')

        with self.assertRaises(Sample.MultipleObjectsReturned):    
            Sample.objects.get(filed_x='A')

    def test_multi_object_returned_with_get_or_create(self):
        Sample.objects.create(filed_x='A')
        Sample.objects.create(filed_x='A')

        with self.assertRaises(Sample.MultipleObjectsReturned):    
            Sample.objects.get_or_create(filed_x='A')            

    def test_multi_object_returned_with_update_or_create(self):
        Sample.objects.create(filed_x='A')
        Sample.objects.create(filed_x='A')

        with self.assertRaises(Sample.MultipleObjectsReturned):    
            Sample.objects.update_or_create(filed_x='A')      

    def test_get_normal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        try:
            Sample.objects.get(filed_x='A',filed_y='B')
        except IntegrityError:
            self.fail('Unexpected Integrity Error')

    def test_get_or_create_normal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        try:
            Sample.objects.get_or_create(filed_x='A',filed_y='B')
        except IntegrityError:
            self.fail('Unexpected Integrity Error')           

    def test_update_or_create_normal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        try:
            Sample.objects.update_or_create(filed_x='A',filed_y='B')
        except IntegrityError:
            self.fail('Unexpected Integrity Error')        
            
    def test_get_abnormal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        with self.assertRaises(Sample.DoesNotExist):  
            Sample.objects.get(filed_x='A',filed_y='B', filed_z='C')

    def test_get_or_create_abnormal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        with self.assertRaises(IntegrityError):  
            Sample.objects.get_or_create(filed_x='A',filed_y='B', filed_z='C')           

    def test_update_or_create_abnormal(self):
        Sample.objects.create(filed_x='A',filed_y='B')

        with self.assertRaises(IntegrityError):  
            Sample.objects.update_or_create(filed_x='A',filed_y='B', filed_z='C')     
