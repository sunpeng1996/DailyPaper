---
title: 'Elicitation without Backpropagation: Steering Model Behavior by Optimizing
  the Latent Posterior'
title_zh: 无需反向传播的Transformer行为引导：基于隐后验优化的prompt生成
authors:
- Garrett Baker
- Vinayak Pathak
- Daniel Murfet
- Susan Wei
affiliations:
- Timaeus
- CORAL
- Monash University
arxiv_id: '2607.18804'
url: https://arxiv.org/abs/2607.18804
pdf_url: https://arxiv.org/pdf/2607.18804
published: '2026-07-21'
collected: '2026-07-23'
category: LLM
direction: LLM行为调控 · 无反向传播prompt优化
tags:
- prefix tuning
- latent posterior
- Bayesian Transformer
- gradient-free optimization
- model steering
one_liner: 提出后验前缀调优PPT方法，无需反向传播即可基于隐后验优化生成高期望效用的prompt
practical_value: '- 多目标文案生成场景（如广告卖点、推荐理由、商品标题生成需同时满足点击率、合规性、相关性等多效用目标）可复用PPT的一次预采样、多效用零边际成本优化思路，大幅降低大模型调用开销

  - 黑盒LLM调用场景（仅能通过API访问大模型、无法获取梯度）可借鉴Predictive Monte Carlo仅用前向采样提取模型隐先验的方法，实现无梯度高效prompt优化

  - 生成式推荐的Semantic ID prompt调优场景可参考PPT的「连续参数空间优化+离散硬prompt映射」范式，平衡优化效率与工程落地兼容性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有prompt优化方法（如GCG）每步都需要反向传播过Transformer，计算开销极高，且每类效用目标都需要单独优化，无法复用中间计算结果；同时离散prompt空间规模随长度指数级增长，无法穷举搜索，在模型安全测试、多目标内容生成等场景效率极低，难以快速找到能引导模型输出高期望效用的prompt。
### 方法关键点
- 基于贝叶斯过滤Transformer（BFT）的隐后验分解特性，将离散prompt空间的优化目标映射到连续隐后验空间，避免遍历token组合
- 设计Predictive Monte Carlo（PMC）：仅通过Transformer前向采样一次性提取模型隐先验样本，采样过程与效用函数完全无关，可复用支撑任意数量效用目标的优化
- 设计后验前缀调优（PPT）：通过重要性采样估计目标梯度，优化全程无Transformer前向/反向调用，仅需操作预采样的隐先验样本，优化完成后将连续参数映射为可用的硬prompt
### 关键实验
在Beta-Bernoulli、强化瓮两类BFT上测试3类效用函数（反向交叉熵、频率匹配、Dyck有效性），对比基线GCG：
1. 短prompt（长度6）场景下，PPT-RB在强化瓮BFT的Dyck有效性任务上所有种子都达到全局最优，反向交叉熵任务上prompt平均排名1-3，远优于GCG的5-16名
2. 长prompt（长度50）场景下，PPT在强化瓮BFT的反向交叉熵任务上目标值比GCG高1~1.9
### 核心记忆点
对于满足隐后验分解特性的Transformer，一次无梯度前向采样即可支撑任意多效用的prompt优化，边际成本几乎为零。
