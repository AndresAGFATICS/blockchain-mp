# Ejemplo de consumo de Signer API y creación de cuenta usando Python
import requests
url = "<URL_SIGNER>" # Especificar la ruta correcta
account_url = f'{url}/account'
response = requests.request("GET", signer_url)
print(response.text)
'''
{
version: 3,
id: 'c8843162-474c-4d47-9bce-2f9842d1b833',
address: 'a24406d8dde54140976df25b98aade5583450604',
crypto: {
ciphertext: '1ec134bc02de07a7309073a67e5ffc8024c8271a9186372009967c4c60fdd323',
cipherparams: {iv: '48c5044636f4cb28db91c679aa657b97'},
cipher: 'aes-128-ctr',
kdf: 'scrypt',
kdfparams: {
dklen: 32,
salt: 'ad4d20102ff1d69a051132e750eea692bde2da113690603447b4814777f9ff0e',
n: 8192,
r: 8,
p: 1,
},
mac: 'bf0733445a3243e5e021917e5699a8b0ef0091d3226ba28ac18d3074439f94bb',
}
}
'''
