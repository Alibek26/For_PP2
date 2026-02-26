import json  

# Open the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# Table header
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':6} {'MTU':6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

# Iterate over each interface
for item in data['imdata']:
    intf = item['ethpmPhysIf']['attributes']
    dn = intf['dn']
    descr = intf['descr']
    speed = intf['speed']
    mtu = intf['mtu']
    
    # Print the row with formatting
    print(f"{dn:50} {descr:20} {speed:6} {mtu:6}")