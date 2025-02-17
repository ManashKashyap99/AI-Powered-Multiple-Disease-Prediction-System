# -*- coding: utf-8 -*-
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('C:/Users/Manash/Desktop/DATAANALYSTPROJECT/Capstone/sav files/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Manash/Desktop/DATAANALYSTPROJECT/Capstone/sav files/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Manash/Desktop/DATAANALYSTPROJECT/Capstone/sav files/parkinsons_model.sav', 'rb'))

# Initialize session state for theme
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Theme-aware CSS
theme_css = f"""
<style>
    :root {{
        --primary-color: #2E86C1;
        --secondary-color: #148F77;
        --text-color: {'#ECF0F1' if st.session_state.dark_mode else '#2E4053'};
        --bg-color: {'#2C3E50' if st.session_state.dark_mode else '#FFFFFF'};
        --input-bg: {'#34495E' if st.session_state.dark_mode else '#FFFFFF'};
        --disclaimer-bg: {'#34495E' if st.session_state.dark_mode else '#F9E79F'};
    }}

    .header {{
        font-size: 24px !important;
        color: var(--primary-color) !important;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }}

    .section-title {{
        font-size: 20px !important;
        color: var(--secondary-color) !important;
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 5px;
        margin-top: 20px;
    }}

    .input-label {{
        font-weight: bold !important;
        color: var(--text-color) !important;
    }}

    .disclaimer {{
        background-color: var(--disclaimer-bg);
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
        font-size: 14px;
    }}

    html, body, .stApp {{
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }}

    .stNumberInput input, .stTextInput input, .stSelectbox select, .stTextArea textarea {{
        background-color: var(--input-bg) !important;
        color: var(--text-color) !important;
    }}

    .st-bd, .st-ae, .st-cb, .st-cc {{
        background-color: var(--bg-color) !important;
    }}

    .stSidebar {{
        background-color: {'#1A1A1A' if st.session_state.dark_mode else '#F0F2F6'} !important;
    }}

    .stButton>button {{
        background-color: {'#4A90E2' if st.session_state.dark_mode else '#2E86C1'} !important;
        color: white !important;
    }}
</style>
"""

st.markdown(theme_css, unsafe_allow_html=True)

# Dark theme fix
st.markdown("""
<style>
    /* Target all input labels */
    .stNumberInput label,
    .stTextInput label,
    .stSelectbox label,
    .stTextArea label {
        color: var(--text-color) !important;
        font-weight: bold !important;
    }

    /* Specific fix for Parkinson's grid labels */
    [data-testid="stHorizontalBlock"] label {
        color: var(--text-color) !important;
        font-size: 14px !important;
    }

    /* Ensure number input text remains visible */
    .stNumberInput input {
        color: var(--text-color) !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    # Theme toggle at the bottom of sidebar
    st.session_state.dark_mode = st.checkbox('🌓 Dark Mode', value=st.session_state.dark_mode)
    
    st.markdown('<div class="header">🔍 Multi Disease Prediction System Using Machine Learning</div>', unsafe_allow_html=True)
    selected = option_menu(
        'Menu',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['droplet', 'heart-pulse', 'person-bounding-box'],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "var(--bg-color)"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "color": "var(--text-color)"
            },
            "nav-link-selected": {"background-color": "var(--primary-color)"},
        }
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown('<div class="header">🩸 Diabetes Prediction Using Machine Learning</div>', unsafe_allow_html=True)
    st.markdown("**Please provide the following health metrics for diabetes risk assessment:**")
    
    with st.expander("Patient Information", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
            glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=300, step=1)
            blood_pressure = st.number_input('Blood Pressure (mmHg)', min_value=0, max_value=200, step=1)
            
        with col2:
            age = st.number_input('Age (years)', min_value=0, max_value=120, step=1)
            bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1)
            diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01)

    with st.expander("Advanced Metrics", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, step=1)
        with col2:
            insulin = st.number_input('Insulin Level (μU/mL)', min_value=0, max_value=900, step=1)

    if st.button('🔍 Analyze Diabetes Risk'):
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
        prediction = diabetes_model.predict(input_data)[0]
        
        if prediction == 1:
            st.error('⚠️ High risk of diabetes detected. Please consult a healthcare professional.')
        else:
            st.success('✅ No signs of diabetes detected. Maintain a healthy lifestyle!')

    st.markdown('<div class="disclaimer">⚠️ Note: This prediction is not a substitute for professional medical advice.</div>', unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown('<div class="header">❤️ Heart Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown("**Please provide cardiovascular health information:**")

    with st.expander("Personal Information", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input('Age (years)', min_value=0, max_value=120, step=1)
            sex = st.selectbox('Gender', options=[('Male', 0), ('Female', 1)], format_func=lambda x: x[0])[1]
        with col2:
            cp = st.selectbox('Chest Pain Type: 0=No pain | 1=Typical angina | 2=Atypical angina | 3=Non-anginal pain', options=[
                ('No pain', 0), 
                ('Typical angina', 1), 
                ('Atypical angina', 2), 
                ('Non-anginal pain', 3)
            ], format_func=lambda x: x[0])[1]

    with st.expander("Medical Metrics", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            trestbps = st.number_input('Resting BP (mmHg)', min_value=0, max_value=250, step=1)
            chol = st.number_input('Cholesterol (mg/dL)', min_value=0, max_value=600, step=1)
        with col2:
            fbs = st.selectbox('Fasting Blood Sugar > 120mg/dL | NO->0 | YES->1', options=[('No', 0), ('Yes', 1)], format_func=lambda x: x[0])[1]
            restecg = st.selectbox('Resting ECG | Normal-> 0 | ST-T wave abnormality-> 1 | Left ventricular hypertrophy->2 ', options=[
                ('Normal', 0),
                ('ST-T wave abnormality', 1),
                ('Left ventricular hypertrophy', 2)
            ], format_func=lambda x: x[0])[1]
        with col3:
            thalach = st.number_input('Max Heart Rate', min_value=0, max_value=220, step=1)
            exang = st.selectbox('Exercise Induced Angina | No->0 | Yes->1', options=[('No', 0), ('Yes', 1)], format_func=lambda x: x[0])[1]

    with st.expander("Advanced Parameters", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=10.0, step=0.1)
            slope = st.selectbox('ST Segment Slope | Upsloping-> 0 | Flat->1  | Downsloping->2', options=[('Upsloping', 0), ('Flat', 1), ('Downsloping', 2)], format_func=lambda x: x[0])[1]
        with col2:
            ca = st.number_input('Major Vessels', min_value=0, max_value=3, step=1)
            thal = st.selectbox('Thalassemia', options=[('0', 0), ('1', 1), ('2', 2),('3',3)], format_func=lambda x: x[0])[1]

    if st.button('🔍 Analyze Heart Disease Risk'):
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        prediction = heart_disease_model.predict(input_data)[0]
        
        if prediction == 1:
            st.error('⚠️ Potential heart disease detected. Please consult a cardiologist.')
        else:
            st.success('✅ No significant signs of heart disease detected.')

    st.markdown('<div class="disclaimer">⚠️ Note: Cardiovascular assessment should be performed by qualified professionals.</div>', unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.markdown('<div class="header">🧠 Parkinson\'s Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown("**Please provide voice measurement parameters:**")
    
    cols = st.columns(5)
    voice_metrics = {}
    with cols[0]:
        voice_metrics.update({
            'fo': st.number_input('MDVP:Fo(Hz)', min_value=0.0, format="%.3f"),
            'jitter_abs': st.number_input('Jitter(Abs)', min_value=0.00000, format="%.6f"),
            'shimmer': st.number_input('MDVP:Shimmer', min_value=0.00, format="%.5f"),
            'apq': st.number_input('MDVP:APQ', min_value=0.0000, format="%.5f"),
            'rpde': st.number_input('RPDE', min_value=0.0000, format="%.5f"),
            'd2': st.number_input('D2', format="%.6f")
        })
    
    with cols[1]:
        voice_metrics.update({
            'fhi': st.number_input('MDVP:Fhi(Hz)', min_value=0.0, format="%.3f"),
            'rap': st.number_input('RAP', min_value=0.0000, format="%.5f"),
            'shimmer_db': st.number_input('Shimmer(dB)', min_value=0.00, format="%.3f"),
            'dda': st.number_input('DDA', min_value=0.0000, format="%.5f"),
            'dfa': st.number_input('DFA', format="%.6f"),
            'ppe': st.number_input('PPE', format="%.6f")
        })
    
    with cols[2]:
        voice_metrics.update({
            'flo': st.number_input('MDVP:Flo(Hz)', min_value=0.0, format="%.3f"),
            'ppq': st.number_input('PPQ', min_value=0.0000, format="%.5f"),
            'apq3': st.number_input('Shimmer:APQ3', min_value=0.0000, format="%.5f"),
            'nhr': st.number_input('NHR', min_value=0.00000, format="%.5f"),
            'spread1': st.number_input('spread1', format="%.6f")     
        })
    
    with cols[3]:
        voice_metrics.update({
            'jitter_percent': st.number_input('Jitter(%)', min_value=0.00000, format="%.5f"),
            'ddp': st.number_input('Jitter:DDP', min_value=0.00000, format="%.5f"),
            'apq5': st.number_input('Shimmer:APQ5', min_value=0.0000, format="%.4f"),
            'hnr': st.number_input('HNR', min_value=0.00, format="%.3f"),
            'spread2': st.number_input('spread2', format="%.6f")
        })
    

    if st.button('🔍 Analyze Parkinson\'s Risk'):
        input_data = [list(voice_metrics.values())]
        prediction = parkinsons_model.predict(input_data)[0]
        
        if prediction == 1:
            st.error('⚠️ Potential Parkinson\'s markers detected. Neurological consultation recommended.')
        else:
            st.success('✅ No significant Parkinson\'s markers detected.')

    st.markdown('<div class="disclaimer">⚠️ Note: Voice analysis should be conducted by qualified specialists.</div>', unsafe_allow_html=True)