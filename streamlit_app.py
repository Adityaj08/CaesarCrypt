import streamlit as st
from cipher import Cipher

# Streamlit App
def main():
    st.set_page_config("CaesarCrypt")
    st.title("Cipher Encryption and Decryption")
    cipher = Cipher()
    st.sidebar.title("Cipher Options")
    choice = st.sidebar.selectbox("Choose the Mode", ["Encrypt", "Decrypt"],label_visibility="collapsed",index=None) or "Encrypt"
    st.sidebar.markdown("---")
    if st.sidebar.button("sign-in",use_container_width=True):
        st.sidebar.info("To be Added soon...",icon=":material/info:")
    st.sidebar.link_button("Github >","https://github.com/Adityaj08/CaesarCrypt/blob/main/README.md",use_container_width=True,type="primary")

    if choice == "Encrypt":
        st.subheader("Encryption")
        message = st.text_input("Enter the message to encrypt",placeholder="Ex: Secret Message")
        key = st.number_input("Enter the Key", min_value=0, step=1,placeholder="Ex: 11")
        st.info("Pressing Encrypt will automatically enable copy to clipboard option",icon=":material/info:")
        if st.button("Encrypt",use_container_width=True,type="primary"):
            if message:
                encrypted_message = cipher.encrypt(message, key)
                st.write("Encrypted text")
                st.code(encrypted_message,language="str")
                st.toast("Encrypted text copied to clipboard!",icon=":material/content_paste:")
            else:
                st.toast(":red[Please enter a message to encrypt!]",icon=":material/error:")

    elif choice == "Decrypt":
        st.subheader("Decryption")
        message = st.text_input("Enter the message to decrypt",placeholder="Ex: Encrypted Message")
        key = st.number_input("Enter the Key", min_value=0, step=1)
        if st.button("Decrypt",use_container_width=True,type="primary"):
            if message:
                decrypted_message = cipher.decrypt(message, key)
                st.write("Decrypted text")
                st.code(decrypted_message,language="str")      
            else:
                st.toast(":red[Please enter a message to decrypt!]",icon=":material/error:")


if __name__ == '__main__':
    main()
