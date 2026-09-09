---
title: 'WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data'
title_zh: WearableQA：面向真实可穿戴数据的健康推理基准
authors:
- Ji Soo Lee
- Xilun Chen
- Pierce Chuang
- Ashish Shenoy
- Jason Wei
- Dohwan Ko
- Hyunwoo J. Kim
- Benoit Corda
affiliations:
- Meta
- KAIST
- Korea University
arxiv_id: '2609.05405'
url: https://arxiv.org/abs/2609.05405
pdf_url: https://arxiv.org/pdf/2609.05405
published: '2026-09-04'
collected: '2026-09-09'
category: Eval
direction: LLM推理评测 · 可穿戴健康场景
tags:
- Benchmark
- Health Reasoning
- Wearable Data
- LLM Evaluation
- Time Series Reasoning
one_liner: 构建含4084道多选题的可穿戴数据健康推理基准，可精准区分不同LLM的时序生理数据推理能力
practical_value: '- 搭建用户时序行为（如浏览、交易、交互）的LLM推理评测集时，可复用双锚定框架，结合领域知识与人群统计规律批量生成题目，大幅降低标注成本

  - 评估多模态/多信号用户行为的模型推理能力时，可参考「单信号/跨信号+数据/业务逻辑推理」的二维能力拆分框架，精准定位模型短板

  - 布局健康场景电商推荐/导购Agent时，可引入该基准的推理范式对齐用户生理时序特征与健康需求，提升推荐匹配度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基准极少评估AI系统对真实用户长期可穿戴时序记录的推理能力，缺乏保留设备噪声、个体差异等真实特征的评测体系。
### 方法关键点
1. 基于200名真实用户最长500天的可穿戴时序、血液生物标记、人口属性数据，构建含4084道10选多选题的WearableQA基准，完整保留真实数据分布特征；
2. 设计16类问题，沿「数据推理/健康推理」「单信号/跨信号推理」二维轴拆分，可评估不同维度的推理能力；
3. 采用双锚定框架批量生成可靠题目，结合文献验证的生理结论与统计显著的人群规律，保证题目合理性。
### 关键结果
14款闭源/开源LLM在该基准上准确率范围为19.6%~72.9%（随机baseline为10%），多数模型准确率低于60%，可有效区分模型能力且当前仍未被解决。
