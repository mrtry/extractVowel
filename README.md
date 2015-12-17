# extractFormant

## Description
- 音声データから歌唱フォルマントを持つフレームを抽出するプログラム

## Usage
- python app.py {wavFile}

## Construct
- **app.py**
    実行ファイル
- **cmd.py**
    ファイル操作のAPI的なもの
- **frame.py**
    wavデータを分割
- **formant.py**
    歌唱フォルマントの有無を判別
- **lpc.py**
    線形予測法
- **levinson_durbin.py**
    線形予測法に使う計算アルゴリズム


## Tools
- [SPTK](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjdmfLVleLJAhUBKqYKHfvMDv8QFggjMAE&url=http%3A%2F%2Fsp-tk.sourceforge.net%2F&usg=AFQjCNEGK_dTaLv3vwhuzngn9HPIalvNNg&sig2=frn8E5dEsnqB75gKFRfcnw)が必要です
    - raw2wav
    - wav2raw
    - bcut

## Homage
- [LPCの実装](http://aidiary.hatenablog.com/entry/20120415/1334458954)
- [母音区間推定法](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://www.splab.net/papers/2010/2010_17.pdf)
