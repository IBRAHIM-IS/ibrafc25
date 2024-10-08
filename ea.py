import streamlit as st
import pandas as pd
import numpy as np

# Streamlit app title and description
st.set_page_config(page_title="Role-Based Attribute Calculator", layout="centered")

# Add an image (local or online)
st.image('img.png', use_column_width=True)  # Replace with the path to your image

st.title('⚽ Role-Based Attribute Calculator')
st.markdown("""
This tool helps calculate weighted attribute values for different football positions based on key stats like 
**PAC (Pace)**, **SHO (Shooting)**, **PAS (Passing)**, **DRI (Dribbling)**, **DEF (Defense)**, **PHY (Physicality)**, and now **GK Stats**.
Select your role and input the corresponding stats to see the result.
""")

# Sidebar for input fields
st.sidebar.header('Input Player Details')

# Player details
player_name = st.sidebar.text_input('Player Name (اسم اللاعب)')
tshirt_number = st.sidebar.number_input('T-Shirt Number (رقم القميص)', min_value=1, max_value=99, step=1)
preferred_foot = st.sidebar.selectbox('Preferred Foot (القدم المفضلة)', options=['Right', 'Left'])

# Regular player attributes
st.sidebar.header('Input Player Attributes')

# PAC and its sub-attributes
st.sidebar.subheader('PAC (Pace)')
acceleration = st.sidebar.number_input('Acceleration (التسارع)', min_value=0, max_value=100, step=1)
sprint_speed = st.sidebar.number_input('Sprint Speed (سرعة الجري)', min_value=0, max_value=100, step=1)
pac = (acceleration + sprint_speed) / 2

# SHO and its sub-attributes
st.sidebar.subheader('SHO (Shooting)')
att_position = st.sidebar.number_input('Att. Position (التمركز الهجومي)', min_value=0, max_value=100, step=1)
finishing = st.sidebar.number_input('Finishing (الانهاء)', min_value=0, max_value=100, step=1)
shot_power = st.sidebar.number_input('Shot Power (التسديد القوي / باور شوت)', min_value=0, max_value=100, step=1)
long_shots = st.sidebar.number_input('Long Shots (التسديدات البعيدة)', min_value=0, max_value=100, step=1)
volleys = st.sidebar.number_input('Volleys (التسديدات الهوائية)', min_value=0, max_value=100, step=1)
penalties = st.sidebar.number_input('Penalties (البلنتيات)', min_value=0, max_value=100, step=1)
sho = (att_position + finishing + shot_power + long_shots + volleys + penalties) / 6

# PAS and its sub-attributes
st.sidebar.subheader('PAS (Passing)')
vision = st.sidebar.number_input('Vision (الرؤية)', min_value=0, max_value=100, step=1)
crossing = st.sidebar.number_input('Crossing (العرضيات)', min_value=0, max_value=100, step=1)
fk_accuracy = st.sidebar.number_input('FK Acc. (الركلات الحرة)', min_value=0, max_value=100, step=1)
short_pass = st.sidebar.number_input('Short Pass (التمرير القصير)', min_value=0, max_value=100, step=1)
long_pass = st.sidebar.number_input('Long Pass (التمرير الطويل)', min_value=0, max_value=100, step=1)
curve = st.sidebar.number_input('Curve (التقويس)', min_value=0, max_value=100, step=1)
pas = (vision + crossing + fk_accuracy + short_pass + long_pass + curve) / 6

# DRI and its sub-attributes
st.sidebar.subheader('DRI (Dribbling)')
agility = st.sidebar.number_input('Agility (الرشاقة)', min_value=0, max_value=100, step=1)
balance = st.sidebar.number_input('Balance (التوازن)', min_value=0, max_value=100, step=1)
reactions = st.sidebar.number_input('Reactions (ردود الافعال)', min_value=0, max_value=100, step=1)
ball_control = st.sidebar.number_input('Ball Control (التحكم بالكرة)', min_value=0, max_value=100, step=1)
dribbling = st.sidebar.number_input('Dribbling (المراوغة)', min_value=0, max_value=100, step=1)
composure = st.sidebar.number_input('Composure (الهدوء)', min_value=0, max_value=100, step=1)
dri = (agility + balance + reactions + ball_control + dribbling + composure) / 6

# DEF and its sub-attributes
st.sidebar.subheader('DEF (Defense)')
interceptions = st.sidebar.number_input('Interceptions (الاعتراضات)', min_value=0, max_value=100, step=1)
heading_accuracy = st.sidebar.number_input('Heading Acc. (دقة الرأسيات)', min_value=0, max_value=100, step=1)
def_aware = st.sidebar.number_input('Def. Aware (الوعي الدفاعي)', min_value=0, max_value=100, step=1)
stand_tackle = st.sidebar.number_input('Stand Tackle (التدخل وقوفا)', min_value=0, max_value=100, step=1)
slide_tackle = st.sidebar.number_input('Slide Tackle (التدخل بالزحلقة)', min_value=0, max_value=100, step=1)
def_ = (interceptions + heading_accuracy + def_aware + stand_tackle + slide_tackle) / 5

# PHY and its sub-attributes
st.sidebar.subheader('PHY (Physical)')
jumping = st.sidebar.number_input('Jumping (القفز)', min_value=0, max_value=100, step=1)
stamina = st.sidebar.number_input('Stamina (التحمل)', min_value=0, max_value=100, step=1)
strength = st.sidebar.number_input('Strength (القوة البدنية)', min_value=0, max_value=100, step=1)
aggression = st.sidebar.number_input('Aggression (العنف)', min_value=0, max_value=100, step=1)
phy = (jumping + stamina + strength + aggression) / 4

# GK specific attributes
st.sidebar.subheader('Goalkeeper Attributes')
gk_diving = st.sidebar.number_input('GK Diving', min_value=0, max_value=100, step=1)
gk_handling = st.sidebar.number_input('GK Handling', min_value=0, max_value=100, step=1)
gk_kicking = st.sidebar.number_input('GK Kicking', min_value=0, max_value=100, step=1)
gk_positioning = st.sidebar.number_input('GK Positioning', min_value=0, max_value=100, step=1)
gk_reflexes = st.sidebar.number_input('GK Reflexes', min_value=0, max_value=100, step=1)

# New columns for Weak Foot and Skill Move
st.sidebar.subheader('Additional Attributes')
weak_foot = st.sidebar.slider('Weak Foot Rating (out of 5)', min_value=1, max_value=5, step=1)
skill_move = st.sidebar.slider('Skill Move Rating (out of 5)', min_value=1, max_value=5, step=1)

# Define role weights using pandas DataFrame
role_weights = pd.DataFrame({
    'Role': ['CB', 'RB/LB', 'CM', 'CDM', 'CAM', 'RW/LW', 'ST', 'GK'],
    'PAC': [0.1, 0.2, 0.166, 0.15, 0.1, 0.35, 0.2, 0],
    'SHO': [0.1, 0.1, 0.166, 0.05, 0.2, 0.2, 0.35, 0],
    'PAS': [0.1, 0.2, 0.166, 0.2, 0.35, 0.15, 0.05, 0],
    'DRI': [0.1, 0.15, 0.166, 0.1, 0.25, 0.2, 0.2, 0],
    'DEF': [0.4, 0.3, 0.166, 0.35, 0.05, 0.05, 0.05, 0],
    'PHY': [0.2, 0.15, 0.166, 0.15, 0.05, 0.05, 0.15, 0],
    'GK Diving': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Handling': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Kicking': [0, 0, 0, 0, 0, 0, 0, 0.1],
    'GK Positioning': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Reflexes': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'Weak Foot': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    'Skill Move': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0]
})

# Store input attributes in a numpy array
attributes = np.array([pac, sho, pas, dri, def_, phy, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes, weak_foot, skill_move])

# Select the role from a dropdown
role = st.selectbox('Select Role', role_weights['Role'], index=2)  # Default to CM

# Get the corresponding row for the selected role
role_row = role_weights[role_weights['Role'] == role].iloc[:, 1:].values.flatten()

# Calculate the weighted value using numpy
weighted_value = np.dot(attributes, role_row)

# Display the weighted result with a styled message
st.markdown(f"""
### Calculated Attribute Value for **{role}**:
#### {weighted_value:.2f}
""")

# Display player details
st.markdown(f"**Player :** {player_name} | **T-Shirt Number :** {tshirt_number} | **Preferred Foot :** {preferred_foot}")

# Add a note for interpretation
st.info("The weighted value is calculated based on the specific priorities for each role. Adjust the attributes to explore different results.")
