---
title: 'Richness Is Not Evenness: Ordered Renyi Crossings under Self-Training'
title_zh: 丰富度≠均匀度：自训练场景下的Rényi熵有序交叉现象
authors:
- Pranjal Srivastava
affiliations:
- University of Michigan
arxiv_id: '2611.08892'
url: https://arxiv.org/abs/2611.08892
pdf_url: https://arxiv.org/pdf/2611.08892
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 大语言模型自训练 · 熵指标评估
tags:
- Self-Training
- Rényi Entropy
- Model Collapse
- LLM Evaluation
- Sampling Temperature
one_liner: 揭示LLM递归自训练中不同阶Rényi熵的有序交叉规律，否定单一熵指标判定模型退化的有效性
practical_value: '- 评估LLM生成的商品文案、Agent回复等业务内容多样性时，不要仅用单一熵或词汇丰富度指标，需同时报告不同阶Rényi熵完整分布避免误判

  - 自训练蒸馏电商垂类LLM时，可通过调整训练采样温度平衡生成内容的词汇丰富度与均匀度：T≈1时可减少生僻词同时提升常用词分布合理性

  - 判定自训练后模型是否退化时，不能仅依赖熵指标变化，必须搭配点击率、回复准确率等独立业务质量指标做最终校验'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
过往研究依赖单一多样性指标评估LLM自训练过程中的模型退化问题，不同指标常给出矛盾结论，无法准确反映生成质量的实际变化。
### 方法关键点
以GPT-2为基底开展9代递归自训练实验，控制训练数据的采样温度变量，全程采用固定采样器测量各阶Rényi熵变化，跨语言、文本表示、随机种子完成多组鲁棒性验证。
### 关键结果
① 随训练温度升高，不同阶Rényi熵由降转升的顺序固定：min-entropy最先，之后依次是collision entropy、Shannon entropy、observed richness；
② T=1无截断训练场景下，第9代模型词汇类型较初代减少24%，但collision entropy高出0.91bit；
③ 单一熵指标的变化方向无法可靠判定模型似然表现优劣，推荐同时报告固定预算下的熵分布与独立质量指标。
