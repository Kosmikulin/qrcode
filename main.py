import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data('https://docs.google.com/spreadsheets/d/2gW60FH3esPnokBwR2ohLLZ86WigS-yUNAiYKtczDXvg/edit#gid=0')

img = qr.make_image(fill_color='black', back_color='white')
img.save('qrcode.png', 'PNG')
