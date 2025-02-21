import json

# Load the data from the JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Create the header
print("Interface Status")
print("="*80)
print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)

# Extract the required fields for each interface and print them
for item in data.get('imdata', []):
    if 'l1PhysIf' in item:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes.get('dn', '')
        description = attributes.get('descr', 'inherit')  # Default to 'inherit' if description is missing
        speed = attributes.get('speed', '')
        mtu = attributes.get('mtu', '')
        
        # Print each interface in the desired format
        print("{:<50} {:<20} {:<6} {:<6}".format(dn, description, speed, mtu))
