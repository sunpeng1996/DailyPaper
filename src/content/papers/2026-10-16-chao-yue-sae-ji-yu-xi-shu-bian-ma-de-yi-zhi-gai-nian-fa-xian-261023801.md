---
title: 'Beyond SAEs: Consistent Concept Discovery with Sparse Coding'
title_zh: 超越SAE：基于稀疏编码的一致概念发现方法
authors:
- Jinho Choi
- Hyesu Lim
- Jaegul Choo
- Steffen Schneider
affiliations:
- KAIST
- Helmholtz Munich
arxiv_id: '2610.23801'
url: https://arxiv.org/abs/2610.23801
pdf_url: https://arxiv.org/pdf/2610.23801
published: '2026-10-16'
collected: '2026-10-20'
category: LLM
direction: 大模型可解释 · 稀疏字典学习
tags:
- SAE
- Sparse Coding
- Dictionary Learning
- Interpretability
- Consistency
one_liner: 提出ConSDL方法，用逐样本稀疏编码替代SAE线性编码器，提升字典学习跨种子一致性
practical_value: '- 电商推荐的用户/物品表征稀疏解耦场景，可替换SAE为ConSDL的逐样本稀疏编码方案，提升跨训练批次的表征一致性，降低线上特征分布偏移

  - LLM4Rec可解释分析场景，采用ConSDL学习的稳定字典，跨训练种子的概念对齐误差更低，适合合规要求高的推荐理由生成业务

  - RAG检索向量稀疏化压缩场景，ConSDL的稳定字典可减少不同批次训练的向量分布偏移，降低召回效果波动'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
Sparse autoencoders (SAE) 是当前大模型表征分解、可解释分析的主流方案，但相同配置不同随机种子训练得到的字典差异大，可复现性、可靠性不足，限制了落地应用。
### 方法关键点
提出Consistent Sparse Dictionary Learning (ConSDL)，替换SAE的标准线性编码器为逐样本稀疏编码优化；合成分析验证，逐样本优化得到的系数比单步线性编码器推理的系数更优，稀疏编码是更可靠的字典学习机制。
### 关键结果
- 16种合成实验设置下，ConSDL实现接近完美的字典与系数恢复
- 4种视觉、语言实验场景下，对比6个SAE基线平均水平，字典一致性提升17.6%，系数一致性提升35.9%，达到SOTA跨种子一致性
