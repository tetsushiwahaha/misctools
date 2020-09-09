# misctools

このリポジトリにはウエタ研の研究に必要な雑多なツールを置いておくことにす
る．適当な頻度で更新される．

## グラフ作成用スクリプト `plot_file.py` `plot_func.py`

コンセプトは，
* 再現可能
* 人の手を入れない
* PDF生成

である．（捏造にならない程度の）凝ったアレンジは，
生成したPDFに対してillustrator等を適用して実現する．しかし，
Python で念入りにコーディングすれば，
illustratorも要らないとは思う．

ところで以下の3つの図の違いが判るだろうか？

<img align="center" width="512" alt="a screen shot" src="https://user-images.githubusercontent.com/52724526/92588793-806f7c80-f2d4-11ea-87c8-5f35952fae34.png">
<img align="center" width="512" alt="a screen shot" src="https://user-images.githubusercontent.com/52724526/92586600-6b451e80-f2d1-11ea-833c-0495df82254d.png">
<img align="center" width="512" alt="a screen shot" src="https://user-images.githubusercontent.com/52724526/92589637-cbd65a80-f2d5-11ea-9606-e0a6eb22ceac.png">



### 必要なもの
* python 3.8 or later
	* matplotlib, numpy
* TeXLive 
	* `tlmgr` などで最新なパッケージと同期しておこう

### 準備
時系列データなどを計算してファイルに保存した場合，例えば，
```text
時刻0 状態1(0) 状態2(0) 状態3(0)
時刻1 状態1(1) 状態2(1) 状態3(1)
時刻2 状態1(2) 状態2(2) 状態3(2)
...
```
っと記録されることも多いだろう．このファイルを読み込み，グラフにする．
`autonomous_pp2` は，設定ファイルで`dump_data` を1に定義しておけばこの形
式のデータを書き出す．
* データのファイル名は `data.txt`としているが，ダサいので適当に変更して
くれたまえ
* フォント関係は LaTeX のものを使用する．掲載する論文が，TimesRoman 系な
らばこのまま利用すればよい（1つ目の図）．
ComputerModern 系であれば，`text.latex.preamble` の行をコメントアウトす
るとよい（2つ目の図）
内部でLaTeXを呼ぶので動作は極めて遅い．よって試行錯誤でさっさと
結果を見たい場合は，`plt.rcParams.update(params)` の行をコメントアウトし
て，LaTeX によるレンダリングをやめるとよい（3つ目の図）
* グラフのサイズは，論文に合わせて適切に設定する．縮小して論文に貼り込む
ならば，ラベルの数値なども小さくなるわけなので，十分目視できるフォントサ
イズを選んでおくこと．
* `params` で指定するフォントサイズなどの指定と，それ以下の`figure`や
`axes` で指定するサイズとのコンフリクトは，よく判らないので実験してみて
ほしい（分かったら教えて）．
* コメントアウトしてあるところは参考のために書いたオプションである．所望
の仕上がりイメージに合わせて取捨選択せよ．
* 画面にグラフを投影すると同時に，PDFとして書き出す．
* `plot_func.py` は，データをファイルから読み出す代わりに，
データに相当する`x_list`, `y_list` を関数で生成している．
詳細はコードを参照のこと（ほとんど`plot_file.py`と変わりは無い）．
* 以下に，`plot_file.py` のコードを示しておく(special thanks to 
Dr. Miino)：

```python
#!/usr/bin/env python 
'''
	Plotting data from a text file containing t, x(t), y(t)...
'''

import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages

params = {'text.usetex': True,
          'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize' :12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
         }
plt.rcParams.update(params)

x_list=[] 
y_list=[] 
fd = open('data.txt','rt') 	# specify appropriate data file here
for line in fd:
    data = line[:-1].split(' ')
    x_list.append(float(data[0]))
    y_list.append(float(data[1]))

fig = plt.figure(figsize = (5, 5/16*5)) 	# create a figure object
ax = fig.add_subplot(111)					# associate an axes object
fig.subplots_adjust(bottom=0.3)

# PLOT options 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

# AXES helpers
ax.set_xlabel(r'$t \longrightarrow$', fontsize=12)
ax.set_ylabel(r'$\varphi(t) \longrightarrow $', fontsize=12)
ax.set_xlim([0, x_list[-1]])
ax.set_ylim([-0.5, 0.5])

### DATA PLOTTING 
ax.plot(x_list, y_list, 
	label = r'$\varphi(t)$', color = 'BLUE', linewidth = 0.8)
#ax.plot(x_list, y_list) 
#ax.plot(x_list, y_list, color='RED',linewidth=4.0) 
#ax.plot(x_list, y_list, marker='o') 
#ax.plot(x_list, y_list,'o') 
#ax.hlines([y1,y2], xmin, xmax, linestyles="dashed")  

ax.legend(loc='best') # legend
#ax.legend(loc=0)
ax.grid(c='gainsboro', zorder=2)
#ax.grid(True)

# Publish a PDF in the same time.
#
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()
```
### 実行方法
```
% python plot_file.py
```

## スライド作成用テンプレート `slide.tex` 

### 必要なもの
* TeXLive を入れてあれば特に問題ない

### 使い方
* `slide.tex` を適当にエディットする．
* 発表用スライドにデザインされた，`beamer` というクラスを用いて，
2つのテーマ，`metropolis` および `focus` 用に例題を記述しておいた．
* コンパイルは `latexmk` を用いると楽だろう．`.latexmkrc` は例えば
以下とすればよい(Mac用):
```text
$pdflatex      = 'xelatex %O %S && cp %D ~/Desktop';
$pdf_previewer = 'open -a Preview.app ~/Desktop/%S';
$bibtex        = 'pbibtex %O %S';
$bibtex_use    = 2;
$pdf_mode      = 1; # dvi->pdf
$dvi_mode      = 0;
$clean_ext = '%R.nav %R.snm %R.vrb';
```

## ちょっとした資料用テンプレート `docsample.tex`

### 必要なもの
* TeXLive を入れてあれば特に問題ない

### 使い方

* `docsample.tex` を適当に編集する．
* コンパイルは `latexmk` を用いると楽だろう．`.latexmkrc` は例えば
以下とすればよい(Mac用):
```text
$latex         = 'platex --shell-escape -halt-on-error';
$dvipdf        = 'dvipdfmx %O -o %D %S && cp %D ~/Desktop';
$pdf_previewer = 'open -a Preview.app ~/Desktop/%S';
$bibtex        = 'pbibtex %O %S';
$bibtex_use    = 2;
$pdf_mode      = 3; 
$clean_ext     = '%R.nav %R.snm %R.vrb %R.tex.bak';
```
