from turtle import width
from click import option
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('さおたのパイソニスト超入門')

# streamlitのリファレンス
# https://docs.streamlit.io/

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

'Done!!!!!'

st.write('DataFrame')

df = pd.DataFrame({
  '1列目': [1,2,3,4],
  '2列目': [10,20,30,40]
})

st.write(df)

# 動的な表(ソートができる)
# 縦と横の引数を指定できる
# highlight_max→一番大きい値をハイライト
# axis→0=列、1=行
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

# 静的な表(ソートができない)
st.table(df.style.highlight_max(axis=0))

# マジックコマンド
# マークダウン記法が適用できる
"""
# 章
## 節
### 項
``` python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)

# 折れ線グラフ
st.line_chart(df2)

# 折れ線グラフのエリアを塗ってる
st.area_chart(df2)

# 棒グラフ
st.bar_chart(df2)

df3 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)

st.map(df3)

# インタラクティブなウィジット
# https://docs.streamlit.io/library/api-reference/widgets
st.write('Interactive Widgets')

st.write('Display Image')

# checkboxはcheckが入っていたらtrue、checkが入っていなかったらfalseを返す
if st.checkbox('Show Image'):
  img = Image.open('noimage-760x460.png')
  # use_column_width→画面の横幅に合わせて表示
  st.image(img, caption='NoImage', use_column_width=True)

# 動的な値をoptionという変数に入れる
option = st.selectbox(
  'あなたの好きな数字は？',
  list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'

# st.sidebar

# text = st.sidebar.text_input('あなたの趣味は？')
# slider→最小値,最大値,デフォルト値
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

# Please replace st.beta_columns with st.columns.
# st.beta_columns will be removed after 2021-11-02.

left_column, right_colunm = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_colunm.write('ここは右カラム')

# Please replace st.beta_expander with st.expander.
# st.beta_expander will be removed after 2021-11-02.

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
