# from .note.cpp.refresh import Main as refresh
from datetime import datetime
import os


def info(log):
    print(f"[Info] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} " + log)


def warn(log):
    print(f"[Warning] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} " + log)


def err(log):
    print(f"[Error] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} " + log)

# ---------
# replace index.html


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file: 文件名
    :param old_str: 旧字符串
    :param new_str: 新字符串
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


try:
    if not int(env.get("CF_PAGES")) == 1:
        err("Not CF Pages, will not replace index.html.")
    else:
        alter("./index.html", "[ENV_build]", env.get('CF_PAGES_COMMIT_SHA'))
        alter("./index.html", "[ENV_build_branch]", env.get('CF_PAGES_BRANCH'))
        alter("./index.html", "[ENV_build_time]",
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        info("Wrote build info into index.html ok")
except:
    err("get CF Pages env failed, will not replace index.html.")

# ---


# def get_nested_subdirectory_paths(directory, prefix=''):
#     subdirectories = [os.path.join(directory, d) for d in os.listdir(directory)
#                       if os.path.isdir(os.path.join(directory, d)) and d not in exclude]

#     # 递归调用，获取每一个子目录下的所有子目录
#     for subdir in subdirectories:
#         yield from get_nested_subdirectory_paths(subdir, prefix + subdir + '/' if prefix else subdir)

#     # 如果不在递归中，返回目录本身
#     if prefix:
#         yield prefix


# exclude = ['.git', '__pycache__', '__MACOSX', 'src']  # 添加你需要排除的目录

# # 获取所有子目录（包括多层）
# nested_paths = list(get_nested_subdirectory_paths('./'))
# all_paths = []
# for n in nested_paths:
#     all_paths += [n.replace('./', '')]

# print(all_paths)