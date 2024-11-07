import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Insert API Key as a string that is provided by Instructor in D2L
# YOUR CODE HERE (1 line)
# I'm not committing your API key to GitHub, you're welcome
key=os.getenv("AZURE_KEY")

# 2. getCountry function is used to look up the appropriate country code
# assigned to the IP Address. This function requires one argument (ip)
# You will need to insert the key and ip variables to complete the apiURL string
# Example API URL: 'https://atlas.microsoft.com/geolocation/ip/json?subscription-key=<key inside D2L>&api-version=1.0&ip=###.###.###.###
def getCountry(ip):
    apiURL = f'https://atlas.microsoft.com/geolocation/ip/json?api-version=1.0&subscription-key={key}&ip={ip}'
    r = requests.get(apiURL)
    
    # Print statements are extremely helpful!
    # OPTIONAL Print statements can be used here
    #print(r.json())

    # 3. Some requests returned may not be what we expect. We must add an exception handling
    # statement to avoid errors that may prevent all the IPs from being processed.
    # You need to extract the country code from the JSON returned.
    # YOUR CODE HERE (Less than 10 lines)
    if r.status_code == 200:
        return r.json()['countryRegion']['isoCode']
    else:
        print(f"Error {r.status_code} for {ip}")



def main(): 
  print("Good Luck")
  # Print statements are extremely helpful!
  # OPTIONAL the print statement below to test if your function is working. 
  # HINT it should only print "US", and this script is done!

  print(getCountry('8.8.8.8'))
  

if __name__ == "__main__":
    main()