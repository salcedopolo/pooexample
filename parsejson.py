# Fill in this file with the code from parsing JSON exercise
import json
import yaml

with open ("myfile.json") as json_file:
    ourjson = json.load(json_file)

print(ourjson)


print("El token de acceso es: {}".format(ourjson["access_token"]))
print("El token expira en {} segundos".format(ourjson["expires_in"])) 


print("\n\n---") 
print(yaml.dump(ourjson))
