---
title: 'Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage
  to Supervision Reliability'
title_zh: 重新思考跨分词器On-Policy蒸馏：从对齐覆盖到监督可靠性
authors:
- Bingxi Hou
- Guochao Jiang
- Guofeng Quan
- Weiqing Li
- Wenfeng Feng
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2610.08448'
url: https://arxiv.org/abs/2610.08448
pdf_url: https://arxiv.org/pdf/2610.08448
published: '2026-10-05'
collected: '2026-10-07'
category: Training
direction: 大模型知识蒸馏 · On-Policy训练
tags:
- On-Policy Distillation
- Cross-Tokenizer
- Knowledge Distillation
- LLM Training
- Reverse KL
one_liner: 提出优先保障监督可靠性的跨分词器On-Policy蒸馏方案，效果超越现有基线
practical_value: '- 业务跨基座蒸馏小模型（如端侧Agent、推荐文案生成小模型）时，无需做复杂的全词表/不对齐span监督，仅用1:1严格对齐位置+学生选的top-16共享词表做reverse
  KL蒸馏，就能拿到96%以上的全监督收益，同时大幅降低计算开销

  - 新增蒸馏损失前需验证梯度一致性：弱对齐的额外监督信号（如不对齐span的MSE损失）会和主梯度方向弱相关甚至负相关，反而导致效果下降，不要盲目追求对齐覆盖度

  - 垂域小模型蒸馏（如电商query理解、商品文案生成模型）可直接复用本文范式，无需额外实现词表映射、字节对齐等复杂逻辑，落地成本低收益明确'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
跨分词器On-Policy蒸馏（OPD）是不同基座大模型间知识迁移的核心方案，过往研究普遍认为最大化对齐覆盖度（覆盖更多不对齐token span、更大词表范围）能提升蒸馏效果，但缺乏对新增监督信号可靠性的验证，反而可能引入噪声导致效果下降。

### 方法关键点
- 蒸馏损失拆分为两部分：1:1严格对齐位置的reverse KL损失（仅在师生token严格匹配同一段文本的位置计算，分布约束在共享词表），以及不对齐span的log概率MSE损失，通过权重λ控制后者的影响
- 严格对齐位置的蒸馏进一步优化：仅取学生预测概率最高的top-k个共享词表子集做reverse KL，无需覆盖全共享词表

### 关键结果
实验覆盖3组异质师生对（Qwen2.5-7B→Llama3.2-3B、Granite-8B→Phi-4-mini、Granite-8B→Qwen2.5-7B-base），对比ULD、SimCT等4个跨分词器蒸馏基线：
1. 静态词表Jaccard重合度仅39.49~64.87%的情况下，学生生成序列中严格对齐的token占比达85.57~96.98%，共享词表覆盖师生99%以上的预测概率质量
2. 仅用严格对齐位置+top-16子集的蒸馏方案，保留全共享词表OPD 96%以上的效果提升，比最强基线高0.51~1.05个百分点；只要加入不对齐span的MSE损失（任意λ>0），效果下降0.27~1.2个百分点
3. 不对齐span的梯度和主严格损失梯度方向一致性弱甚至负相关，且训练过程中相对梯度幅值不断增大，是效果下降的核心原因

**最值得记住的一句话**：跨分词器蒸馏无需盲目追求对齐覆盖度，紧凑的高可靠监督信号效果优于覆盖广但噪声大的信号
