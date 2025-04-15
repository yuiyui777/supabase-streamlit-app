import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import Optional

# 環境変数の読み込み
load_dotenv()

# デバッグ情報の表示、suapbaseの接続確認のために一旦表示してます
st.write("環境変数の確認:")
st.write(f"SUPABASE_URL: {os.environ.get('SUPABASE_URL', 'Not found')}")
st.write(f"SUPABASE_KEY: {'Found' if os.environ.get('SUPABASE_KEY') else 'Not found'}")

# Supabaseクライアントの初期化
def get_supabase_client() -> Client:
    """Supabaseクライアントの初期化と取得"""
    url: str = os.environ.get("SUPABASE_URL", "")
    key: str = os.environ.get("SUPABASE_KEY", "")
    supabase: Client = create_client(url, key)
    return supabase

def sign_up(email: str, password: str):
    """ユーザー登録"""
    supabase = get_supabase_client()
    return supabase.auth.sign_up({"email": email, "password": password})

def sign_in(email: str, password: str):
    """ログイン"""
    supabase = get_supabase_client()
    return supabase.auth.sign_in_with_password({"email": email, "password": password})

def sign_out():
    """ログアウト"""
    supabase = get_supabase_client()
    supabase.auth.sign_out()
    st.session_state.clear()

def check_auth() -> bool:
    """認証状態のチェック"""
    return 'user' in st.session_state

def login_signup_page():
    """ログイン/サインアップページの表示"""
    st.title("ログイン / サインアップ")
    tab1, tab2 = st.tabs(["ログイン", "サインアップ"])
    
    with tab1:
        email = st.text_input("メールアドレス", key="login_email")
        password = st.text_input("パスワード", type="password", key="login_password")
        if st.button("ログイン"):
            try:
                res = sign_in(email, password)
                st.session_state.user = res.user
                st.success("ログインに成功しました")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"ログインに失敗しました: {str(e)}")

    with tab2:
        new_email = st.text_input("メールアドレス", key="signup_email")
        new_password = st.text_input("パスワード", type="password", key="signup_password")
        if st.button("サインアップ"):
            try:
                res = sign_up(new_email, new_password)
                st.success("アカウントが作成されました。メールを確認してアカウントを有効化してください。")
            except Exception as e:
                st.error(f"サインアップに失敗しました: {str(e)}")


def main():
    """アプリケーションのメイン処理"""
    if not check_auth():
        login_signup_page()
    else:
        main_app()

def main_app():
    """メインアプリケーションの表示"""
    st.title("メインアプリケーション")
    st.write(f"ようこそ、{st.session_state.user.email}さん！")

    menu = ["ホーム", "コンテンツ"]
    choice = st.sidebar.selectbox("メニュー", menu)

    if choice == "ホーム":
        st.subheader("ホーム")
        st.write("ホームページです。")
    elif choice == "コンテンツ":
        st.subheader("コンテンツ")
        st.write("ここにコンテンツを表示できます。")

    if st.sidebar.button("ログアウト"):
        sign_out()
        st.experimental_rerun()

if __name__ == "__main__":
    main()