---
title: 'Relevance-Based Embeddings: Lightweight Candidate Retrieval via Heavy-Ranker
  Calls'
title_zh: 基于相关性的嵌入：利用重排器调用实现轻量级候选召回
authors:
- Kirill Shevkunov
- Andrey Ploskonosov
- Liudmila Prokhorenkova
affiliations:
- Yandex
arxiv_id: '2607.03515'
url: https://arxiv.org/abs/2607.03515
pdf_url: https://arxiv.org/pdf/2607.03515
published: '2026-07-03'
collected: '2026-07-07'
category: RecSys
direction: 推荐系统召回 · 相关性轻量化嵌入
tags:
- Candidate Retrieval
- Dual Encoder
- Heavy Ranker
- Embedding
- Relevance Modeling
one_liner: 提出利用重排器对预选支持集的相关性得分构造轻量化召回嵌入，效果远超双塔等基线
practical_value: '- 现有推荐/搜索系统可直接复用已上线的精排/重排模型能力构造召回层，无需复杂特征工程，RBE参数量仅数万级，训练成本远低于双塔模型

  - 支持集选择优先尝试KMeans聚类中心策略，性价比最高；电商/内容场景可直接用热门/品类中心的物品作为支持集，几乎无额外成本就能带来召回效果提升

  - 新品冷启动无需重训召回模型，仅需计算新品对固定支持集的重排得分即可生成嵌入加入ANN索引，适配商品/内容频繁更新的业务场景

  - 大规模商品库场景下可先对物品做下采样再选择支持集，对最终效果影响很小，能大幅降低离线预处理的重排调用成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
双塔召回模型采用分离编码，无法利用query-item交叉特征，效果上限远低于交叉结构的精排模型；现有重排器蒸馏方案依然需要大参数量，且缺乏理论保证；此前基于支持集的CUR近似方法采用随机采样支持集，效果仍有较大优化空间。

### 方法关键点
- 用query对预选支持物品、item对预选支持query的重排相关性得分作为基础表征，通过轻量MLP映射为嵌入，理论证明可一致逼近任意连续相关性函数，解决双塔无法利用交叉特征的问题
- 优化支持集选择策略：对比随机、热门、聚类中心、最大多样性、l2-greedy等方案，l2-greedy（最小化CUR近似MSE）效果最优，KMeans聚类中心是无监督场景下的最优性价比选择
- 推理逻辑与双塔完全兼容，item嵌入预计算后存入ANN索引，在线query仅需调用m次（实验取100）重排器得到相关性向量即可生成嵌入，额外开销极低

### 关键结果
- 学术数据集上，RBE+l2-greedy相比基线AnnCUR的HitRate@100最高提升18.9%
- 生产游戏/音乐推荐数据集上，RBE参数量仅约50K，对比参数量300M/700M的生产双塔模型，HitRate@100分别提升4.5%/4.5%，召回Top200时相对增益超过10%
- 仅需100次重排器调用的额外开销，召回效果就超过多消耗100次重排算力的双塔+AXN方案

### 核心结论
复用已有的重排器信号构造召回嵌入，是成本极低、收益极高的召回效果优化路径
