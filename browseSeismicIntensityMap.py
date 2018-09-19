# -*- coding:utf-8 -*-
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
      36.6 degrees north latitude, 137.9 degrees east longitude as notation by Japanese.
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

"""

import os
import sys
import re

import tkinter as tk
import webbrowser

import pyperclip

class ClipBoard():
    """
    read the text content of the current clipboard, 
    or paste the new text contents and update the contents
    [現在のクリップボードのテキスト内容を読む、ないし新たなテキスト内容を貼り付け内容を更新する]
    """

    def get(self):
        return (str(pyperclip.paste()))

    # def set(self, past_text):
    #     pyperclip.copy(past_text)

class ExtractEpiCenter():
    """
    extract gps data of epicenter from clipboard content
    [クリップボード内容から震源のgpsデータを抽出する]
    """

    def get(self, soc):
        self.soc = soc
        self.epi_center = ""
        self.types = False

        # epicenter information by Nippon Meteorological Agency
        # [気象庁]
        # [北緯４０．４度、東経１４２．３度）]
        m = re.search(r'（([^）]+)）', self.soc)
        if (m):
            self.epi_center = m.group(0)
            return (self.epi_center)

        # epicenter information by Japan Broadcasting Corporation
        # NHK
        # 震源 / 深さ
        if (self.types == False):
            m = re.search(r'緯度 / 経度(.+)\r\n', self.soc)
            if (m):
                self.epi_center = m.group(0)
                self.epi_center = self.epi_center.replace('緯度 / 経度', '')
                self.epi_center = self.epi_center.replace(' \t', '')
                self.epi_center = self.epi_center.replace('\r\n', '')
                return (self.epi_center)

        # epicenter information USGS Latest Earthquakes
        #     58.729°N 158.697°E
        if (self.types == False):
            m = re.search(r'\s+([0-9.]+°[NSns]\s+[0-9.]+°[EWew])',
                          self.soc)
            if (m):
                self.epi_center = m.group(0)
                self.epi_center = self.epi_center.replace('\r\n    ', '')
                return (self.epi_center)
        return ("")

class EpicenterMap():
    """
    map browsing at specified gps
    [指定のgpsにてMapブラウジングする]
    """
    def brows(self, gps):
        url = "https://maps.google.com/maps/place/" + gps + "?hl=en"
        webbrowser.open(url, new=0, autoraise=True)

class Application(tk.Frame):
    """
    tkinter frame
    """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        # set widgets to use
        self.create_widgets()

        # construct the classes to use
        self.clip_board = ClipBoard()
        self.extract_epicenter = ExtractEpiCenter()
        self.epicenter_map = EpicenterMap()

        # set clip information immediately after invoke
        self.setup_for_prerequisit()

    def create_widgets(self):
        """
            make tkinter widgets, and map them
        """
        # make tkinter widgets
        self.gps_lbl = tk.Label(self, text="epicenter: ")
        self.gps_txt = tk.Text(self, width=40, height=1)
        self.is_gps_lbl = tk.Label(self, text="This may be: ")
        self.is_gps_txt = tk.Text(self, width=40, height=1)
        self.go = tk.Button(self, text="map epicenter",
                            command=self.push_map_epicenter)
        self.seismic_info = tk.Text(self, width=80, height=60)

        # map tkinter widgets
        self.gps_lbl.grid(column=0, row=0)
        self.gps_txt.grid(column=1, row=0)
        self.is_gps_lbl.grid(column=0, row=1)
        self.is_gps_txt.grid(column=1, row=1)
        self.go.grid(column=2, row=1)
        self.seismic_info.grid(column=0, columnspan=3, row=2)

    def map_clip(self, clip_text):
        """
            set information on the epicenter from clip board
        """
        self.clip_text = clip_text
        self.seismic_info.delete('1.0', 'end')
        self.seismic_info.insert(tk.INSERT, self.clip_text)

    def map_is_gps(self, epicenter_text):
        """
            estimated epicenter information part(e.g gps) is set up
        """
        self.epicenter_text = epicenter_text
        self.is_gps_txt.delete('1.0', 'end')
        self.is_gps_txt.insert(tk.INSERT, self.epicenter_text)

    def setup_for_prerequisit(self):
        """
            get and set clip information
        """
        self.clip_text = self.clip_board.get()
        self.epicenter_text = self.extract_epicenter.get(self.clip_text)

        self.map_clip(self.clip_text)
        self.map_is_gps(self.epicenter_text)

    def get_real_gps_by_is_gps(self, gps):
        """
            replace gps format with us type
        """
        self.gps = gps;
        self.simple_re_dict = {
            "（": "",
            "度": "",
            "°": "",
            "、": "",
            "/": "",
            "）": "",
            "北緯": "n",
            "南緯": "s",
            "東経": " e",
            "西経": " w",
            "．": ".",
            "０": "0",
            "１": "1",
            "２": "2",
            "３": "3",
            "４": "4",
            "５": "5",
            "６": "6",
            "７": "7",
            "８": "8",
            "９": "9",
        }
        try:
            for k in self.simple_re_dict:
                v = self.simple_re_dict[k]
                self.gps = self.gps.replace(k, v)
            return(self.gps)
        except ValueError:
            pass

    def log_out(self):
        """
           output log to console
        """
        print("epicenter: " + self.to_gps)
        print("This may be: " + self.is_gps_txt.get('1.0', 'end'))
        print("各地の震度に関する情報\n")
        print(self.seismic_info.get('1.0', 'end'))

    def push_map_epicenter(self):
        """
            behavior when 'map_epicenter' button is pressed
        """
        # set clip information immediately
        # when 'map_epicenter' button is pressed
        self.setup_for_prerequisit()

        # set contents of "This may be: "
        self.to_gps = self.is_gps_txt.get('1.0', 'end')
        self.to_gps = self.get_real_gps_by_is_gps(self.to_gps)

        # set contents of "epicenter: "
        self.gps_txt.delete('1.0', 'end')
        self.gps_txt.insert(tk.INSERT, self.to_gps)

        # output log to console
        self.log_out()

        # map browsing at specified gps
        self.epicenter_map.brows(self.to_gps)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("各地の震度に関する情報")
    app = Application(master=root)
    app.mainloop()
