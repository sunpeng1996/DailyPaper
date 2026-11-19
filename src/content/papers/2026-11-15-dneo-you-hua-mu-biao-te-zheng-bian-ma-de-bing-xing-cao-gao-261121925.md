---
title: 'DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding'
title_zh: DNeo：优化目标特征编码的并行草稿模型 LLM 推理加速方案
authors:
- Jameson Sandler
- Shane Bergsma
- Mostafa Elhoushi
- Bin Claire Zhang
- Gavia Gray
- Joel Hestness
- Nolan Dey
- Ferdinando Fioretto
affiliations:
- University of Virginia
- Cerebras Systems
arxiv_id: '2611.21925'
url: https://arxiv.org/abs/2611.21925
pdf_url: https://arxiv.org/pdf/2611.21925
published: '2026-11-15'
collected: '2026-11-19'
category: LLM
direction: LLM推理 · 投机解码并行草稿优化
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Feature Encoding
- Parallel Draft Model
- MoFA
one_liner: 通过结构保留特征编码、拒绝记忆等优化，实现LLM无损推理速度较SOTA提升30%
practical_value: '- 电商智能客服、商品文案生成、多轮Agent等场景可直接引入DNeo的并行草稿+投机解码方案，在不损失生成质量的前提下降低推理延迟，同时减少推理算力成本

  - 垂域小模型蒸馏（如推荐场景的query改写、文案生成小模型对齐大模型）可复用MoFA结构，用目标层隐藏态加权融合替代全连接投影，参数减少99.95%的同时提升对齐效果

  - 长文本生成、多轮对话场景可复用拒绝记忆设计，通过跨注意力复用之前被拒绝的生成结果特征，无需额外计算即可提升后续生成准确率

  - 大模型特征对齐场景可复用DNeo层选择协议，优先采样目标模型后半层隐藏态，无需均匀采样全层，降低计算量的同时提升特征有效性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
投机解码是当前LLM无损推理加速的主流方案，通过小型并行草稿模型生成批量候选token，再由大目标模型并行验证，推理速度核心取决于草稿质量。现有并行草稿模型的特征编码存在三个核心缺陷：全连接投影导致的残差混合损失特征结构、无历史拒绝结果记忆浪费有效信息、均匀采样目标层忽略深层高价值隐藏态，限制了加速比上限。

### 方法关键点
- 提出MoFA特征编码器，加权融合目标模型不同层隐藏态，从结构上避免残差混合，参数量仅为传统全连接编码的0.05%
- 新增拒绝记忆模块，将上一轮验证被拒绝的token隐藏态通过跨注意力引入草稿生成过程，复用已计算结果无需额外开销
- 设计融合因果头，在隐空间结合低秩全词表调整和上下文感知重排能力，解决并行生成的因果不一致问题
- 采用前缀-only注意力去掉mask块双向自注意力，结合2-tap因果卷积降低计算开销，优先采样目标模型后半层隐藏态提升特征有效性

### 关键实验
基于Qwen3-4B作为目标模型，在GSM8K、HumanEval、MT-Bench等6个基准测试：单用户场景生成速度较SOTA DFlash-2最高提升30%，TPF提升25.1%；batch size=32时吞吐量较DFlash-2提升58%，batch size=64时吞吐量与自回归解码基本持平，其余SOTA方案下降10%~18%；消融实验显示MoFA单模块提升TPF 0.65，拒绝记忆提升0.182，融合因果头提升0.217。

### 核心结论
并行草稿模型的核心瓶颈是目标特征的有效编码，保留特征结构、利用已计算的拒绝信息，比盲目增加模型容量更能提升推理效率。
