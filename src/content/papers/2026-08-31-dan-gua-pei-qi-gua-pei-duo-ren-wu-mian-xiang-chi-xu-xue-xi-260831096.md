---
title: 'One Adapter, Many Tasks: Task-Conditioned Feature Transformations for Continual
  Learning'
title_zh: 单适配器适配多任务：面向持续学习的任务条件特征变换
authors:
- Yunxiang Fu
- Meng Lou
- Yizhou Yu
affiliations:
- The University of Hong Kong
arxiv_id: '2608.31096'
url: https://arxiv.org/abs/2608.31096
pdf_url: https://arxiv.org/pdf/2608.31096
published: '2026-08-31'
collected: '2026-09-02'
category: Training
direction: 持续学习 · 轻量适配器优化
tags:
- Continual Learning
- Adapter
- LoRA
- Class-incremental Learning
- Feature Transformation
one_liner: 提出FACET单共享适配器持续学习方案，兼顾参数效率、推理性能与抗灾难性遗忘
practical_value: '- 多场景/多任务推荐场景可复用单共享Adapter+动态任务条件特征变换思路，替代多场景独立LoRA/Adapter，大幅降低参数量与推理开销

  - 电商增量上新（新类目/新商品/新场景）的推荐模型增量训练，可引入无回放的任务条件特征一致性损失，无需留存历史数据规避合规风险，同时缓解灾难性遗忘

  - 超200个细分场景的长序列多任务模型迭代，可参考FACET的任务特征分布打散思路，降低不同任务的表示干扰，提升跨任务整体效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
类增量持续学习（CIL）需在无历史训练数据的前提下增量学习含新类别的任务，同时保留旧类识别能力。现有基于冻结预训练backbone的适配方案存在两大缺陷：单任务专属Adapter参数/计算效率极低；LoRA合并方法的静态聚合权重易引发推理阶段不同任务的特征表示干扰。
### 方法关键点
1. 提出FACET框架，仅训练单个共享Adapter，引入动态任务条件特征变换，将Adapter输出特征分布塑造成重叠度极低的多任务专属分量混合分布；
2. 设计无回放的任务条件特征一致性损失，无需留存历史数据即可缓解Adapter特征空间的灾难性遗忘。
### 关键结果
在20任务标准序列上效果优于现有基线，200个任务的超长序列下仍保持鲁棒性，同时可训练参数量、GFLOPs显著低于对比方案
