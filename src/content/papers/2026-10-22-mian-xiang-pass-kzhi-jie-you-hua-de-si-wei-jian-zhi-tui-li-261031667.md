---
title: 'Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity
  in Test-Time Reasoning'
title_zh: 面向Pass@k直接优化的思维剪枝：推理时兼顾质量与多样性
authors:
- Mahdi Salmani
- Adel Javanmard
- Devansh Gupta
- Meisam Razaviyayn
affiliations:
- University of Southern California
arxiv_id: '2610.31667'
url: https://arxiv.org/abs/2610.31667
pdf_url: https://arxiv.org/pdf/2610.31667
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: LLM推理优化 · 测试时思维剪枝
tags:
- Test-Time Pruning
- Pass@k
- Reasoning LLM
- Submodular Optimization
- Quality-Diversity Tradeoff
one_liner: 提出直接优化Pass@k的思维剪枝框架PKTP，平衡推理路径质量与多样性，降低测试时算力消耗
practical_value: '- 电商搜索Query改写、商品多候选粗排场景可直接复用PKTP的质量-多样性联合优化逻辑，替代人工调权重的融合方案，提升@k召回率的同时降低候选冗余

  - Agent多工具调用/多路径推理场景可引入PKTP剪枝，动态保留高潜力低冗余的路径，在不降低任务成功率的前提下减少推理token消耗

  - 推荐系统多路召回后粗排阶段，可借鉴其潜变量高斯建模+子模函数贪心优化的工程实现，用低算力成本实现兼顾个性化与多样性的候选集筛选

  - 做best-of-N采样优化时，可复用其联合建模候选相关性与冗余度的损失函数，避免纯质量排序带来的结果同质化问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM测试时缩放策略需生成大量推理路径，全量生成与验证的算力成本极高；现有剪枝方法分为两类：纯质量排序易选择冗余路径导致集体出错，纯多样性排序易浪费算力在低质量路径，两者均未直接优化核心目标Pass@k，需人工调参平衡质量与多样性的tradeoff，适配性差。

### 方法关键点
- 剪枝目标直接定义为最大化保留k条路径的Pass@k（至少1条路径正确的概率），由目标本身自动平衡质量与多样性
- 用潜变量高斯模型建模多条路径的正确性联合分布，捕捉相似路径的错误相关性，推导得到Pass@k的闭式二阶近似，证明其为子模函数，贪心优化可获得(1-1/e)的近似最优解
- 贪心过程支持秩一更新，时间复杂度仅为O(k(Nd + d²))，模型训练完成后可在推理时动态调整k值无需重训

### 关键实验
在8个开源推理模型（0.6B~7B）、多套数学推理基准上测试，对比纯质量剪枝（Linear Probe）、纯多样性剪枝（RepExp）、随机剪枝三个基线：PKTP在k=4时最高比纯质量方法高3.3个百分点，比纯多样性方法高3.2个百分点；所有k≥2的场景下均优于随机剪枝，且前缀越长、候选池越大增益越明显。

### 核心结论
平衡质量与多样性的最优方案不是手动调权重融合两个目标，而是直接优化最终关心的@k业务指标，让目标本身自动实现两者的权衡
