#from cgitb import text
import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!!'
"""
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
"""
#st.write(df)

#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

#st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```

"""

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']
#)
#st.map(df)

st.write('Interactive Widgets')

#    if st.checkbox('Show Image'):
#        img = Image.open('google.jpeg')
#        st.image(img,caption='Google',use_column_width=True)

left_column, mid_column, right_column = st.columns(3)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

button2 = mid_column.button('中央カラムに文字を表示')
if button2:
    mid_column.write('ここは中央カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
expander3.image('google.jpeg')

#    text = st.text_input('あなたの趣味をおしえてください。')
#    'あなたの趣味は,',text, 'です。'

#    condition = st.slider('あなたの今の調子は？',0,100,70)
#    'コンディション：', condition