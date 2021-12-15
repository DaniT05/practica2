import meraki
import json
import csv
import pprint
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)
print("\nValidación de algun error de la solicitud getOrganizations:",response.raise_for_status())
resp=response.json()
pprint.pprint(resp)



url = "https://api.meraki.com/api/v1/organizations/681155/devices/statuses?productTypes%5B%5D=wireless&productTypes%5B%5D=appliance"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response2 = requests.request('GET', url, headers=headers, data = payload)
print("\nValidación de algun error de la solicitud getOrganizationDevicesStatuses:",response2.raise_for_status())
resp2=response2.json()
pprint.pprint(resp2)




with open('inventario.csv', mode='w') as csv_file:
    fieldnames = ['Tipo','Modelo_del_equipo', 'Nombre', 'dirección_MAC','dirección_IP_pública','dirección_IP_LAN','serial','status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR84', 'Nombre': 'Alexs MR84 - 1' ,        'dirección_MAC': 'e0:55:3d:10:56:8a', 'dirección_IP_pública': '75.187.61.126', 'dirección_IP_LAN': 'none'  ,        'serial': 'Q2EK-2LYB-PCZP','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR84', 'Nombre': 'Vegas Living Room MR84', 'dirección_MAC': 'e0:55:3d:10:5a:ca', 'dirección_IP_pública': '71.222.80.198', 'dirección_IP_LAN': '192.168.0.20',  'serial': 'Q2EK-3UBE-RRUY','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR84', 'Nombre': '...'                  ,  'dirección_MAC': 'e0:55:3d:10:5b:d8', 'dirección_IP_pública': 'none',          'dirección_IP_LAN': 'none',          'serial': 'Q2EK-ACGE-URXL','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR84', 'Nombre': 'Vegas Balcony MR84',     'dirección_MAC': 'e0:55:3d:10:5c:48', 'dirección_IP_pública': '71.222.80.198', 'dirección_IP_LAN': 'none',          'serial': 'Q2EK-D4XP-235S','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR84', 'Nombre': 'Sun Room',               'dirección_MAC': 'e0:55:3d:10:5e:b2', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.99','serial': 'Q2EK-UKGM-XSD9','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR32', 'Nombre': 'Alex MR32',              'dirección_MAC': 'e0:55:3d:b8:3e:70', 'dirección_IP_pública': '71.79.148.43',  'dirección_IP_LAN': '192.168.1.16'  ,'serial': 'Q2JD-7RNY-EB7Z','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR42', 'Nombre': '...'                   , 'dirección_MAC': 'e0:cb:bc:8c:1f:fe', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.0.2',   'serial': 'Q2KD-KWMU-7U92','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': 'Basement AP',            'dirección_MAC': 'e0:55:3d:c0:73:56', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.17','serial': 'Q2LD-3Y7V-7Y2X','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '2nd Floor AP',           'dirección_MAC': 'e0:55:3d:c0:5e:2e', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.15','serial': 'Q2LD-AN9B-S6AJ','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b2:2f:2c', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.4', 'serial': 'Q2LD-D932-NRPU','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b2:77:f8', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.7', 'serial': 'Q2LD-FGN3-VP7S','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '1st Floor AP',           'dirección_MAC': 'e0:55:3d:c0:76:f4', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.202','serial':'Q2LD-GYL3-KEHX','status': 'online'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b2:8a:5a', 'dirección_IP_pública': '24.144.215.84', 'dirección_IP_LAN': '24.144.215.84', 'serial': 'Q2LD-N2U5-D83H','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b2:8c:f0', 'dirección_IP_pública': 'null',          'dirección_IP_LAN': 'null',          'serial': 'Q2LD-X2S2-AG2U','status': 'dormant'})
    writer.writerow({'Tipo': 'wireless', 'Modelo_del_equipo': 'MR52', 'Nombre': 'Office AP'             , 'dirección_MAC': 'e0:55:3d:c0:72:d8', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '192.168.128.16','serial': 'Q2LD-ZWCZ-UA77','status': 'online'})
    writer.writerow({'Tipo': 'appliance','Modelo_del_equipo': 'MX65', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b0:c2:dc', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '...',           'serial': 'Q2QN-Q6EY-NP7J','status': 'online'})
    writer.writerow({'Tipo': 'appliance','Modelo_del_equipo': 'MX65', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b0:c3:44', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '...',           'serial': 'Q2QN-UTMQ-ZJQA','status': 'online'})
    writer.writerow({'Tipo': 'appliance','Modelo_del_equipo': 'MX65', 'Nombre': '...'                   , 'dirección_MAC': '0c:8d:db:b0:c4:55', 'dirección_IP_pública': 'null',          'dirección_IP_LAN': '...',           'serial': 'Q2QN-Y5ED-P57W','status': 'dormant'})
    writer.writerow({'Tipo': 'appliance','Modelo_del_equipo': 'MX250','Nombre': 'BigCat'                , 'dirección_MAC': 'ac:17:c8:24:4f:68', 'dirección_IP_pública': '76.250.206.183','dirección_IP_LAN': '...',           'serial': 'Q2SW-SWQ2-HZ9L','status': 'online'})