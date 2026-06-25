import streamlit as st
from backend.database.feedback import save_feedback, get_recent_feedback


def feedback_page():
    st.title("💬 Feedback")

    st.write(
        "We’d love to hear your thoughts about this project. "
        "Your feedback helps us improve."
    )

    # ================= FEEDBACK FORM =================
    with st.form("feedback_form"):
        name = st.text_input("Name (optional)")
        email = st.text_input("Email (optional)")

        st.info("Use the slider to give a rating.")
        rating = st.slider("Rating", min_value=1, max_value=5, value=5)

        message = st.text_area("Your Feedback (comments)", height=120)

        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            if not message.strip():
                st.error("Feedback message cannot be empty.")
            elif email and "@" not in email:
                st.error("Please enter a valid email address.")
            else:
                st.success(
    "Thank you for your feedback! (Local demo mode - feedback is not being stored.)"
)

    st.divider()

    # ================= RECENT FEEDBACK =================
st.subheader("What others are saying")

st.info(
    "Community feedback is unavailable in the local version because MongoDB is not configured."
)