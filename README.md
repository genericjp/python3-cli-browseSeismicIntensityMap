# python3-cli-browseSeismicIntensityMap
browseSeismicIntensityMap

# python browseSeismicIntensityMap.py

"""
    Browse GoogleMap (us)
    from the information on the seismic intensity of the earthquake
    [地震の震度に関する情報からGoogleMap（us）をブラウズする]

    It is used for the following three patterns...
    [下記の3パタンに対応する。]

      1) Earthquake information by Nippon Meteorological Agency
            (Information on seismic intensity of each place)
              http://www.jma.go.jp/jp/quake/quake_local_index.html
              [日本気象庁による地震情報（各地の震度に関する情報）]

       proof:

        epicenter: n42.7 e141.9
        This may be: （北緯４２．７度、東経１４１．９度）

        各地の震度に関する情報
        平成３０年　９月１５日０４時３０分　気象庁発表

        １５日０４時２７分ころ、地震がありました。
        震源地は、胆振地方中東部（北緯４２．７度、東経１４１．９度）で、
        震源の深さは約１０ｋｍ、地震の規模（マグニチュード）は２．７と推定されます。
        この地震による津波の心配はありません。

        この地震により観測された最大震度は１です。

        ［ 震度１以上が観測された地点］
         ＊印は気象庁以外の震度観測点についての情報です。

         北海道　　震度１　　厚真町鹿沼　厚真町京町＊　安平町早来北進＊

      2) Information on earthquakes by NHK (Japan Broadcasting Corporation)
              https://www3.nhk.or.jp/sokuho/jishin/
              [NHK（日本放送協会）の地震に関する情報]

       proof:

        epicenter: n 42.7     e 141.9
        This may be: 北緯 42.7度  /  東経 141.9度

        各地の震度に関する情報
        2018年9月15日　4時27分ごろ　北海道胆振地方中東部
        概況
          ...
        地震に関する情報
        震源 / 深さ     北海道胆振地方中東部  /  10km
        緯度 / 経度     北緯 42.7度  /  東経 141.9度
        マグニチュード     2.7
        震度 1    厚真町　安平町

      3) USGS Latest Earthquakes
               https://earthquake.usgs.gov/earthquakes/map/

       proof:

         epicenter: 42.588N 141.977E
         This may be: 42.588°N 141.977°E

         M 4.3 - 31km E of Tomakomai, Japan
         Time     2018-09-14 08:31:42 (UTC)
         Location 42.588°N 141.977°E
         Depth    35.0 km

    1. intention
       [動機、ないし意図]

      Earthquake hits the earthquake and seismic intensity, 
      but the information is also scrambled.
      I thought that I would like to grasp the situation roughly.
      [地震毎に震源・震度が気になるが情報もかき乱れる。出来たら、ざっくり状況を把握したいとの思い。]

      What I want to do: Google Maps (en) does not recognize the following.
      36.6 degrees north latitude, 137.9 degrees east longitude as notation as Japanese.
      Somehow, n 36.6 e 137.9, or not.
      [私のやりたい事：　Google Maps (en )では、（表記は日本語としては）下記を認識しない。
　　　　北緯３６．６度、東経１３７．９度、　なんとか、　n36.6 e137.9 と、ならないか]

    2. Prerequisites for using
        [使う上での前提条件]

      1) python 3 If possible install v 3.6 or later.
         However, considering when python 2 is already installed.
         [python3 出来れば　v3.6以降をインストール。
          但し、python2がインストール済みの場合の考慮すること]

          https://www.python.org/downloads/release/python-366/ is no problem

      2) Since clipboard operation is used, after installing python 3,
         execute the following command to acquire external library
         [クリップボード操作を使うのでpython3インストール後、
         外部ライブラリ取得のため、下記コマンドを行う]

          >pip install pyperclip

      3) How to use, (1) Select and clip information about the epicenter.
                     (2) Selection of other information even after startup 
                     　　　You can browse continuously if you clip.
         [使用方法は、（１）震源に関する情報を選択しクリップする。
                      （２）起動後も、他の情報を選択クリップすれば連続ブラウズできる。]

         By pressing "map epicenter", 
         you can browse with the clip information.
         [ボタン"map epicenter”を押下すればクリップ時の情報でブラウズできる]
 History
     2018/09/15 13:31 (JST,UTC+9h)  v1.0.1 by ShozoNamikawa
      1) Corrects deviating from python style guide 
         (mostly 80 lines violation). No functionarity change.
         [pythonスタイルガイドを逸脱する（多くは80行違反）を補正。機能変更なし。]
     2018/09/15 10:31 (JST,UTC+9h)  v1.0.0 by ShozoNamikawa
      1) 1st edition
