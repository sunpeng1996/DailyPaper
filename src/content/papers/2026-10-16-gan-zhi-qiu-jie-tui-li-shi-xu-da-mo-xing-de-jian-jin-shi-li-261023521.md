---
title: 'Perceive, Solve, Reason: Progressive Capability Formation in Time Series-LLMs'
title_zh: 感知、求解、推理：时序大模型的渐进式能力形成
authors:
- Xin Qiu
- Junlong Tong
- Wei Zhang
- Xiaoyu Shen
affiliations:
- EIT-NLP Lab, Eastern Institute of Technology, Ningbo
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2610.23521'
url: https://arxiv.org/abs/2610.23521
pdf_url: https://arxiv.org/pdf/2610.23521
published: '2026-10-16'
collected: '2026-10-20'
category: LLM
direction: 时序大模型 · 渐进式能力训练
tags:
- Time Series LLM
- Progressive Training
- Multimodal Encoder
- LLM Evaluation
- Capability Transfer
one_liner: 构建首个覆盖时序大模型三级渐进能力的训练评测套件，提出专用编码器+分阶段训练的高效范式
practical_value: '- 处理业务侧用户行为时序、销量时序、流量时序等序列数据时，优先采用专用模态编码器接入LLM，避免文本序列化带来的8-10点推理精度损失

  - 多能力融合LLM训练可复用「感知→求解→推理」分阶段渐进训练范式，同等数据量下效果优于混合训练，可大幅降低高难度任务的标注成本

  - 跨域时序类任务（如销量预测、用户行为预判）可直接复用本文训练配方，4B小参数量模型即可超越7B大模型效果，降低推理部署成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM已实现图像、音频的感知与推理能力，但时序理解能力研究较薄弱，现有工作仅聚焦预测、分类等基础任务，缺乏覆盖全能力链路的训练评测基准，也未明确时序输入方式、能力训练顺序的最优方案。
### 方法关键点
构建覆盖「感知-求解-推理」三级渐进能力的时序数据集，包含337K训练样本、44K评测样本，对比不同时序输入方案（专用编码器/文本序列化）、不同训练策略（分阶段/混合/单能力训练）的效果差异。
### 关键结果数字
搭载专用时序编码器的4B模型感知能力全面超过GPT-4o，文本序列化输入会降低8-10点推理精度；分阶段渐进训练效果优于同数据量混合训练，仅需1/3推理标注数据即可媲美纯推理训练效果；4B模型无目标域微调数据时，在8个跨域指标中7个优于现有7B时序大模型，最高提升11个点
