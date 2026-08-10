---
title: Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement
title_zh: 云侧赋能的低计算量多通道语音增强框架
authors:
- Xulin Fan
- Juan Azcarreta
- Ashutosh Pandey
- Jesus Alvarez
- Ke Tan
- Jacob Donley
- Ritwik Giri
- Buye Xu
affiliations:
- University of Illinois Urbana-Champaign
- Meta Reality Labs Research
arxiv_id: '2608.07423'
url: https://arxiv.org/abs/2608.07423
pdf_url: https://arxiv.org/pdf/2608.07423
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 云边协同 低计算量语音增强
tags:
- Speech Enhancement
- Edge-Cloud Collaboration
- On-Device AI
- Low-Compute Inference
- Multi-Channel Processing
one_liner: 提出云边协同低计算量语音增强框架，3项技术实现极低开销下大幅提升端侧性能
practical_value: '- 云边协同知识蒸馏思路可复用在端侧推荐/搜索模型轻量化场景，用云侧大模型的中间特征、输出结果指导端侧小模型推理，仅增加极低开销即可提升小模型效果

  - 多源预测结果加权融合策略可迁移到推荐系统多路召回/排序结果融合场景，比如将云侧精排结果和端侧轻量排序结果加权融合，降低整体链路延迟

  - 层间特征迁移方法可用于小推荐模型蒸馏微调，引入大模型中间层特征作为额外监督信号，提升蒸馏效率和小模型最终效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
可穿戴设备端侧实时语音增强需满足低延迟、低功耗要求，端侧轻量模型容量有限，效果远落后于云侧大模型，现有知识赋能方案在语音增强场景下增益十分有限。
### 方法关键点
1. 引入延迟可控的云侧输出作为端侧模型的额外输入
2. 层间特征赋能机制：迁移云侧模型中间表征指导端侧推理
3. 协同多通道维纳滤波：融合云边两侧估计的加权协方差矩阵优化波束形成效果
### 关键结果
相比纯端侧基线模型，仅增加极低额外计算开销的前提下，语音增强效果实现显著提升。
