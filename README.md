# UPI QR Code Generator

A Python application that generates QR codes for UPI payments compatible with popular payment apps like Google Pay, PhonePe, and Paytm.

## Features
- Generates QR codes for UPI payments
- Supports multiple payment apps:
  - Google Pay
  - PhonePe
  - Paytm
- Saves QR codes as PNG files
- Shows QR codes immediately after generation

## Requirements
- Python 3.9 and above
- qrcode library
- PIL/Pillow library

## Installation
```bash / cmd 
pip install qrcode pillow
```

## Usage
1. Run the script
2. Enter your UPI ID when prompted
3. QR codes will be generated and displayed
4. A Google Pay QR code will be saved as 'google_pay_qr.png'

## License
MIT License