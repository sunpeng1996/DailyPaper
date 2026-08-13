---
title: Post-Calibration Reliability Reranking of Relevance Decisions via Label-wise
  Monotone Projection
title_zh: 基于标签维度单调投影的相关性决策后校准可靠性重排序
authors:
- Inwoo Tae
- Yongjae Lee
affiliations:
- UNIST
- LinqAlpha
arxiv_id: '2608.10406'
url: https://arxiv.org/abs/2608.10406
pdf_url: https://arxiv.org/pdf/2608.10406
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 推荐/搜索 · 相关性决策可靠性校准
tags:
- Calibration
- Relevance Ranking
- Reranking
- Selective Prediction
- Confidence Estimation
one_liner: 在不修改原有预测标签和校准概率的前提下，通过标签级单调映射生成可靠性分数实现校准后预测的风险重排序
practical_value: '- 电商搜索/广告相关性审核场景可直接复用：为Exact/Substitute/Irrelevant等不同相关性标签单独训练单调可靠性映射曲线，无需修改原有排序模型输出即可提升低置信度错case的优先审核效率

  - 预算有限的fallback场景：自动放行低风险query-商品对，高风险转人工/强模型，MRP重排序后10%覆盖率下自动预测准确率平均提升7.6pp，适合降本需求

  - 工程上MRP是可插拔后处理层，不依赖原有模型结构，兼容温度缩放、直方图校准等所有常用后校准方法，上线成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有后校准方法仅保证置信度与平均正确率对齐，同一置信度下不同预测标签的实际正确率仍存在显著差异，导致系统要么过度信任错误预测，要么不必要地搁置正确预测，无法满足搜索、电商等场景下按风险优先级做fallback、审核的需求。

### 方法关键点
- 提出Label-wise Monotone Reliability Projection（MRP），针对每个预测的相关性标签单独训练单调映射函数，将校准后的置信度转换为对应决策的实际正确率（可靠性分数）
- 约束同一标签下置信度越高可靠性分数越高，完全保留原有预测标签和校准后的类概率，仅修改用于重排序的可靠性分数
- 采用一维单调晶格实现，搭配二阶差分正则化避免曲线震荡，训练目标为二分类交叉熵拟合实际正确性

### 关键实验
在6个覆盖电商搜索、网页搜索、QA检索的公开数据集、6种常用后校准器上测试，MRP平均降低NLLcorrect 0.12，提升AUPR-Error 0.13，降低AURC 0.05；预算fallback场景下10%覆盖率时自动预测准确率平均提升7.6pp，90%覆盖率时仍提升2pp，全程不改变原有模型的全量准确率和ECE。

最值得记住的结论：校准解决的是置信度的数值准确性，而MRP解决的是同置信度下预测的风险优先级排序，二者是互补而非替代关系。
