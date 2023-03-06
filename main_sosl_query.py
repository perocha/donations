from mysecrets import username, password, security_token
from salesforce_api import SalesForceAPI


def print_results(results):
    for result in results['searchRecords']:
        print(f"Name: {result['Name']}")
        print(f"Phone: {result['Phone']}")
        print(f"Email: {result['Email']}")
        print(f"Id: {result['Id']}")
        print(f"Tipo: {result['ContactType__c']}")
        print(f"Tesorería: {result['SituacionTesoreria__c']}")
        print(f"Fecha alta: {result['aesrFechaAlta__c']}")
        print(f"Fecha baja: {result['aesrFechaBaja__c']}")
        print()

# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()

# Get the contact information by generic search
generic_info = input("Enter the generic info:")
result = my_sf.get_contactid_bygeneric (generic_info)

# Print the results
print_results (result)