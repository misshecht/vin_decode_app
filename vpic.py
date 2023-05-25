import requests

class VpicApiClient:
    BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

    def lookup(self, vin):
        url = f"{self.BASE_URL}/DecodeVinValues/{vin}?format=json"
        # Sanity check - is VIN exactly 17 chars in length? If not, alert user
        if len(vin) != 17:
            raise Exception(f"Invalid VIN: {vin}, please try again")
            return 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get("Results"):
                return data.get("Results")[0]
            else:
                raise Exception("No results found for the VIN")
        else:
            raise Exception("Failed to retrieve data from VPIC API")
