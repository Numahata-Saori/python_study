from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('さおたのパイソニスト超入門')

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

st.write('画像表示')

img = Image.open('noimage-760x460.png')
# use_column_width→画面の横幅に合わせて表示
st.image(img, caption='NoImage', use_column_width=True)
