
import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Quest",
    page_icon="🎮",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #090d1b, #17132e, #101a32);
    color: white;
}

.block-container {
    max-width: 750px;
    padding-top: 2rem;
}

.game-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(90deg, #00e5ff, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #aab4d0;
    font-size: 17px;
    margin-bottom: 30px;
}

.game-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(168,85,247,0.4);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 25px rgba(124,58,237,0.12);
    margin-bottom: 20px;
}

.stat {
    background: #171d35;
    border: 1px solid #343b5b;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
}

.stat-label {
    color: #9ba8c7;
    font-size: 13px;
}

.stat-value {
    font-size: 28px;
    font-weight: bold;
    color: #00e5ff;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    height: 48px;
    font-size: 17px;
    font-weight: bold;
    transition: 0.2s;
}

div.stButton > button:hover {
    box-shadow: 0 0 18px #7c3aed;
    border: 1px solid #00e5ff;
    color: white;
}

div[data-testid="stNumberInput"] input {
    background: #171d35;
    color: white;
    border: 1px solid #555b82;
    border-radius: 10px;
}

.footer {
    text-align: center;
    color: #777f9d;
    font-size: 13px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- GAME INITIALIZATION ----------------
def new_game():
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.won = False
    st.session_state.message = "Your mission starts now. Make your first guess!"
    st.session_state.message_type = "info"


if "secret" not in st.session_state:
    new_game()


# ---------------- HEADER ----------------

st.markdown('<div class="game-title">⚡ NUMBER QUEST</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Think smart. Guess right. Beat the number.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="game-card">
    <h2>🎯 YOUR MISSION</h2>
    <p style="color:#aab4d0;">
        A secret number is hidden between
        <b style="color:#00e5ff;">1 and 100</b>.
        Can you find it?
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- STATISTICS ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="stat">
        <div class="stat-label">ATTEMPTS</div>
        <div class="stat-value">{st.session_state.attempts}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat">
        <div class="stat-label">NUMBER RANGE</div>
        <div class="stat-value">1 – 100</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# ---------------- GUESS INPUT ----------------
st.markdown("### 🔢 Enter your guess")

with st.form("guess_form"):
    guess = st.number_input(
        "Choose a number",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        disabled=st.session_state.won
    )

    submitted = st.form_submit_button(
        "🚀 SUBMIT GUESS",
        disabled=st.session_state.won
    )

    if submitted:
        st.session_state.attempts += 1

        if guess == st.session_state.secret:
            st.session_state.won = True
            st.session_state.message = (
                f"You found the secret number: {st.session_state.secret}!"
            )
            st.session_state.message_type = "success"

        elif guess > st.session_state.secret:
            st.session_state.message = "📈 TOO HIGH! Try a smaller number."
            st.session_state.message_type = "warning"

        else:
            st.session_state.message = "📉 TOO LOW! Try a bigger number."
            st.session_state.message_type = "info"


# ---------------- GAME FEEDBACK ----------------
if st.session_state.message_type == "success":
    st.balloons()
    st.success(st.session_state.message)
    st.markdown(
        f"### 🏆 You won in {st.session_state.attempts} attempts!"
    )

elif st.session_state.message_type == "warning":
    st.warning(st.session_state.message)

else:
    st.info(st.session_state.message)


# ---------------- RESTART ----------------
st.write("")

if st.button("🔄 NEW GAME", use_container_width=True):
    new_game()
    st.rerun()


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    NUMBER QUEST · Created by <b style="color:#00e5ff;">Birat Pandey</b><br>
    Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)

