OpenCVによる映像処理
----
プログラムの説明
----
このプログラムはOpenCVを利用して、ガンマ変換によるコントラスト調整やカラー(色調)の変化、フィルタリングの処理をGUIによってインタラクティブに行うものです。

実装した処理は以下の三種類です。

・累乗型トーンカーブの一種であるガンマ変換により、コントラストの変更を行います

・B,G,Rそれぞれの画素値を増減させ、色調の変化を行います

・鮮鋭化フィルタ、ラプラシアンフィルタ、グラディエントフィルタを利用してフィルタリングを行います

実行環境及び実行方法
----
このプログラムはOpenCV及びnumpyモジュールがインストールされた環境で実行できます。

jupyter notebook上で実行する場合はこのプログラムをコピーし貼り付けてからCtrlキー+Enterキーなどで実行できます。

使用方法
----
GUIのバーの値が0になっている箇所の処理は実行されません。0より大きい値に変化させることで処理が実行されます。

・contrastについて

バーが左にいくほど明るく、右にいくほど暗くなります。

・red,blue,greenについて

バーが左にいくほど特定の色が濃くなり、右にいくほど特定の色が薄くなります。

・filterについて

バーの値が1のとき、映像がグレースケールに変更されます。

バーの値が2のとき、映像がグレースケールに変更されたあと、鮮鋭化フィルタによるフィルタリングが行われます。

バーの値が3のとき、映像がグレースケールに変更されたあと、ラプラシアンフィルタによるフィルタリングが行われます。

バーの値が4のとき、映像がグレースケールに変更されたあと、グラディエントフィルタによるフィルタリングが行われます。

参考文献
----
OpenCVで各種フィルター処理をする（グラディエント、ハイパス、ラプラシアン、ガウシアン）

https://qiita.com/hitomatagi/items/93e01ef22e46b14a60a9

このサイトでは各フィルタの値やOpenCVでの処理について参考にしました。

ディジタル画像処理[改訂新版]

こちらの資料ではではガンマ変換や色調変化、鮮鋭化フィルタについて参考にしました。

実行の様子
----
Youtubeに動画をアップロードしました。以下のリンクからアクセスできます。

https://youtu.be/8vuTFYoppqU
