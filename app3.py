import streamlit as st
import qrcode
from PIL import Image, ImageFilter

st.title('QRコード自動生成アプリL217')

url = st.text_input('QRコードを生成したいURL：')

img = qrcode.make('https://note.nkmk.me/python-pillow-qrcode/')

if st.button('QRコード生成'):
    _img = qrcode.make('https://note.nkmk.me/python-pillow-qrcode/')
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
    
