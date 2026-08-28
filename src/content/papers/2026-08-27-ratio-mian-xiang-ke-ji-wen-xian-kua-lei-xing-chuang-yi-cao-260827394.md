---
title: 'RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific
  Literature'
title_zh: 《RATIO：面向科技文献跨类型创意操作的检索基准》
authors:
- Maayan Sharon
- Tom Hope
affiliations:
- The Hebrew University of Jerusalem
- The Allen Institute for AI (AI2)
arxiv_id: '2608.27394'
url: https://arxiv.org/abs/2608.27394
pdf_url: https://arxiv.org/pdf/2608.27394
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: 文献启发式多类型检索评估基准
tags:
- Retrieval Benchmark
- Distant Supervision
- Scientific Literature
- Ideation Retrieval
- LLM Vetting
one_liner: 构建覆盖三类创意检索意图的大规模科技文献检索基准RATIO及配套训练评估框架
practical_value: '- 电商多意图搜索/推荐场景可复用三类ideation move的分类逻辑，给用户检索意图打标签，分别优化「找解决方案、找泛化品类、找细分款」的召回效果

  - 大规模垂直领域检索训练数据构建可复用「discourse-marker弱监督+LLM校验+人工抽检」的流水线，大幅降低标注成本

  - 多意图检索系统可参考operation-specific fine-tuning策略，针对不同检索意图单独微调召回模型，比通用模型效果提升更显著'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有科技文献检索仅关注语义相似匹配，未覆盖创意阶段不同抽象层级的检索需求（找解决方案、泛化思路、落地案例），缺乏对应评估与训练基准。
### 方法关键点
1. 定义三类ideation move检索任务：Address（给定问题找对应解决方案）、Broaden（给定具体问题找更通用的理论/框架）、Specify（给定抽象方向找具体落地实例）
2. 基于千万级CS领域全文文献，将原本仅用于分类任务的discourse-marker弱监督方法扩展到语料级检索样本生成，再结合LLM校验、人工审核构建基准数据集
### 关键结果
实验显示针对单类检索任务的专属微调能显著提升检索器匹配效果，但当前最优模型仍有较大性能缺口，RATIO可支撑后续相关检索模型的训练与评估
