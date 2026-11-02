#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""整书构建：python build/make_all.py

步骤：
1. 从各章「本章判断点」表自动汇总 附录B
2. md2tex.py 生成 body.tex / appendix.tex
3. xelatex 两遍
4. 把 PDF 复制到仓库根目录（数学物理方法-讲义.pdf）
5. 生成 GitHub 阅读用的 数理方法讲义-全文.md
"""
import io, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
sys.path.insert(0, BUILD)
import md2tex


def split_row(r):
    r = r.strip()
    if r.startswith('|'):
        r = r[1:]
    if r.endswith('|'):
        r = r[:-1]
    cells, cur, inmath = [], '', False
    for i, c in enumerate(r):
        if c == '$' and (i == 0 or r[i - 1] != '\\'):
            inmath = not inmath
            cur += c
        elif c == '|' and not inmath:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += c
    cells.append(cur.strip())
    return cells


def make_appendix_b():
    """扫描各章，只取「本章判断点」小节里的那张表，汇总成附录 B。"""
    rows = []
    for name in md2tex.CHAPTERS[1:]:          # 跳过导论
        num = int(name[:2])
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            continue
        lines = io.open(path, encoding='utf-8').read().splitlines()
        # 找到最后一个含「判断点」的标题行
        start = None
        for i, ln in enumerate(lines):
            st = ln.strip()
            if st.startswith('#') and '判断点' in st:
                start = i
        if start is None:
            continue
        # 从该标题往下找第一张表
        tbl = None
        for i in range(start, len(lines)):
            if not lines[i].strip().startswith('|'):
                if tbl is not None:
                    break
                continue
            if tbl is None:
                tbl = []
            tbl.append(split_row(lines[i].strip()))
            if len(tbl) > 2 and not lines[i + 1].strip().startswith('|'):
                break
        if not tbl:
            continue
        tbl = [r for r in tbl if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
        for r in tbl[1:]:
            r = r + [''] * (4 - len(r))
            rows.append([r[0], r[1], r[2], r[3], '第 %d 章' % num])
    out = ['# 附录 B 判断点总表', '',
           '> 全书所有「这里能不能这么干」的问题汇总成一张表。按症状查，比按章节查快。',
           '', '## B.1 全表', '',
           '| 判断点 | 什么时候成立 | 破了会怎样 | 怎么在现场发现 | 出处 |',
           '|---|---|---|---|---|']
    for r in rows:
        out.append('| ' + ' | '.join(c.replace('|', r'\|') for c in r) + ' |')
    out += ['', '## B.2 怎么用这张表', '',
            '1. 先找「症状」：结果反常、级数不收敛、频率不对、边界处误差大。',
            '2. 在「怎么在现场发现」一列里找到对应条目。',
            '3. 回到「什么时候成立」确认是哪条假设破了，再翻回对应章节看后果。',
            '', '这张表不替代正文。它只是在你不确定「能不能这么干」时，给你一个快速定位的方向。']
    io.open(os.path.join(ROOT, '附录B-判断点总表.md'), 'w', encoding='utf-8').write('\n'.join(out))
    print('附录B：%d 条判断点' % len(rows))


def make_full_md():
    """生成单一 Markdown 全文（GitHub 阅读用）。图用图注文字代替。"""
    parts = []
    files = md2tex.CHAPTERS + md2tex.APPENDICES
    fig_re = re.compile(r'^!\[[^\]]*\]\(\s*figs/[^)\s"]+\.tex\s*(?:"([^"]*)")?\s*\)\s*$')
    for name in files:
        if name == '附录C-习题详解.md':
            txt = md2tex.build_answers()
        else:
            p = os.path.join(ROOT, name)
            if not os.path.exists(p):
                continue
            txt = io.open(p, encoding='utf-8').read()
        out, chap, k = [], 0, 0
        for ln in txt.splitlines():
            m = re.match(r'^#\s+第\s*(\d+)\s*章', ln.strip())
            if m:
                chap = int(m.group(1))
                k = 0
            mf = fig_re.match(ln.strip())
            if mf:
                k += 1
                cap = (mf.group(1) or '').strip()
                out.append('> **图 %d.%d**　%s' % (chap, k, cap))
            else:
                out.append(ln)
        parts.append('\n'.join(out).strip())
    io.open(os.path.join(ROOT, '数理方法讲义-全文.md'), 'w', encoding='utf-8').write(
        '\n\n'.join(parts) + '\n')
    print('全文 md 已生成')


def main():
    make_appendix_b()
    subprocess.run([sys.executable, os.path.join(BUILD, 'md2tex.py')], check=True)
    ok = True
    for i in range(3):
        p = subprocess.run(['xelatex', '-interaction=nonstopmode', 'main.tex'],
                           cwd=BUILD, capture_output=True)
        if p.returncode != 0:
            ok = False
            log = io.open(os.path.join(BUILD, 'main.log'), encoding='utf-8', errors='replace').read()
            errs = [l for l in log.splitlines() if l.startswith('! ')]
            print('第 %d 遍编译失败，错误：' % (i + 1))
            for e in errs[:15]:
                print('  ' + e)
            break
    if not ok:
        return 1
    src = os.path.join(BUILD, 'main.pdf')
    dst = os.path.join(ROOT, '数学物理方法-讲义.pdf')
    shutil.copyfile(src, dst)
    info = subprocess.run(['pdfinfo', src], capture_output=True, text=True).stdout
    m = re.search(r'Pages:\s+(\d+)', info)
    print('PDF 生成：%s 页 -> %s' % (m.group(1) if m else '?', dst))
    make_full_md()
    io.open(os.path.join(ROOT, '附录C-习题详解.md'), 'w', encoding='utf-8').write(
        md2tex.build_answers() + '\n')
    print('附录C 单文件已生成')
    return 0


if __name__ == '__main__':
    sys.exit(main())
