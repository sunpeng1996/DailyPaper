---
title: Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning
title_zh: 数学推理场景下的答案不变性与表示敏感性研究
authors:
- Zhixu Silvia Tao
affiliations:
- Princeton University
arxiv_id: '2609.28442'
url: https://arxiv.org/abs/2609.28442
pdf_url: https://arxiv.org/pdf/2609.28442
published: '2026-09-23'
collected: '2026-09-24'
category: Reasoning
direction: 大模型数学推理 · 内部表征机制
tags:
- Mathematical Reasoning
- LLM Representation
- Permutation SNR
- Model Evaluation
- Internal Mechanism
one_liner: 测试16款1B-8B LLM，证实数学推理准确率与规则顺序的表征区分度正相关
practical_value: '- 针对规则类推理业务（如电商满减计算、营销规则匹配Agent），可引入Permutation SNR指标评估模型对规则顺序的表征能力，提前预判推理准确率

  - 面向输入顺序不影响输出的场景（如多条件商品筛选、多标签用户意图理解），无需强制模型表征不变性，允许保留顺序相关表征可提升最终输出准确率

  - 评估LLM推理能力时，除最终准确率外可补充内部表征区分度指标，更精准筛选适配规则推理场景的基座模型'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
逻辑等价的数学规则仅调整顺序时，业界默认推理准确率高的LLM会忽略顺序差异、生成相似内部表征，该假设从未被系统性验证。
### 方法关键点
构造多组规则重排但答案完全一致的合成多步函数运算测试集，提出Permutation SNR指标量化模型对规则顺序的表征区分度，覆盖测试16款参数量1B~8B的主流LLM。
### 关键结果
层平均Permutation SNR与模型数学推理准确率呈稳定正秩相关，所有测试场景下Spearman相关系数最高达0.86；推理效果越好的模型，对等价规则不同排序的内部表征差异越大，打破了「输出不变则内部表征必须不变」的固有认知。
