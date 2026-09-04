---
title: 'Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of
  Tokens'
title_zh: 稀疏读出棱镜：基于特征而非Token解释Logit Lens得分
authors:
- Matteo He
- William F. Shen
- Xinchi Qiu
- Nicholas D. Lane
affiliations:
- University of Cambridge
arxiv_id: '2609.01936'
url: https://arxiv.org/abs/2609.01936
pdf_url: https://arxiv.org/pdf/2609.01936
published: '2026-08-31'
collected: '2026-09-04'
category: LLM
direction: 大模型可解释性 · logit lens分析
tags:
- Logit-Lens
- LLM Interpretability
- Sparse Decomposition
- Unembedding Matrix
- Corpus Robustness
one_liner: 提出无语料依赖的稀疏读出棱镜SRP，通过特征分解解决logit lens分析的语料依赖问题
practical_value: '- LLM4Rec可解释性分析场景可复用SRP分解unembedding矩阵的思路，摆脱推荐场景特定语料依赖，稳定分析不同层logit生成逻辑

  - 生成式推荐/广告文案生成场景可将SRP提取的稀疏特征作为可控生成控制信号，降低语料偏移导致的生成结果波动

  - Agent调用LLM决策场景中可通过SRP分析中间层关键特征贡献，做决策过程可解释性校验，降低幻觉风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Logit lens是分析Transformer大模型中间层预测演化过程的常用方法，但现有lens解码结果依赖训练语料，相同隐状态在不同语料训练的lens下会输出不同token，无法实现跨场景、跨lens的稳定分析。
### 方法关键点
1. 提出Sparse Readout Prism（SRP），仅基于unembedding矩阵权重做稀疏分解，无需任何训练语料
2. 将任意token的logit或logit差值拆解为稀疏读出特征的贡献之和，用特征作为lens分析的核心单元，替代易受语料影响的token标识
### 关键结果
SRP的稀疏近似替换原读出矩阵后，对logit差值的重建效果比6种最优基线高出8.9-17.3个百分点；消融特征时，logit差值的变化幅度与SRP计算的特征贡献成正比；即使token解码结果随语料变化，SRP提取的主导读出特征仍保持稳定。
