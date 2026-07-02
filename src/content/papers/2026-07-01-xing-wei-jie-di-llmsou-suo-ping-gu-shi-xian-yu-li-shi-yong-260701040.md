---
title: 'As It Was: Aligning LLM Search Evaluation with Historical User Preferences'
title_zh: 行为接地LLM搜索评估：实现与历史用户偏好的对齐
authors:
- Ali Vardasbi
- Gustavo Penha
- Enrico Palumbo
- Claudia Hauff
- Hugues Bouchard
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2607.01040'
url: https://arxiv.org/abs/2607.01040
pdf_url: https://arxiv.org/pdf/2607.01040
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: LLM搜索评估 · 行为接地
tags:
- LLM-as-judge
- behavioral grounding
- search evaluation
- user preference alignment
- QRI card
one_liner: 通过轻量历史交互QRI卡片，提升LLM搜索评估与用户偏好、线上A/B结果的对齐度
practical_value: '- 做LLM-as-judge评估搜索/推荐效果时，可直接复用QRI卡设计：将待评估item的历史相似query的去偏相关性、曝光量做成结构化卡片喂给LLM，无需额外训练即可提升评估和用户偏好的对齐度

  - 歧义query/长尾意图评估场景可参考QRI卡的预处理逻辑：用IPS校正历史交互的位置偏置，再按与当前query的语义相似度排序取Top-k，兼顾prompt长度控制与证据有效性

  - 线下评估与线上A/B对齐场景可优先在语义推理分歧case启用行为接地策略：实验显示分歧case下对齐度提升最显著，可大幅减少线下评估与线上结果的错配'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产环境搜索/推荐系统迭代速度远超人工评估的扩展上限，尤其难以覆盖长尾意图、多语言query；仅依赖语义相似度与常识的纯语义LLM-as-judge，对歧义query、地域化特殊偏好的判断容易偏离真实用户行为，与线上A/B测试结果对齐度低，亟需低成本、高可靠性的规模化评估方案。

### 方法关键点
- 对比基线为仅输入query、上下文、item元数据的纯语义LLM judge，改进版为每个SERP item新增QRI（Query-Relevance-Impressions）行为先验卡
- QRI卡基于历史搜索日志构建：用IPS（逆倾向得分）校正位置偏置得到「历史相似query-去偏相关性-曝光量」三元组，按与当前query的语义相似度取Top-10，同时过滤相似度>0.9的近重复query避免数据泄露，控制prompt长度
- 明确要求LLM将QRI作为辅助行为证据而非直接真值，仅在歧义场景做决策参考。

### 关键结果
- 在Spotify 6000条重组SERP的日志标注数据集上，Spearman秩相关系数整体提升5%，两类法官的分歧case下相对提升91%
- 在5种语言265条人工标注数据集上，与人工判断的相关系数相对提升15%
- 线上A/B测试对齐实验中，与线上获胜模型的对齐率从30.6%提升至36.8%，统计显著

### 核心结论
轻量行为接地无需修改LLM本身，仅通过prompt注入结构化历史交互证据，就能显著提升LLM评估的实用性，尤其在语义推理不足以解决的歧义场景效果最优。
