---
title: 'Multi-Label Agreement: A Flexible Framework for Inter-Annotator Reliability'
title_zh: 多标签一致性：标注者间可靠性评估的灵活框架
authors:
- Tim Menzner
- Jochen L. Leidner
affiliations:
- Center for Responsible Artificial Intelligence (CRAI), Coburg University of Applied
  Sciences
arxiv_id: '2610.37292'
url: https://arxiv.org/abs/2610.37292
pdf_url: https://arxiv.org/pdf/2610.37292
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: 多标签标注一致性评估框架
tags:
- Inter-Annotator Agreement
- Multi-Label Annotation
- Evaluation Metric
- Hamming Distance
- Annotation Consistency
one_liner: 提出适配多标签标注任务的MLA一致性评估框架，支持多维度输出，配套开源Python实现
practical_value: '- 做用户兴趣标签、商品类目打标、Query意图标注等多标签标注场景时，可直接复用MLA框架替代传统单标签IAA指标，更准确评估标注一致性

  - 框架支持item/label/corpus多维度结果输出，可快速定位低一致性的具体标签、样本，针对性优化标注指南，降低标注成本

  - 配套开源Python实现可直接集成到标注平台的质控模块，无需从零开发多标签一致性评估逻辑'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统Cohen's kappa、Krippendorff's alpha等标注者间一致性（IAA）指标仅适用于单标签场景，无法覆盖多标签任务中标签集对比、联合选中/遗漏的评估需求，缺少灵活可解释的多标签一致性评估方案。
### 方法关键点
提出MLA框架，保留每个样本的完整二进制标签向量，基于平均pairwise Hamming一致性同时覆盖联合选中、联合遗漏两类场景；支持pooled-marginal、Gwet AC1、固定基线三种归一化方式，可输出样本级、标签级、语料级三类结果，内置最低一致性诊断能力。
### 关键结果
通过实例验证与蒙特卡洛模拟证明MLA结果受标签流行度、标签集定义、预期一致性模型选择的影响规律，配套开源Python实现可直接调用，透明可解释，不预设通用最优归一化方案。
