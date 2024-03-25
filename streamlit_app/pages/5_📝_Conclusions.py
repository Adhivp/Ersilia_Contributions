import streamlit as st

st.subheader("Conclusion Model Bias")
st.markdown("- The model has clearly <span style='color:red;font-weight:bold'>shown a bias towards non-blockers</span>, as it's more likely to output molecules as non-blockers.", unsafe_allow_html=True)
st.markdown("- <span style='color:green;font-weight:bold'> This bias may not be a problem </span>, as the random datasets used for testing contain more non-blockers, and blockers may possess specific qualities that only some molecules have in the real world.", unsafe_allow_html=True)

st.subheader("Conclusion Reproducibility Table S7")
st.markdown("- <span style='color:red;font-weight:bold'>The values predicted by the model do not match those in the research paper.</span>", unsafe_allow_html=True)
st.markdown("- The predicted values differ significantly from the paper, as shown in the graph above.", unsafe_allow_html=True)
st.markdown("- Using a threshold greater than 0.5, the model identifies <span style='color:red;font-weight:bold'>410 molecules</span> as blockers and <span style='color:green;font-weight:bold'>1,318</span> as non-blockers.", unsafe_allow_html=True)
st.markdown("- In the original research paper, out of <span style='color:blue;font-weight:bold'>1,728 molecules</span>, <span style='color:red;font-weight:bold'>526</span> are considered positive (blockers), and the remaining <span style='color:green;font-weight:bold'>1,202</span> are negative.", unsafe_allow_html=True)
st.markdown("- Only <span style='color:red;font-weight:bold'>324 molecules</span> match as blockers in both datasets.", unsafe_allow_html=True)
st.markdown("- Therefore, the probability values were unable to reproduce the expected outcomes, with <span style='color:red;font-weight:bold'>410 molecules</span> identified as blockers (<span style='color:red;font-weight:bold'>324</span> being the actual number, indicating numerous false positives).", unsafe_allow_html=True)

st.subheader("Conclusion Reproducibility Table S6")
st.markdown("- <span style='color:red;font-weight:bold'>The values predicted by the model do not match those in the research paper.</span>", unsafe_allow_html=True)
st.markdown("- The predicted values differ significantly from the paper, as shown in the graph above.", unsafe_allow_html=True)
st.markdown("- Using a threshold greater than 0.5, the model identifies <span style='color:red;font-weight:bold'>22 molecules</span> as blockers and <span style='color:green;font-weight:bold'>27</span> as non-blockers.", unsafe_allow_html=True)
st.markdown("- In the original research paper, all <span style='color:red;font-weight:bold'>49 molecules</span> are classified as blockers.", unsafe_allow_html=True)
st.markdown("- Thus, the probability values were unable to reproduce the expected outcomes, with only <span style='color:red;font-weight:bold'>22 molecules</span> identified as blockers.", unsafe_allow_html=True)
