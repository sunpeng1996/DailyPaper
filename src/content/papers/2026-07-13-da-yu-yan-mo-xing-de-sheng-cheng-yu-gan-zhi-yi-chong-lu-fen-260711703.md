---
title: 'Production and Perception in LLMs: A Token Probability Approach'
title_zh: 大语言模型的生成与感知：一种Token概率分析方法
authors:
- Anna Marklová
- Jiří Milička
- Martina Vokáčová
- Rudolf Rosa
affiliations:
- Faculty of Arts, Charles University, Prague
- Faculty of Mathematics and Physics, Charles University, Prague
arxiv_id: '2607.11703'
url: https://arxiv.org/abs/2607.11703
pdf_url: https://arxiv.org/pdf/2607.11703
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: 大语言模型行为特性 · prompt框架效应
tags:
- LLM
- token probability
- prompt engineering
- decoder-only LLM
- psycholinguistics
one_liner: 通过Token概率测量验证仅prompt框架即可让解码器LLM产生稳定的生成-感知差异
practical_value: '- 做prompt engineering时可利用生成/感知框架差异：文案生成类任务用生产导向prompt，用户query/内容理解类任务用感知导向prompt，提升专项任务效果

  - 长序列LLM调用时，感知类prompt的影响集中在序列开头，做RAG/Agent长上下文处理时可将感知类指令放在上下文最前，强化指令遵循效果

  - 评估LLM生成内容（如电商商品文案、推荐话术）质量时，可采用生成-感知概率差作为量化评估指标，替代部分人工标注降低成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
心理语言学已证实人类语言生成与感知存在不对称性，但仅基于next-token prediction的LLM是否存在类似功能差异缺乏实证，过往研究多依赖元语言prompt而非直接量化测量。
### 方法关键点
以Llama-3.1-8B为基准，用生产类prompt生成诗歌，再分别用改写后的生产类prompt、感知类prompt对相同token重打分，控制prompt表层差异变量，同时在5款开源基座/指令微调LLM上做复现验证。
### 关键结果
生产-感知概率差是生产-生产概率差的1.8倍，两类区间无重叠；生产-生产组相关度接近天花板，证明差异来自沟通框架而非prompt措辞；感知prompt的影响在序列开头最强，随上下文积累逐渐衰减，该效应在所有测试模型中均稳定存在。
