---
title: 'Xeno-Interpretability: Investigating the Alien Minds of LLMs'
title_zh: 异质可解释性：探索大语言模型的非人类认知原生表征体系
authors:
- F. Pierucci
- M. Bracale Syrnikov
- M. Prandi
- M. Galisai
- F. Giarrusso
- P. Bisconti
affiliations:
- Icaro Foundation
- Sant’Anna School of Advanced Studies
- Sapienza University of Rome
- University of Amsterdam
arxiv_id: '2609.20408'
url: https://arxiv.org/abs/2609.20408
pdf_url: https://arxiv.org/pdf/2609.20408
published: '2026-09-17'
collected: '2026-09-19'
category: LLM
direction: 大语言模型可解释性 · 原生内部表征
tags:
- LLM
- interpretability
- xeno-representation
- multi-agent
- AI-safety
one_liner: 提出异质可解释性研究框架，探索LLM中无对应人类概念的原生内部表征规律
practical_value: '- 做LLM4Rec/Agent的bad case排查时，可借鉴「识别-表征-因果干预」流程，无需强行对应人类概念，直接定位影响输出的隐层表征节点做干预，解决不符合预期的推荐/回复问题

  - 多Agent协作的推荐/广告系统中，可监控跨Agent传播的无人类对应语义的隐层信号，避免未知表征传播导致的系统输出不可控风险

  - 做LLM微调对齐（比如电商文案生成、推荐理由生成）时，可量化异质表征占比，平衡模型原生能力和人类可解释性的tradeoff，避免为了可解释性过度损失模型效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM可解释性研究均基于人类已有概念（真实性、有害性、拒答等）开展，忽略了模型可能存在的无对应人类认知的原生内部表征，这类表征可能导致模型行为不可预测，甚至在多Agent系统中传播放大风险。
### 方法关键点
1. 提出异质可解释性（xeno-interpretability）研究范式，将模型表征空间划分为人类可解释语义空间和无人类概念对应的异质语义空间
2. 分离表征识别与语义解释环节，明确即便无法用人类语言描述表征含义，也可对其完成定位、几何特征刻画、因果干预、下游行为关联
3. 给出异质表征的系统性识别实验框架
### 关键结果
证明LLM内部可区分的表征空间远大于有限人类描述能覆盖的空间，异质表征可在多Agent交互中稳定传播且无法通过人类可读通信完全观测
