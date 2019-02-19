# 入力文字列が pangram (アルファベット a ~ z (大小関係無し) を全て一回以上使った文) であるかを判定する
def is_pangram(sentence):
    # 1. 大文字を小文字に変換
    sentence = sentence.lower()
    # 2. アルファベットの出現回数を記録する辞書を作成
    alphabets = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    # 3. pangram かどうかの判定用の変数を定義
    judge = 1

    # 4. 文字列を先頭から見て, アルファベットであれば辞書の value をインクリメント
    for s in sentence:
        if(s in alphabets.keys()):
            alphabets[s] += 1
    
    # 5. 辞書の value を全て掛け合わせ, judge に代入
    for key in alphabets:
        judge *= alphabets[key]

    # 6. judge が 1 以上で True (アルファベット全ての出現回数が 1 以上である)
    return 0 < judge