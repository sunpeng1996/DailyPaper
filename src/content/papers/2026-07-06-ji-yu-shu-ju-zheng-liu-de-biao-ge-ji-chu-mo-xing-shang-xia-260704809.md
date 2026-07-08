---
title: Context-Constrained Transfer Learning for Tabular Foundation Models via Data
  Distillation
title_zh: 基于数据蒸馏的表格基础模型上下文约束迁移学习
authors:
- Yijun Lin
- Sai Li
affiliations:
- Renmin University of China
- Tsinghua University
arxiv_id: '2607.04809'
url: https://arxiv.org/abs/2607.04809
pdf_url: https://arxiv.org/pdf/2607.04809
published: '2026-07-06'
collected: '2026-07-08'
category: Training
direction: 表格基础模型 · 迁移学习优化
tags:
- Tabular Foundation Model
- Transfer Learning
- Data Distillation
- Optimal Transport
- In-Context Learning
one_liner: 提出TL-ANDI蒸馏框架解决表格基础模型迁移的上下文限制与分布偏移负迁移问题
practical_value: '- 电商/推荐小样本冷启动场景可借鉴最优运输选锚样本的思路，在有限ICL上下文里选最适配目标任务的历史样本，缓解负迁移

  - 跨域推荐迁移时可加入后验兼容性度量筛选源域样本，结合少量目标域数据做残差校准，降低分布偏移带来的效果下降

  - 表格大模型落地时可复用TL-ANDI的蒸馏逻辑压缩上下文长度，降低KV cache占用，提升推理效率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有Tabular Foundation Models（TFM）通过In-Context Learning实现黑盒推理，但迁移落地面临两大核心瓶颈：一是严格的上下文长度限制无法容纳大量源数据，二是源/目标任务分布偏移极易引发负迁移，直接混用异构源数据效果劣化明显。
### 方法关键点
提出TL-ANDI后验感知蒸馏框架：1）求解带预算约束的最优运输问题，同时度量目标协变量覆盖度与后验兼容性，筛选得到极小体量的源域锚样本作为上下文；2）为锚样本配置本地蒸馏标签，结合少量目标域数据做残差校准；3）理论上给出无负迁移的形式化保障。
### 关键结果
仿真与真实数据集实验验证，在分类、回归两类任务上均显著优于朴素迁移学习基线，稳定消除负迁移现象。
