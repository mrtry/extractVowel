# extractFormant

## Description
- 音声データから歌唱フォルマントを持つフレームを抽出するプログラム

## Usage
`python app.py {wavFile}`

## Input/Output
### Input
- WavFile
- 16bit/16kHz想定

### Output
- splitedRaw
    - 入力された`wav`を`raw`に変換,以下の基準で分割
    - 4,000 Sample/frame, 2,000 Sample/Shift

- splitedWav
    - 分割した`raw`を`wav`に変換したもの
    - 変換後、母音と子音とでディレクリに割り振る

- graph
    - 分割されたフレームの周波数解析したものと、LPCスペクトラム包絡のグラフ
    - 母音と子音とでディレクトリに割り振っている

## Construct
- **app.py**
    - 実行ファイル

    - **module/cmd.py**
        - ファイル操作のAPI的なもの
    - **module/frame.py**
        - データを分割
    - **module/formant.py**
        - 歌唱フォルマントの有無を判別
    - **module/lpc.py**
        - 線形予測法
    - **module/levinson_durbin.py**
        - 線形予測法に使う計算アルゴリズム

## Tools
- [SPTK](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjdmfLVleLJAhUBKqYKHfvMDv8QFggjMAE&url=http%3A%2F%2Fsp-tk.sourceforge.net%2F&usg=AFQjCNEGK_dTaLv3vwhuzngn9HPIalvNNg&sig2=frn8E5dEsnqB75gKFRfcnw)が必要
    - raw2wav
    - wav2raw
    - bcut

## Homage
- [LPCの実装](http://aidiary.hatenablog.com/entry/20120415/1334458954)
- [母音区間推定法](http://www.splab.net/papers/2010/2010_17.pdf)

