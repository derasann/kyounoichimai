import streamlit as st
from PIL import Image
import os

st.title('今日の一枚')

# 「開く」ボタンが押されたら、写真を表示する
if st.button('開く'):
    # 画像が保存されているフォルダのパス
    folder_path = '/Users/onoderakyoko/03112024/'

    # フォルダ内の写真ファイルのリストを取得
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    # フォルダ内の最初の写真を表示
    if len(image_files) > 0:
        # 写真のパス
        image_path = os.path.join(folder_path, image_files[0])
        # PILを使用して画像を開く
        pil_image = Image.open(image_path)
        # 写真を表示
        st.image(pil_image, caption='まいうー', use_column_width=True)
    else:
        st.write('フォルダ内に写真が見つかりませんでしたよ。')




# source venv/bin/activate  1. 仮想環境に入る
# cd /Users/onoderakyoko/03112024/   2.ディレクトリに移動
# streamlit run app.py   3.ひらく
# コントロール + C  4. 止める 
# 画像を選択し、上の「編集」からオプションを押して　（オプション+コマンド+C）  4. パスをコピー　

#github は@derasann, tcore8599
#kyonodera@gmail.com , github.com/derasann

#バージョンは pip show パッケージ名　で見る。streamlit は Version: 1.32.0  pillow は　ersion: 10.2.0