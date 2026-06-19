# cs2-crosshair-extractor

`cs2-crosshair-extractor` 是一个轻量级的 CS2 Demo 准星代码提取工具。通过底层二进制流扫描算法，直接从 `.dem` 文件中剥离所有形如 `CSGO-XXXXX` 的明文准星特征码。支持官匹、完美世界等多种来源的demo，不受游戏版本更新或平台自定义协议的网络封包影响（？）。采用纯原生 Python 开发，无任何第三方库依赖，支持跨平台运行及文件拖拽操作。
这里在编辑框里看着没问题，但最后显示出来会有点语序问题？

## 功能特性

* **多平台兼容：** 支持扫描和识别经第三方平台、修改过网络实体路径的 Demo 文件。
* **零依赖项：** 基于原生标准库编写，无需配置复杂的 Protobuf 解包环境或运行 `pip install`。
* **极简交互：** 提供双击自动扫描与文件拖拽运行两种交互模式。

## 使用方法

### 方式一：拖拽运行
1. 确保系统已安装 Python 环境。
2. 将 `.dem` 录像文件直接拖拽至 `cs2_crosshair_extractor.py` 脚本图标上释放，即可自动输出提取结果。

### 方式二：同目录执行
1. 将 `.dem` 录像文件与 `cs2_crosshair_extractor.py` 脚本放置于同一文件夹内。
2. 双击运行 `cs2_crosshair_extractor.py` 脚本。

### 方式三：拖拽导入
1. 将 `.dem` 录像文件直接拖拽至 `cs2_crosshair_extractor.py` 脚本运行窗口，即可自动导入，输出提取结果。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
