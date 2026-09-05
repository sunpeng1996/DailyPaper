---
title: 'GRASP: Graph-Retrieval Automated Scoring Pipeline for Label-Free Multi-Topic
  Essay Grading'
title_zh: GRASP：面向无标注多主题作文评分的图检索自动打分流水线
authors:
- Aafreen Husain
- Samar Shailendra
- Saad Sajid Hashmi
affiliations:
- Melbourne Institute of Technology, Australia
arxiv_id: '2609.03857'
url: https://arxiv.org/abs/2609.03857
pdf_url: https://arxiv.org/pdf/2609.03857
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 无监督自动评分 · 图增强RAG
tags:
- RAG
- Graph Retrieval
- Automated Scoring
- Sentence-BERT
- Zero-Shot Learning
one_liner: 提出无需训练数据的图增强RAG无标注多主题短文自动评分流水线GRASP
practical_value: '- 召回阶段可复用GRAG思路：以向量检索TopK结果为种子节点，沿语义相似图遍历召回漏召的相关item，提升低语义相似度相关物料的召回率

  - 多目标匹配场景可复用匈牙利算法做最优分配，解决召回结果和用户需求/query片段的一对一对齐问题，避免重复匹配

  - 无标注文本分段场景可先用规则启发式兜底，歧义场景调用LLM做校正，平衡推理成本和效果，无需依赖领域训练数据'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统自动短文评分仅支持单主题场景，无标注多主题短文（不同问题的回答混在同一段无拆分标记）的评分缺乏无需训练数据的落地方案。
### 方法关键点
1. 用Sentence-BERT编码所有问题的参考答案，构建FAISS向量索引和参考答案间的语义相似图；
2. 先用句子数启发式规则+LLM消歧，无监督预测学生回答覆盖的主题数，无需领域标注数据；
3. 结合普通余弦RAG和GRAG（以TopK余弦匹配结果为种子遍历语义图补召回）获得候选参考节点；
4. 用匈牙利算法将回答片段和参考节点做唯一最优匹配，避免重复匹配，再用GPT-4.1-mini逐片段打分。
### 关键结果
实验验证检索质量直接影响评分精度，相比纯余弦相似检索，GRAG在不同复杂度的短文场景下均取得效果提升
