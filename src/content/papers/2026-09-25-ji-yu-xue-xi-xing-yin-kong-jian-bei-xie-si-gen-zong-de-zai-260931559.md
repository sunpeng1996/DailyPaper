---
title: Online Learning via Learned Latent Bayesian Tracking
title_zh: 基于学习型隐空间贝叶斯跟踪的在线学习方法
authors:
- Guy Gerson
- Tomer Raviv
- Nir Shlezinger
- Tirza Routtenberg
- Osvaldo Simeone
affiliations:
- Ben-Gurion University
- Northeastern University London
arxiv_id: '2609.31559'
url: https://arxiv.org/abs/2609.31559
pdf_url: https://arxiv.org/pdf/2609.31559
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 在线学习 · 高维模型贝叶斯自适应
tags:
- OnlineLearning
- BayesianFiltering
- MetaLearning
- LatentSpace
- KalmanFiltering
one_liner: 提出AURA元学习框架，通过学习低维隐空间实现高维模型的高效在线贝叶斯自适应
practical_value: '- 推荐系统应对非平稳用户行为/季节/热点变化时，可借鉴离线预训练低维参数隐空间的思路，降低在线模型更新计算开销，提升自适应速度

  - 高维LLM/MoE推荐模型在线微调场景，可复用「低维隐空间滤波+全参数升维映射」架构，替代全参数/LoRA微调，兼顾效率与效果

  - Agent在动态环境（如实时电商导购、流量动态变化的广告投放）的在线适配，可参考AURA元学习预训练+在线单步更新的流程，降低延迟'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
非平稳环境下的在线学习要求模型在低计算约束下快速适配流式数据，传统贝叶斯滤波方案受限于高维模型参数空间，只能依赖强假设近似或手动设计低维子空间，适配效果与效率难以兼顾。
### 方法关键点
AURA为元学习框架，离线阶段学习控制分布偏移下最优模型参数演化规律的低维隐状态空间模型；在线阶段仅在该隐空间执行扩展卡尔曼滤波更新，再通过预训练的升维映射重建全量模型参数，实现单步高效更新且不损失模型表达能力。
### 关键结果
在时变信道无线接收器自适应、非平稳图像分类任务上，AURA相比现有在线学习、贝叶斯滤波基线，适配速度、精度、计算效率均有显著提升。
