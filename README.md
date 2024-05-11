
## Description
The Parkinson's Disease Detection Project is a Machine Learning model aimed at detecting the presence of Parkinson's disease based on an Individual's biomedical voice measurements. The model analyzes various voice characteristics extracted from voice recordings to distinguish between individuals with Parkinson's disease and healthy individuals.

## Purpose
Parkinson's disease is a neurodegenerative disorder that affects movement, and early detection is crucial for effective management and treatment. This project provides a tool for early detection of Parkinson's disease using non-invasive voice recordings, which can aid in timely diagnosis and intervention.

## Getting Started
To get started with the Parkinson's Disease Detection Project:
1. Clone this repository to your local machine.
2. Install the required dependencies listed in the 'requirements.txt' file.
3. Explore the provided python scripts or notebooks 'detector.py' and 'parkinsons_disease_detection_project.ipynb' for model training.
4. Run the file 'app.py' to create a web app for the Parkinson's Disease Detector using the model trained in 'detector.py'


## Data Set Characteristics
- **Type**: Multivariate
- **Number of Instances**: 197
- **Area**: Life
- **Attribute Characteristics**: Real
- **Number of Attributes**: 23
- **Date Donated**: 2008-06-26
- **Associated Tasks**: Classification
- **Missing Values**: N/A

## Source
The dataset was created by Max Little of the University of Oxford, in collaboration with the National Centre for Voice and Speech, Denver, Colorado, who recorded the speech signals. The original study published the feature extraction methods for general voice disorders.

## Data Set Information
This dataset consists of a range of biomedical voice measurements from 31 people, 23 of whom have Parkinson's disease (PD). Each column in the table represents a particular voice measure, and each row corresponds to one of 195 voice recordings from these individuals. The main aim of the data is to discriminate healthy people from those with PD, based on the "status" column, which is set to 0 for healthy and 1 for PD. The data is provided in ASCII CSV format, with each row containing an instance corresponding to one voice recording. There are approximately six recordings per patient, with the patient's name identified in the first column.

For further information or to provide feedback, please contact Max Little (littlem '@' robots.ox.ac.uk).

Further details are contained in the following reference:
- Max A. Little, Patrick E. McSharry, Eric J. Hunter, Lorraine O. Ramig (2008), 'Suitability of dysphonia measurements for telemonitoring of Parkinson's disease', IEEE Transactions on Biomedical Engineering (to appear).

## Attribute Information
The dataset includes the following attributes:
- **name**: ASCII subject name and recording number
- **MDVP:Fo(Hz)**: Average vocal fundamental frequency
- **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency
- **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency
- **MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP**: Several measures of variation in fundamental frequency
- **MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA**: Several measures of variation in amplitude
- **NHR,HNR**: Two measures of the ratio of noise to tonal components in the voice
- **status**: Health status of the subject (1 for Parkinson's, 0 for healthy)
- **RPDE,D2**: Two nonlinear dynamical complexity measures
- **DFA**: Signal fractal scaling exponent
- **spread1,spread2,PPE**: Three nonlinear measures of fundamental frequency variation

## Citation Request
If you use this dataset, please cite the following paper: 
- 'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. BioMedical Engineering OnLine 2007, 6:23 (26 June 2007)

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

