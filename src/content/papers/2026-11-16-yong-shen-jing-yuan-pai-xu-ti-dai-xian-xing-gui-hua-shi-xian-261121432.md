---
title: Just sort it! A note on the LP behind rank-one anti-loop edits
title_zh: 用神经元排序替代线性规划实现秩一更新消除LLM推理循环
authors:
- Matteo Fischetti
affiliations:
- University of Padova
arxiv_id: '2611.21432'
url: https://arxiv.org/abs/2611.21432
pdf_url: https://arxiv.org/pdf/2611.21432
published: '2026-11-16'
collected: '2026-11-17'
category: Training
direction: LLM权重编辑·秩一更新优化
tags:
- Weight-Space Programming
- Rank-One Update
- Linear Programming
- Neuron Selection
- Reasoning Optimization
one_liner: 用神经元激活变异系数排序替代LP求解一阶秩反循环更新，性能与原方案无显著差异
practical_value: '- 做Agent/电商场景小模型定向行为对齐（如反幻觉、反重复话术、推理循环消除）时，可直接用基于神经元激活统计的排序替代复杂LP求解，大幅降低工程实现成本，性能损失可忽略

  - 小参数LLM的定向编辑任务中，核心价值来自行为方向向量u而非后续复杂求解步骤，可大幅简化对齐链路，仅保留关键方向的权重偏移即可

  - 线上部署轻量LLM编辑能力时，可借鉴无LP的排序方案，将权重编辑耗时从分钟级降至毫秒级，满足实时性要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
AHA框架通过对MLP输出矩阵做秩一更新`W' = W + uv^T`消除小推理模型的思考循环，其中v需要通过大规模稀疏线性规划（LP）求解得到，20层模型单轮求解总耗时约2.2分钟，计算开销大，工程落地门槛高，需要验证是否可用更简单的方法替代LP求解。

### 方法关键点
- 核心假设：LP求解得到的v本质是生成沿u方向的近似恒定偏置，只需选择激活最稳定的神经元即可实现同等效果
- 排序规则：计算每个神经元激活的变异系数`σ_j/|m_j|`，选择最小的8个神经元，平均分配原LP方案的总push剂量；无LP版本直接用AHA预计算的阈值δ作为剂量，完全不依赖LP求解
- 对照方案：同时测试仅选激活均值最大的8个神经元的knap_k8方案，验证排序指标的有效性

### 关键实验
- 测试模型为Qwen3.5-0.8B，数据集为MATH-500+GSM8K共1000个推理问题，多种子验证鲁棒性
- 基准结果：未编辑模型准确率9.5%，原LP编辑方案准确率67.4%
- 排序方案sort_k8（复用LP剂量）准确率67.0%，与LP方案的配对差异为-0.4，95%置信区间[-2.9, +2.1]，落在预设的5个点非劣效区间内
- 完全不依赖LP的sortd_k8准确率66.3%，与LP方案差异仅-0.8，仍满足非劣效要求，计算开销从分钟级降至单遍激活统计的毫秒级

小模型定向权重编辑的核心价值来自行为方向向量u，而非后续实现该方向的复杂优化求解步骤，简单统计规则即可达到几乎同等效果。
