
#second function needs to be updated with the the current days informationw when testing

#testing using pytest
import name_to_tick

def test_name_to_tick():
    name=name_to_tick.name_convert('google')
    assert name == 'GOOG'


#This test fails on first version. Not sure if assert is being compared correctly
def test_company_data():
    tick=name_to_tick.company_data('GOOG')
    assert tick ==('967.84', '965.40', '+0.39%')