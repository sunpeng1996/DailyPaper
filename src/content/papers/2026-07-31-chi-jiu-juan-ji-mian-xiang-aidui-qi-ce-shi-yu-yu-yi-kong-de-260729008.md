---
title: 'Persistent Convolution: A Topological Framework for AI Alignment Testing and
  Semantic Space Characterization'
title_zh: 持久卷积：面向AI对齐测试与语义空间表征的拓扑框架
authors:
- Tyler Ashoff
- Jordan Rodu
affiliations:
- University of Virginia
arxiv_id: '2607.29008'
url: https://arxiv.org/abs/2607.29008
pdf_url: https://arxiv.org/pdf/2607.29008
published: '2026-07-31'
collected: '2026-08-03'
category: Eval
direction: AI模型评估 · 语义空间对齐测试
tags:
- Semantic Space
- AI Alignment
- Topological Data Analysis
- Model Evaluation
- Persistent Homology
one_liner: 提出基于拓扑持久同伦的无维度限制多模态语义空间对齐测试方法，用于模型选择与评估
practical_value: '- 推荐/广告场景下，当离线AUC、召回率等指标饱和时，可将业务预设的品类分层、用户分层等概念结构作为baseline，用该方法对比不同微调版本模型的embedding空间与baseline的对齐度，选择更符合业务认知的模型，避免唯指标论。

  - LLM+Agent的意图识别、工具调用模块选型时，可将人工标注的意图层级结构作为对齐基准，对比不同prompt工程、不同LoRA微调版本的表征对齐度，不需要大量标注样本即可快速完成选型。

  - 多模态推荐场景下，可使用该方法校验文本、图像、商品属性等不同模态embedding空间的语义结构一致性，不受维度限制，直接为多模态融合策略优化提供量化依据。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有AI模型评估过度依赖测试集指标，在小样本、垂直细分等场景下测试集容易饱和，无法有效区分性能相近的模型优劣；同时传统embedding对比方法受维度、模态限制，无法跨模型、跨模态统一验证模型表征是否符合人类认知的知识结构，缺乏可解释的对齐评估能力。

### 方法关键点
- 基于拓扑持久同伦，将任意维度、任意模态的embedding空间转换为持久图，进一步生成持久景观、持久剪影两种拓扑表征，消除维度、模态差异带来的对比障碍
- 采用能量统计、Wasserstein距离、JSD三种指标，结合置换检验实现两个语义空间的正式对齐假设检验，输出统计显著性结果，量化对齐程度
- 支持高度自定义对齐baseline：可使用人工构建的知识图谱、概念层级结构、甚至手绘的2D概念关系图作为基准，适配不同业务偏好与评估需求

### 关键结果
- 艺术品分类任务：CLIP的不同LoRA微调版本测试集准确率全部≥96.88%，其中6个版本达100%，指标完全饱和的情况下，该方法可清晰区分不同LoRA权重的语义空间与三类艺术家聚类baseline的对齐度，α/r=0.5的微调版本对齐度最优
- 多边形形态分类任务：5个训练数据覆盖度不同的CNN模型测试集准确率全部≥96.83%，指标无显著差异，该方法可有效追踪语义结构变化：10%数据覆盖的模型语义空间更接近平滑过渡的真实数据生成过程，50%数据覆盖的模型更符合分类任务的聚类需求

最值得记住的一句话：当测试集指标无法区分模型时，语义空间的拓扑结构对齐度是更符合业务认知的模型选择依据。
