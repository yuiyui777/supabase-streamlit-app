# Supabase-Streamlit アプリケーション

SupabaseとStreamlitを使用したWebアプリケーション

## 環境構築

1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

2. 環境変数の設定:
`.env`ファイルを作成し、以下の内容を設定してください：
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

3. アプリケーションの起動:
```bash
streamlit run app.py
```