---
title: 'Knowledge-Base Gradient Descent: Self-Structuring Learning through Question
  Answering'
title_zh: 知识库梯度下降：通过问答实现知识库自结构学习
authors:
- Masahiro Kato
affiliations:
- The University of Tokyo
arxiv_id: '2611.34841'
url: https://arxiv.org/abs/2611.34841
pdf_url: https://arxiv.org/pdf/2611.34841
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: RAG · 知识库结构自动优化
tags:
- RAG
- KnowledgeBase
- KnowledgeGraph
- SchemaOptimization
- QuestionAnswering
one_liner: 提出通过问答误差迭代优化知识库结构的知识库梯度下降方法，支持图Schema与知识卡片结构
practical_value: '- 电商商品/用户知识库、Agent工具知识库可复用该迭代优化框架：用业务真实query作为学习集，对比预期答案与RAG实际回答的误差，自动提出结构调整（知识卡片拆分、KG关系增删等），验证loss下降则保留，替代人工拍板Schema设计

  - 电商RAG场景优先选择图Schema结构做优化，实验显示Schema优化在跨query泛化上表现更稳定，人类问题集Answer F1提升1.1个点，生成测试集提升12.91个点，优于知识卡片结构

  - 用于结构优化的学习query必须完全匹配业务真实query分布，若用合成query训练，优化后的结构会过拟合合成query，反而在真实用户query上效果下降，如论文中卡片结构优化后合成query涨4.45，人类query降2.89'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RAG系统常出现源数据包含答案却检索失败、回答错误的问题，核心原因是知识库结构（知识单元拆分、关联关系、Schema设计）不合理；传统人工设计Schema成本高、适配业务场景误差大，现有自动建库方法未以问答效果为目标做迭代优化。

### 方法关键点
- 提出Self-Structuring Learning范式，以问答的预期答案与实际回答的误差为优化信号，迭代优化知识库持久化结构
- 知识库梯度下降（KBGD）流程：每轮诊断回答误差→提出结构编辑→重建知识库→验证整体loss下降则保留编辑，兼容图Schema、知识卡片两类知识库结构
- 提出Schema Descent实例化方法，针对知识图谱Schema做实体、关系类型的增删改，显式建模结构编辑的交互影响，避免单独编辑效果叠加的误差

### 关键实验
数据集为5个各包含10篇学术论文的文档集合，对比初始结构、原生段落检索基线；核心结果：Schema优化后生成测试集Answer F1相对初始提升12.91个点，人类问题集提升1.1个点，所有文档的生成测试集均实现涨点；知识卡片优化后生成测试集涨4.45个点，人类问题集降2.89个点。

**最值得记住的一句话**：知识库结构优化的训练query必须完全匹配业务实际接收的query分布，否则优化后的结构只会适配训练query类型，泛化到真实query时效果反而可能下降。
