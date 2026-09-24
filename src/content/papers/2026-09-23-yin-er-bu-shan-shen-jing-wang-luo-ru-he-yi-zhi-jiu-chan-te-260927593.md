---
title: 'Hidden not Deleted: How Networks Suppress Entangled Features'
title_zh: 隐而不删：神经网络如何抑制纠缠特征
authors:
- Akash Samanta
- Manish Pratap Singh
- Debasis Chaudhuri
affiliations:
- Techno India University
- DRDO Young Scientist Laboratory - CT
arxiv_id: '2609.27593'
url: https://arxiv.org/abs/2609.27593
pdf_url: https://arxiv.org/pdf/2609.27593
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 模型训练 · 概念擦除与机器遗忘
tags:
- Machine Unlearning
- Feature Entanglement
- Concept Erasure
- Linear Projection
- LLM Alignment
one_liner: 揭示特征纠缠下线性概念擦除失效机制，解释LLM遗忘后知识复现的底层原因
practical_value: '- 做LLM敏感内容擦除/合规遗忘时，避免仅依赖线性投影方法，特征纠缠会导致关联业务特征被误删，建议先做特征解耦预处理

  - 评估模型遗忘效果时，不能仅验证表层行为消失，需新增底层特征残留检测环节，避免敏感知识被触发复现

  - 若需快速恢复被误删的业务特征，可尝试单标量补丁干预，无需全量重训，大幅降低修复成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于线性投影的概念擦除方法默认特征子空间可分离，实际应用中LLM机器遗忘后频繁出现知识复现问题，底层作用机制缺乏因果性解释。
### 方法关键点
针对特征密集叠加的纠缠场景，对比线性擦除与梯度下降训练的非线性擦除效果，追踪初始化对收敛结果的影响，通过定向因果干预验证擦除后的特征残留情况。
### 关键结果
当两个特征形成反极对共享单个子空间时，SOTA线性擦除会同时销毁目标与关联特征，而非仅擦除目标；梯度下降优化的非线性擦除会收敛为镜像/阴影两种电路级稳定解，均保留大量被擦除特征的可测量痕迹，仅需单个标量补丁即可恢复特征，无需重训；该机制为LLM遗忘后知识复现的常见失效模式提供了经因果验证的机理解释。
