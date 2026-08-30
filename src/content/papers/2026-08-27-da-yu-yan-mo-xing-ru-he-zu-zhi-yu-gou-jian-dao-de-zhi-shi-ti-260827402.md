---
title: How Language Models Organize and Structure Moral Knowledge
title_zh: 大语言模型如何组织与构建道德知识体系
authors:
- Orion Reblitz-Richardson
arxiv_id: '2608.27402'
url: https://arxiv.org/abs/2608.27402
pdf_url: https://arxiv.org/pdf/2608.27402
published: '2026-08-27'
collected: '2026-08-30'
category: LLM
direction: 大语言模型内部知识表征结构分析
tags:
- LLM
- Linear Probe
- Knowledge Representation
- Moral Alignment
- Representation Space
one_liner: 通过线性探针揭示LLM道德知识表征的几何结构，既区分多道德维度又共享通用道德组件
practical_value: '- 合规/价值观对齐场景可复用线性探针方法，无需全量微调即可快速定位LLM内部的风险表征维度，降低对齐成本

  - Agent多场景合规管控可利用道德表征的通用共享组件，仅需少量样本对齐即可覆盖多类合规要求，提升对齐效率

  - 内容风控系统可参考多独立探针架构，同时并行检测多个合规类别，相比串行单分类器大幅提升检测效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM道德相关研究仅停留在道德/非道德二分类检测层面，无法解释其内部道德知识的组织逻辑，也无法验证LLM是否具备结构化的道德理解能力。
### 方法关键点
基于道德基础理论（MFT）定义的6类道德范畴，在开源LLM上训练6个独立线性探针，分析不同探针输出的表征向量在隐空间的几何关系，同时构建匹配的非道德概念组作为对照。
### 关键结果数字
1. 道德表征维度既不坍缩为单一检测器也不相互孤立，平均两两余弦相似度0.26，远高于非道德对照组的0.013，存在道德专属的共享通用组件；
2. 该几何结构在不同架构、不同规模LLM中保持一致，且预训练早期就已形成，远早于探针准确率饱和点；
3. 道德困境的表征2.7倍于错配基线由基础道德维度组合而来，大部分方差编码冲突特定结构而非预存判断。
