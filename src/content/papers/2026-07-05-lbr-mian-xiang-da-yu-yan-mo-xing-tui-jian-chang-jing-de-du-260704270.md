---
title: 'LBR: Towards Mitigating Length Bias in Large Language Models for Recommendation'
title_zh: LBR：面向大语言模型推荐场景的长度偏差缓解框架
authors:
- Hongchen Li
- Bohao Wang
- Jingbang Chen
- Weiqin Yang
- Hang Pan
- Bingde Hu
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- The Chinese University of Hong Kong
- University of Science and Technology of China
- Bangsun Technology
arxiv_id: '2607.04270'
url: https://arxiv.org/abs/2607.04270
pdf_url: https://arxiv.org/pdf/2607.04270
published: '2026-07-05'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 长度偏差缓解
tags:
- LLM4Rec
- Length Bias
- Debiasing
- Sequential Recommendation
- Attention Calibration
one_liner: 从注意力和解码双端设计轻量通用框架，缓解LLM推荐的长度偏差，平均NDCG@5提升16.82%
practical_value: '- 输入侧可直接复用Length-Aware Attention Calibration方法：仅需在attention logits加长度依赖偏移项，无额外推理开销，可无缝嵌入所有Transformer结构的LLM推荐模型

  - 输出侧解码时用基于Trie分支系数的Effective Information Length替换原生token长度归一化：解决传统长度归一化偏长短/长item的问题，尤其适配Trie约束的生成式推荐解码场景

  - 无需修改模型结构、无需增加训练数据的轻量debias方案：额外仅2个可学习参数，训练推理开销几乎可忽略，适合线上大流量的生成式推荐业务快速落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM-based推荐将任务转化为token级生成任务，但普遍存在未被充分研究的长度偏差问题：输入侧长文本item占更多token，获得不成比例的高注意力权重，干扰用户偏好建模；输出侧自回归对数似然打分天然偏好短item，传统长度归一化又会反向偏向长item，同时忽略token信息异质性，最终同时损伤推荐精度和公平性。

### 方法关键点
- 输入侧**Length-Aware Attention Calibration**：在attention logits中加入与item长度负相关的偏移项，抵消长item的注意力优势，偏移项通过简单线性函数建模，可与推荐目标端到端联合训练
- 输出侧**Effective Information Length Normalization**：基于Trie节点分支系数用Hartley熵量化每个token的信息含量，累加得到item的有效信息长度，替换原生token长度做打分归一化，同时按token信息量加权对数似然得分，实现不同长度item的公平比较

### 关键结果
在3个Amazon公开数据集（Toy、Office、Book）上，在BIGRec、LLaRA两个主流LLM推荐骨干上验证，对比S-DPO、IGD等10余种SOTA基线，平均NDCG@5提升16.82%，训练推理开销几乎无增加，不同长度item的推荐分布方差降低50%以上，同时提升精度和公平性。

### 核心结论
LLM推荐的长度偏差本质是输入侧token数量带来的注意力不平等、输出侧token信息异质性带来的打分不公平，无需复杂改动的轻量校准即可获得显著收益
