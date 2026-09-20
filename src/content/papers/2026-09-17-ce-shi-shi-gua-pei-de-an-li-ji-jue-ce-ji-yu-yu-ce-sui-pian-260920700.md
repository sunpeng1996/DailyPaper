---
title: Should This Case Be Adapted? Prediction Fragmentation Controls Test-Time Adaptation
title_zh: 测试时适配的案例级决策：基于预测碎片化的管控方案
authors:
- Lili Wang
- Jing Li
- Xiaowen Sun
- Xiangyu Hu
- Zhuangzhuang Gu
- Jian Liu
- Srihari Nelakuditi
- Yan Tong
arxiv_id: '2609.20700'
url: https://arxiv.org/abs/2609.20700
pdf_url: https://arxiv.org/pdf/2609.20700
published: '2026-09-17'
collected: '2026-09-20'
category: Training
direction: 测试时适配 · 案例级路由优化
tags:
- Test-Time Adaptation
- Distribution Shift
- Case-level Router
- Model Adaptation
- Segmentation
one_liner: 提出基于源模型与适配后模型预测分歧的无标签案例级TTA路由器，大幅降低有害适配占比
practical_value: '- 线上推荐/LLM模型遇到分布漂移做测试时适配时，可引入案例级路由逻辑，避免全量适配导致的部分样本效果劣化

  - 可直接复用「源模型与小步适配后模型的预测分歧度」作为适配决策指标，决策时无需额外标签、无需额外反向传播，时延极低

  - 路由框架可跨架构跨域复用，仅需在独立标注集上校准一次阈值，跨场景部署时仅需调整切点即可落地'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有分段式测试时适配（TTA）对所有案例采用固定迭代步数，忽略单案例适配必要性，比如跨厂商心脏MRI场景下适配的平均Dice提升几乎为0，但58.7%的单个案例效果反而劣化，且全局适配预算无法跨基准迁移。

### 方法关键点
定义有害适配区域（HA）量化适配带来的效果损伤，提出预测碎片化指标（源模型M0与k步适配后模型Mk的预测分歧几何特征）预测HA，基于该指标构建案例级适配路由器，仅对收益为正的案例执行适配。

### 关键结果数字
在3个基准上预测HA的Spearman ρ达0.50~0.60，时延仅为梯度范数方法的1/4；心脏MRI基准上HA从0.129降至0.013，劣化案例占比从58.7%降至20.0%；跨未参与设计的基准部署时HA从0.228降至0.139。
