---
title: Distribution Matching Distillation for Continuous Diffusion Language Models
title_zh: 面向连续扩散语言模型的分布匹配蒸馏方法
authors:
- Paul Le Van Kiem
- Dario Shariatian
- Umut Simsekli
- Alain Durmus
affiliations:
- Inria
- PSL Research University
- Cohere
- Ecole Polytechnique
arxiv_id: '2609.40235'
url: https://arxiv.org/abs/2609.40235
pdf_url: https://arxiv.org/pdf/2609.40235
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: 扩散语言模型 · 蒸馏加速
tags:
- Diffusion LM
- Knowledge Distillation
- Sampling Acceleration
- Distribution Matching
- Reverse KL
one_liner: 提出两种互补的分布匹配蒸馏方法，大幅降低连续扩散语言模型的采样成本
practical_value: '- 线上低延迟生成场景（如实时推荐文案、搜索联想词生成）可复用Simplex-DMD方案，仅4次NFE即可将生成质量相对基线提升49%，满足
  latency 要求

  - 离线批量生成场景（如批量生成商品描述、营销素材）可采用Reinforce-DMD方案，256次NFE下生成PPL相对基线降低20%，兼顾质量与多样性

  - 扩散类生成模型蒸馏可直接复用3项训练trick：学生从教师权重初始化、加入与教师输出的KL锚点稳定训练、采样阶段采用前向重加噪策略优化质量-多样性权衡'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
连续扩散语言模型支持并行生成全序列token，相比自回归模型有显著速度潜力，但高质量生成仍需数百次网络前向计算（NFE），现有蒸馏方案要么适配离散扩散，要么质量-多样性权衡较差，无法落地线上低延迟生成场景。

### 方法关键点
- 构建统一的分布匹配蒸馏框架，基于反向KL散度匹配加噪后的学生输出分布与数据分布，原生支持多步生成场景
- 针对少步采样场景设计Simplex-DMD：采用连续token松弛+路径梯度优化，搭配辅助去噪器估计学生分布的分数，训练效率高
- 针对多步高预算场景设计Reinforce-DMD：采用类别采样+REINFORCE梯度估计，搭配判别器学习学生与数据的密度比，加入教师KL锚点避免训练崩溃
- 采样阶段采用前向重加噪策略，相比其他采样方案获得最优的质量-多样性权衡

### 关键结果
在OpenWebText数据集上蒸馏170M参数的LangFlow教师模型，对比ReDi、D-MMD等主流蒸馏基线：
- 4 NFE下，Simplex-DMD在单字熵5.44nats时生成困惑度（Gen PPL）达45.6，相对最优基线ReDi降低49%，性能接近1024步推理的OPT-125M
- 256 NFE下，Reinforce-DMD在单字熵5.00nats时Gen PPL达14.9，相对最优基线D-MMD降低20%，优于1024步推理的OPT-125M

### 核心结论
针对扩散类生成模型的蒸馏，需根据线上推理的采样预算匹配对应的梯度估计方案：少步场景用连续松弛路径梯度，多步场景用离散采样REINFORCE，可实现最优的质量-延迟权衡
