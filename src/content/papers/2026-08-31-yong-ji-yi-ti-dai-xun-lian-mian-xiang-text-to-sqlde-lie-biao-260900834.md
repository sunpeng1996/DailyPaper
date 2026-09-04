---
title: 'Replacing Training with Memory: Listwise Selection for Text-to-SQL'
title_zh: 用记忆替代训练：面向Text-to-SQL的列表式选择方法
authors:
- Yeonseok Jeong
- Soyoung Yoon
- Seongjun Lee
- Seung-won Hwang
affiliations:
- IPAI, Seoul National University
- KAIST
arxiv_id: '2609.00834'
url: https://arxiv.org/abs/2609.00834
pdf_url: https://arxiv.org/pdf/2609.00834
published: '2026-08-31'
collected: '2026-09-04'
category: Reasoning
direction: 大模型推理优化 · 免微调记忆检索
tags:
- Text-to-SQL
- Listwise Selection
- Memory Retrieval
- No Fine-tuning
- Positional Bias Mitigation
one_liner: 提出免微调的列表式Text-to-SQL选择器，通过结构化记忆与排名聚合提升选择效率与精度
practical_value: '- 候选集排序场景（如召回结果排序、多Agent输出选择）可复用结构化记忆替代微调的思路，将历史匹配规则蒸馏为可检索记忆，降低微调成本

  - 列表式排序的位置偏差问题，可借鉴多输入排列+聚合排名的方案，结合pointwise预筛降低额外推理开销

  - Agent执行SQL查询的电商用户自助分析、BI场景可直接复用本方法优化Text-to-SQL候选选择精度，无需额外微调LLM'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Text-to-SQL系统多采用「生成-执行-选择」pipeline，通过列表式选择器对比多候选选优，但这类选择器微调成本高，且存在原生位置偏差问题。
### 方法关键点
1. 构建可复用结构化记忆替代模型参数学习选择行为，记忆从训练数据蒸馏，存储自然语言到库表元素、SQL操作、预期输出的映射规则，作为列表式评估候选的显式判据，全程无需微调；
2. 聚合多组输入排列的排名结果缓解位置偏差，结合执行结果与pointwise打分提前过滤低质候选，降低推理开销。
### 关键结果
在BIRD-dev基准上，使用相同候选集时，比SOTA选择器方法R^3-SQL平均执行准确率高2.02pp，token消耗降低2.92倍，兼容现有主流LLM，选择稳定性显著优于现有方法。
