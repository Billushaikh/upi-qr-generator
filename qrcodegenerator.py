
# In this program we are creating a qr code for a upi id and it is scannable using different 
# applications like googlepay, paytm, phonepe

import qrcode

# taking upi id as the input
upi_id = input("Enter the UPI ID = ")

# upi://pay?pa=UPI_ID&apn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

# defining the payments URL based in upi id and the payment app
# you can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# create qr codes for each payment apps
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file(optional)
google_pay_qr.save('google_pay_qr.png')

# display the qr codes for that we may need to install PIL/Pillow library

google_pay_qr.show()
phonepe_qr.show()
paytm_qr.show()
