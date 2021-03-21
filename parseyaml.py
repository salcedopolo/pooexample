# Fill in this file with the code from parsing YAML exercise

import json
import yaml

with  open ("myfile.yaml") as yamfile:
    ouryaml = yaml.safe_load (yamfile)

print(ouryaml)

print("El token de acceso es: {}".format(ouryaml["access_token"]))
print("El token expira en {} segundos".format(ouryaml["expires_in"]))


print("\n\n") 
print(json.dumps(ouryaml, indent=4))
