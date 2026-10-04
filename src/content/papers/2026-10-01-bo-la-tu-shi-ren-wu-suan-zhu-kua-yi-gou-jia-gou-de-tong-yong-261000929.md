---
title: Platonic Task Arithmetic
title_zh: 柏拉图式任务算术：跨异构架构的通用任务知识迁移方法
authors:
- Junghwan Park
- Woojin Cho
affiliations:
- TelePIX
arxiv_id: '2610.00929'
url: https://arxiv.org/abs/2610.00929
pdf_url: https://arxiv.org/pdf/2610.00929
published: '2026-10-01'
collected: '2026-10-04'
category: Training
direction: 跨异构模型任务知识迁移框架
tags:
- Task Arithmetic
- Cross-Architecture Transfer
- Model Editing
- LoRA
- Task Vector
one_liner: 提出架构无关的通用任务描述符，实现跨异构模型无需结构对齐的任务算术操作
practical_value: '- 跨异构模型任务迁移思路可复用在多基座LLM/MoE推荐系统的能力迁移，无需对齐模型结构即可快速迁移排序/召回任务能力

  - 通用任务描述符设计可用于搭建推荐场景任务能力库，通过线性组合快速适配多业务需求，降低重复训练成本

  - 两种任务编辑方案可直接复用在业务模型快速迭代：冷启动场景优先用无训练的最小二乘末层编辑降本，复杂多任务组合用LoRA适配'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有权重空间任务算术仅支持同架构同尺寸模型的任务向量操作，跨异构模型迁移任务能力需结构对齐，无对应关系时任务知识完全无法复用。
### 方法关键点
1. 提出柏拉图式任务向量假设：不同模型的任务参数更新是同一通用、架构无关任务对象的投影
2. 设计独立于模型架构、嵌入维度的Universal Task Descriptors，记录任务功能效应，支持矩阵加减运算
3. 提供两种落地实现：基于最小二乘的末层权重线性编辑（无额外训练，支持多任务线性组合）、基于LoRA的全层适配（支持多任务组合联合拟合）
### 关键结果
跨6个模型族、8个分类任务及音文多模态场景验证，跨模型任务迁移可保留目标模型自身任务描述符74%~80%的性能增益
