#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把人名公式统一改成中文规范译名：python build/zhnames.py [文件或目录...]

默认处理仓库根目录的所有章节 md、附录 md，以及 build/figs/*.tex。
可以重复运行（幂等）。
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAIRS = [
    ("Cole–Cole", "科尔–科尔"),
    ("Johnson–Nyquist", "约翰逊–奈奎斯特"),
    ("Breit–Wigner", "布赖特–维格纳"),
    ("Condon–Shortley", "科顿–肖特利"),
    ("Lorentz", "洛伦兹"),
    ("Matsubara", "松原"),
    ("Yukawa", "汤川"),
    ("Drude", "德鲁德"),
    ("Hilbert", "希尔伯特"),
    ("Goldstone", "戈德斯通"),
    ("Madelung", "马德隆"),
    ("Clairaut", "克莱罗"),
    ("Frobenius", "弗罗贝尼乌斯"),
    ("Maxwell", "麦克斯韦"),
    ("Balmer", "巴耳末"),
    ("Rodrigues", "罗德里格斯"),
    ("Kummer", "库默尔"),
    ("Robin", "罗宾"),
    ("Hadamard", "阿达马"),
    ("Parseval", "帕塞瓦尔"),
    ("Gibbs", "吉布斯"),
    ("Bohr", "玻尔"),
    ("Fermi", "费米"),
    ("Bose", "玻色"),
    ("Heaviside", "赫维赛德"),
    ("Kirchhoff", "基希霍夫"),
    ("Sommerfeld", "索末菲"),
    ("Doppler", "多普勒"),
    ("Kepler", "开普勒"),
    ("Compton", "康普顿"),
    ("Rutherford", "卢瑟福"),
    ("Snell", "斯涅尔"),
    ("Bragg", "布拉格"),
    ("Wiener", "维纳"),
    ("Debye", "德拜"),
    ("Volterra", "沃尔泰拉"),
    ("Duhamel", "杜阿梅尔"),
    ("Clausius", "克劳修斯"),
    ("Onsager", "昂萨格"),
    ("Langevin", "朗之万"),
    ("Landau", "朗道"),
    ("Levinson", "莱文森"),
    ("Wentzel", "温策尔"),
    ("Brillouin", "布里渊"),
    ("Kramers–Kronig", "克拉默斯–克罗尼格"),
    ("Kramers-Kronig", "克拉默斯–克罗尼格"),
    ("Sturm–Liouville", "施图姆–刘维尔"),
    ("Sturm-Liouville", "施图姆–刘维尔"),
    ("Euler–Lagrange", "欧拉–拉格朗日"),
    ("Euler-Lagrange", "欧拉–拉格朗日"),
    ("d'Alembert", "达朗贝尔"),
    ("D'Alembert", "达朗贝尔"),
    ("Fourier–Bessel", "傅里叶–贝塞尔"),
    ("Fourier-Bessel", "傅里叶–贝塞尔"),
    ("Fourier", "傅里叶"),
    ("Laplace", "拉普拉斯"),
    ("Poisson", "泊松"),
    ("Green", "格林"),
    ("Gauss", "高斯"),
    ("Stokes", "斯托克斯"),
    ("Cauchy", "柯西"),
    ("Laurent", "洛朗"),
    ("Taylor", "泰勒"),
    ("Maclaurin", "麦克劳林"),
    ("Rouché", "儒歇"),
    ("Rouche", "儒歇"),
    ("Jordan", "若尔当"),
    ("Bessel", "贝塞尔"),
    ("Neumann", "诺伊曼"),
    ("Hankel", "汉克尔"),
    ("Legendre", "勒让德"),
    ("Laguerre", "拉盖尔"),
    ("Hermite", "埃尔米特"),
    ("Jacobi", "雅可比"),
    ("Dirichlet", "狄利克雷"),
    ("Joukowski", "儒可夫斯基"),
    ("Zhukovsky", "儒可夫斯基"),
    ("Kutta", "库塔"),
    ("Magnus", "马格努斯"),
    ("Bernoulli", "伯努利"),
    ("Euler", "欧拉"),
    ("Lagrange", "拉格朗日"),
    ("Beltrami", "贝尔特拉米"),
    ("Fermat", "费马"),
    ("Rayleigh", "瑞利"),
    ("Ritz", "里兹"),
    ("Newton", "牛顿"),
    ("Einstein", "爱因斯坦"),
    ("Christoffel", "克里斯托费尔"),
    ("Riemann", "黎曼"),
    ("Ricci", "里奇"),
    ("Fresnel", "菲涅耳"),
    ("Helmholtz", "亥姆霍兹"),
    ("Schrödinger", "薛定谔"),
    ("Schrodinger", "薛定谔"),
    ("Boltzmann", "玻尔兹曼"),
    ("Planck", "普朗克"),
    ("Stirling", "斯特林"),
    ("Noether", "诺特"),
    ("Hamilton", "哈密顿"),
    ("Poynting", "坡印廷"),
    ("Debye", "德拜"),
    ("Wronskian", "朗斯基行列式"),
    ("Airy", "艾里"),
    ("Abel", "阿贝尔"),
    ("Dirac", "狄拉克"),
]

# 残留检测（正文里出现即违规）
PAT = re.compile(r'(?<![A-Za-z\\])(' + '|'.join(sorted({p[0] for p in PAIRS}, key=len, reverse=True)) + r')(?![A-Za-z])')


def fix_text(s):
    for a, b in PAIRS:
        s = s.replace(a, b)
    # 去掉紧跟译名的英文括注，如「傅里叶（Fourier）」
    s = re.sub(r'（\s*(?:' + '|'.join({p[0] for p in PAIRS}) + r')[^）]*）', '', s)
    s = re.sub(r'\(\s*(?:' + '|'.join({p[0] for p in PAIRS}) + r')[^)]*\)', '', s)
    # 中文之间、中文与标点之间的多余空格
    s = re.sub(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', '', s)
    s = re.sub(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[，。；：、！？（）《》“”‘’—])', '', s)
    s = re.sub(r'(?<=[，。；：、！？（）《》“”‘’—])[ \t]+(?=[\u4e00-\u9fff])', '', s)
    return s


def process(path, dry=False):
    txt = io.open(path, encoding='utf-8').read()
    new = fix_text(txt)
    if new != txt:
        if not dry:
            io.open(path, 'w', encoding='utf-8').write(new)
        return True
    return False


def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    args = [a for a in args if a != '--dry']
    targets = []
    if not args:
        for n in os.listdir(ROOT):
            if n.endswith('.md') and n != '写作规范.md':
                targets.append(os.path.join(ROOT, n))
        figd = os.path.join(ROOT, 'build', 'figs')
        if os.path.isdir(figd):
            for n in os.listdir(figd):
                if n.endswith('.tex'):
                    targets.append(os.path.join(figd, n))
        pre = os.path.join(ROOT, 'build', 'preface.tex')
        if os.path.exists(pre):
            targets.append(pre)
    else:
        for a in args:
            p = a if os.path.isabs(a) else os.path.join(ROOT, a)
            if os.path.isdir(p):
                for n in os.listdir(p):
                    if n.endswith(('.md', '.tex')):
                        targets.append(os.path.join(p, n))
            else:
                targets.append(p)
    changed = 0
    for t in targets:
        if process(t, dry):
            changed += 1
            print(('would fix ' if dry else 'fixed ') + os.path.basename(t))
    print('共 %d 个文件%s' % (changed, '需要改' if dry else '已改'))

    # 残留
    left = []
    for t in targets:
        txt = io.open(t, encoding='utf-8').read()
        for i, ln in enumerate(txt.splitlines(), 1):
            m = PAT.search(ln)
            if m:
                left.append('%s:%d  %s' % (os.path.basename(t), i, m.group(1)))
    if left:
        print('仍有外文人名 %d 处：' % len(left))
        for l in left[:20]:
            print('  ' + l)


if __name__ == '__main__':
    main()
