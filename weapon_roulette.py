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

# --- 🛠️ ユーザーの邪魔になるコピーボタン・拡大ボタンを完全に非表示にする設定 ---
st.html(
    """
    <style>
        /* 文字にホバーしたときに出るコピーボタン（リンク）を完全に消す */
        button[data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        /* 画像の全画面表示ボタン（拡大マーク）を完全に消す */
        button[data-testid="stImageFullscreenButton"] {
            display: none !important;
        }
    </style>
    """
)
# ----------------------------------------------------------------------

# 画面を「左・真ん中・右」に3分割する（中央寄せのレイアウト）
left_space, center_content, right_space = st.columns([1, 3, 1])

# すべての要素を「真ん中のエリア」の中に配置
with center_content:
    
    st.title("スプラ3 ルーレットでブキを決めるマン")
    st.write("ボタンを押すと、ブキがランダムに選ばれるよ！")
    
    # ブキが1つも見つからない場合の警告
    if not weapons:
        st.error("製作者が何かを間違えています、文句言ってやってください。")
    else:
        # ルーレットボタン
        if st.button("ルーレットを回す！", use_container_width=True):
            placeholder_text = st.empty()
            
            # パラパラ切り替わるアニメーション（演出用）
            for i in range(10):
                temp_weapon = random.choice(weapons)
                placeholder_text.header(f"🎲{temp_weapon}🎲")
                time.sleep(0.08)
            
            # 最終的な武器を決定
            final_weapon = random.choice(weapons)
            
            # 決定したブキの名前を表示
            placeholder_text.header(final_weapon)
            
            # 決定したブキの名前に対応する画像を検索
            actual_file = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[0] == final_weapon][0]
            image_path = os.path.join(IMAGE_DIR, actual_file)
            
            # 画像を画面に表示
            st.image(image_path, use_container_width=True)