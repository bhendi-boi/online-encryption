# Online Encryption
RSA algorithm restricts encryption to maximum 501 bytes of text and does NOT work for encrypting large text file. 😤

If you want to transfer large text file using encryption and without letting anyone else read it, Here is a workaround that can help 😉

- Firstly, generate a `symmetric key`, and encrypt the large text with it.
- Encrypt the symmetric key using your `RSA public key`.
- Then, finally send encrypted text with the encrypted symmetric key.

By this way only receiver who has the `private key` will be able to decrypt the symmetric key and the message.
