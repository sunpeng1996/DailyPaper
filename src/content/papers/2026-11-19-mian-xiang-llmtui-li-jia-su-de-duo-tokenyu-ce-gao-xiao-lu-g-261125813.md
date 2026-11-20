---
title: Efficient and Robust Drafting with Multi-Token Prediction
title_zh: 面向LLM推理加速的多Token预测高效鲁棒草稿生成框架G-MTP
authors:
- Filippo Galgani
- Ziwei Ji
- Omri Homburger
- Ganesh Jawahar
- Michelle Ramanovich
- Ivan Korotkov
- Luciano Martins
- Utku Evci
- Edouard Yvinec
- Pooja Consul
affiliations:
- Google
arxiv_id: '2611.25813'
url: https://arxiv.org/abs/2611.25813
pdf_url: https://arxiv.org/pdf/2611.25813
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理加速 · Speculative Decoding
tags:
- Speculative Decoding
- Multi-Token Prediction
- KV Cache
- LLM Inference
- On-device LLM
one_liner: 提出集成式多Token预测架构G-MTP，实现服务端/端侧LLM推理最高3.14倍无损加速
practical_value: '- 端侧电商场景（如端侧推荐文案生成、智能客服）可复用零拷贝KV缓存共享、聚类词表投影优化，大幅提升小规格LLM响应速度

  - 垂直领域LLM（如电商营销文案、商品理解模型）fine-tune时，采用两阶段蒸馏/联合LoRA微调对齐MTP头，可避免加速比掉点，比仅微调主干少1.83倍目标前向传播

  - 服务端部署生成式推荐、Agent调用用的30B级大模型时，集成G-MTP架构可实现3倍左右推理提速，降低部署成本'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有speculative decoding依赖独立draft模型生成候选token，额外的prefill计算与内存开销严重拉低服务端吞吐量，且完全无法适配内存受限的端侧场景；主干模型做域微调时，draft头易出现分布偏移，导致加速比暴跌。
### 方法关键点
- 集成式架构：在主干LLM最后层后接共享4层Transformer draft头，无需独立训练小尺寸draft模型
- 目标激活注入：直接取主干最后层激活与当前token embedding拼接作为draft输入，锚定语义提升候选token接受率
- 零拷贝KV cache交叉注意力：draft头直接查询主干预计算的KV cache，完全消除draft侧prefill开销，无需维护独立KV cache
- 聚类词表投影：离线将262K词表聚为2048簇，推理时仅计算Top32簇的token logit，解码计算量降低43倍
- 域适配方案：基于LoRA实现联合微调/两阶段蒸馏，对齐draft头与微调后的主干，避免分布偏移
### 关键实验
在Gemma 4全系列模型上测试：H100上31B模型最高提速3.14倍，三星S26 Ultra端侧E4B模型提速2.18倍；对比EAGLE-3、DFlash等主流方案，31B场景下加速比领先20%以上；域迁移场景下，对齐后的draft头比仅微调主干的方案少1.83倍目标前向传播。
### 核心结论
Speculative解码的效率优化核心是在提升draft接受率的同时，尽可能降低draft本身的计算和内存开销，而非单纯追求draft生成速度
