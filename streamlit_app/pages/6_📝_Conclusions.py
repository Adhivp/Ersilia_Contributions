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

st.subheader("External Validation")
metrics_content = """
1. **Accuracy:**  
   - The accuracy of the model is <span style='color:red;font-weight:bold'>74.90%</span>, indicating that it correctly predicts the class labels for nearly three-quarters of the observations.

2. **Sensitivity (True Positive Rate):**
   - The sensitivity of the model is <span style='color:red;font-weight:bold'>64.72%</span>, indicating that it correctly identifies 64.72% of the actual positive cases.

3. **Specificity (True Negative Rate):**
   - The specificity of the model is <span style='color:red;font-weight:bold'>78.86%</span>, indicating that it correctly identifies 78.86% of the actual negative cases.

4. **Precision (Positive Predictive Value):**
   - The precision of the model is <span style='color:red;font-weight:bold'>54.31%</span>, indicating that when it predicts a positive case, it is correct 54.31% of the time.

5. **Recall (Same as Sensitivity):**
   - The recall of the model is <span style='color:red;font-weight:bold'>64.72%</span>, indicating the same as sensitivity.

6. **Negative Predictive Value:**
   - The negative predictive value of the model is <span style='color:red;font-weight:bold'>85.20%</span>, indicating that when it predicts a negative case, it is correct 85.20% of the time.

7. **Balanced Accuracy:**
   - The balanced accuracy of the model is <span style='color:red;font-weight:bold'>71.79%</span>, which is the average of sensitivity and specificity, providing a balanced view of the model's performance.

8. **Matthew's Correlation Coefficient:**
   - The Matthew's correlation coefficient of the model is <span style='color:red;font-weight:bold'>0.41</span>, indicating a moderate level of correlation between the predicted and true binary classifications.

9. **F1 Score:**
   - The F1 score of the model is <span style='color:red;font-weight:bold'>59.06%</span>, which is the harmonic mean of precision and recall, providing a balance between the two metrics.

10. **AUROC (Area Under the Receiver Operating Characteristic Curve):**
    - The AUROC of the model is <span style='color:red;font-weight:bold'>71.79%</span>, indicating the model's ability to distinguish between the positive and negative classes across various threshold values.

11. **R2 Value:**
    - The R-squared value of the model is <span style='color:red;font-weight:bold'>-0.25</span>, which is negative, indicating that the model performs worse than a horizontal line (a horizontal line would have an R2 value of 0), suggesting that the model does not fit the data well in the context of regression analysis.
"""

st.markdown(metrics_content, unsafe_allow_html=True)