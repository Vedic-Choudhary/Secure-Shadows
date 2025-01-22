import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Shadows")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Load background image
        self.background_image = ImageTk.PhotoImage(Image.open("BACKGROUND.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1, relx=0.0, rely=0.0)
        # Load and resize background image to zoom out
        original_background = Image.open("BACKGROUND.png")
        resized_background = original_background.resize((int(original_background.width * 0.8), int(original_background.height * 0.8)))  
        # Scale down to 90% of the original size
        self.background_image = ImageTk.PhotoImage(resized_background)

        # Update background label
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1, relx=0.0, rely=0.0)


        # Title Label
        self.title_label = tk.Label(
            self.root,
            text="Secure Shadows",
            font=("Brush Script MT", 36, "bold"),
            bg="#000000",
            fg="#FFD700",
        )
        self.title_label.pack(pady=20)

        # These are the  Buttons for encoding and decoding
        self.encode_button = tk.Button(
            self.root,
            text="Encode Image",
            font=("Arial", 14, "bold"),
            bg="#333333",
            fg="#FFFFFF",
            command=self.encode_image,
        )
        self.encode_button.pack(pady=10)

        self.decode_button = tk.Button(
            self.root,
            text="Decode Image",
            font=("Arial", 14, "bold"),
            bg="#333333",
            fg="#FFFFFF",
            command=self.decode_image,
        )
        self.decode_button.pack(pady=10)

        # Label to show the status of the operation
        self.status_label = tk.Label(
            self.root, text="Select an option above", font=("Arial", 12), bg="#000000", fg="#FFFFFF"
        )
        self.status_label.pack(pady=20)

    def encode_image(self):
        try:
            # Open a file dialog to select the cover image
            image_path = filedialog.askopenfilename(
                title="Select Image to Encode Into",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],
            )
            if not image_path:
                return

            # Open a file dialog to select the secret image
            secret_image_path = filedialog.askopenfilename(
                title="Select Secret Image",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],
            )
            if not secret_image_path:
                return

            # Load cover and secret images
            cover_image = Image.open(image_path)
            secret_image = Image.open(secret_image_path)

            # Resize the secret image to match the size of the cover image
            secret_image_resized = secret_image.resize(cover_image.size)

            # Convert images to numpy arrays
            cover_image_np = np.array(cover_image, dtype=np.float32)
            secret_image_np = np.array(secret_image_resized, dtype=np.float32)

            # Ensure images are in grayscale or color
            if len(cover_image_np.shape) == 2:  # Grayscale
                cover_dct = cv2.dct(cover_image_np / 255.0)
                secret_dct = cv2.dct(secret_image_np / 255.0)

                # Embed the secret image into the cover image using a subtle scaling factor
                encoded_dct = cover_dct + secret_dct * 0.02  # Subtle scaling factor

                # Perform inverse DCT to get the encoded image
                encoded_image_np = cv2.idct(encoded_dct) * 255
            else:  # Color
                # Split into channels
                cover_channels = cv2.split(cover_image_np)
                secret_channels = cv2.split(secret_image_np)

                # Perform DCT on each channel
                encoded_channels = []
                for cover_channel, secret_channel in zip(cover_channels, secret_channels):
                    cover_dct = cv2.dct(cover_channel / 255.0)
                    secret_dct = cv2.dct(secret_channel / 255.0)
                    encoded_dct = cover_dct + secret_dct * 0.05  # Subtle scaling factor
                    encoded_channel = cv2.idct(encoded_dct) * 255
                    encoded_channels.append(encoded_channel)

                # Merge channels back
                encoded_image_np = cv2.merge(encoded_channels)

            # Normalize and convert back to an image
            encoded_image_np = np.clip(encoded_image_np, 0, 255).astype(np.uint8)
            encoded_image = Image.fromarray(encoded_image_np)

            # Save the encoded image
            encoded_image_path = filedialog.asksaveasfilename(
                title="Save Encoded Image As",
                defaultextension=".jpg",
                filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")],
            )
            if encoded_image_path:
                encoded_image.save(encoded_image_path, format="JPEG")
                self.status_label.config(
                    text=f"Image encoded successfully! Saved to: {encoded_image_path}"
                )
            else:
                self.status_label.config(text="Save operation was cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decode_image(self):
        try:
            # Open a file dialog to select the encoded image
            encoded_image_path = filedialog.askopenfilename(
                title="Select Encoded Image",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],
            )
            if not encoded_image_path:
                return

            # Load the encoded image
            encoded_image = Image.open(encoded_image_path)
            encoded_image_np = np.array(encoded_image, dtype=np.float32)

            # Check if the image is grayscale or color
            if len(encoded_image_np.shape) == 2:  # Grayscale
                encoded_dct = cv2.dct(encoded_image_np / 255.0)
                extracted_dct = encoded_dct * 50  # Reverse scaling factor

                # Perform inverse DCT to get the secret image
                secret_image_np = cv2.idct(extracted_dct) * 255
            else:  # Color
                encoded_channels = cv2.split(encoded_image_np)

                # Perform DCT on each channel
                extracted_channels = []
                for channel in encoded_channels:
                    channel_dct = cv2.dct(channel / 255.0)
                    extracted_dct = channel_dct * 20  # Reverse scaling factor
                    extracted_channel = cv2.idct(extracted_dct) * 255
                    extracted_channels.append(extracted_channel)

                # Merge channels back
                secret_image_np = cv2.merge(extracted_channels)

            # Normalize and convert back to an image
            secret_image_np = np.clip(secret_image_np, 0, 255).astype(np.uint8)
            secret_image = Image.fromarray(secret_image_np)

            # Save the extracted secret image
            secret_image_path = filedialog.asksaveasfilename(
                title="Save Decoded Image As",
                defaultextension=".jpg",
                filetypes=[("JPG Files", "*.jpg"), ("All Files", "*.*")],
            )
            if secret_image_path:
                secret_image.save(secret_image_path, format="JPEG")
                self.status_label.config(
                    text=f"Secret image decoded successfully! Saved to: {secret_image_path}"
                )
            else:
                self.status_label.config(text="Save operation was cancelled.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()













