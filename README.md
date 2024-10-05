# これは何
指定したフォルダに入っているオーディオファイルをXLD( https://tmkk.undo.jp/xld/ )を用い、一括で任意のフォーマットに変換します。
作者はCDをALAC形式で取り込む習慣があり、それをDJ用にAAC形式に変換する作業を手動で行っているため、自動化しました。
XLDはmacOS専用ソフトのためmacOSでしか動きません

# 使い方
1. XLDをアプリケーションフォルダに入れてインストールしてください
2. XLDにて、お好みの変換形式の詳細設定をしてください（ビットレート、VBR/ABR/CBRなど）（CLIでは詳細設定ができず、GUIに従う仕様になっています）
3. XLDのイメージファイルをマウントすると入っているCLIフォルダ内のxldファイルをmain.pyと同じ階層に設置してください
   ```
   .
   ├── main.py
   ├── test_folder
   └── xld
   ```
4. Pythonが動く環境で、
   ```
   python main.py <xldファイルのディレクトリ> <変換元のフォルダ> <変換先フォーマット>
   ```
   を実行してください

    例）
    ```
    python main.py ./xld test_folder aac
    ```
    （標準のモジュールのみ使用しているためpipで追加モジュールのインストールは必要ありません）
5. 実行が成功すると、元のフォルダ名に"_<変換先フォーマット>"が付いたフォルダ内に変換されたオーディオファイルが作成されています。
   ```
   .
   ├── main.py
   ├── test_folder
   ├── test_folder_aac
   └── xld
   ```

