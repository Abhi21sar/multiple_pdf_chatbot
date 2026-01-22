import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            background-color: #f8f9fa;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e9ecef;
        }
        
        /* Chat message styling */
        .chat-container {
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .user-message {
            background-color: #007bff;
            color: white;
            align-self: flex-end;
            margin-left: 20%;
        }
        
        .bot-message {
            background-color: #ffffff;
            color: #212529;
            align-self: flex-start;
            margin-right: 20%;
            border: 1px solid #dee2e6;
        }
        
        /* Custom buttons */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
            background-color: #007bff;
            color: white;
            font-weight: 500;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #0056b3;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Header styling */
        h1 {
            color: #1a1e21;
            font-weight: 700 !important;
        }
        
        h3 {
            color: #495057;
            font-weight: 600 !important;
        }
        
        /* Avatar placeholder */
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 12px;
            display: inline-block;
            vertical-align: middle;
        }
        
        .user-avatar { background-color: #007bff; }
        .bot-avatar { background-color: #343a40; }
        </style>
    """, unsafe_allow_html=True)

bot_template = """
<div class="chat-container bot-message">
    <div style="display: flex; align-items: flex-start;">
        <div class="avatar bot-avatar"></div>
        <div style="flex-grow: 1;">
            <strong>Assistant</strong><br>
            {{MSG}}
        </div>
    </div>
</div>
"""

user_template = """
<div class="chat-container user-message">
    <div style="display: flex; align-items: flex-start; flex-direction: row-reverse;">
        <div class="avatar user-avatar"></div>
        <div style="flex-grow: 1; text-align: right; margin-right: 12px;">
            <strong>You</strong><br>
            {{MSG}}
        </div>
    </div>
</div>
"""
