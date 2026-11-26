---
title: Lightweight Reasoning Transfer via Chain-of-Thought Vector Projection
title_zh: 基于思维链向量投影的轻量化推理能力迁移
authors:
- Yulin Qi
- Shuo Xu
- Shuxia Lin
- Qingjian Ni
- Xu Yang
- Xin Geng
affiliations:
- Southeast University
arxiv_id: '2611.34183'
url: https://arxiv.org/abs/2611.34183
pdf_url: https://arxiv.org/pdf/2611.34183
published: '2026-11-25'
collected: '2026-11-26'
category: Reasoning
direction: LLM推理 · 跨模型CoT向量迁移
tags:
- Chain-of-Thought
- Knowledge Distillation
- Reasoning Transfer
- Activation Steering
- Lightweight Adaptation
one_liner: 通过轻量化线性投影将大模型CoT推理向量迁移到异构小模型，全程主干模型冻结
practical_value: '- 对于端侧/边缘部署的电商导购Agent、实时推理场景，可复用该架构：先在云端大模型训练任务级CoT向量，仅通过线性投影适配端侧小模型，无需微调主干，大幅降低部署成本与延迟

  - 推荐场景query理解、订单合规校验等需要逻辑推理的小模型优化，可借鉴仅用最终答案监督训练投影层的方案，无需标注中间推理过程，降低标注成本

  - 多Agent系统中不同参数规模Agent的能力对齐，可复用一次训练的任务向量，仅新增对应每个小Agent的投影层即可实现能力复用，减少重复训练开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型CoT推理能力优异但部署成本高，传统知识蒸馏需要大量教师输出、中间推理标注，且需微调小模型主干，迁移成本高；现有CoT向量仅支持同维度模型间直接迁移，无法适配异构小模型，亟需低成本跨模型推理能力迁移方案。

### 方法关键点
- 两阶段架构，教师、学生主干全程冻结：第一阶段在教师模型上学习任务级CoT向量，用带完整解决方案的训练数据，对齐带CoT和不带CoT两条路径的表征，结合最终答案交叉熵损失优化向量
- 第二阶段仅训练无偏线性投影层，将固定教师CoT向量映射到学生残差空间，学生侧训练仅用不到3%的训练数据和最终答案监督，无需访问教师logits、中间表征或推理过程
- 从验证集取少量样本选择最优学生注入层和缩放系数，推理时预计算投影后的向量直接注入学生残差流，仅需加载冻结学生和固定向量，无额外开销

### 关键实验
在GSM8K、MATH数学推理数据集上，1.5B基础学生模型精度提升10.37~21.98个百分点；代码生成任务上Qwen2.5-7B-Instruct学生pass@1提升3.23~4.67个百分点；同数据预算下效果远超LoRA、SFT、DistiLLM等基线，投影层参数量仅为学生的0.0001%左右。

最值得记住的一句话：大模型的任务级推理能力可以被编码为单个固定向量，仅通过轻量化线性投影就能跨不同维度的小模型复用，迁移成本远低于传统蒸馏方案。
