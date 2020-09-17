import base64
import creds

password = creds.password
password_bytes = password.encode("ascii") 
  
base64_bytes = base64.b64encode(password_bytes) 
base64_string = base64_bytes.decode("ascii") 
  
print(f"Encoded string: {base64_string}") 
