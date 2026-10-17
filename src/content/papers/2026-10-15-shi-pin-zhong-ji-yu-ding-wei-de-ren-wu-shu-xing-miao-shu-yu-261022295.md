---
title: Grounded Human-Attributed Description and Activity Recognition in Videos
title_zh: 视频中基于定位的人物属性描述与行为识别
authors:
- Jay N. Paranjape
- Jurijs Nazarovs
- Rohan Sarkar
- Yue Guo
- Lipeng Ke
- Sankar Venkataraman
- Vishal M. Patel
- Nataraj Jammalamadaka
affiliations:
- Johns Hopkins University
- Amazon
arxiv_id: '2610.22295'
url: https://arxiv.org/abs/2610.22295
pdf_url: https://arxiv.org/pdf/2610.22295
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态视频理解 · 人物行为识别
tags:
- Vision-Language Model
- Video Understanding
- Activity Recognition
- Attention Mask
- Evaluation Metric
one_liner: 提出GHADAR视频人物属性与行为识别任务框架，配套数据集、VLM优化方法及无标注评估体系
practical_value: '- 短视频电商商品关联人物行为识别场景，可复用约束VLM cross-attention mask的方法，聚焦指定检测框内目标，减少背景干扰提升识别准确率

  - 生成式短视频内容审核场景，可借鉴VLM-based评估方案，跳过文本对齐环节直接对比生成结果与原始视频的概念匹配度，降低人工标注成本

  - 短视频用户兴趣建模场景，可复用GHADAR的开放集人物属性/行为标注思路，批量生成训练数据补充用户行为标签库'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频人物行为识别数据集多局限于群体/单人/闭集场景，训练出的模型泛化性差；传统评估指标依赖人工标注与精确文本匹配，落地实用性不足。
### 方法关键点
1. 定义GHADAR新任务：输入视频中人物的定位框，输出对应人物的开放集属性描述与行为识别结果，更贴合真实业务场景需求
2. 基于AVA-Actions生成配套数据集，自动生成人物属性、行为的开放集标注
3. 训练VLM时约束cross-attention掩码，强制模型聚焦定位框内的目标人物信息，过滤背景干扰
4. 提出无人工标注的VLM评估框架，直接对比原始视频与生成结果的概念匹配度，规避文本精确匹配的不合理性
### 关键结果
所提方法在GHADAR任务上性能优于所有现有SOTA VLM
