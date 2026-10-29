---
title: Can Discrete Tokens Serve as Semantically Lossless Representations of Visual
  Signals?
title_zh: 离散视觉Token能否作为视觉信号的无损语义表示？
authors:
- Jialv Zou
- Xiaotong Li
- Zhengrong Yue
- Xu Huang
- Yaxin Luo
- Wenhao Yan
- Haodong Li
- Wenyu Liu
- Xinggang Wang
affiliations:
- Huazhong University of Science and Technology
- Meituan LongCat
- Shanghai Jiao Tong University
- Peking University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.37662'
url: https://arxiv.org/abs/2610.37662
pdf_url: https://arxiv.org/pdf/2610.37662
published: '2026-10-26'
collected: '2026-10-29'
category: Multimodal
direction: 多模态表征 · 离散视觉Token量化
tags:
- Discrete Visual Token
- Vector Quantization
- Multimodal LLM
- FVQ
- Semantic Representation
one_liner: 提出因子化向量量化FVQ，实现性能匹敌连续表征的离散视觉表示，大幅超越现有离散多模态SOTA
practical_value: '- 电商多模态内容理解（商品图OCR、属性识别）场景可直接复用FVQ量化方案，用统一离散Token范式搭建多模态模型，避免异构连续/离散表征的融合成本

  - 构建生成式多模态推荐系统时，FVQ输出的无损离散视觉Token可直接与LLM文本Token拼接，大幅降低多模态生成链路的开发复杂度

  - 工业级多模态模型训练可参考论文结论，无需执着于降低量化误差，优先提升有效bit预算即可快速提下游任务效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
离散视觉Token可天然适配LLM的next-token预测范式，是原生多模态建模的核心基础，但业界普遍假设量化误差会带来不可避免的语义损失，认定连续视觉表征是离散表示无法突破的性能上限。
### 方法关键点
以多模态理解效果为语义保真度代理的验证显示，量化误差与语义保真度无正相关，有效bit预算才是下游性能的核心决定因子。针对现有量化器随码本增加性能快速饱和的问题，Factorized Vector Quantization（FVQ）采用对称并行码本，对视觉特征的互补固定维度视图分别量化，可随bit预算提升持续优化性能，最终在多模态理解任务上追平连续视觉表征效果。
### 关键结果数字
工业级多模态数据训练后，模型在9项指标平均精度上较UniAR、Emu3-Chat分别高出22.8%、59.2%，是首个可与Qwen3-VL等强连续表征模型匹敌的离散表示方案，细粒度OCR任务效果也达到相当水平。
