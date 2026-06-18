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

# --- 🛠️ エラーの原因だったCSSを削除し、安全な設定に変更 ---
# アプリのタイトル（htmlを使って直接中央寄せにします）
st.markdown("<h1 style='text-align: center;'>🦑 スプラ3 武器ルーレット 🐙</h1>", unsafe_with_html=True)
st.markdown("<p style='text-align: center;'>ボタンを押すと、画像付きでブキがランダムに選ばれるよ！</p>", unsafe_with_html=True)

# ブキが1つも見つからない場合の警告
if not weapons:
    st.error("images フォルダの中に画像が見つかりません。ファイル名を確認してください。")
else:
    # 左右に空のスペースを作り、中央の「列」にボタンや画像を配置することで中央寄せにします
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # ルーレットボタン
        if st.button("ルーレットを回す！", use_container_width=True):
            placeholder_text = st.empty()
            
            # パラパラ切り替わるアニメーション（演出用）
            for i in range(10):
                temp_weapon = random.choice(weapons)
                placeholder_text.markdown(f"<h3 style='text-align: center;'>🎲 {temp_weapon}</h3>", unsafe_with_html=True)
                time.sleep(0.08)
            
            # 最終的な武器を決定
            final_weapon = random.choice(weapons)
            
            # 決定したブキの名前を表示（中央寄せ）
            placeholder_text.markdown(f"<h2 style='text-align: center;'>🎉 決定: 【 {final_weapon} 】 🎉</h2>", unsafe_with_html=True)
            
            # 決定したブキの名前に対応する画像を検索
            actual_file = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[0] == final_weapon][0]
            image_path = os.path.join(IMAGE_DIR, actual_file)
            
            # 画像を画面に表示（列の中に配置されるので自動で中央寄りになります）
            st.image(image_path, use_container_width=True)