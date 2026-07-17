---
title: 'T^2MLR: Transformer with Temporal Middle-Layer Recurrence'
title_zh: T²MLR：带时序中间层循环的Transformer架构
authors:
- Ziyang Cai
- Xingyu Zhu
- Yihe Dong
- Yinghui He
- Sanjeev Arora
affiliations:
- Princeton University
arxiv_id: '2607.15178'
url: https://arxiv.org/abs/2607.15178
pdf_url: https://arxiv.org/pdf/2607.15178
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: LLM架构优化 · 时序中间层循环
tags:
- Transformer
- Recurrent Architecture
- Latent Reasoning
- Reasoning
- Finetuning
- KV Cache
one_liner: 通过Transformer中间层跨解码步骤的时序循环缓存，低开销提升推理能力，可直接适配现有预训练模型
practical_value: '- 业务侧小参数LLM（如推荐文案生成、Agent多轮意图推理用的1.7B/7B模型）可直接加装T²MLR中间层循环模块，仅少量SFT即可提升多跳推理能力，推理overhead仅增~8%，完全符合线上
  latency 要求

  - 无需从头预训练，直接在现有成熟预训练模型中插入门控融合模块即可，例如给电商客服Agent基座加装后，可大幅提升复杂售后咨询的逻辑推理准确率，迁移成本极低

  - 多步推理类任务（如长会话用户状态跟踪、复杂搜索意图拆解）可复用中间层缓存思路，仅对20%左右的中间层做时序缓存即可拿到最优效果，无需全层循环，大幅节省训练与推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
标准Transformer自回归解码时，中间层生成的抽象推理状态只能通过离散token空间压缩传递，存在严重信息瓶颈；现有latent reasoning方法要么推理开销随循环次数线性增长，要么需要从头预训练，落地门槛极高。

### 方法关键点
- 新增跨解码步骤的中间层循环通路：将上一token的ℓ_end层输出缓存为固定大小的Recurrent Cache，直接注入到当前token的ℓ_start层输入，通过门控融合模块Φ合并当前表示与历史缓存
- 门控融合模块采用输入独立的全局可学习门+输入依赖的局部sigmoid门控，初始化即可兼容原有模型权重，训练稳定性高
- 采用近似时序并行训练方案：通过固定步数的Jacobi迭代做缓存refinement，支持标准teacher forcing训练，兼容现有序列并行训练框架

### 关键结果
- 预训练阶段：135M参数量模型在10B FineWeb-Edu数据上训练，仅对20%中间层做循环，零样本下游平均准确率比基线高1.31分，推理overhead仅增加~8%
- 微调阶段：在多跳推理、数学推理任务上平均准确率比基线高3~10pct，且中间层循环效果显著优于全层循环
- 存量模型适配：给预训练的1.7B SmolLM2加装循环通路后，GSM8K准确率从35.8提升到39.9（+11.5%相对），MATH500从12.8提升到18.0（+40.6%相对），仅需少量finetune无需从头预训练

**最值得记住的结论：Transformer的循环增益不取决于是否覆盖全层，而取决于是否把循环放在抽象推理最活跃的中间层位置**
