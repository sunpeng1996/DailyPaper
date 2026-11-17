---
title: 'The Price of Choosing Examples: Context Overfitting in Adaptive In-Context
  Learning'
title_zh: 选择示例的代价：自适应上下文学习中的上下文过拟合
authors:
- Xiaoyu Li
- Jiangxuan Long
affiliations:
- University of New South Wales
- The University of Hong Kong
arxiv_id: '2611.21251'
url: https://arxiv.org/abs/2611.21251
pdf_url: https://arxiv.org/pdf/2611.21251
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: LLM 上下文学习泛化理论
tags:
- In-Context Learning
- Context Overfitting
- PAC-Bayes
- RAG
- Prompt Engineering
one_liner: 量化自适应prompt构造的上下文过拟合风险，提出可验证的稳定检索规则SCAR
practical_value: '- RAG/Agent系统prompt调优不要反复复用同一份验证集选择最优配方，会触发上下文过拟合，导致线上效果远低于验证集表现；电商导购、搜索query改写等场景需预留完全独立的holdout集做最终评估，验证集数据不可用于prompt迭代

  - 可复用SCAR方法替代硬选最优prompt/检索结果，用带温度的Gibbs采样从候选池中抽样，在holdout效果仅下降0.01的前提下，获得可验证的线上风险上界，减少AB测试成本

  - 多轮prompt编辑的信息代价可叠加核算，若候选prompt总数为M，验证集效果的过拟合gap约为√(logM/k)，k为验证样本数；不要盲目扩大候选池规模，避免验证集结果完全失真'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前In-Context Learning、RAG系统的prompt构造流程均为看到query后自适应完成检索、重排、示例选择、多轮编辑，现有ICL理论默认prompt示例为预采样得到，完全忽略了自适应选择带来的上下文过拟合问题：在复用的验证集上表现最优的prompt，上线后实际效果往往大幅低于验证集得分，缺乏可量化的统计代价度量和可落地的风险规避方案。
### 方法关键点
- 定义**上下文容量**，即数据存储与最终prompt转录本之间的互信息/近似最大信息，可覆盖检索、重排、验证集复用、多轮prompt编辑全流程的信息泄露量，支持多轮代价叠加核算
- 证明自适应ICL的泛化界为O(√(κ/k))，κ为上下文容量，k为选入prompt的示例数，该界为紧界，最坏场景下的过拟合代价不可避免
- 提出SCAR（Stability-Constrained Adaptive Retrieval）规则，用PAC-Bayesian正则化的Gibbs采样替代硬选最优prompt，平衡验证集拟合度与过拟合风险，可输出可验证的部署风险上界
### 关键实验
在Banking77意图分类数据集上测试Qwen2.5-7B、GPT-4.1-mini两类模型，覆盖64种检索prompt配方，共24000次重采样选择事件：所有事件下提出的泛化界均成立；SCAR的风险上界在k=64（Qwen2.5-7B）/128（GPT-4.1-mini）时，超过99%的概率低于zero-shot误差；SCAR的holdout效果与硬选最优配方仅差0.01，且风险上界更紧。

最值得记住的结论：自适应选择的prompt的验证集效果不能直接作为部署效果的依据，要么控制prompt构造过程的信息容量，要么用完全独立的新鲜数据评估。
