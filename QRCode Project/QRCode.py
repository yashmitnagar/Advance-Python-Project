import qrcode

#Features of our QRCode
features = qrcode.QRCode(version=1,box_size=10,border=4,)
features.add_data('https://www.instagram.com/yashmit_nagar_/')
features.make(fit=True)

#Genarate an QRCode
generate_image = features.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
generate_image.save('Yashmit_Nagar_.png')

