import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import Optional

# 環境変数の読み込み
load_dotenv()

# Supabaseクライアントの初期化
def get_supabase_client() -> Client:
    """Supabaseクライアントの初期化と取得"""
    url: str = os.environ.get("SUPABASE_URL", "")
    key: str = os.environ.get("SUPABASE_KEY", "")
    supabase: Client = create_client(url, key)
    return supabase

# アプリケーションのメイン処理
def main():
    st.title("Supabase-Streamlit App")
    
    # Supabaseクライアントの取得
    try:
        supabase = get_supabase_client()
        st.success("Supabaseに接続しました")
    except Exception as e:
        st.error(f"Supabaseへの接続に失敗しました: {str(e)}")
        return

if __name__ == "__main__":
    main()