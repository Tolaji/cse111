from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name  function works correctly 
        Parameters: none
        returns: nothing
        """
    fn = make_full_name("Osibo", "Olutola")
    assert isinstance(fn, str), "full_name function must return  full name"
    
    # Call the make_full_name function six times and use an assert
    # statement to verify the name returned by the 
    # make_full_name function is correct each time
    assert make_full_name("Efe", "Tunde") == "Tunde;Efe"
    assert make_full_name("Adetola", "Omobolanle") == "Adetola;Omobolanle"
    assert make_full_name("", "") == ""
    assert make_full_name("Harry", "Henry") == "Harry;Henry"
    assert make_full_name("Olayinka", "Dimka") == "Olayinka;Dimka"
    assert make_full_name("Biriska", "Mildred") == "Biriska;Mildred"
    assert make_full_name("Olanipekun", "Adams") == "Olanipekun;Adams"
    assert make_full_name("Adetokunbo", "Alfred") == "Adetokunbo;Alfred"
    assert make_full_name("Baba-tunde", "Paul") == "Baba-tunde;Paul"
    


    
def test_extract_family_name():
    """Verify that the extract_family_name function works correctly 
        Parameters: none
        returns: nothing
        """
    efn = extract_family_name("Osibo")
    assert isinstance(efn, str), "extract_family_name function must return family name"
    
    # Call the make_full_name function six timse and use an assert
    # statement to verify the name returned by the 
    # make_full_name function is correct each time
    assert extract_family_name("Efe", "Tunde") == "Tunde"
    assert extract_family_name("Adetola", "Omobolanle") == "Omobolanle"
    assert extract_family_name("", "") == ""
    assert extract_family_name("Harry", "Henry") == "Henry"
    assert extract_family_name("Olayinka", "Dimka") == "Dinka"
    assert extract_family_name("Biriska", "Mildred") == "Mildred"
    assert extract_family_name("Olanipekun", "Adams") == "Adams"
    assert extract_family_name("Adetokunbo", "Alfred") == "Alfred"
    assert extract_family_name("Baba-tunde", "Paul") == "Paul"
    


def test_extract_given_name():
    """Verify that the extract_given_name function works correctly 
        Parameters: none
        returns: nothing
        """
    gn = extract_given_name("Olutola;Osibo")
    assert isinstance(gn, str), "extract_given_name function must return given name"
    
    # Call the make_given_name function six timse and use an assert
    # statement to verify the name returned by the 
    # make_given_name function is correct each time
    assert extract_given_name("Efe", "Tunde") == "Efe"
    assert extract_given_name("Adetola", "Omobolanle") == "Adetola"
    assert extract_given_name("", "") == ""
    assert extract_given_name("Harry", "Henry") == "Harry"
    assert extract_given_name("Olayinka", "Dimka") == "Olayinka"
    assert extract_given_name("Biriska", "Mildred") == "Biriska"
    assert extract_given_name("Olanipekun", "Adams") == "Olanipekun"
    assert extract_given_name("Adetokunbo", "Alfred") == "Adetokunbo"
    assert extract_given_name("Baba-tunde", "Paul") == "Baba-tunde"
    
    
    
    
# Call the main function that is part of the pytest so that the 
# computer will execute the test function in this file
pytest.main(["-v", "--tb=line", "-rN", __file__])
    