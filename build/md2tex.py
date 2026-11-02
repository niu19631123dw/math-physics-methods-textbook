#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""把本讲义 Markdown 转成 XeLaTeX 正文（v2）。

支持的 Markdown 子集（只做本书用到的部分）：
  # / ## / ### / ####      标题（章节号由 LaTeX 自动编号）
  **粗体**                  -> \textbf
  `代码`                    -> \texttt
  $$ ... $$                 -> \[ ... \]
  > 引用                    -> quote
  | 表格 |                  -> longtable（列宽按内容长度自适应）
  - / 1. 列表               -> itemize / enumerate
  ``` 代码块                -> lstlisting
  ![alt](figs/x.tex "图注") -> figure 环境（自动编号 + 图注）
"""
import re, io, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')

CHAPTERS = [
    '00-导论.md',
    '01-振动的弦.md',
    '02-分离变量.md',
    '03-圆形的振动.md',
    '04-球形的世界.md',
    '05-点源与响应.md',
    '06-复平面上的捷径.md',
    '07-把圆掰成翅膀.md',
    '08-分解与因果.md',
    '09-自然选择极值.md',
    '10-弯曲时空的算术.md',
]

APPENDICES = [
    '附录A-数学约定.md',
    '附录B-判断点总表.md',
    '附录C-习题详解.md',        # 由 build/answers/*.md 自动拼接
    '附录D-矢量微积分.md',
    '附录E-特殊函数速查.md',
    '附录F-母题对照.md',
]

UNICODE_MATH = {
    '→': r'$\to$', '⇒': r'$\Rightarrow$', '⇔': r'$\Leftrightarrow$',
    '≠': r'$\neq$', '≈': r'$\approx$', '≥': r'$\geq$', '≤': r'$\leq$',
    '×': r'$\times$', '·': r'$\cdot$', '∞': r'$\infty$', '±': r'$\pm$',
    '∂': r'$\partial$', '∫': r'$\int$',
    '∑': r'$\sum$', '∮': r'$\oint$', '∼': r'$\sim$', '≪': r'$\ll$',
    '≫': r'$\gg$', '∝': r'$\propto$', '∈': r'$\in$', '√': r'$\surd$',
    '°': r'$^\circ$',
    'α': r'$\alpha$', 'β': r'$\beta$', 'γ': r'$\gamma$', 'δ': r'$\delta$',
    'ε': r'$\varepsilon$', 'ζ': r'$\zeta$', 'η': r'$\eta$', 'θ': r'$\theta$',
    'ι': r'$\iota$', 'κ': r'$\kappa$', 'λ': r'$\lambda$', 'μ': r'$\mu$',
    'ν': r'$\nu$', 'ξ': r'$\xi$', 'π': r'$\pi$', 'ρ': r'$\rho$',
    'σ': r'$\sigma$', 'τ': r'$\tau$', 'φ': r'$\varphi$',
    'χ': r'$\chi$', 'ψ': r'$\psi$', 'ω': r'$\omega$',
    'Γ': r'$\Gamma$', 'Δ': r'$\Delta$', 'Θ': r'$\Theta$', 'Λ': r'$\Lambda$',
    'Ξ': r'$\Xi$', 'Π': r'$\Pi$', 'Σ': r'$\Sigma$', 'Φ': r'$\Phi$',
    'Ψ': r'$\Psi$', 'Ω': r'$\Omega$',
    # 多字符优先：∇² 必须在 ∇ 与 ² 之前
    '∇²': r'$\nabla^2$', '∇': r'$\nabla$',
    '²': r'$^2$', '³': r'$^3$',
    'Å': r'$\mathrm{\AA}$',
    '✔': r'$\checkmark$', '✓': r'$\checkmark$',
    '✘': r'$\times$', '✗': r'$\times$',
}


def escape_text(s):
    s = s.replace('\\', '\x02')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}')]:
        s = s.replace(a, b)
    s = s.replace('~', r'\textasciitilde{}').replace('^', r'\textasciicircum{}')
    s = s.replace('\x02', r'\textbackslash{}')
    for a, b in UNICODE_MATH.items():
        s = s.replace(a, b)
    s = s.replace('…', r'\dots{}').replace('—', '——').replace('–', '--')
    return s


def inline_core(s):
    s = re.sub(r'—{2,}', '—', s)
    toks = []

    def stash(x):
        toks.append(x)
        return '\x03%d\x03' % (len(toks) - 1)

    s = re.sub(r'`([^`]+)`', lambda m: stash(r'\texttt{' + escape_text(m.group(1)) + '}'), s)
    # 行内出现的 $$...$$（作者把行间公式写在句子中间）：先抠出来，避免被单 $ 切碎
    s = re.sub(r'\$\$(.+?)\$\$', lambda m: stash(r'\[' + m.group(1).strip() + r'\]'), s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', lambda m: stash(inline(m.group(1))), s)
    segs = re.split(r'(?<!\\)\$', s)
    out = []
    for i, seg in enumerate(segs):
        if i % 2 == 1:
            out.append('$' + seg + '$')
        else:
            out.append(escape_text(seg))
    s = ''.join(out)
    for i, t in enumerate(toks):
        s = s.replace('\x03%d\x03' % i, t)
    return s


def inline(s):
    parts = s.split('**')
    if len(parts) == 1:
        return inline_core(s)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(r'\textbf{' + inline_core(p) + '}')
        else:
            out.append(inline_core(p))
    return ''.join(out)


def strip_cjk_comment(line):
    if '#' in line:
        head, _, tail = line.partition('#')
        if any('\u4e00' <= c <= '\u9fff' for c in tail):
            return head.rstrip()
    return line


def split_row(r):
    r = r.strip()
    if r.startswith('|'):
        r = r[1:]
    if r.endswith('|'):
        r = r[:-1]
    cells, cur, inmath, i = [], '', False, 0
    while i < len(r):
        c = r[i]
        if c == '$' and (i == 0 or r[i - 1] != '\\'):
            inmath = not inmath
            cur += c
        elif c == '|' and not inmath:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += c
        i += 1
    cells.append(cur.strip())
    return cells


def text_width(s):
    """CJK 计 2，其余计 1。用于估算列宽。"""
    n = 0
    for c in s:
        n += 2 if '\u4e00' <= c <= '\u9fff' else 1
    return n


def convert_table(rows):
    parsed = [split_row(r) for r in rows]
    n = len(parsed[0])
    body = [r for r in parsed[1:]
            if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
    # 按内容自适应列宽
    weights = []
    for j in range(n):
        w = max(text_width(r[j]) if j < len(r) else 0 for r in parsed)
        weights.append(max(w, 4) ** 0.5)     # 开方，压缩长短差距
    total = sum(weights)
    raw = [w / total for w in weights]
    raw = [max(0.09, x) for x in raw]
    scale = 0.94 / sum(raw)
    widths = [x * scale for x in raw]
    spec = '@{}' + ''.join(r'p{%.3f\linewidth}' % w for w in widths) + '@{}'
    L = [r'{\small\renewcommand{\arraystretch}{1.18}\setlength{\tabcolsep}{4pt}',
         r'\begin{longtable}{' + spec + r'}', r'\toprule']
    L.append(' & '.join(inline(c) for c in parsed[0]) + r' \\')
    L += [r'\midrule', r'\endhead']
    for r in body:
        r = r + [''] * (n - len(r))
        L.append(' & '.join(inline(c) for c in r[:n]) + r' \\')
    L += [r'\bottomrule', r'\end{longtable}}']
    return '\n'.join(L)


FIG_RE = re.compile(r'^!\[[^\]]*\]\(\s*(figs/[^)\s"]+\.tex)\s*(?:"([^"]*)")?\s*\)\s*$')

SKIP_NAV = ('**上一章**', '**下一章**')


def convert(lines):
    out, i = [], 0
    while i < len(lines):
        raw = lines[i].rstrip('\n')
        s = raw.strip()
        if not s:
            out.append('')
            i += 1
            continue
        if s.startswith('<!--'):
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            i += 1
            continue
        if s.startswith('```'):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i].rstrip('\n'))
                i += 1
            i += 1
            out.append(r'\begin{lstlisting}')
            out += [strip_cjk_comment(b) for b in buf]
            out.append(r'\end{lstlisting}')
            continue
        m = FIG_RE.match(s)
        if m:
            path, cap = m.group(1), m.group(2) or ''
            out.append(r'\begin{figure}[htbp]')
            out.append(r'\centering')
            out.append(r'\input{' + path[:-4] + '}')
            out.append(r'\caption{' + inline(cap) + '}')
            out.append(r'\end{figure}')
            i += 1
            continue
        if s.startswith('#### '):
            out.append(r'\subsubsection{' + inline(re.sub(r'^[0-9A-Z]+(?:\.[0-9]+)+\s+', '', s[5:].strip())) + '}')
            i += 1
            continue
        if s.startswith('### '):
            hd = re.sub(r'^[0-9A-Z]+(?:\.[0-9]+)+\s*', '', s[4:].strip())
            if re.match(r'^[ABCD]\s*组|^概念|^判断', hd):
                out.append(r'\subsection*{' + inline(hd) + '}')
            else:
                out.append(r'\subsection{' + inline(hd) + '}')
            i += 1
            continue
        if s.startswith('## '):
            t = re.sub(r'^[0-9A-Z]+(?:\.[0-9]+)+\s*', '', s[3:].strip())
            out.append(r'\section{' + inline(t) + '}')
            i += 1
            continue
        if s.startswith('# '):
            title = re.sub(r'^第\s*[0-9]+\s*章\s*', '', s[2:].strip())
            title = re.sub(r'^附录\s*[A-Z]\s*', '', title)
            out.append(r'\chapter{' + inline(title) + '}')
            i += 1
            continue
        if s == '---':
            out.append(r'\medskip')
            i += 1
            continue
        if s.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(r'\begin{quote}\small ' + inline(' '.join(buf)) + r'\end{quote}')
            continue
        if s.startswith('|'):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                buf.append(lines[i].strip())
                i += 1
            out.append(convert_table(buf))
            continue
        if re.match(r'^[-*] ', s):
            buf = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i].strip()):
                buf.append(lines[i].strip()[2:])
                i += 1
            out.append(r'\begin{itemize}[leftmargin=2em,itemsep=0.25em]')
            out += [r'\item ' + inline(b) for b in buf]
            out.append(r'\end{itemize}')
            continue
        if re.match(r'^\d+\. ', s):
            buf = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
                buf.append(re.sub(r'^\d+\. ', '', lines[i].strip()))
                i += 1
            out.append(r'\begin{enumerate}[leftmargin=2em,itemsep=0.25em]')
            out += [r'\item ' + inline(b) for b in buf]
            out.append(r'\end{enumerate}')
            continue
        if s.startswith('$$'):
            first = s[2:]
            if first.endswith('$$') and first != '$$':
                out.append(r'\[' + first[:-2] + r'\]')
                i += 1
                continue
            buf = [first]
            i += 1
            while i < len(lines):
                l = lines[i].strip()
                if l.endswith('$$'):
                    buf.append(l[:-2])
                    i += 1
                    break
                buf.append(l)
                i += 1
            out.append(r'\[' + '\n'.join(buf) + r'\]')
            continue
        buf = [s]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith('#') or nxt.startswith('|')
                    or nxt.startswith('```') or nxt.startswith('>')
                    or nxt.startswith('$$') or nxt.startswith('![')
                    or nxt == '---' or re.match(r'^[-*] ', nxt)
                    or re.match(r'^\d+\. ', nxt)):
                break
            buf.append(nxt)
            i += 1
        out.append(inline(' '.join(buf)))
        out.append('')
    return '\n'.join(out)


def build_answers():
    """把 build/answers/chNN.md 拼成附录 C 的 Markdown 文本。

    各章答案文件开头的标题（# 或 ##）统一替换成二级标题，避免每一章
    都被 LaTeX 当成一个 appendix。
    """
    d = os.path.join(BUILD, 'answers')
    parts = ['# 附录 C 习题详解',
             '',
             '> 每题给关键步骤、中间结果和最终答案。缺的步骤请自己补全后再看。',
             '']
    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not name.endswith('.md'):
            continue
        try:
            num = int(name[2:4])
        except ValueError:
            continue
        lines = io.open(os.path.join(d, name), encoding='utf-8').read().splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and lines[0].lstrip().startswith('#'):
            lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
        parts.append('## 第 %d 章' % num)
        parts.append('')
        parts.extend(lines)
        parts.append('')
    return '\n'.join(parts)


def build(names, answers=False):
    """answers=True 时，只有 附录D 由 build/answers/*.md 自动拼接，其余照常读文件。"""
    chunks = []
    for n in names:
        if answers and n == '附录C-习题详解.md':
            txt = build_answers().splitlines()
        else:
            p = os.path.join(ROOT, n)
            if not os.path.exists(p):
                sys.stderr.write('MISSING %s\n' % n)
                continue
            txt = io.open(p, encoding='utf-8').read().splitlines()
        txt = [l for l in txt if not any(k in l for k in SKIP_NAV)]
        chunks.append(convert(txt))
    return '\n\n'.join(chunks)


def main():
    io.open(os.path.join(BUILD, 'body.tex'), 'w', encoding='utf-8').write(build(CHAPTERS))
    io.open(os.path.join(BUILD, 'appendix.tex'), 'w', encoding='utf-8').write(build(APPENDICES, answers=True))
    print('md2tex: body.tex + appendix.tex ok')


if __name__ == '__main__':
    main()
