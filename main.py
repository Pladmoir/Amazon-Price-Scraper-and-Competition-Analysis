import streamlit as st

def render_header():
    st.title("Amazon Competitior Analysis")
    st.caption("Enter your ASIN to get product insights.")

def render_inputs():
    asin = st.text_input("ASIN", placeholder="e.g. B0D5QJWZFL")
    geo = st.text_input("Zip/Postal Code", placeholder="e.g., N2L 3G1")
    domain = st.selectbox("Domain", [
        "ca", "com", "co.uk", "de", "fr", "it", "tv", "ai", "gov"
    ])
    return asin.strip(), geo.strip(), domain

def main():
    st.set_page_config(page_title="Amazon Competitor Analysis", page_icon="📚")
    render_header()
    asin, geo, domain = render_inputs()

if __name__ == "__main__":
    main()