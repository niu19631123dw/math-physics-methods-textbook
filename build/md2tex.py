#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把本讲义 Markdown 转成 XeLaTeX 正文。只处理本书用到的子集。"""
import re, io, sys, os

CHAPTERS = ['00-导论.md', '01-振动与波.md', '02-圆与球.md',
            '03-点源与响应.md', '04-留数定理.md', '05-变换.md',
            '06-变分法.md', '07-张量与黎曼几何.md']
APPENDICES = ['附录A-数学约定.md', '附录B-判断清单.md',
              '附录C-数值演示.md', '附录D-计算题答案.md',
              '附录E-矢量微积分.md', '附录F-特殊函数速查.md',
              '附录G-母题对照.md']

UNICODE_MATH = {
    '→': r'$\to$', '⇒': r'$\Rightarrow$', '⇔': r'$\Leftrightarrow$',
    '≠': r'$\neq$', '≈': r'$\approx$', '≥': r'$\geq$', '≤': r'$\leq$',
    '×': r'$\times$', '·': r'$\cdot$', '∞': r'$\infty$', '±': r'$\pm$',
    '∂': r'$\partial$', '∇': r'$\nabla$', '∫': r'$\int$',
    '∑': r'$\sum$', '∮': r'$\oint$', '∼': r'$\sim$', '≪': r'$\ll$',
    '≫': r'$\gg$', '∝': r'$\propto$', '∈': r'$\in$', '√': r'$\surd$',
    '…': r'\dots{}', '°': r'$^\circ$',
    'α': r'$\alpha$', 'β': r'$\beta$', 'γ': r'$\gamma$', 'δ': r'$\delta$',
    'ε': r'$\varepsilon$', 'ζ': r'$\zeta$', 'η': r'$\eta$', 'θ': r'$\theta$',
    'ι': r'$\iota$', 'κ': r'$\kappa$', 'λ': r'$\lambda$', 'μ': r'$\mu$',
    'ν': r'$\nu$', 'ξ': r'$\xi$', 'π': r'$\pi$', 'ρ': r'$\rho$',
    'σ': r'$\sigma$', 'τ': r'$\tau$', 'υ': r'$\upsilon$', 'φ': r'$\varphi$',
    'χ': r'$\chi$', 'ψ': r'$\psi$', 'ω': r'$\omega$',
    'Γ': r'$\Gamma$', 'Δ': r'$\Delta$', 'Θ': r'$\Theta$', 'Λ': r'$\Lambda$',
    'Ξ': r'$\Xi$', 'Π': r'$\Pi$', 'Σ': r'$\Sigma$', 'Φ': r'$\Phi$',
    'Ψ': r'$\Psi$', 'Ω': r'$\Omega$',
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

def inline_core(s):
    toks = []
    def stash(x):
        toks.append(x)
        return '\x03%d\x03' % (len(toks) - 1)
    s = re.sub(r'`([^`]+)`', lambda m: stash(r'\texttt{' + escape_text(m.group(1)) + '}'), s)
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

def convert_table(rows):
    parsed = [split_row(r) for r in rows]
    n = len(parsed[0])
    body = [r for r in parsed[1:]
            if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
    first_narrow = parsed[0][0].strip() == '编号'
    if n == 2:
        widths = [0.28, 0.63]
    elif n == 3:
        f = 0.11 if first_narrow else 0.22
        widths = [f, (0.92 - f) * 0.58, (0.92 - f) * 0.42]
    elif n == 4:
        widths = [0.16, 0.26, 0.26, 0.23]
    else:
        widths = [0.12] + [0.87 / (n - 1)] * (n - 1)
    spec = '@{}' + ''.join(r'p{%.3f\linewidth}' % w for w in widths) + '@{}'
    L = [r'{\small\renewcommand{\arraystretch}{1.15}\setlength{\tabcolsep}{4pt}',
         r'\begin{longtable}{' + spec + '}', r'\toprule']
    L.append(' & '.join(inline(c) for c in parsed[0]) + r' \\')
    L += [r'\midrule', r'\endhead']
    for r in body:
        r = r + [''] * (n - len(r))
        L.append(' & '.join(inline(c) for c in r[:n]) + r' \\')
    L += [r'\bottomrule', r'\end{longtable}}']
    return '\n'.join(L)

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
        if s.startswith('# '):
            title = re.sub(r'^第\s*\d+\s*章\s*', '', s[2:].strip())
            title = re.sub(r'^附录\s*[A-Z]\s*', '', title)
            out.append(r'\chapter{' + inline(title) + '}')
            i += 1
            continue
        if s.startswith('## '):
            t = s[3:].strip()
            t = re.sub(r'^[0-9A-Z]+(?:\.[0-9]+)+\s+', '', t)
            out.append(r'\section{' + inline(t) + '}')
            i += 1
            continue
        if s.startswith('### '):
            out.append(r'\subsection{' + inline(s[4:].strip()) + '}')
            i += 1
            continue
        if s == '---':
            out.append(r'\par\medskip')
            i += 1
            continue
        if s.startswith('![') and '(figs/' in s and s.endswith('.tex)'):
            path = s.split('(', 1)[1].rstrip(')')
            out.append(r'\input{' + path[:-4] + '}')
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
            out.append(r'\begin{itemize}[leftmargin=2em,itemsep=0.2em]')
            out += [r'\item ' + inline(b) for b in buf]
            out.append(r'\end{itemize}')
            continue
        if re.match(r'^\d+\. ', s):
            buf = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
                buf.append(re.sub(r'^\d+\. ', '', lines[i].strip()))
                i += 1
            out.append(r'\begin{enumerate}[leftmargin=2em,itemsep=0.2em]')
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
                    or nxt.startswith('$$')
                    or nxt == '---' or re.match(r'^[-*] ', nxt)
                    or re.match(r'^\d+\. ', nxt)):
                break
            buf.append(nxt)
            i += 1
        out.append(inline(' '.join(buf)))
        out.append('')
    return '\n'.join(out)

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    src = os.path.dirname(base)
    def build(names):
        chunks = []
        for n in names:
            p = os.path.join(src, n)
            txt = io.open(p, encoding='utf-8').read().splitlines()
            txt = [l for l in txt if not any(k in l for k in SKIP_NAV)]
            chunks.append(convert(txt))
        return '\n\n'.join(chunks)
    io.open(os.path.join(base, 'body.tex'), 'w', encoding='utf-8').write(build(CHAPTERS))
    io.open(os.path.join(base, 'appendix.tex'), 'w', encoding='utf-8').write(build(APPENDICES))
    print('ok')

if __name__ == '__main__':
    main()
