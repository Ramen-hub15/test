import streamlit as st
import random
import time
import os

# 1. imagesフォルダの中にある画像ファイルを自動で読み込む
IMAGE_DIR = "images"

if os.path.exists(IMAGE_DIR):
    weapons = [
        os.path.splitext(f)[0] 
        for f in os.listdir(IMAGE_DIR) 
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))
    ]
else:
    weapons = []

# --- 🎨 画面全体の要素を中央寄せにし、不要なボタンを消す魔法のCSS ---
st.markdown("""
    <style>
        /* タイトルやテキスト、ボタンなど全ての要素を中央寄せにする */
        .block-container, .stButton, div[data-testid="stMarkdownContainer"] {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        /* 文章にカーソルを合わせたときに出るリンク・コピーボタンを非表示にする */
        button[data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        .css-v37955 a, a {
            display: none !important;
        }
        
        /* 画像の全画面表示（拡大）ボタンを非表示にする */
        button[data-testid="stImageFullscreenButton"] {
            display: none !important;
        }
    </style>
""", unsafe_with_html=True)
# -------------------------------------------------------------

# アプリのタイトル（中央寄せになります）
st.title("スプラ3 武器ルーレット")
st.write("ボタンを押すと、画像付きでブキがランダムに選ばれるよ！")

# ブキが1つも見つからない場合の警告
if not weapons:
    st.error("images フォルダの中に画像が見つかりません。ファイル名を確認してください。")
else:
    # ルーレットボタン（中央寄せになります）
    if st.button("ルーレットを回す！"):
        placeholder_text = st.empty()
        placeholder_image = st.empty()
        
        # パラパラ切り替わるアニメーション（演出用）
        for i in range(10):
            temp_weapon = random.choice(weapons)
            placeholder_text.markdown(f"### 🎲 {temp_weapon}")
            time.sleep(0.08)
        
        # 最終的な武器を決定
        final_weapon = random.choice(weapons)
        
        # 決定したブキの名前を表示（中央寄せ）
        placeholder_text.markdown(f"## 【 {final_weapon} 】")
        
        # 決定したブキの名前に対応する画像を検索
        actual_file = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[0] == final_weapon][0]
        image_path = os.path.join(IMAGE_DIR, actual_file)
        
        # 画像を画面に表示（中央寄せ、横幅200ピクセル）
        st.image(image_path, width=200)