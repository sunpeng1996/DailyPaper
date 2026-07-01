---
title: 'TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling
  in Forestry via Compiled Expert Rules and Vision-Language Models'
title_zh: TreeAgent：结合专家规则与VLM的林业偏置标注多智能体通用框架
authors:
- Shiyi Chen
- Nicholas Saban
- Collin Hargreaves
- Huiqi Wang
affiliations:
- University of California, Berkeley
arxiv_id: '2606.31976'
url: https://arxiv.org/abs/2606.31976
pdf_url: https://arxiv.org/pdf/2606.31976
published: '2026-06-30'
collected: '2026-07-01'
category: MultiAgent
direction: 多智体协作 · 专家规则+VLM自动化标注
tags:
- MultiAgent
- VLM
- Expert Rule
- Automated Annotation
- Decision Tree
one_liner: 提出融合专家决策树与VLM的多智能体标注框架，降低专家标注成本并保持可解释性
practical_value: '- 电商内容审核、类目标注场景可复用「专家决策树+多VLM投票」架构，将人工标注规则拆解为决策树节点，每个节点用VLM做局部感知，投票降低VLM幻觉，替代部分人工标注降本

  - 标注平台研发可参考D3解耦框架，把专家规则结构与模型感知逻辑拆分，不同类目、业务的标注规则可零修改适配，无需重复调优模型

  - 推荐系统的用户标签、商品标签标注场景可用该架构，在保留规则可解释性的同时，减少标注人力投入，提升标注一致性'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
专家驱动领域的人工标注普遍存在一致性差、效率低、成本高的问题，是ML任务规模化落地的核心瓶颈，林业遥感树高偏置分类这类细分场景的标注瓶颈尤为突出。
### 方法关键点
1. 构建多智能体系统，将专家决策树作为结构先验，每个决策节点由VLM完成局部语义感知任务，通过多智能体投票机制缓解VLM输出随机性；
2. 提出Decoupled Declarative Decision（D3）框架，将决策结构与模型感知逻辑解耦，支持不同专家定义的决策规则零修改适配。
### 关键结果
在林业树高偏置分类测试集上效果优于所有有监督ML基线，大幅减少专家标注工作量，同时全程保持标注逻辑的可解释性。
