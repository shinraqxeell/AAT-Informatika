import streamlit as st

# Title Web Page
st.set_page_config (page_title= "Mencari Akar Kuadrat", page_icon=":book:", layout="wide"  )

# Header Section 
st.markdown("<h4 style='text-align: center; color: white;'> Mencari Hasil Akar Kuadrat Sebuah Angka </h4>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'> | Muhammad Wildan Hamid X-4 SMAN 103 Jakarta | </h4>", unsafe_allow_html=True)
st.divider()

# Mencari Akar Kuadrat
def square_root(number):
    return number ** 0.5

# Streamlit app code
def main():

    #Header 
    st.markdown("<h5 style='text-align: center; color: white;'> Masukan Angka </h4>", unsafe_allow_html=True)

    # User input
    number = st.number_input("", value=0.0, step=0.01)

    # Calculate square root
    result = square_root(number)

    # Display result
    st.write(f"Akar Kuadrat Dari {number} adalah {result}")

if __name__ == "__main__":
    main()