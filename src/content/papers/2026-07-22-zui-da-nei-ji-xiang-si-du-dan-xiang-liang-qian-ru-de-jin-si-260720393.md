---
title: Near-Optimal Dimension Lower Bounds for Single-Vector Embeddings of Maximum
  Inner Product Similarity
title_zh: 最大内积相似度单向量嵌入的近似最优维度下界
authors:
- Rajesh Jayaram
- Honghao Lin
- Vahab Mirrokni
- David P. Woodruff
affiliations:
- Google Research
arxiv_id: '2607.20393'
url: https://arxiv.org/abs/2607.20393
pdf_url: https://arxiv.org/pdf/2607.20393
published: '2026-07-22'
collected: '2026-07-25'
category: RecSys
direction: 向量检索嵌入 · 维度理论下界
tags:
- MAX-IP
- Single-Vector Embedding
- Vector Retrieval
- Chamfer Similarity
- Lower Bound
one_liner: 补全MAX-IP单向量嵌入维度下界的指数缺口，逼近现有上界的1/ε²依赖
practical_value: '- 单向量嵌入逼近MAX-IP的维度下限接近m^{O(1/ε²)}，选型时可直接参考该指数关系平衡精度与存储、检索耗时

  - 若业务对MAX-IP近似误差要求高（ε极小），无需强上单向量嵌入，优先选择ColBERT类多向量方案降低维度压力

  - 理论上任意数据依赖的嵌入优化都无法突破该下界，无需浪费算力在无意义的极端维度压缩尝试上'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
多向量嵌入通过Chamfer相似度计算查询与文档的匹配度，单点查询时退化为最大内积相似度（MAX-IP）。现有MUVERA给出的单向量嵌入维度上界为$m^{O(1/\varepsilon^2)}$，但此前的下界仅为$(\varepsilon^2m)^{\Omega(1/\varepsilon)}$，指数在$1/\varepsilon$和$1/\varepsilon^2$之间存在明显缺口。
### 方法关键点
结合Sherstov模式矩阵方法与多项式规模、常数宽度的DNF公式，通过均匀宽度填充、块编码构造$\Omega(\varepsilon)$的误差间隙，再引入哑坐标均衡所有负样本，生成单位球上的MAX-IP矩阵，基于近似秩约束推导维度下界。
### 关键结果
对任意固定$\delta\in(0,1)$，当$\varepsilon$足够小、$m\ge(1/\varepsilon)^{A_\delta}$时，将MAX-IP值逼近到加性误差$\varepsilon$的单向量嵌入维度下界为$m^{c_\delta/\varepsilon^{2-2\delta}}$，$\delta$可任意小，指数逼近上界的$1/\varepsilon^2$依赖，该结论同样适用于Chamfer相似度，且数据依赖的嵌入方案也无法突破该下界。
