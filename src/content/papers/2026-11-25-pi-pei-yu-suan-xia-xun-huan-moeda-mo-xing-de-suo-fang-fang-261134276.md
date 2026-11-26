---
title: 'Scaling Looped MoE Language Models under Matched Budgets: Information Flow
  and Parameter Allocation'
title_zh: 匹配预算下循环MoE大模型的缩放方法：信息流优化与参数分配
authors:
- Shipeng Bai
- Jiayu Qin
- Hong Liu
- Xili Wang
- Jianchao Tan
- Jiacheng Li
- He Zhang
- Yifan Lu
- Jiaqi Zhang
- Kefeng Zhang
affiliations:
- Meituan
arxiv_id: '2611.34276'
url: https://arxiv.org/abs/2611.34276
pdf_url: https://arxiv.org/pdf/2611.34276
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: 大模型训练 · 循环MoE架构优化
tags:
- MoE
- Looped Transformer
- Parameter Allocation
- Information Flow
- Pre-training
one_liner: 优化循环MoE的信息流与参数配置，同参同FLOP下性能显著优于非循环基线
practical_value: '- 搭建垂直领域LLM（如电商导购Agent、推荐场景prompt生成模型）时，可直接采用2次迭代的循环MoE架构，将共享Core单次深度设为总展开深度的25%-35%，把权重共享节省的参数用于扩充每层路由专家数，零额外计算成本提升性能，且完全兼容现有训练基建

  - 循环模型的信息流优化trick可直接复用：首步直接输入归一化后的Prelude特征，迭代间用边界RMSNorm对齐特征尺度，搭配独立参数化的通道维度门控融合，再新增Prelude到Coda的跨阶段残差连接，仅增加极少量参数即可稳定训练、提升效果

  - 电商/推荐场景的小参数LLM落地可套用该配置，在保持推理FLOP不变的前提下提升模型效果，适用于query理解、商品文案生成、用户意图识别等轻量化模型的优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Looped Transformer通过权重共享解耦计算深度与参数量，可在同等预算下提升模型效果，但缺乏严格等参、等FLOP约束下的通用配置原则，循环过程存在信息流不稳定、梯度传导受阻的问题，权重共享节省的参数也没有最优分配策略，无法最大化性能增益。
### 方法关键点
- 信息流优化：①首步直接将归一化后的Prelude输出喂入共享Core，避免随机初始状态带来的优化冲突；②迭代间新增边界RMSNorm对齐循环状态与固定输入的特征尺度，采用独立参数化的通道维度门控融合历史状态与输入，避免状态保留与输入注入的参数耦合；③新增Prelude到Coda的跨阶段残差连接，恢复被归一化、门控打断的直接梯度通路，无额外训练参数。
- 参数配置原则：①循环次数设为2次，共享Core的单次深度占总展开深度的25%~35%，平衡计算复用与边界层独立参数容量；②权重共享节省的参数全部用于扩充每层路由专家数，不改动原有层维度、注意力配置，兼容现有训练与推理基建，零额外计算成本。
### 关键实验
1T预训练token下，69B MLA、51B KDA架构的循环MoE，分别比同预算非循环基线平均提升1.16pp、2.29pp，BBH推理任务最高提升4.08pp；200B token训练的通用Qwen3风格GQA-MoE backbone上，验证集PPL比Parcae、SMELT分别低0.58%、0.55%，LAMBADA PPL低6.86%、3.93%。
### 核心结论
循环MoE采用「2次迭代+25%~35%深度共享Core+省出参数加专家数」的配置，零额外计算成本即可提升性能，完全兼容现有训练与推理基建
