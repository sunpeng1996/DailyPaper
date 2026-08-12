---
title: 'Order Matters: LVLMs as Judges for Temporal Reasoning in Image Sequences'
title_zh: 顺序优先：LVLM作为图像序列时序推理评估器的缺陷分析
authors:
- Martina Ianaro
- Guilherme Fernandes
- Maurizio Gabbrielli
- Joao Magalhaes
affiliations:
- University of Bologna
- NOVA School of Science and Technology
- NOVA Laboratory for Computer Science and Informatics
arxiv_id: '2608.10908'
url: https://arxiv.org/abs/2608.10908
pdf_url: https://arxiv.org/pdf/2608.10908
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 多模态时序推理能力评估
tags:
- LVLM
- Temporal Reasoning
- Multimodal Evaluation
- Positional Bias
- Sequence Understanding
one_liner: 揭示LVLM作为图像序列评估器的时序推理结构性缺陷，提出需发展时序感知评估范式
practical_value: '- 业务中若使用LVLM做商品短视频、种草脚本等多模态时序内容的自动打分，不可直接用单帧点式评分，必须补充时序顺序校验逻辑

  - 搭建多模态Agent推理链路时，需注意LVLM的首因/近因位置偏差，可通过关键帧随机重排多次投票的方式抵消位置干扰

  - 长序列多模态内容一致性校验场景下，现有Transformer结构LVLM能力不足，可拆分短序列处理或额外增加时序规则模块兜底'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
生成式多媒体已从静态图像生成发展到复杂交互视觉叙事阶段，现有自动评估系统对序列连续性感知缺失，无法区分连贯叙事与语义打乱的矛盾序列，依赖LVLM作为评估器的范式存在结构性缺陷。
### 方法关键点
通过多组诊断探针实验，对比LVLM在单帧点式评分、时序顺序成对判别两类任务的表现差异，定位性能缺陷的底层来源。
### 关键结果
LVLM单帧点式评分表现合格，但执行时序顺序成对判别任务时性能出现灾难性崩溃；存在显著首因、近因效应，帧的位置对判定结果的影响远高于语义一致性；该偏差根源来自Transformer的因果掩码与旋转位置编码设计，现有结构天然不适配长程视觉时序推理。
