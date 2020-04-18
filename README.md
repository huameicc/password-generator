# A method to generate passwords 

### Use a source_key, a domain and a salt to generate passwords reproducibly. 

- You should only remember one source_key in your brain. When you want to get a new password, just provide a new domain or salt.

- You can keep domains and salts in a text, and store it in a cloud or somewhere. Or you could just write it down with your pen, and keep it under your pillow.

- When You forget a password, just re-calculate it with your source_key along with domain and salt.

### Algorithm: 

```
URLSAFE_BASE64(SHA256(SHA256(source_key), domain, salt))
```
*Note: [Check out the One-Way feature of hash-digest.]*



[^domain]: could be a website name or something.
[^salt]: could be user_name or something.



