---
title: 'Cartridges++: KV Cache Compression without Off-Context Derailment'
title_zh: Cartridges++：无上下文外偏离的KV缓存压缩方法
authors:
- Sonia Laguna
- Joao Monteiro
- Marco Cuturi
- Pierre Ablin
- Eleonora Gualdoni
affiliations:
- Apple
- ETH Zurich
arxiv_id: '2609.35621'
url: https://arxiv.org/abs/2609.35621
pdf_url: https://arxiv.org/pdf/2609.35621
published: '2026-09-28'
collected: '2026-09-29'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- compression
- long context
- inference optimization
- Cartridges
one_liner: 针对Cartridges KV压缩的跨上下文干扰问题，提出双优化方案，保留保真度同时恢复模型原生能力
practical_value: '- 电商/Agent场景预计算长上下文KV缓存（如商品库、客服知识库）时，可复用数据混合trick：训练时混入1-5%比例的无关query样本，几乎不损失上下文相关回答准确率，还能大幅降低无关query的回答幻觉

  - 推理侧轻量路由方案可直接落地：用kNN匹配query和预存的上下文相关query embedding，90%+准确率判断是否加载KV缓存，无关query直接走无缓存模式，工程实现成本极低

  - 做长上下文RAG/Agent效果评估时，必须新增无关query的能力保留评估（通用知识、指令遵循、上下文污染三个维度），避免上线后用户问无关问题出现离谱回答'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于学习的KV缓存压缩方法（如Cartridges）在长上下文复用场景下，仅优化上下文内query的回答准确率，但部署时存在严重的隐形成本：用户询问与缓存内容无关的问题时，模型被缓存内容干扰，出现幻觉、通用知识退化、指令遵循能力下降，干扰程度甚至超过加载完整长上下文，而原有评估体系仅测试上下文保真度，完全掩盖了这些缺陷，严重影响落地体验。

### 方法关键点
- 训练侧优化$C_D^{++}$：在Cartridges自监督训练的QA对中，混入γ比例（推荐0.05）的通用无关query对，无关样本以无缓存的原生模型输出为蒸馏目标，约束压缩KV在无关query下不干扰模型原生行为，无额外推理开销
- 推理侧优化$C_R^{++}$：新增轻量kNN relevance router，用query embedding与上下文相关query池的相似度判断是否加载KV缓存，阈值通过保形校准得到，无关query直接走无缓存模式，无需重新训练原有Cartridges

### 关键实验
在QASPER-16、LongHealth-10、MTOB等4个长上下文基准，压缩率0.1%-20%区间内，对比H2O、SnapKV、Attention Matching等7种KV压缩基线：
- Cartridges++保留原Cartridges 99%+的上下文内回答准确率，同时将上下文外通用知识准确率从62%提升至75%，上下文污染率从22%降至7%，接近无缓存原生模型表现
- $C_R^{++}$路由准确率达90%+，可正确接受90%以上相关query、拒绝90%以上无关query

### 核心结论
可复用的压缩KV缓存不能只评估上下文内信息保留能力，还必须评估其在无关query下的干扰程度，这是上线前不可忽略的核心指标。
