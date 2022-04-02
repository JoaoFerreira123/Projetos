import qrcode
qr = qrcode.QRCode(
    box_size=20, #tamanho do QRcode
    border=2, #tamanho da borda
)

qr.add_data('Olha só meu QR code em PYTHONNN') #conteúdo do QR Code

img = qr.make_image(fill_color="white", back_color="blue") #altera as cores do código e do fundo. Também aceita valores RGB como parâmetros
img.save("TesteQRcode.png") #cria o arquivo com um determinado nome

#mais informações em: https://pypi.org/project/qrcode/

