import os
import sys
import subprocess
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def duplicate_folder_with_suffix(src_folder, audio_format) -> any:
    # 複製元のフォルダが存在するか確認
    if not os.path.exists(src_folder):
        raise Exception(f"フォルダ {src_folder} が存在しません")

    # フォルダ名を作成（末尾に変換先フォーマットを追加）
    new_folder = src_folder + "_" + audio_format

    # 作成するフォルダが既に存在するか確認
    if os.path.exists(new_folder):
        raise Exception(f"フォルダ {new_folder} は既に存在します")

    # フォルダを作成
    try:
        os.mkdir(new_folder)
        print(f"新しいフォルダ {new_folder} を作成しました")
    except Exception as e:
        print(f"エラー: {e}")

    return new_folder


def run_shell_command(xld_binary, file, new_folder, audio_format):
    command = [xld_binary, "-o", new_folder, file, "-f", audio_format]
    # command = ["afconvert", "-d", audio_format, "-s", encode_mode, "-b", bitrate, file, new_folder]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"変換に成功しました {file}")
    else:
        raise Exception(f"変換に失敗しました {file}")


if __name__ == "__main__":
    # python main.py ./xld test_file aac
    args = sys.argv
    xld_binary = args[1]  # xldの実行ファイル ./xld
    src_folder = args[2]  # 元のフォルダパス test_file
    audio_format = args[3]  # 変換先のフォーマット aac

    new_folder: str = duplicate_folder_with_suffix(src_folder, audio_format)
    list_file: list[str] = [
        str(file) for file in Path(src_folder).iterdir() if file.is_file()
    ]
    # with ProcessPoolExecutor() as executor:
    #     # 各ファイルごとにrun_shell_commandを並列実行
    #     processes = [
    #         executor.submit(
    #             run_shell_command, xld_binary, file, new_folder, audio_format
    #         )
    #         for file in list_file
    #     ]
    #     for process in processes:
    #         process.result()
    with ThreadPoolExecutor() as executor:
        # 各ファイルごとにrun_shell_commandを並列実行
        executor.map(lambda file: run_shell_command(xld_binary, file, new_folder, audio_format), list_file)


