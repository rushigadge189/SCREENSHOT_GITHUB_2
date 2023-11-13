import pytest


class Test_015_markers():

    @pytest.mark.skip
    def test_add(self):
        a=10;
        b=5;
        add=a+b;
        if(add==15) :
             print('\n********ADDITION IS SUCCESSFUL*********') ;
             print('ADDITION=',add) ;
             assert True ;
        else:
             print('\n*********INVALID OPERATION**********') ;
             assert False ;

    @pytest.mark.skipif
    def test_sub(self):
        a=10;
        b=5;
        sub=a-b ;
        if(sub==5) :
            print('\n*********SUBSTARCTION IS SUCCESSFUL*********') ;
            print('SUBSTRACTION=',sub) ;
            assert True ;
        else:
            print('*********INVALID OPERATION*******4') ;
            assert False ;


    @pytest.mark.xfail
    def test_mul(self):
        a=10;
        b=5;
        mul=a*b;
        if(mul==50):
            print('\n********MULTIPLICATION IS SUCCESSFUL**********') ;
            print('MULTIPLICATION=',mul) ;
            assert True ;
        else:
            print('\n***********INVALID OPERATION********') ;
            assert False ;

    def test_div(self):
        a=10;
        b=5;
        div=a/b ;
        if(div==2):
            print('\n********DIVISION IS OPERATION*********') ;
            print('DIVISION=',div) ;
            assert True ;
        else:
            print('\n********INVALID OPERATION*******') ;
            assert False ;

