# config.py
import os  # <--- 修复：加上这一行
from utils import get_abs_path

# 目录名
NOTES_DIR = "notes"
IMAGES_DIR = "images"
ATTACHMENTS_DIR = "attachments"
TRASH_DIR = "trash_notes"
STAGING_DIR = "staging"
ORDER_FILE = "list_order.json"
TRASH_FILE = "trash.json"
MAX_TRASH_SIZE = 1024 * 1024 * 1024  # 1GB

# 确保所有目录存在
for d in [NOTES_DIR, IMAGES_DIR, ATTACHMENTS_DIR, TRASH_DIR, STAGING_DIR]:
    os.makedirs(get_abs_path(d), exist_ok=True)