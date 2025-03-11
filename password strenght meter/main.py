import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase Letter": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"[0-9]", password)),
        "Special Character": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    
    # Calculate score
    score = sum(criteria.values())

    # Determine strength level
    if score == 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return score, strength, color, criteria

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input field
password = st.text_input("Enter your password:", type="password")

if password:
    score, strength, color, criteria = check_password_strength(password)

    # Display password strength
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:18px;'>{strength}</span>", unsafe_allow_html=True)

    # Progress bar
    st.progress(score / 5)

    # Show criteria check
    st.write("### ✅ Password Criteria")
    for key, value in criteria.items():
        st.write(f"- {'✅' if value else '❌'} {key}")

    if strength == "Weak":
        st.warning("⚠️ Your password is weak! Try adding uppercase, numbers, and special characters.")
    elif strength == "Moderate":
        st.info("ℹ️ Your password is okay but could be stronger.")
    else:
        st.success("🎉 Your password is strong!")

