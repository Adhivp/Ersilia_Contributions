import streamlit as st


st.set_page_config(page_title="hERG Information", page_icon="⚡️", layout="wide")



st.title("Understanding hERG (the human Ether-à-go-go-Related Gene)")
st.image("https://upload.wikimedia.org/wikipedia/commons/5/58/PBB_Protein_KCNH2_image.jpg", width=300)



def colorful_section(title, content, color):
    st.markdown(f"<h2 style='color:{color}'>{title}</h2>", unsafe_allow_html=True)
    st.write(content)


def bullet_points(points):
    for point in points:
        st.write(f"- {point}")


colorful_section("Introduction", """
hERG (the human Ether-à-go-go-Related Gene) codes for the Kv11.1 protein, which mediates the repolarizing IKr current in the heart's action potential.
""", "blue")

colorful_section("Function", """
- hERG forms the 'rapid' delayed rectifier current (IKr), conducting potassium ions out of cardiac myocytes.
- IKr is crucial for timing the return to the resting state of cell membrane during the cardiac action potential.
""", "green")

colorful_section("Structure", """
- hERG comprises 4 identical alpha subunits, each with 6 transmembrane helices.
- The S4 helix acts as a voltage-sensitive sensor, enabling the channel to respond to voltage changes.
- The selectivity filter region of the channel pore contains the sequence SVGFG.
""", "orange")

colorful_section("Genetics", """
- Loss-of-function mutations in hERG may lead to long QT syndrome (LQT2), while gain-of-function mutations may lead to short QT syndrome.
- Both clinical disorders can result in potentially fatal cardiac arrhythmias.
""", "purple")

colorful_section("Drug Interactions", """
- hERG is sensitive to drug binding, leading to drug-induced long QT syndrome.
- Many drugs, including antiarrhythmics and certain antibiotics, can interact with hERG.
""", "red")

colorful_section("Drug Development Considerations", """
- The FDA recommends establishing a cardiac safety profile during pre-clinical drug development to evaluate the potential for QT interval prolongation.
- Preclinical hERG studies should be conducted in GLP environment.
""", "brown")
