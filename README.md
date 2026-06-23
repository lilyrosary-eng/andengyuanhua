#  岸灯鸢花 (Andeng Yuanhua) v1.0

> **Lightweight · Geek‑styled · Local Markdown notes + universal file manager for Windows**

[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-blue)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)
[![Qt](https://img.shields.io/badge/Qt-PyQt6-41CD52)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

Built with **PyQt6** and **QWebEngine**, this tool follows the philosophy of *“clever hacks over reinventing the wheel”*. It combines a powerful Markdown editor with universal file parsing, native system menus, and an extensible DLC architecture – all packed into a self‑contained, crash‑resilient application.

---

## Table of Contents

- [Features](#features)
  - [ Note Editor](#-note-editor)
  - [ Universal File Parsing & Drag‑and‑Drop](#-universal-file-parsing--drag-and-drop)
  - [ Geeky Image Editor](#️-geeky-image-editor)
  - [ File Management & Data Security](#-file-management--data-security)
  - [ Modular Themes & DLC Extensions](#-modular-themes--dlc-extensions)
  - [ Other System‑Level Features](#️-other-system-level-features)
- [ Quick Reference Shortcuts](#️-quick-reference-shortcuts)
- [Getting Started](#getting-started)
- [Packaging & Distribution](#packaging--distribution)
- [System Requirements](#system-requirements)
- [License](#license)

---

## Features

###  Note Editor

- **Dual‑pane Markdown preview** – edit and preview side‑by‑side, or switch to a distraction‑free “edit‑only” mode.
- **Rich shortcut toolbar** – includes buttons for bold, italic, links, and manual save (`Ctrl+S`).
- **Intelligent timeline grouping** – notes in the left sidebar are automatically grouped by “Today”, “Yesterday”, and specific dates, with fuzzy search support.
- **Drag‑to‑sort sidebar** – reorder notes via drag‑and‑drop; also pin/unpin notes from the right‑click context menu.
- **Tile / floating window** – detach any note into a separate, always‑on‑top floating window, enabling true multitasking with independent note views.

###  Universal File Parsing & Drag‑and‑Drop

- **Global drag‑and‑drop** – the entire application window accepts dropped files (not just the editor area).
- **Images & code files** – drag `.png`, `.jpg` to automatically insert as Markdown images; drag `.py`, `.cmd`, `.xml`, `.json`, and other source/config files to import them as syntax‑highlighted code blocks.
- **Office document intelligence**:
  - **PDF / Word / PPTX** – extracts text, preserves formatting, and **automatically extracts embedded images** into the note.
  - **Excel** – reads table data and converts it into a clean Markdown table (with horizontal scrolling for extra‑wide sheets).
- **Global screenshot system** – press `Ctrl+Shift+S` to capture the full screen; the image is saved and automatically pasted at the end of the current note.

###  Geeky Image Editor

- **Instant launch** – double‑click any image in the preview pane to open a lightweight, standalone image editor.
- **Essential toolkit** – includes **pen, eraser, colour picker, 90° rotation**, and **mouse‑wheel zoom**.
- **One‑click save** – save the edited image as PNG or JPG.

###  File Management & Data Security

- **Staging area** – whenever you modify and save a note containing images/attachments, the original files are backed up to the `staging/` folder (e.g., `original_file_changed.png`) as a safety net.
- **Hidden trash (Recycle Bin)** – deleted notes are not physically erased but moved to a trash bin. You can **restore, permanently delete, or empty the trash**.
- **Smart orphan cleanup** – when a note is deleted, the app checks whether its referenced images/attachments are shared with other notes. If they are exclusive, they are physically removed; otherwise, only the reference is deleted and the files are moved to the trash.
- **Fast export** – export notes as `.md` files or as beautifully formatted `.pdf` documents.
- **One‑click full backup** – package the three core data directories (`notes/`, `images/`, `attachments/`) into a `.zip` backup file.

###  Modular Themes & DLC Extensions

- **Built‑in theme switching** – toggle between Light and Dark modes, and customise navigation element colours.
- **Theme pack DLC** – modular design allows you to drop JSON configuration files into the `themes/` folder, enabling an unlimited number of external themes (e.g., Deep Ocean Blue, Minimal Pure White, etc.).
- **Smart colour inversion** – instantly invert colours for specific UI elements (like the navigation bar) without breaking overall visual harmony.

###  Other System‑Level Features

- **Crash‑proof frontend** – uses a geek‑level safe binding mechanism to eliminate `null` errors caused by Qt WebEngine rendering races, ensuring rock‑solid stability.
- **Native system tray** – close/minimise to the system tray; double‑click the tray icon to restore the window. Single‑instance prevention is also enforced.
- **Hidden developer mode** – a built‑in geek console (accessible via a special command) unlocks hidden features like the trash bin, providing a backdoor for future customisation and extension.

---

##  Quick Reference Shortcuts

| Shortcut | Action |
| :------- | :----- |
| `Ctrl + B` / `I` / `K` | Bold, italic, insert link in the editor |
| `Ctrl + S` | Manually save the current note |
| `Ctrl + Shift + S` | Global screenshot – insert into current note |
| `Double‑click preview image` | Open the built‑in image editor |
| `Right‑click a note` | Access native context menu (copy, tile, pin, export MD/PDF) |

---

## Getting Started

1. Download the latest release package (`.zip` or `.7z`) from the [Releases](../../releases) page.
2. Extract the folder to any location on your computer.
3. Run `AndengYuanHua.exe` (or the appropriate executable).
4. Start writing – all your notes are automatically saved to the `notes/` folder.

> **Note**: No additional installation or runtime setup is required. Everything is bundled.

---

## Packaging & Distribution

This application is fully self‑contained and does **not** require a Python environment to run.  
Using PyInstaller, all external engines (e.g., `wkhtmltopdf`) are embedded inside the package – **just unzip and run**.

- **Bundle size**: Optimised with UPX compression, startup time is only 2–3 seconds.
- **No registry pollution** – all data is stored locally in the application folder.

---

## System Requirements

- **OS**: Windows 10 / 11 (64‑bit recommended)
- **RAM**: ≥ 512 MB (1 GB recommended for heavy documents)
- **Disk**: ≥ 200 MB free space
- **Display**: Optimised for 4K 144Hz monitors (flicker‑free)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.





----------------------------------
以下是中文

双栏 Markdown 编辑：左侧写 Markdown 源码，右侧实时渲染预览。

独立的标题栏：笔记标题与正文分离，解决了 Markdown # 号带来的双标题视觉问题。

智能自动保存：打字停止 1 秒后（可调节）自动保存为本地独立的 .md 文件（存储在 notes/ 文件夹）。

便捷列表管理：支持新建、双击重命名、复制笔记（克隆），以及右键删除。

全局截图快捷键：支持自定义组合键（如 Ctrl+Shift+S），一键截屏并自动转化为 PNG 保存。

无缝插入笔记：截图后自动以 Markdown ![]() 的形式追加到当前笔记末尾。

拖拽插入图片：支持从电脑文件夹直接拖拽图片到左侧编辑区，自动保存为图片并插入代码。

原生拖拽出图：支持鼠标按住预览区的图片，直接拖到电脑桌面上生成真实的 .png 文件。

点击放大查看：预览区图片点击后弹出无边框大图全屏查看。

智能图片垃圾回收：在保存笔记时，自动检索所有笔记，清理掉 images/ 中未被任何笔记引用的冗余截图，防止硬盘空间浪费。

轻量化动效与美观：玻璃透明质感、选中笔记的微动效（平移+高亮）、切换笔记时的优雅淡入动画。

深色/亮色模式：一键切换全局主题（底层采用 CSS 变量，无卡顿）。

多款主题色：支持经典蓝、青草绿、浪漫紫、活力橙、烈焰红。

系统真实字体：直接读取 Windows 系统真实的已安装字体库（ 扫描注册表驱动，支持几百种字体）。

面板透明度控制：滑块调节，支持从 30% 到 100% 随意调节。

快捷键自定义：极简的操作体验——单击输入框捕获按键，双击可手动输入，按下 ESC 取消。

系统托盘（最小化挂后台）：点击右上角关闭按钮不会退出，而是隐藏至右下角托盘，双击托盘图标即可瞬间呼出。

4K 144Hz 体验优化：通过命令行限制和设定 OpenGL 渲染后端，最大限度适配了高分辨率高刷新屏幕，消除了闪烁和卡顿。

极致轻盈打包：抛弃了一碰就崩溃的 200MB+ 单文件 EXE 打包方式，采用文件夹结构 + UPX 压缩，拿到后解压即用，启动速度仅需 2~3 秒。

后续还在开发中，优先保障ui，我讨厌丑陋的ui

感谢您的使用！
