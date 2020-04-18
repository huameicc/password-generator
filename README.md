A method to generate passwords: Use a source_key, a domain and a salt to 
generate password. 

You could only remember one source_secret in your brain. When You want to get 
a new password, just provide a new domain or salt.  

domain: could be a website name or something.
salt: could be username or something.

Just keep domains and salts in a txt, and store it in a cloud or something. Or 
you could even write it down with your pen, keep it under your pillow.

When You forget a password, just re_calculate it with your source_key along with 
domain and salt.


Algorithm: 
  URLSAFE_BASE64(SHA256(SHA256(source_key), domain, salt))

Note: [Check out the One-Way feature of hash-digest.]




