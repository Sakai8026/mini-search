import streamlit as st
import json

def read_json_value(file_name, i):
  with open(f"{file_name}.json",'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    if i < len(data):
      return data[i]
    else:
      return None

def main():
  st.title('タグと単語の番号検索')

  selected_file = st.radio("対象を選択（青：tags / 緑：words）", ("tags", "words"))

  # ユーザーから数値を受け取る
  i = st.number_input('タグ番号を入力:', min_value=0, step=1)

  # JSONファイルから値を読み取る
  result = read_json_value(selected_file, int(i))

  # 結果を表示する
  if result is not None:
      st.success(f'{i}番タグ: {result}')
  else:
      st.error('指定された行は存在しません')



if __name__ == "__main__":
  main()
