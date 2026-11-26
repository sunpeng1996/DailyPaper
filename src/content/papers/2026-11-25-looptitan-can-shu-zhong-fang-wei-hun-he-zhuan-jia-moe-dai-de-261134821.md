---
title: 'LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?'
title_zh: LoopTitan：参数重访为混合专家（MoE）带来的实际价值分析
authors:
- Zichen Tian
- Yudong Lu
- Xuansheng Wu
- Na Zou
- Xia Hu
- Guanchu Wang
- Qianru Sun
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Singapore Management University
arxiv_id: '2611.34821'
url: https://arxiv.org/abs/2611.34821
pdf_url: https://arxiv.org/pdf/2611.34821
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: MoE架构优化 · 大模型训练
tags:
- MoE
- Looped Transformer
- Muon
- Parameter Sharing
- Model Training
one_liner: 通过严格对照实验证明循环MoE的参数重访本身几乎无增益，收益来自结构、优化器与额外计算
practical_value: '- 落地MoE时无需优先考虑循环参数重访架构，改用「更深+每层更少专家」的标准MoE结构即可拿到几乎全部收益，还能避免循环结构带来的工程复杂度

  - 目前用AdamW训练MoE的业务场景，直接切换到Muon优化器可获得比调整MoE架构高3~4倍的loss收益，无需改动模型结构

  - 用AdamW训练深层MoE时，可通过给中间层加残差缩放（等效降低中间层学习率）的方式，缓解AdamW层间步长不均的问题，获得稳定loss下降

  - 评估新MoE架构时要做严格资源对齐（参数、FLOPs、KV cache）的对照组，避免把结构调整、优化器带来的收益错算成新架构的增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有循环MoE架构被报道在相同参数、FLOPs、KV cache预算下显著优于标准MoE，但过往研究未将参数重访的独立价值与网络结构调整、残差缩放等伴随设计的增益拆解开，行业对循环MoE的价值存在认知偏差，需要明确参数重访的实际贡献。
### 方法关键点
- 严格构造资源对齐的非重访对照组：将循环MoE的优化方案拆分为网络形状调整（更深更窄、每层更少专家）、专家布局调整、残差缩放、参数重访4个顺序步骤，前3步输出无参数重访的对照模型，所有步骤保证参数、FLOPs、KV cache偏差在5%以内
- 分别采用AdamW和Muon两种优化器训练，验证优化器对各步骤增益的影响
- 额外设置固定参数、增加计算量的场景对照：对比「增加1次参数重访」和「增加层数、减少每层专家数的标准MoE」的收益差异
### 关键实验
实验基于DCLM-baseline数据集、Qwen3 tokenizer，覆盖1.3B~3.0B参数量、5B~24B训练tokens规模：
1. 匹配预算下，AdamW时循环MoE较标准MoE降6.3mBPB，无重访对照组降7.0mBPB，参数重访本身反而升0.7mBPB（处于噪声区间）；Muon时循环MoE较标准MoE降3.2mBPB，无重访对照组降3.8mBPB，参数重访本身升0.6mBPB
2. 固定参数增加31%计算量时，增加1次重访降11.5mBPB，无重访的更深标准MoE降10.4mBPB，拿到90.2%的增益，参数重访仅贡献1.1mBPB
3. 标准MoE仅将优化器从AdamW切换为Muon，即可获得23.6mBPB的loss下降，是循环MoE全流程增益的3.7倍
### 核心结论
循环MoE的参数重访本身几乎没有独立价值，所有宣称的增益都可以通过标准MoE调整网络结构、更换Muon优化器、增加计算量来获得。
