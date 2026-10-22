---
title: 'Loopholing All the Way: Language Modeling with pure Self-Conditioning'
title_zh: LAW：基于纯自条件的连续语言生成模型
authors:
- Adrien Deschenaux
- Nadezhda Ilieva
- Justin Deschenaux
- Manuel Madeira
- Dorina Thanou
- Aurélien Lucchi
- Antonio Orvieto
- Caglar Gulcehre
- Pascal Frossard
affiliations:
- EPFL
- University of Basel
- Microsoft AI
- ELLIS Institute Tübingen
- MPI for Intelligent Systems
arxiv_id: '2610.30068'
url: https://arxiv.org/abs/2610.30068
pdf_url: https://arxiv.org/pdf/2610.30068
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM生成 · 纯自条件建模
tags:
- Self-Conditioning
- Diffusion Language Model
- Expectation Embedding
- Generative Model
- Language Modeling
one_liner: 提出仅传播期望嵌入自条件状态的LAW模型，性能超现有扩散语言模型，接近自回归模型
practical_value: '- 生成式推荐/Agent推理场景可复用LAW的纯自条件状态传播思路：无需每步采样离散token，仅最后一步解码，减少多步生成的误差累积，提升长序列（商品文案、推理链、推荐理由）生成质量

  - 训练带自条件的生成模型时，可直接复用温度正则化trick：训练时随机缩放logits温度，让模型适配不同采样温度下的自条件状态，大幅提升低温度采样的准确率，适配电商高确定性生成需求（合规文案、精准活动话术）

  - 现有预训练扩散语言模型可通过LAW的微调范式快速提效：仅增加8%~26%的训练步数就能大幅提升推理性能，适合业务侧快速迭代已有生成模型，无需从零训练'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有扩散语言模型（DLM）支持并行双向生成，可弥补自回归模型左到右因式分解的缺陷，但每步独立采样离散token会丢弃预测不确定性，导致信息坍塌；此前自条件（SC）仅作为辅助模块嵌入扩散模型，未被作为核心生成范式探索，无法充分发挥连续状态传递的优势。

### 方法关键点
- 提出纯自条件生成模型LAW，生成全程仅传播自条件状态，无需每步采样离散token，仅在最后一步解码为输出，大幅减少多步采样误差；
- 自条件状态采用去噪器预测下的**期望嵌入（E.E.）**，而非模型隐层表示，避免状态与预训练token嵌入分布不匹配问题；
- 训练加入温度正则化，随机缩放logits温度生成自条件状态，让模型适配不同采样温度的输入；采用多-pass训练仅回传最后一步梯度，降低训练成本。

### 关键结果
- Sudoku（180NFE）：硬难度准确率96.5%，优于此前最优LDDM-U的91.0%；
- GSM8K（T=1，1024NFE）：从零训练准确率42.2%，超基线LDDM-U的34.5%；微调预训练Duo checkpoint后准确率提升至48.1%，较原Duo的17.2%提升30.9个百分点；
- OpenWebText（64NFE）：相同熵下生成困惑度接近自回归模型（ARM），1024NFE时在熵≤5.2区间优于ARM。

最值得记住的一句话：纯自条件状态传播可作为独立的生成范式，而非仅作为扩散模型的辅助模块，性能超过主流带自条件的离散扩散模型。
