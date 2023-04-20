import streamlit as st
import base64
import math

def gptb2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = 'PTB1 có vô số nghiệm'
            else:
                ket_qua = 'PTB1 vô nghiệm'
        else:
            x = -c/b
            ket_qua = 'PTB1 có nghiệm %.2f' % x
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            ket_qua = 'PTB2 vô nghiệm'
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            ket_qua = 'PTB2 có nghiệm x1 = %.2f và x2 = %.2f' % (x1, x2)
    return ket_qua

def clear_input():
    st.session_state["nhap_a"] = 0.0
    st.session_state["nhap_b"] = 0.0
    st.session_state["nhap_c"] = 0.0

st.subheader('Giải phương trình bậc 2')
def set_background(png_file):
    bin_str = base64.get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('gorou.jpg')
with st.form(key='columns_in_form', clear_on_submit = False):
    a = st.number_input('Nhập a', key = 'nhap_a')
    b = st.number_input('Nhập b', key = 'nhap_b')
    c = st.number_input('Nhập c', key = 'nhap_c')
    c1, c2 = st.columns(2)
    with c1:
        btn_giai = st.form_submit_button('Giải')
    with c2:
        btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)
    if btn_giai:
        s = gptb2(a, b, c)
        st.markdown('Kết quả: ' + s)
    else:
        st.markdown('Kết quả:')