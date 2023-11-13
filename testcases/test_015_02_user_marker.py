import pytest


class Test_015_02_userdefined_markers():

    @pytest.mark.customer
    def test_add_cust(self):
        print('\n****CUSTOMER ADDED SUCCESSFULLY*****') ;

    @pytest.mark.customer
    def test_del_cust(self):
        print('\n*****CUSTOMER DELETED SUCCESSFULLY*****') ;

    @pytest.mark.product
    def test_add_prod(self):
        print('\n*****PRODUCT ADDED SUCCESSFULLY*****') ;

    @pytest.mark.product
    def test_del_prod(self):
        print('\n*****PRODUCT DELETED SUCCESSFULLY****') ;

    @pytest.mark.bill
    def test_add_bill(self):
        print('\n******BILL ADDED SUCCESSFULLY*****') ;

    @pytest.mark.bill
    def test_del_bill(self):
        print('\n*****BILL DELETD SUCCESSFULLY*****') ;

    @pytest.mark.sanity
    @pytest.mark.patient
    def test_add_patient(self):
        print('\n******PATIENT ADMITTED SUCCESSFULLY*****') ;


    @pytest.mark.regression
    @pytest.mark.patient
    def test_dis_patient(self):
        print('\n*****PATIENT DISCHARGED SUCCESSFULLY*****') ;