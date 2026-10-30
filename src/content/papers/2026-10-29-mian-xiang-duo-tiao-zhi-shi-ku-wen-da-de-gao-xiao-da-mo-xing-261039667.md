---
title: Efficient LLM-based Subgraph Retrieval for Multi-Hop Knowledge Base Question
  Answering
title_zh: 面向多跳知识库问答的高效大模型子图检索方法
authors:
- Duanyang Yuan
- Sihang Zhou
- Xiaoshu Chen
- Haoyuan Chen
- Ke Liang
- Jian Huang
affiliations:
- National University of Defense Technology
- National Key Laboratory of Equipment State Sensing and Smart Support
arxiv_id: '2610.39667'
url: https://arxiv.org/abs/2610.39667
pdf_url: https://arxiv.org/pdf/2610.39667
published: '2026-10-29'
collected: '2026-10-30'
category: Reasoning
direction: 多跳KBQA · LLM引导MCTS子图检索
tags:
- KBQA
- MCTS
- Subgraph Retrieval
- Multi-hop Reasoning
- LLM
one_liner: 结合MCTS与LLM实现多跳KBQA高效子图检索 兼顾性能与计算效率
practical_value: '- 电商商品/用户知识图谱多跳查询场景，可复用LLM引导MCTS的子图检索框架，替代传统k-hop召回，减少无关节点引入，降低多跳推理的计算开销

  - 搜索推荐的复杂意图理解场景，可借鉴关系边实体化+LLM路径打分反馈的机制，优化多跳召回路径的筛选，提升长路径意图匹配准确率

  - 调用外部知识图谱的Agent系统，可复用这套多终止条件+奖励反向传播的设计，平衡检索召回率和token消耗，提升知识调用效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统多跳KBQA的IR类方法多采用固定k-hop子图或语义相似度召回，会引入大量无关节点，跳数越高噪声越大、计算开销呈指数级上升；现有MCTS类检索方法缺乏语义引导，容易累积中间错误，难以平衡子图质量、答案覆盖率和计算效率。

### 方法关键点
- 提出M-ER框架，将子图检索转化为MCTS树搜索过程，基于UCB1指标做节点选择，优先扩展高相关节点，避免全图遍历
- 引入LLM做双模块优化：反射阶段基于当前推理路径预测下一步检索方向，同时对候选节点按单步正确性、语义一致性、节点有效性三维度打分，反馈优化MCTS的节点选择权重
- 知识图谱关系边实体化为节点，直接计算语义相似度减少匹配偏差，设置路径重复、置信度坍塌、结构终止、答案验证四类终止条件减少无效计算
- 设计奖励分数反向传播机制，从叶节点到父节点迭代更新路径权重，优化后续搜索方向

### 关键实验
在WebQSP、CWQ、MetaQA三个标准KBQA数据集上测试，对比20+三类基线：WebQSP上Hits@1达78.88%，超之前SOTA SR方法7.08%，超MCTS-KBQA 4.28%；相同子图大小下答案覆盖率比基线高10%以上；单query平均耗时6.08s，比同类LLM方法快35%+，token消耗量与基线持平。

最值得记住的结论：LLM的语义理解能力结合MCTS的高效搜索特性，可在多跳检索场景下同时实现效果提升和计算开销下降，无需盲目扩大召回范围
