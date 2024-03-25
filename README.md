# hERG Blocker Classification Model (eos30gr)
Welcome to the hERG Blocker Classification Model. This model predicts the probability that a molecule is a hERG blocker.

## Model Characteristics
- **Input:** Compound
- **Task:** Classification
- **Output:** Probability
- **Interpretation:** Probability of hERG blockade. The training dataset used a threshold of 80% inhibition to define hERG blockers.

## Model Testing Information (My Contribution)
As per the guidance from the mentor, I have tested the model. One dataset was used to identify model bias, and the other two were used to check reproducibility.

## Repository organisation
The repository is organised in folders:
- '/notebooks' contains the jupyter notebooks where most of the work is being developed
- '/data' contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder. Subfolders might be created if needed
- '/src' contains important functions I will re-use throughout the repository, to avoid typing them each time
- '/streamlit_app' contains the code used for deploying streamlit_app
- 'requirements.txt' lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.

# hERG information
## Introduction
hERG (the human Ether-à-go-go-Related Gene) codes for the Kv11.1 protein, which mediates the repolarizing IKr current in the heart's action potential.

## Function
- hERG forms the 'rapid' delayed rectifier current (IKr), conducting potassium ions out of cardiac myocytes.
- IKr is crucial for timing the return to the resting state of cell membrane during the cardiac action potential.

## Structure
- hERG comprises 4 identical alpha subunits, each with 6 transmembrane helices.
- The S4 helix acts as a voltage-sensitive sensor, enabling the channel to respond to voltage changes.
- The selectivity filter region of the channel pore contains the sequence SVGFG.

## Genetics
- Loss-of-function mutations in hERG may lead to long QT syndrome (LQT2), while gain-of-function mutations may lead to short QT syndrome.
- Both clinical disorders can result in potentially fatal cardiac arrhythmias.

## Drug Interactions
- hERG is sensitive to drug binding, leading to drug-induced long QT syndrome.
- Many drugs, including antiarrhythmics and certain antibiotics, can interact with hERG.

## Drug Development Considerations
- The FDA recommends establishing a cardiac safety profile during pre-clinical drug development to evaluate the potential for QT interval prolongation.
- Preclinical hERG studies should be conducted in GLP environment.

## License
All the code in this repository is licensed under a GPLv3 License.