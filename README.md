# Secure-Shadows
Secure Shadows is a Python-based steganography tool that leverages the Discrete Cosine Transform (DCT) to securely encode and decode hidden images within cover images. The tool uses a simple graphical user interface (GUI) built with Tkinter, making it easy for users to perform steganographic operations with minimal effort.

Features
Encode Images: Hide a secret image within a cover image using subtle modifications based on the DCT.
Decode Images: Extract the hidden image from an encoded image with high accuracy.
User-Friendly GUI: A clean and intuitive interface built using Tkinter.
Image Format Support: Works with a variety of image formats, including PNG, JPEG, and BMP.
Dynamic Scaling: Automatically resizes the secret image to match the dimensions of the cover image.
DCT-Based Embedding: Ensures minimal distortion to the cover image for better security and visual quality.
How It Works
Encoding:

The cover image and the secret image are converted into the frequency domain using DCT.
A subtle portion of the secret image's frequency coefficients is embedded into the cover image.
The modified frequency coefficients are transformed back to the spatial domain using inverse DCT to create the encoded image.
Decoding:

The encoded image is processed using DCT to retrieve the embedded frequency coefficients.
These coefficients are scaled back to reconstruct the secret image.





