import frappe
import json
from urllib.request import urlopen

@frappe.whitelist(allow_guest=True)
def dolar_price():
    url = "https://www.dolarsi.com/api/api.php?type=dolar"
    response = urlopen(url)
    data = json.loads(response.read())
    jsonData = data['message']
    
    return jsonData
