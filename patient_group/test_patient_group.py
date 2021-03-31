import pytest
from group_patients import get_name

@pytest.fixture
def patient():
    return "PID14,CLARA^OSWALD^COLEMAN,F,19890224"


def test_get_name_with_middle_name(patient):
    name = get_name(patient)
    assert name == "claraoswald"
    assert name.islower()


def test_name_with_lower_case():
    patient = "PID14,clara^oswald,F,19890224"
    name = get_name(patient)
    assert name == "claraoswald"
    assert name.islower()


def test_name_with_mix_case():
    patient = "PID14,cLaRA^OSwAld,F,19890224"
    name = get_name(patient)
    assert name == "claraoswald"
    assert name.islower()


def test_patient_with_more_than_4_fields():
    patient = "PID14,cLaRA^OSwAld,F,19890224,extra"
    with pytest.raises(Exception, match=r'information.*invalid'):
        get_name(patient)


def test_patient_name_has_more_than_3_fields():
    patient = "PID14,CLARA^OSWALD^COLEMAN^Fourth,F,19890224"
    with pytest.raises(Exception, match=r'name.*invalid'):
        get_name(patient)
