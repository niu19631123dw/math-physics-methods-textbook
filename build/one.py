#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""单章快编：python build/one.py 03

把某一章单独编译成 build/_preview/03.pdf，30-90 秒，用来检查 LaTeX 错误。
"""
import io, os, re, subprocess, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
PREV = os.path.join(BUILD, '_preview')
sys.path.insert(0, BUILD)
import md2tex


def find_chapter(num):
    for name in md2tex.CHAPTERS:
        if name.startswith(num + '-'):
            return name
    return None


def main():
    if len(sys.argv) < 2:
        print('用法: python build/one.py 03')
        return 1
    num = sys.argv[1].zfill(2)
    name = find_chapter(num)
    if not name:
        print('找不到第 %s 章' % num)
        return 1
    os.makedirs(PREV, exist_ok=True)

    txt = io.open(os.path.join(ROOT, name), encoding='utf-8').read().splitlines()
    body = md2tex.convert(txt)
    chapnum = int(num)
    tex = ['\\input{preamble}', '\\begin{document}', '\\mainmatter',
           '\\setcounter{chapter}{%d}' % (chapnum - 1), body, '\\end{document}']
    src = os.path.join(BUILD, '_one_%s.tex' % num)
    io.open(src, 'w', encoding='utf-8').write('\n'.join(tex))

    ok = True
    for run in range(2):
        p = subprocess.run(['xelatex', '-interaction=nonstopmode',
                            '-output-directory', PREV, '_one_%s.tex' % num],
                           cwd=BUILD, capture_output=True)
        if p.returncode != 0:
            ok = False
            break
    log = os.path.join(PREV, '_one_%s.log' % num)
    errors, warns = [], []
    if os.path.exists(log):
        lines = io.open(log, encoding='utf-8', errors='replace').read().splitlines()
        for i, l in enumerate(lines):
            if l.startswith('! '):
                errors.append('\n'.join(lines[i:i + 6]))
            elif l.startswith('Overfull') or l.startswith('Underfull'):
                warns.append(l)
    pdf = os.path.join(PREV, '_one_%s.pdf' % num)
    pages = '?'
    if os.path.exists(pdf) and os.path.getsize(pdf) > 1024:
        try:
            out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
            m = re.search(r'Pages:\s+(\d+)', out)
            if m:
                pages = m.group(1)
        except Exception:
            pass
    print('章：%s  ->  %s  页数 %s' % (name, pdf, pages))
    if errors:
        print('\n=== LaTeX 错误 %d 处 ===' % len(errors))
        for e in errors[:12]:
            print(e)
            print('---')
        return 1
    if not ok:
        print('\n编译失败，但日志里没有 "! " 错误，检查 log：%s' % log)
        return 1
    print('编译通过。警告 %d 条（多为 overfull box，可忽略，但图超出页面要修）' % len(warns))
    for w in warns[:5]:
        print('  ' + w)
    return 0


if __name__ == '__main__':
    sys.exit(main())
