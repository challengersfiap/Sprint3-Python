import qrcode

# Texto que você deseja codificar no QR code
link = "https://www.instagram.com"

# Cria um objeto QRCode com o texto
codigo = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,  # Ajuste o tamanho do QR code conforme necessário
    border=2,    # Ajuste a margem conforme necessário
)
codigo.add_data(link)
codigo.make(fit=True)

# Gera o QR code como uma imagem usando o Pillow (PIL)
imagem = codigo.make_image(fill_color="black", back_color="white")

# Exibe o QR code no console
imagem.show()
