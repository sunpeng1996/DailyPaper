---
title: Neighborhood-Aware Dual Biomedical Entity Linking
title_zh: 邻域感知双路生物医学实体链接方法
authors:
- Yicheng Tao
- Jie Liu
affiliations:
- University of Michigan, Department of Electrical Engineering and Computer Science
- University of Michigan, Gilbert S. Omenn Department of Computational Medicine and
  Bioinformatics
arxiv_id: '2608.04144'
url: https://arxiv.org/abs/2608.04144
pdf_url: https://arxiv.org/pdf/2608.04144
published: '2026-08-04'
collected: '2026-08-08'
category: Other
direction: 生物医学实体链接 · 知识库匹配优化
tags:
- Entity Linking
- Knowledge Base
- Retrieval
- Reranking
- Score Fusion
one_liner: 提出含邻域感知检索、双路重排序的三阶段PILOT框架，在5个生物医学实体链接基准上达SOTA且推理高效
practical_value: '- 检索阶段可借鉴「query侧提及改写+知识库侧实体邻域嵌入池化」思路，引入知识图谱结构信息，提升电商商品/品牌实体链接、SPU标准化场景的召回准确率

  - 重排序阶段可复用表层特征+上下文特征双路打分融合的trick，适配多信号互补的召回、粗排场景

  - 大知识库匹配场景可直接套用「检索-重排序-分数融合」三阶段架构，兼顾效果与推理效率'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
生物医学实体链接需将临床、科研文本中的提及映射到结构化知识库实体，面临三大核心挑战：知识库实体规模过大无法全量打分、提及歧义高仅靠词汇匹配无法消歧、不同语料标注规则差异大。
### 方法关键点
三阶段PILOT框架：1）邻域感知检索：同时从query侧改写提及、知识库侧池化实体邻域嵌入，注入本体结构信息缩小候选集；2）双路重排序：分别从表层形态、上下文语义两个互补视角对候选集打分；3）分数融合：融合两路打分结果输出最终匹配实体。
### 关键结果
在5个广泛使用的生物医学实体链接基准上平均性能达SOTA，同时保持高效推理速度。
