---
title: Improving Tail-Augmented Speculative Drafting with Hidden State Mixing and
  Gradient Detach
title_zh: 基于隐状态混合与梯度截断的尾部增强投机解码训练优化
authors:
- Yaniv Galron
- Rabeeh Karimi Mahabadi
- Maor Ashkenazi
- Roger Waleffe
- Talor Abramovich
- Tiyasa Mitra
- Yoav Miron
- Dor Tsur
- Sanjeev Satheesh
- Jimmy Zhang
affiliations:
- NVIDIA
arxiv_id: '2611.34092'
url: https://arxiv.org/abs/2611.34092
pdf_url: https://arxiv.org/pdf/2611.34092
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM 投机解码训练优化
tags:
- Speculative Decoding
- Multi-Token Prediction
- EAGLE
- Hidden State Mixing
- Gradient Detach
- LLM Inference
one_liner: 提出两种无推理开销的训练方法，提升多token预测类投机解码接受率，显存开销远低于EAGLE-3的TTT方案
practical_value: '- 搜推/Agent业务中用到LLM推理加速时，可直接复用HSM/HSGD训练MTP/EAGLE类投机模块，无需改动推理逻辑即可提升token接受率，降低端到端延迟

  - 高并发短响应场景（如实时搜索query补全、推荐理由实时生成）优先用HSGD提升早期draft位置接受率；低并发长文本生成场景（如商品描述批量生成、客服多轮回复）优先用HSM提升尾部接受率

  - 定制化训练EAGLE类轻量投机小模型时，可用HSM替代TTT方案，峰值训练显存最高降低48%，大幅降低训练成本同时达到相当的接受率效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
EAGLE、MTP类尾部增强投机解码存在严重训练推理不匹配：训练时仅输入主干模型或单步MTP输出的隐状态，推理时上下文是主干模型前缀隐状态+不断增长的自生成MTP隐状态序列，导致draft尾部接受率大幅下降；现有TTT方案通过显式模拟推理过程优化，显存开销随模拟步数线性增长，难以规模化集成到大模型预训练流程。
### 方法关键点
- **Hidden State Mixing (HSM)**：训练时在对齐到同一预测目标的主干模型、各步MTP输出的隐状态中随机采样作为输入，无需显式模拟推理过程即可让模型适配混合深度的隐状态上下文，无任何推理侧开销
- **Hidden State Gradient Detach (HSGD)**：正则化方法，训练时随机截断隐状态、token嵌入路径的梯度回传，保留前向计算不变，缓解多步MTP训练的跨步骤共适应问题，同样无推理开销
### 关键实验结果
在SPEED-Bench数据集上对比基线共享参数MTP、EAGLE-3 TTT方案：
1. 冻结主干的MTP boosting场景下，HSM跨4款Nemotron模型、DeepSeek-V4-Pro将平均接受长度最高提升52.2%
2. Qwen3-8B 4步训练对比中，HSM达到与TTT相当的接受率，峰值训练显存低48%
3. 联合预训练+SFT场景下，HSGD提升前4个draft位置接受率，HSM提升第5位及之后尾部接受率，长草稿场景下平均接受长度从5.19提升到5.57
### 核心结论
投机解码的效果优化可完全在训练侧完成且无推理开销，根据业务并发度、生成长度选择HSM/HSGD可实现性价比最高的LLM推理加速
