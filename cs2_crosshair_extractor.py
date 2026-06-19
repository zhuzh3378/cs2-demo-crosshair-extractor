import re
import os
import sys

def process_demo(demo_path):
    # 去除 Windows 拖拽路径时可能自带的各种引号
    demo_path = demo_path.strip().strip('"').strip("'")
    
    if not os.path.exists(demo_path) or not demo_path.lower().endswith('.dem'):
        print("❌ 错误：无效的文件路径或文件非 .dem 格式！")
        return False

    file_name = os.path.basename(demo_path)
    print(f"\n🔍 正在物理扫描文件: {file_name} ...")
    print("根据文件大小，这可能需要 3~10 秒钟，请稍候...\n")
    
    try:
        with open(demo_path, 'rb') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 无法读取文件: {e}")
        return False
    
    pattern = rb'CSGO-[A-Za-z0-9\-]+'
    matches = re.findall(pattern, content)
    
    codes = set()
    for match in matches:
        try:
            decoded_str = match.decode('ascii')
            if 25 < len(decoded_str) < 38:
                codes.add(decoded_str)
        except UnicodeDecodeError:
            continue
            
    print("=" * 50)
    if not codes:
        print("❌ 扫描完成：未能在该 Demo 的底层二进制中剥离出明文准星代码。")
    else:
        print(f"🎉 成功分析 Demo！共发现 {len(codes)} 个可能属于选手的准星代码：")
        print("-" * 50)
        for i, code in enumerate(sorted(codes), 1):
            print(f" [{i}]  {code}")
        print("-" * 50)
        print("💡 提示：在一场比赛里，这里面必然有一个是你想找的那位玩家的。")
        print("用鼠标在窗口里拖动选中代码，按【Ctrl+C】即可复制。")
    print("=" * 50)
    return True

def main():
    print("==================================================")
    print("   CS2 Demo 准星代码提取器   ")
    print("==================================================")

    # 1. 优先判断是否直接把文件拖拽到 .py 脚本图标上运行 (sys.argv)
    if len(sys.argv) > 1:
        process_demo(sys.argv[1])
        return

    # 2. 自动寻找当前文件夹下的第一个 .dem 文件
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
    demo_files = [f for f in os.listdir(current_dir) if f.endswith('.dem')]
    
    if demo_files:
        demo_path = os.path.join(current_dir, demo_files[0])
        process_demo(demo_path)
    else:
        # 3. 核心修改：未找到同目录文件时，支持直接拖拽文件到运行窗口中
        print("💡 未在当前目录下检测到 .dem 文件。")
        print("👉 请直接将你的 .dem 录像文件【拖拽】到本窗口内，然后按下【回车键】开始扫描：")
        dragged_path = input("\n[输入文件路径或直接拖入文件]: ")
        process_demo(dragged_path)

if __name__ == '__main__':
    main()
    print("\n")
    input("按下【回车键 (Enter)】即可关闭此窗口...")