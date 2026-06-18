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

# --- 🛠️ エラーの元だったHTML(st.markdown)を完全に排除！ ---

# 画面を「左・真ん中・右」に3分割する（比率を 1:3:1 にして真ん中を広くします）
left_space, center_content, right_space = st.columns([1, 3, 1])

# すべての要素を「真ん中のエリア（center_content）」の中に配置します
with center_content:
    
    # タイトルと説明文（Streamlit標準の st.title と st.write を使用）
    st.title("スプラ3 ルーレットでブキを決めるマン")
    st.write("ボタンを押すと、ブキがランダムに選ばれるよ！")
    
    # ブキが1つも見つからない場合の警告
    if not weapons:
        st.error("製作者が何かをミスっています、文句言ってやってください。")
    else:
        # ルーレットボタン（use_container_width=True で真ん中のエリアいっぱいに広げます）
        if st.button("ルーレットを回す！", use_container_width=True):
            placeholder_text = st.empty()
            
            # パラパラ切り替わるアニメーション（演出用）
            for i in range(10):
                temp_weapon = random.choice(weapons)
                placeholder_text.header(f"🎲 {temp_weapon}")
                time.sleep(0.08)
            
            # 最終的な武器を決定
            final_weapon = random.choice(weapons)
            
            # 決定したブキの名前を表示（st.header を使用）
            placeholder_text.header(f"【 {final_weapon} 】")
            
            # 決定したブキの名前に対応する画像を検索
            actual_file = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[0] == final_weapon][0]
            image_path = os.path.join(IMAGE_DIR, actual_file)
            
            # 画像を画面に表示（use_container_width=True でエリア幅に自動で合わせます）
            st.image(image_path, use_container_width=True)