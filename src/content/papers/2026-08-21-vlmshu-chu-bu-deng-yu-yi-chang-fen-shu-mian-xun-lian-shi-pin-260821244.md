---
title: 'A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video
  Anomaly Detection'
title_zh: VLM输出不等于异常分数：免训练视频异常检测中的排序压缩问题
authors:
- Inpyo Song
- Jangwon Lee
affiliations:
- SungKyunKwan University
arxiv_id: '2608.21244'
url: https://arxiv.org/abs/2608.21244
pdf_url: https://arxiv.org/pdf/2608.21244
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态大模型 · 输出分数校准
tags:
- VLM
- Training-free
- Ranking Compression
- Score Readout
- Anomaly Detection
one_liner: 揭示免训练VLM视频异常检测的排序压缩问题，概率读出法较生成读出提升5-13个指标点
practical_value: '- 电商内容审核、商品违规检测、推荐素材质量打分等VLM打分类任务，不要直接取最高概率生成答案作为分数，改用全候选答案概率分布加权计算，可显著提升排序效果

  - 落地时无需调整原有prompt、解码策略，仅需额外读取候选答案的概率分布即可实现概率读出，改造工程量极小

  - 做排序类大模型应用时要规避排序压缩问题：仅取top1输出会导致大量样本分数撞车，损失相对顺序信息量，优先保留细粒度分数分辨率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
免训练VLM做视频异常检测时需输出每个片段的标量异常分用于排序，但现有方案直接取最高概率生成答案作为分数，排序精度不达预期，且答案接口的设计长期被忽略为无关紧要的格式细节。

### 方法关键点
明确定义VLM打分任务的答案接口包含两部分：可接受答案的范围（answer scale）、将模型输出映射为分数的读出规则。对比两类读出规则：1）生成读出：仅取最高概率答案映射为分数；2）概率读出：基于全量候选答案的分布加权计算分数。

### 关键结果
在4个7-8B VLM上测试，所有答案规模、基准、指标组合下，概率读出均优于生成读出，4组基准-指标对的平均提升幅度为5~13个点；即便答案规模达91种，生成读出仅能产出4~18种离散分数，存在严重的排序压缩问题，远低于概率读出的细粒度分数分辨率，且该优势不受解码策略、prompt措辞的影响。
