#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""符号与结构审计：python build/check.py 03   （或 all）

检查：禁用记号、导数下角标、拉普拉斯三角形、$ 配对、标题编号、
      图文件与图注与正文引用、例题/习题编号连续、题目与答案一一对应、
      字数与页数估计、禁用语。
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
sys.path.insert(0, BUILD)
import md2tex
import zhnames

ERR, WARN = [], []


def err(n, line, msg):
    ERR.append('[第%s章:%s] %s' % (n, line, msg))


def warn(n, line, msg):
    WARN.append('[第%s章:%s] %s' % (n, line, msg))


FORBID_DERIV = re.compile(
    r'\b(u|v|w|T|f|g|X|Y|R|Z|G|p|h|n)_(\{?(?:t|tt|x|xx|yy|zz|xy|xt|rt|rr|r)\b\}?)')


def cjk_count(s):
    return sum(1 for c in s if '\u4e00' <= c <= '\u9fff')


def check_chapter(num):
    num = num.zfill(2)
    name = None
    for c in md2tex.CHAPTERS:
        if c.startswith(num + '-'):
            name = c
            break
    if not name:
        err(num, 0, '找不到章节文件（md2tex.CHAPTERS 里没有 %s-*.md）' % num)
        return
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        err(num, 0, '文件不存在：%s' % name)
        return
    text = io.open(path, encoding='utf-8').read()
    lines = text.splitlines()
    chap = int(num)
    is_intro = (num == '00')

    in_code = False
    for i, raw in enumerate(lines, 1):
        s = raw
        st = s.strip()
        if st.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        # 1. 禁用记号
        if re.search(r'\\Delta\s*(u|T|\\phi|\\psi|\\varphi|V|p)\b', s):
            err(num, i, '用 \\Delta 表示拉普拉斯算子 —— 统一写 \\nabla^2')
        if re.search(r'\\Box', s):
            err(num, i, '出现 \\Box —— 统一写 \\nabla^2 与显式的时间项')
        if re.search(r'\\partial_[a-zA-Z]', s):
            err(num, i, '出现 \\partial_x 类简写 —— 写成 \\frac{\\partial}{\\partial x}')
        if re.search(r'\\dot\b|\\ddot\b|_\{\s*,\s*[a-zA-Z]', s):
            err(num, i, '出现 \\dot/\\ddot 或 f_{,x} 类写法 —— 时间导数也写全')
        m = FORBID_DERIV.search(s)
        if m:
            err(num, i, '导数下角标 %s —— 写成 \\frac{\\partial %s}{\\partial ...}' % (m.group(0), m.group(1)))
        mzh = zhnames.PAT.search(s)
        if mzh:
            err(num, i, '外文人名 %s —— 一律用中文规范译名（见写作规范 §12）' % mzh.group(1))
        if re.search(r'\\vec\b', s):
            warn(num, i, '用 \\vec 表示矢量 —— 请用 \\boldsymbol')
        # 2. $ 配对（逐行；$$ 单独处理）
        t = re.sub(r'\\\$', '', s)
        if '$$' not in t:
            if t.count('$') % 2 == 1:
                err(num, i, '$ 数目为奇数（行内公式没闭合）')
        # 3. 禁用语
        for bad, why in [('TODO', '留了 TODO'), ('XXX', '留了 XXX'), ('待补', '留了待补'),
                         ('众所周知', '空话'), ('不难看出', '跳步借口'),
                         ('alert(', '禁止弹窗'), ('confirm(', '禁止弹窗'), ('prompt(', '禁止弹窗')]:
            if bad in s:
                warn(num, i, '%s —— %s' % (bad, why))
        # 4. 标题编号
        if re.match(r'^##\s+\d', st):
            m2 = re.match(r'^##\s+(\d+)\.(\d+)\s', st)
            if not m2:
                err(num, i, '节标题格式应为 "## %d.1 标题"' % chap)
        if re.match(r'^###\s+\d', st):
            m2 = re.match(r'^###\s+(\d+)\.(\d+)\.(\d+)\s', st)
            if not m2:
                err(num, i, '小节标题格式应为 "### %d.1.1 标题"' % chap)
        # 5. 表格列数
        if st.startswith('|') and i < len(lines) and set(st) <= set('|-: '):
            pass
    if in_code:
        err(num, 0, '``` 代码块没有闭合')

    # 6. $$ 块配对
    if text.count('$$') % 2 == 1:
        err(num, 0, '$$ 总数为奇数（行间公式没闭合）')

    # 7. 标题编号连续性
    secs = [int(m.group(2)) for m in re.finditer(r'^##\s+(\d+)\.(\d+)\s', text, re.M)]
    if secs:
        if secs != list(range(1, len(secs) + 1)):
            err(num, 0, '节号不连续：%s' % secs)
    for m in re.finditer(r'^##\s+(\d+)\.(\d+)\s', text, re.M):
        if int(m.group(1)) != chap:
            err(num, text[:m.start()].count('\n') + 1, '节号章号不对：%s（应为 %d.x）' % (m.group(1), chap))

    # 8. 图
    figs = []
    for i, raw in enumerate(lines, 1):
        st = raw.strip()
        m = md2tex.FIG_RE.match(st)
        if m:
            p = os.path.join(BUILD, m.group(1))
            if not os.path.exists(p):
                err(num, i, '图文件不存在：%s' % m.group(1))
            cap = (m.group(2) or '').strip()
            if not cap:
                err(num, i, '图没有图注：%s' % m.group(1))
            elif re.match(r'^图\s*\d+\.\d+', cap):
                err(num, i, '图注不要自带 "图 N.M"（LaTeX 会自动编号）')
            figs.append((i, m.group(1)))
        elif st.startswith('!['):
            err(num, i, '图写成了一行：%s（应单独一行，格式 ![](figs/ch%02d-01.tex "图注")）'
                % (st[:40], chap))
    if len(figs) < 5 and not is_intro:
        warn(num, 0, '图只有 %d 张，规范要求 5-8 张' % len(figs))
    # 图号引用
    for m in re.finditer(r'图\s*(\d+)\.(\d+)', text):
        c, k = int(m.group(1)), int(m.group(2))
        ln = text[:m.start()].count('\n') + 1
        if c != chap:
            err(num, ln, '引用图 %d.%d，章号应为 %d' % (c, k, chap))
        elif k > len(figs):
            err(num, ln, '引用图 %d.%d，但本章只有 %d 张图' % (chap, k, len(figs)))

    # 9. 例题编号
    exs = [int(m.group(1)) for m in re.finditer(r'\*\*例\s*%d\.(\d+)\*\*' % chap, text)]
    if exs and exs != list(range(1, len(exs) + 1)):
        err(num, 0, '例题编号不连续：%s' % exs)
    if not exs and not is_intro:
        warn(num, 0, '没有例题（要求 6-10 道）')

    # 10. 习题
    idx = text.find('## ')
    pos = None
    for m in re.finditer(r'^##\s+%d\.\d+\s*(.+)$' % chap, text, re.M):
        if '习题' in m.group(1):
            pos = m.start()
    if pos is None and not is_intro:
        err(num, 0, '找不到 "## %d.x 习题" 一节' % chap)
    else:
        tail = text[pos:]
        ids = [int(m.group(1)) for m in re.finditer(r'\*\*%d\.(\d+)\*\*' % chap, tail)]
        if not ids and not is_intro:
            err(num, 0, '习题一节里没有题目（格式 **%d.1**）' % chap)
        else:
            if ids != list(range(1, len(ids) + 1)):
                err(num, 0, '习题编号不连续：%s' % ids)
            # 分组统计
            def group_count(tag):
                m = re.search(r'^###\s+.*' + tag + r'.*$', tail, re.M)
                if not m:
                    return 0
                rest = tail[m.end():]
                nxt = re.search(r'^###\s', rest, re.M)
                seg = rest[:nxt.start()] if nxt else rest
                return len(re.findall(r'\*\*%d\.\d+\*\*' % chap, seg))
            calc = group_count('A 组') + group_count('B 组') + group_count('C 组')
            conc = group_count('概念')
            if calc == 0:
                calc = len(ids) - conc
            if calc < 30 and not is_intro:
                err(num, 0, '计算题 %d 道，规范要求 ≥30' % calc)
            if conc < 8 and not is_intro:
                warn(num, 0, '概念题 %d 道，规范要求 ≥8' % conc)
        # 答案
        apath = os.path.join(BUILD, 'answers', 'ch%s.md' % num)
        if not os.path.exists(apath):
            if not is_intro:
                err(num, 0, '缺少答案文件 build/answers/ch%s.md' % num)
        else:
            atxt = io.open(apath, encoding='utf-8').read()
            aids = [int(m.group(1)) for m in re.finditer(r'\*\*%d\.(\d+)\*\*' % chap, atxt)]
            if set(aids) != set(ids):
                miss = sorted(set(ids) - set(aids))
                extra = sorted(set(aids) - set(ids))
                err(num, 0, '题号与答案不一致：缺 %s，多 %s' % (miss[:8], extra[:8]))
            if aids != list(range(1, len(aids) + 1)):
                warn(num, 0, '答案编号不连续：%s' % aids[:12])

    # 11. 篇幅
    nchar = cjk_count(text)
    pages = nchar / 420.0
    if pages < 22 and not is_intro:
        warn(num, 0, '篇幅估计 %.0f 页，低于 25 页目标（%d 汉字）' % (pages, nchar))
    if pages > 45:
        warn(num, 0, '篇幅估计 %.0f 页，超过 40 页，考虑拆分或删减' % pages)
    print('[第%s章] %s：%d 行，%d 汉字，约 %.0f 页，%d 图，%d 例题'
          % (num, name, len(lines), nchar, pages, len(figs), len(exs)))


def main():
    args = sys.argv[1:] or ['all']
    if args == ['all']:
        nums = [c[:2] for c in md2tex.CHAPTERS]
    else:
        nums = args
    for n in nums:
        check_chapter(n)
    print()
    if ERR:
        print('=== 错误 %d 条（必须修） ===' % len(ERR))
        for e in ERR:
            print(e)
    if WARN:
        print('=== 警告 %d 条 ===' % len(WARN))
        for w in WARN[:40]:
            print(w)
    if not ERR:
        print('审计通过（错误 0 条）')
    return 1 if ERR else 0


if __name__ == '__main__':
    sys.exit(main())
