import streamlit as st
import difflib

# --- EXPANDED SECURITY MEMORY STORAGE ---
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 5
if "blocked_list" not in st.session_state:
    st.session_state.blocked_list = []
if "human_error_logs" not in st.session_state:
    st.session_state.human_error_logs = []
if "account_locked" not in st.session_state:
    st.session_state.account_locked = False

# --- CENTRAL STORAGE SYSTEM SECRET ---
PASSWORD_CORRECT = "12345678"
USERNAME_CORRECT = "Admin"

# --- FUTURISTIC UI SIDEBAR DEFINITION (WITH COLOR & SYSTEM INFO) ---
st.sidebar.title("👁️‍🗨️ System Matrix")
st.sidebar.write("Welcome to the :blue[Next-Gen Cyber Security Matrix].")
st.sidebar.markdown("---")

# YOUR BRILLIANT IDEA: Showing the correct credentials inside the Sidebar for the judge
st.sidebar.subheader("🔑 Authorized System Credentials:")
st.sidebar.code(f"Username: {USERNAME_CORRECT}\nPassword: {PASSWORD_CORRECT}", language="text")
st.sidebar.markdown("---")

st.sidebar.info("💡 **Demo Guide / دليل التجربة:**\n1. Type standard random text to trigger :red[Instant Block].\n2. Type close variations to observe adaptive :orange[Human Leniency].")

# --- UI MAIN VISUAL HEADER & APP DEFINITION (WITH TEXT COLORS) ---
st.title("👁️‍🗨️ :blue[Smart Account Guardian]")
st.subheader("نظام حارس الحساب الذكي")
st.write("An advanced **Context-Aware Security Architecture** that monitors input patterns to mitigate brute-force risks :red[Instantly].")
st.write("نظام أمني مبتكر يقوم بتحليل سلوك المدخلات وتطبيق :red[الحظر الفوري] لحماية الحسابات.")
st.markdown("---")

# --- SMART PRE-EMPTIVE DEFENSE GATE ---
if st.session_state.account_locked:
    st.error("🔒 ACCESS DENIED: This account has been locked due to critical brute-force anomalies!")
    
    if st.sidebar.button("🚨 Emergency Unlock System"):
        st.session_state.attempts_left = 5
        st.session_state.blocked_list = []
        st.session_state.human_error_logs = []
        st.session_state.account_locked = False
        st.rerun()
else:
    # --- USER INTERFACE INPUT FIELDS ---
    username = st.text_input("👤 Username / Identity (اسم المستخدم):")
    user_input = st.text_input("🔑 Cryptographic Password (كلمة المرور):", type="password")

    # --- BRAIN LOGIC CYBER ENGINE ---
    if st.button("🔐 Initiate Secure Log In"):
        if user_input:
            similarity = difflib.SequenceMatcher(None, PASSWORD_CORRECT, user_input).ratio()
            similarity_percentage = similarity * 100
            
            st.info(f"📊 [Telemetry Data]: Password sequence match ratio is: :blue[{similarity_percentage:.1f}%]")
            
            # --- SECURITY DECISION TREE ---
            
            # CASE 1: MATCH 100%
            if user_input == PASSWORD_CORRECT and username == USERNAME_CORRECT:
                st.success(f"🔓 ACCESS GRANTED: Welcome back Commander, {username}! Mainframe initialized.")
                st.session_state.attempts_left = 5
                
            # CASE 2: MALICIOUS THREAT DETECTED (< 40%)
            elif similarity_percentage < 40.0:
                st.error("🚨 [CRITICAL THREAT]: Hostile activity detected! Random pattern matching indicates an automated brute-force attack. Connection dropped instantly.")
                st.session_state.blocked_list.append(user_input)
                st.session_state.account_locked = True
                st.rerun()
                
            # CASE 3: ADAPTIVE HUMAN TOLERANCE PROTOCOL (>= 40%)
            else:
                st.session_state.attempts_left -= 1
                st.session_state.human_error_logs.append(user_input)
                
                if st.session_state.attempts_left > 0:
                    st.warning(f"⚠️ [HUMAN LENIENCY PROMPTED]: Authentication failed. Input sequence shares significant similarity. Leniency Matrix active: :orange[{st.session_state.attempts_left} attempts remaining].")
                else:
                    st.error("🔒 SYSTEM INTRUSION WARNING: Maximum close tolerance levels exhausted! Perimeter secured and account locked.")
                    st.session_state.account_locked = True
                    st.rerun()
        else:
            st.warning("Input required: Please populate the cryptographic field to evaluate signature data.")

# --- INTEL ADMIN DASHBOARD VIEW ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
with st.expander("🛠️ Intelligence Command Dashboard (Behind the Scenes)"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛑 Intercepted Cyber Threats (Case 2):")
        if st.session_state.blocked_list:
            for idx, hacked_pass in enumerate(st.session_state.blocked_list, 1):
                st.write(f"**Threat ({idx}):** :red[Random Brute-force String] -> `{hacked_pass}`")
        else:
            st.write("Status: *No malicious patterns intercepted.*")
            
    with col2:
        st.subheader("⚠️ Logged Human Deviations (Case 3):")
        if st.session_state.human_error_logs:
            for idx, close_pass in enumerate(st.session_state.human_error_logs, 1):
                st.write(f"**Mistake ({idx}):** :orange[High-Similarity Text Input] -> `{close_pass}`")
        else:
            st.write("Status: *No human close errors logged.*")
            
    st.markdown("---")
    if st.button("🔄 Full Reset Security Module"):
        st.session_state.attempts_left = 5
        st.session_state.blocked_list = []
        st.session_state.human_error_logs = []
        st.session_state.account_locked = False
        st.rerun()
