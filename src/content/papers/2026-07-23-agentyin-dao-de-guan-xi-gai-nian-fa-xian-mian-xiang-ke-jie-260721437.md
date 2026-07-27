---
title: 'Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin
  Assessment'
title_zh: Agent引导的关系概念发现：面向可解释手术切缘评估
authors:
- Nooshin Maghsoodi
- Amoon Jamzad
- Robert Policelli
- Mohammad Farahmand
- Dilakshan Srikanthan
- Martin Kaufmann
- Kevin Y. M. Ren
- Shaila Merchant
- Sonal Varma
- Ross Walker
affiliations:
- Queen's University, Kingston, Canada
arxiv_id: '2607.21437'
url: https://arxiv.org/abs/2607.21437
pdf_url: https://arxiv.org/pdf/2607.21437
published: '2026-07-23'
collected: '2026-07-27'
category: Agent
direction: Agent 无监督概念发现与知识图谱对齐
tags:
- Agentic AI
- Concept Learning
- Knowledge Graph
- Unsupervised Learning
- Interpretability
one_liner: 提出无预定义概念标签的Agent引导概念发现框架，结合知识图谱提升模型可解释性与泛化性
practical_value: '- 无监督概念发现思路可迁移到电商推荐的用户/物品语义概念挖掘，无需人工标注概念标签，大幅降低运营成本

  - Agent动态调整概念权重的机制可用于GenRec的个性化概念排序，根据转化效率动态优化生成推荐策略

  - 知识图谱对齐概念的方法可复用在RAG检索结果的语义校准，避免生成内容与业务常识、品类规则冲突'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
医疗场景深度学习模型依赖离体标注数据训练，术中noisy无标注数据下泛化性差，且黑盒属性难以临床落地；监督式概念学习所需的概念标注在质谱分析场景获取成本极高。
### 方法关键点
1. 无需预定义概念标签，直接从原始数据中学习可解释语义概念
2. 训练阶段推理Agent自动迭代优化概念的语义描述，根据任务相关性自适应调整概念权重
3. 引入生化知识图谱对生成概念做对齐校验，确保与已知代谢关系一致
### 关键结果
在皮肤癌、乳腺癌数据集上，平衡准确率、敏感度均优于基线模型；术中场景测试下假阳性显著降低，对手术环境的泛化性表现更优。
