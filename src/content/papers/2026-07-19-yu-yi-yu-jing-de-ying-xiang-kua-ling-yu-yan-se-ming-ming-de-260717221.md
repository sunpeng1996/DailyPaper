---
title: 'Semantic Context Matters: Analysis of Color Names Across Domains'
title_zh: 语义语境的影响：跨领域颜色命名的差异分析
authors:
- Adilet Yerkin
- Elnara Kadyrgali
- Malika Ziyada
- Nuray Toganas
- Muragul Muratbekova
- Ayan Igali
- Aruzhan Sabitkyzy
- Pakizar Shamoi
affiliations:
- Kazakh-British Technical University
arxiv_id: '2607.17221'
url: https://arxiv.org/abs/2607.17221
pdf_url: https://arxiv.org/pdf/2607.17221
published: '2026-07-19'
collected: '2026-07-24'
category: RecSys
direction: 商品推荐 · 跨域颜色语义属性建模
tags:
- color naming
- context-aware
- cross-domain
- semantic similarity
- recommendation system
one_liner: 通过COLIBRI模型量化三类领域颜色命名的语境差异，验证语义语境对颜色感知的显著作用
practical_value: '- 电商商品属性标注可按品类构建独立颜色词库，比如彩妆类侧重暖调色名、汽车类侧重蓝/无彩色系命名，提升搜索/推荐的语义匹配准确率

  - 跨域商品搜索/推荐的颜色相似度计算不能仅依赖RGB/HSV等数值距离，需叠加对应领域的语义权重修正匹配结果

  - 可复用论文的类别覆盖率、Shannon entropy、最大lift指标体系，评估不同品类颜色词库的覆盖度与合理性，优化属性运营策略'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有颜色建模多依赖RGB、HSV等数值空间的相似度计算，未考虑语义语境差异，导致同色异名/同名异色问题在跨品类商品搜索、推荐场景匹配准确率低。
### 方法关键点
将彩妆、绘儿乐蜡笔、汽车三类领域的颜色名称数据集，映射到COLIBRI颜色模型的86个模糊颜色类别上，采用类别覆盖率、Shannon entropy、最大lift三个指标量化跨域颜色命名的语境差异。
### 关键结果数字
三类领域对COLIBRI颜色空间的覆盖度差异显著：彩妆覆盖48/86类、蜡笔覆盖50/86类、汽车仅覆盖40/86类；蜡笔的颜色空间使用最均衡，彩妆集中在暖色调区域，汽车颜色集中在蓝色与无彩色区域，验证了语义语境对颜色解释的影响远高于数值相似度。
