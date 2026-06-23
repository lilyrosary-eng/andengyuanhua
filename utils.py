# utils.py
import os
import sys
import json
import urllib.parse

# ===== 应用根目录（可靠） =====
if getattr(sys, 'frozen', False):
    # 打包成 exe 时，sys.executable 是 exe 路径
    APP_ROOT = os.path.dirname(sys.executable)
else:
    # 源码运行时，以本文件所在目录为准（即项目根目录）
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_abs_path(*parts):
    """基于 APP_ROOT 获取绝对路径"""
    return os.path.join(APP_ROOT, *parts)

def file_url_from_path(file_path):
    """本地路径转为 file:// URL，正确处理 Windows 盘符"""
    abs_path = os.path.abspath(file_path)
    # 转换为 POSIX 路径，再处理盘符
    url_path = abs_path.replace(os.sep, '/')
    if not url_path.startswith('/'):
        url_path = '/' + url_path  # 如 C:/... -> /C:/...
    return 'file://' + url_path

def safe_remove(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"删除文件失败 {file_path}: {e}")

def read_json_file(path, default=None):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return default if default is not None else {}

def write_json_file(path, data):
    """原子写入：先写临时文件，再替换，防止损坏"""
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    tmp_path = path + '.tmp'
    try:
        with open(tmp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        os.replace(tmp_path, path)  # 原子操作
        return True
    except Exception as e:
        print(f"写入 JSON 失败 {path}: {e}")
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        return False

def is_windows():
    return sys.platform.startswith('win')