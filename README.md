# Robosys2020_work2
 ウェブカメラからの画像データをモノクロ画像にするプログラム
 
# リポジトリの概要
　講義内で行ったウェブカメラを用いてウェブブラウザに映像を表示させるというものを改造したものです

# 動作環境
ハードウェア

・Raspberry Pi 4 Model B

・WEB CAMERA FULL HD 1080P

ソフトウェア

・Ubuntu 20.04

・ROS noetic

# 事前準備
・ROS noeticがインストールされていること

　インストールの方法については[Ryuichi Ueda](https://github.com/ryuichiueda)氏の[ros_setup_scripts_Ubuntu20.04_server](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)において
 
  　シェルスクリプトstep0.bash、step1.bashを実行すればインストールができる
 
・cv_cameraとweb_video_serverが使える状況にあること

　導入に関してはRyuichi Ueda氏の[ロボットシステム学第10回(ROS)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html)に従って行ってください

# 実装方法
以下の手順で操作を行ってください

- インストール手順

 ROSのインストール等の事前準備が終了している前提で進めていきます

　自分のcatkin_ws/srcに移動

　`$ git clone https://github.com/NSOrange/Robosys2020_work2.git`

# 実行

- 端末1　`$ roscore`

- 端末2　`$ rosrun cv_caera cv_camera_node`

- 端末3　`$ rosrun web_video_server web_video_server` 

- 端末4　`$ rosrun img_change img_change.py`

- 確認方法

　・同じネットワーク内にある端末でブラウザを開き`{ラズパイのIPアドレス:8080}` に
 
 　　アクセスすることでカメラの映像が見られます

　・/cv_camera/image_rawで編集前のカメラの映像を確認でき、/image_grayでモノクロ加工した映像が確認できます
 

# 実際の動画

以下のURLより動画を視聴できます



# ライセンス
このリポジトリには以下のライセンスが付与されています

BSD 2-Clause License

# 参考文献

[1] [ロボットシステム学第10回(ROS)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html)
[2] [ROSで画像処理ができるようになるまで[python編]](https://qiita.com/wakaba130/items/d3a041164c316a9e7a97)
