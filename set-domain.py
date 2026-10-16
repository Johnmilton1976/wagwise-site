#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键把站点里的域名占位符 your-domain.com 换成你自己的真实域名。

为什么需要它：每个页面 <head> 里都有一行 canonical，写的是
    <link rel="canonical" href="https://your-domain.com/...">
canonical 是告诉谷歌"这个页面的正式网址"。如果它指向别人的域名，
谷歌会认为你的页面是重复内容，不给排名。所以上线前必须全部换掉。

用法（在本文件所在目录打开命令行）：
    python set-domain.py                 # 只检查，不修改：看看还有多少处占位符
    python set-domain.py wagwise.org     # 替换成你的域名（不用写 https://）
    python set-domain.py --revert        # 改回占位符（本地重新测试用）

替换范围：public/ 目录下所有 .html / .xml / .txt 文件。
"""

import os
import re
import sys

PLACEHOLDER = "your-domain.com"
EXTS = (".html", ".xml", ".txt")


def site_dir():
    """站点目录：脚本同级的 public/（含 index.html）或脚本同级根。"""
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "public"), here):
        if os.path.isfile(os.path.join(cand, "index.html")):
            return cand
    return None


def target_files(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if fn.lower().endswith(EXTS):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def main():
    root = site_dir()
    if not root:
        print("找不到 public/ 目录。请把本脚本放在 pet-care-site 根目录再运行。")
        return 1

    args = sys.argv[1:]
    revert = "--revert" in args
    args = [a for a in args if a != "--revert"]
    domain = args[0].strip().lower() if args else None

    files = target_files(root)
    total = 0
    for f in files:
        n = open(f, encoding="utf-8").read().count(PLACEHOLDER)
        if n:
            total += n

    print("站点目录: %s" % root)
    print("扫描文件: %d 个，发现占位符 %d 处" % (len(files), total))

    if not domain and not revert:
        if total:
            print("\n还没替换。加上你的域名再运行一次，例如：")
            print("    python set-domain.py wagwise.org")
        else:
            print("\n没有发现占位符，看起来已经换过了。")
        return 0

    if revert:
        new = PLACEHOLDER
        print("\n改回占位符 %s" % PLACEHOLDER)
    else:
        new = re.sub(r"^https?://", "", domain).rstrip("/")
        if not re.match(r"^[a-z0-9][a-z0-9.-]*\.[a-z]{2,}$", new):
            print("\n域名看起来不对：%s" % domain)
            print("应该像 wagwise.org 这样。")
            return 1
        print("\n替换为 %s" % new)

    src = new if revert else PLACEHOLDER
    dst = PLACEHOLDER if revert else new

    changed = 0
    for f in files:
        s = open(f, encoding="utf-8").read()
        if src in s:
            open(f, "w", encoding="utf-8").write(s.replace(src, dst))
            changed += 1

    print("已更新 %d 个文件。" % changed)
    if not revert:
        print("\n下一步：提交并推送到 GitHub（git add -A && git commit && git push），")
        print("Cloudflare 会自动重新部署。之后记得在 Google Search Console 重新提交 sitemap.xml。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
