# Harpocrates

This is a tool which uses a hybrid encryption model combining both RSA algorithm and steganography. It takes a message as input from the user, encrypts it using the public key provided by the user, and encloses it in a cover image. The image can now be safely transferred over to the recipient, who can then remove the cover image and decrypt the message using his/her private key.

## Proposed Features-

- Takes input message, public key, and cover image as input from the user, and encrypt the message.
- Decrypt the received message, using the private key of the owner/recipient.
- A command-line interface for the program to execute.
