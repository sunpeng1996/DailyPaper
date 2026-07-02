---
title: 'Making Multimodal LLMs Reliable Chart Data Extractors: A Benchmark and Training
  Framework'
title_zh: 面向可靠图表数据提取的多模态大模型基准与训练框架
authors:
- Yuchen He
- Peizhi Ying
- Liqi Cheng
- Kuilin Peng
- Yuan Tian
- Dazhen Deng
- Yingcai Wu
affiliations:
- Zhejiang University
- Guangdong University of Technology
- State Key Lab of CAD&CG, Zhejiang University
arxiv_id: '2606.29808'
url: https://arxiv.org/abs/2606.29808
pdf_url: https://arxiv.org/pdf/2606.29808
published: '2026-06-29'
collected: '2026-07-02'
category: Multimodal
direction: 多模态大模型 · 图表数据提取
tags:
- Multimodal LLM
- Benchmark
- Chart Extraction
- Training Framework
- Information Extraction
one_liner: 构建无标签真实图表评估基准，提出类人渐进式训练框架提升MLLM图表数据提取精度
practical_value: '- 做竞品分析、行业报告自动化时，可复用该渐进式训练方案微调多模态模型，提升无标注图表的数值提取准确率

  - 内部运营数据可视化自动解析场景，可直接借鉴该基准的评估方法，验证自研MLLM的结构化信息提取能力

  - 涉及多模态数值推理的任务（如广告投放效果图表自动解读、用户行为可视化分析），可优先采用先学坐标映射、后学语义对应的两阶段训练范式'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有图表数据提取方案存在明显短板：交互式工具准确率高但操作繁琐效率低，混合主动式系统效率更高但泛化性差；当前多模态大语言模型（MLLM）可提供统一的图表解析接口，但无可见数据标签场景下的数值提取精度不足，且缺乏针对性评估基准。
### 方法关键点
1. 构建覆盖多元真实场景的无数据标签图表评估基准，可系统测评MLLM的图表结构重建与数值提取能力；
2. 参考人类读图的渐进式认知过程，提出两阶段训练框架：第一阶段让MLLM学习坐标几何规则，第二阶段学习视觉编码到数据的映射关系。
### 关键结果
7B参数模型经训练后达到SOTA性能，数值提取精度大幅优于现有基线模型，用户研究验证其可有效支撑混合主动式图表数据提取工作流。
