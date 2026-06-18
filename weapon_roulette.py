import streamlit as st
import random
import time
import os

# 1. imagesフォルダの中にある画像ファイルを自動で読み込む
IMAGE_DIR = "images"

# フォルダが存在し、中にファイルがあるか確認
if os.path.exists(IMAGE_DIR):
    # フォルダ内のファイル名から、ブキの名前リストを自動作成
    # (例: "スプラシューター.png" から ".png" を消して "スプラシューター" にする)
    weapons = [
        os.path.splitext(f)[0] 
        for f in os.listdir(IMAGE_DIR) 
        if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))
    ]
else:
    weapons = []

# アプリのタイトル
st.title("スプラ3 武器ルーレット")
st.write("ボタンを押すと、画像付きでブキがランダムに選ばれるよ！")

# ブキが1つも見つからない場合の警告
if not weapons:
    st.error("images フォルダの中に画像が見つかりません。ファイル名を確認してください。")
else:
    # ルーレットは何回でも押せるように st.button を配置
    if st.button("ルーレットを回す！"):
        placeholder_text = st.empty()
        placeholder_image = st.empty()
        
        # パラパラ切り替わるアニメーション（演出用）
        for i in range(10):
            temp_weapon = random.choice(weapons)
            placeholder_text.markdown(f"### 🎲 {temp_weapon}")
            
            # 演出中は画像なし、または簡易表示（今回はテキストのみ高速切り替え）
            time.sleep(0.08)
        
        # 最終的な武器を決定
        final_weapon = random.choice(weapons)
        
        # 決定したブキの名前を表示
        placeholder_text.markdown(f"## 🎉【 {final_weapon} 】 🎉")
        
        # 2. 決定したブキの名前に対応する画像を自動で探して表示
        # フォルダ内にある実際のファイル名を検索
        actual_file = [f for f in os.listdir(IMAGE_DIR) if os.path.splitext(f)[0] == final_weapon][0]
        image_path = os.path.join(IMAGE_DIR, actual_file)
        
        # 画像を画面に表示（横幅を200ピクセルに指定）
        st.image(image_path, width=200)
        st.success(f"今回のブキは「{final_weapon}」に決定！")