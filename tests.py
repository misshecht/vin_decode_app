import json
from main import app

def test_lookup():
    '''
    Tests the lookup route using the given vins, and a few others
    '''
    test_vin1 = "1XPWD40X1ED215307"
    test_vin2= "1XKWDB0X57J211825"
    test_vin3 = "1XP5DB9X7YN526158"
    test_vin4 = "4V4NC9EJXEN171694"
    test_vin5 = "1XP5DB9X7XD487964"
    randomly_generated_vin_6 = "2B4FK55J9KR146695"
    randomly_generated_vin_7 = "2C4GP44362R700796"

    expected_response = {"VIN":"1XPWD40X1ED215307","Make":"PETERBILT","Model":"388","Model_Year":"2014","Body_Class":"Truck-Tractor","Cached_Result":1}
    expected_response2 = {"VIN":"1XKWDB0X57J211825","Make":"KENWORTH","Model":"W9 Series","Model_Year":"2007","Body_Class":"Truck-Tractor","Cached_Result":True}
    expected_response3 = {"VIN":"1XP5DB9X7YN526158","Make":"PETERBILT","Model":"379","Model_Year":"2000","Body_Class":"Truck-Tractor","Cached_Result":True}
    expected_response4 = {"VIN":"4V4NC9EJXEN171694","Make":"VOLVO TRUCK","Model":"VNL","Model_Year":"2014","Body_Class":"Truck-Tractor","Cached_Result":1}
    expected_response5 = {"VIN":"1XP5DB9X7XD487964","Make":"PETERBILT","Model":"379","Model_Year":"1999","Body_Class":"Truck-Tractor","Cached_Result":1}
    expected_response6 = {"VIN":"2B4FK55J9KR146695","Make":"DODGE","Model":"Caravan","Model_Year":"1989","Body_Class":"Van","Cached_Result":True}
    expected_response7 = {"VIN":"2C4GP44362R700796","Make":"CHRYSLER","Model":"Town and Country","Model_Year":"2002","Body_Class":"Minivan","Cached_Result":True}

    with app as client:
        # Test client using first test vin
        response = client.get('/lookup/{}'.format(test_vin1))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response
        
        # Test client using next test vin
        response = client.get('/lookup/{}'.format(test_vin2))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response2

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(test_vin3))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response3

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(test_vin3))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response3

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(test_vin4))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response4

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(test_vin5))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response5

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(randomly_generated_vin_6))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response6

        # Test client using next test vin
        response = client.get('/lookup/{}'.format(randomly_generated_vin_7))
        # Check that we at least got a 200 response back
        assert response.status_code == 200
        # Also check that the response is as expected
        assert json.loads(response.data) == expected_response7

def test_lookup_bad_vin():
    '''
    Let's test badly formed VINs, like too short, too long, including spaces, or invalid characters
    '''
    bad_vin1 = "12345"
    bad_vin2 = "123456789101112131415161718"
    bad_vin3 = "12 12 22222222222"
    bad_vin4 = "!@##$^#$&*&^%$#@!"

    with app as client:
        # Test client using first test bad_vin
        response = client.get('/lookup/{}'.format(bad_vin1))
        # Check that we got a 400 response back to indicate malformed or otherwise bad vin request
        assert response.status_code == 400

        # Test client using first test bad_vin
        response = client.get('/lookup/{}'.format(bad_vin2))
        # Check that we got a 400 response back to indicate malformed or otherwise bad vin request
        assert response.status_code == 400

        # Test client using first test bad_vin
        response = client.get('/lookup/{}'.format(bad_vin3))
        # Check that we got a 400 response back to indicate malformed or otherwise bad vin request
        assert response.status_code == 400

        # Test client using first test bad_vin
        response = client.get('/lookup/{}'.format(bad_vin4))
        # Check that we got a 400 response back to indicate malformed or otherwise bad vin request
        assert response.status_code == 400

test_lookup()

test_lookup_bad_vin()

      