# utils.py
import os
import sys
import json
import urllib.parse

# ===== 应用根目录（可靠） =====
def get_abs_path(*parts):
    # 如果是打包后的运行环境
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)

        # 1. 优先在 exe 同级目录查找（例如 notes, images 等数据文件夹）
        path1 = os.path.join(base, *parts)
        if os.path.exists(path1):
            return path1

        # 2. 如果同级没有，去 _internal 子目录里找（解决 web, wkhtml, icon.png 被藏起来的问题）
        path2 = os.path.join(base, '_internal', *parts)
        if os.path.exists(path2):
            return path2

        # 3. 都找不到，返回默认路径，防止程序直接崩溃
        return path1

    # 开发环境（PyCharm）正常使用当前目录
    return os.path.join(os.getcwd(), *parts)

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