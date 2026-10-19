# -*- coding: utf-8 -*-
import io

ORDER = ['README.md', '00-导论.md', '01-振动与波.md', '02-圆与球.md',
         '03-点源与响应.md', '04-留数定理.md', '05-变换.md', '06-变分法.md', '07-张量与黎曼几何.md',
         '附录A-数学约定.md', '附录B-判断清单.md', '附录C-数值演示.md',
         '附录D-计算题答案.md', '附录E-矢量微积分.md',
         '附录F-特殊函数速查.md', '附录G-母题对照.md']

out = []
for f in ORDER:
    lines = io.open(f, encoding='utf-8').read().splitlines()
    kept = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith('**上一章**') or s.startswith('**下一章**'):
            continue
        kept.append(ln)
    # 去掉章节末尾的 --- 与空行
    while kept and not kept[-1].strip():
        kept.pop()
    if kept and kept[-1].strip() == '---':
        kept.pop()
        while kept and not kept[-1].strip():
            kept.pop()
    out.append('\n'.join(kept).strip())

io.open('数理方法讲义-全文.md', 'w', encoding='utf-8').write('\n\n'.join(out) + '\n')
print('combined ok')
