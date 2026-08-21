---
title: 'Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task
  Selection'
title_zh: Task-CoEvolve：通过自适应验证任务选择实现高效Harness优化
authors:
- Atsuyuki Miyai
- Kiyoharu Aizawa
- Toshihiko Yamasaki
affiliations:
- The University of Tokyo
arxiv_id: '2608.20169'
url: https://arxiv.org/abs/2608.20169
pdf_url: https://arxiv.org/pdf/2608.20169
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 框架优化 · Harness 自适应评估
tags:
- Agent Harness Optimization
- Adaptive Task Selection
- Efficient Evaluation
- LLM Agent
- Harness Evolution
one_liner: 提出与Harness协同进化的自适应验证任务选择框架，持平全量性能的同时降低80%评估成本
practical_value: '- 优化电商导购Agent、推荐系统Prompt/Harness迭代的评估流程，用方差加权采样选择最能区分候选版本的验证用例，可降低约80%评估成本，大幅提升迭代效率

  - 跨迭代的候选对比可复用论文的两种全量性能估计算法（Hajek估计/锚定差分估计），无需每次跑全量验证集，还能避免固定验证子集导致的过拟合问题

  - 做A/B测试或候选策略排序时，可借鉴该思路优先把流量/算力分给区分度最高的实验用例/场景，在不降低决策可信度的前提下压缩实验成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent的Harness（控制逻辑、Prompt、检索策略等外围代码）自动迭代时，每轮都需要在全量验证集上评估所有候选，算力/时间成本极高；且随着Harness性能提升，大量全员通过/全员失败的任务完全没有区分度，浪费大量评估资源，现有优化方案均聚焦于候选生成侧效率，未覆盖评估侧的成本压缩空间。
### 方法关键点
- 方差加权任务采样：以每个任务过往成功率的伯努利方差为采样权重，优先采样成功率接近0.5、对候选区分度最高的任务，同时给少样本任务加探索权重，避免遗漏潜在高价值任务
- 采样感知的全量性能估计：根据任务集特性选择估计算法：任务成功率普遍接近0或1用Hajek加权估计，成功率居中用锚定差分估计，保证不同迭代、不同采样子集的候选得分可比
- 属于评估侧插件式优化，无需修改现有Harness自动进化框架逻辑，兼容性强
### 关键实验
- 在线文本分类基准上，仅用7%评估预算即可接近全量验证的性能，20%预算时性能反超全量验证1%
- Terminal-Bench 2.1长序列Agent基准上，仅用20%评估预算即可达到和全量验证持平的效果，整体搜索成本降低67%-80%，迭代时间缩短近一半

> 最值得记住的一句话：Harness迭代时的评估成本优化空间远大于候选生成侧，优先把算力花在能区分候选的验证任务上，性价比最高
