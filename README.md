# Secure-Shadows
Secure Shadows is a Python-based steganography tool that leverages the Discrete Cosine Transform (DCT) to securely encode and decode hidden images within cover images. The tool uses a simple graphical user interface (GUI) built with Tkinter, making it easy for users to perform steganographic operations with minimal effort.

Features🥇
Encode Images: Hide a secret image within a cover image using subtle modifications based on the DCT.
Decode Images: Extract the hidden image from an encoded image with high accuracy.
User-Friendly GUI: A clean and intuitive interface built using Tkinter.
Image Format Support: Works with a variety of image formats, including PNG, JPEG, and BMP.
Dynamic Scaling: Automatically resizes the secret image to match the dimensions of the cover image.
DCT-Based Embedding: Ensures minimal distortion to the cover image for better security and visual quality.

How It Works:-

Encoding:
The cover image and the secret image are converted into the frequency domain using DCT.
A subtle portion of the secret image's frequency coefficients is embedded into the cover image.
The modified frequency coefficients are transformed back to the spatial domain using inverse DCT to create the encoded image.

Decoding:
The encoded image is processed using DCT to retrieve the embedded frequency coefficients.
These coefficients are scaled back to reconstruct the secret image.

Installation⬇️
1 Clone the repository
  git clone https://github.com/your-username/secure-shadows.git
  cd secure-shadows
2 Install dependencies 
  pip install -r requirements.txt
3 Run the application:
  python stego_dct.py

Requirements⬇️
Python 3.7 or higher
Libraries: Tkinter, NumPy, OpenCV, Pillow

Usage⬇️
Launch the application using python stego_dct.py.
Click Encode Image to select the cover image and the secret image.
Save the encoded image.
To decode, click Decode Image, select the encoded image, and save the extracted secret image.

Contributing⬇️
Contributions are welcome! Please fork the repository and submit a pull request with your updates or enhancements.





