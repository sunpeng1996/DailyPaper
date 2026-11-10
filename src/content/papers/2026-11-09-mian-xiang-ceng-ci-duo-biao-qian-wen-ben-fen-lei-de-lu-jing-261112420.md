---
title: Path-Level Structural and Semantic Alignment for Hierarchical Multi-Label Text
  Classification
title_zh: 面向层次多标签文本分类的路径级结构与语义对齐方法
authors:
- Xindi Wang
- Aifen Xiong
- Baiyang Wang
- Xuri Ge
- Robert Mercer
- Frank Rudzicz
- Yifan Peng
- Zhumin Chen
- Hongjun Wang
affiliations:
- School of Artificial Intelligence, Shandong University
- School of Information Science and Engineering, Shandong University
- Department of Computer Science, Western University
- Faculty of Computer Science, Dalhousie University
- Department of Population Health Sciences, Weill Cornell Medicine
arxiv_id: '2611.12420'
url: https://arxiv.org/abs/2611.12420
pdf_url: https://arxiv.org/pdf/2611.12420
published: '2026-11-09'
collected: '2026-11-10'
category: Other
direction: 层次多标签分类 · 对比训练优化
tags:
- HMTC
- Contrastive Learning
- LLM
- Auxiliary Training
- Text Classification
one_liner: 以根到节点的完整标签路径为共享单元，新增两类辅助训练目标，提升层次多标签文本分类性能
practical_value: '- 电商分层商品类目/用户标签分类场景可复用根到节点路径建模思路，替代单个标签建模，强化层级关联约束

  - 对比学习训练阶段可引入PathSimNCE思路，给结构相似路径设置分级监督信号，提升深层标签预测准确率

  - 静态标签语义向量不足的场景，可调用LLM生成带样本上下文的正路径描述补充监督信号，推理无额外开销'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：层次多标签文本分类（HMTC）需同时捕获标签间结构依赖与不同层级细粒度语义，现有方法结构、语义监督分离，仅建模单个标签或局部关系，深层、细粒度标签预测效果不佳。
**方法关键点**：以根到节点的完整标签路径为共享单元，训练阶段新增两类辅助目标，推理阶段保留标准多标签分类器无额外开销：1. PathSimNCE：基于层级感知的对比目标对齐文档表征与分层路径，给结构相关路径提供分级监督，同时保留真实路径的显式监督；2. 语义对齐目标：用LLM生成依赖文档上下文的正路径描述，补充静态标签表征之外的上下文相关标签语义。
**关键结果**：在3个公开基准数据集上取得一致性能提升，结构对齐对更深层级的效果增益更突出，语义对齐可额外提升细粒度标签的预测效果。
