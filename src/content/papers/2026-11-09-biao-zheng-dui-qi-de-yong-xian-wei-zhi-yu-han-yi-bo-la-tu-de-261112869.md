---
title: Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic
  Representation Hypothesis
title_zh: 表征对齐的涌现位置与含义：柏拉图表征假设的深入验证
authors:
- Julia Herbst
- Simon Roschmann
- Quentin Bouniot
- Zeynep Akata
affiliations:
- Helmholtz Munich
- Technical University of Munich
- Munich Center for Machine Learning
- LTCI, Télécom Paris, Institut Polytechnique de Paris
arxiv_id: '2611.12869'
url: https://arxiv.org/abs/2611.12869
pdf_url: https://arxiv.org/pdf/2611.12869
published: '2026-11-09'
collected: '2026-11-11'
category: Multimodal
direction: 多模态表征对齐 · PRH验证
tags:
- Representational Alignment
- Platonic Representation Hypothesis
- Cross-modal
- Unimodal Model
- Evaluation Baseline
one_liner: 系统分析跨模态表征对齐的涌现位置，验证PRH成立的数据条件，给出对齐度量的标准基线
practical_value: '- 跨模态商品搜索/多模态推荐场景，可复用高能力预训练单模态模型做轻量对齐，无需从头训练多模态对齐模型，大幅降低训练成本

  - 做跨模态表征相似度度量时，必须引入单模态、多模态基线消除模型宽深带来的指标干扰，避免业务迭代中的错误判断

  - 多模态训练优先使用高信息密度的干净图文对，可显著提升跨模态表征对齐效果，适配生成式推荐的多模态Item表征构建需求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
柏拉图表征假设（PRH）提出高能力视觉、语言模型会收敛到相似表征空间，但近期研究质疑新LLM是否符合该趋势，且现有表征相似度度量易受模型宽深干扰，缺乏合理基线支撑结论。
### 方法关键点
1. 逐层、逐维度分析单模态模型间跨模态对齐的涌现位置；
2. 控制图文caption的纯净度与信息量，验证新模型下PRH的成立条件；
3. 构建多数据集下的单模态、多模态对齐基线，消除模型结构带来的指标偏差。
### 关键结果
- 仅当caption足够干净、信息密度达标时，新模型依然符合PRH的能力-对齐正相关趋势；
- 高能力单模态模型的跨模态对齐效果可超过显式对齐的视觉语言模型，但仍远低于同模态模型间的对齐度。
