
from fastapi import FastAPI
import ipaddress

app = FastAPI()

def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       return [True,{ip_object} + " is valid"]
   except ValueError:
       return [False,{ip_string} + " is not valid"]



@app.get("/ipAddress/")
async def siteRank(ip):
    result = {}
    try:
        addr = ipaddress.ip_address(ip)
    except Exception as e:
        print(e)
        result["error"] = [True,str(e)]
    else:
        output = addr.exploded.replace(':','') # remove :
        if '.' not in output: #assume ipv6
            print(addr,"|",(addr.exploded))
            
            result = { 
                       'sourceIP' : addr,
                       'exploded' : addr.exploded,
                       'ipv' : 6
            }

            output = '.'.join(output[i:i+1] for i in range(0, len(output), 1))
        else:
            print(addr)
            result = { 
                       'sourceIP' : addr,
                       'ipv' : 4
            }     
        result['dotNotation'] = output
        result['reversedDotNotation'] = '.'.join(output.split('.')[::-1])

        result["error"] = [False]
    return result





