---
title: 'STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment'
title_zh: STAGE：面向多偏好LLM对齐的可控目标准入方法
authors:
- Yongqi Tong
- Zhenyu Zhang
- Ruirui Wang
- Kewei Fu
- Shaoqing Lin
- Sijie Dong
- Jiang-Ming Yang
- Xin Zhang
- Jianshe Li
affiliations:
- Ant International
arxiv_id: '2608.16553'
url: https://arxiv.org/abs/2608.16553
pdf_url: https://arxiv.org/pdf/2608.16553
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: LLM训练 · 多偏好RLHF对齐
tags:
- RLHF
- Multi-objective Optimization
- Curriculum Learning
- LLM Alignment
- Preference Tuning
one_liner: 提出稳定性引导的主动集控制器，分阶段准入偏好维度优化多目标RLHF，效果优于同期基线
practical_value: '- 电商/Agent多目标优化场景（同时要合规、转化、体验等目标）可借鉴分阶段准入思路，无需一开始加载全量目标，避免目标冲突导致训练崩塌

  - 多目标的优先级排序可复用探针阶段自动计算难易度的方案，替代人工拍序，降低调参成本

  - 自适应权重机制可直接迁移至多目标推荐/排序场景，给表现短板的指标（如复购、深度）更高权重，避免简单指标（如CTR）主导优化

  - ISG/WSG双门限+patience预算的阶段切换逻辑，可复用在多模型迭代的进度管控，平衡训练效率与稳定性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多偏好LLM对齐大多采用多奖励维度直接加权后联合优化的方案，忽略了偏好维度的准入时机设计：全量目标同时优化容易出现简单目标主导、目标冲突导致效果抵消的问题，固定顺序的分阶段训练又容易在切换阶段时破坏已习得的旧目标表现，亟需更可控的多目标准入机制。
### 方法关键点
- 前置短探针阶段：计算每个偏好维度的训练增益与波动率，自动生成难到易的准入顺序，无需人工定义优先级
- 累积主动集设计：已准入的偏好维度全程保留在优化目标中，不会因阶段切换丢失旧目标的优化效果
- 双门限阶段切换：同时满足瞬时稳定性门限（ISG）、窗口稳定性门限（WSG），或阶段patience预算耗尽时，才准入下一个偏好维度
- 阶段内自适应加权：给当前表现较差的偏好维度分配更高权重，避免短板目标被简单目标覆盖
### 关键结果
基于Qwen3-0.6B、Llama3-8B-Instruct两个骨干模型，覆盖15个训练偏好维度，在16个held-out基准上测试，对比6种多目标对齐基线：
- Qwen3-0.6B场景下平均得分44.81，较最强基线提升5.49，较基础模型提升12.03
- Llama3-8B-Instruct场景下平均得分62.93，较最强基线提升5.34，较基础模型提升10.55
- 消融实验验证探针排序、双门限、自适应权重三个核心组件均带来正向收益
### 核心结论
多偏好对齐的优化核心不只是如何给目标加权，更要管控每个目标进入优化流程的时机。
