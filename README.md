# robosys2020_task2

## 概要

ROSの仕組みを使って2人でチャットをすることができるパッケージです。

なお、このパッケージは千葉工業大学 未来ロボティクス学科 2020年度 ロボットシステム学の講義の課題で作成しました。

## 動作環境

- OS: Ubuntu 18.04
- ROSディストリビューション: melodic

## 使用方法

1. 以下のコマンドを実行してこのリポジトリをクローンします

```shell
cd ~/catkin_ws/src
git clone https://github.com/shimotoriharuki/robosys2020_task2
```

2. 以下のコマンドでビルドをします。

```shell
cd ~/catkin_ws
catkin_make
```

3. 以下のコマンドで`roscore`を起動します

```shell
roscore
```

4. 新しいターミナルで、以下のコマンドを実行します

```she;;
rosrun ros_chat player1.py
```

5. 新しいターミナルで、以下のコマンドを実行します

```she;;
rosrun ros_chat player2.py
```

6. 4と5でコマンドを実行した2つのターミナル間でチャットをすることができます。
