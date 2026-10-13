---
title: 'OccludeBench: Can VLMs Find What''s Missing?'
title_zh: OccludeBench：视觉语言模型能否识别图像中被遮挡的物体？
authors:
- Jasin Cekinmez
- Addison J. Wu
- Ryo Mitsuhashi
- Linrong Cai
- Xingyu Fu
- Zhuang Liu
affiliations:
- Princeton University
arxiv_id: '2610.13790'
url: https://arxiv.org/abs/2610.13790
pdf_url: https://arxiv.org/pdf/2610.13790
published: '2026-10-09'
collected: '2026-10-13'
category: Multimodal
direction: 多模态推理 · VLM基准构建
tags:
- VLM
- Benchmark
- Visual Reasoning
- Multimodal Eval
- Occlusion
one_liner: 构建遮挡物体推理基准OccludeBench与诊断工具，提出干预方法缩小VLM性能gap
practical_value: '- 电商多模态商品理解场景可复用inpaint-then-confront逻辑，对遮挡、缺失的商品部件/包装内容先生成候选再验证，提升识别准确率

  - 多模态Agent的视觉环境感知模块，可参考OccludeTrace四阶段诊断框架定位推理瓶颈，针对性优化遮挡场景下的物体识别能力

  - 多模态模型业务落地评测时，可参考OccludeBench的分层（直接物理线索/上下文推理）设计，构造贴合业务场景的细粒度评测集'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有视觉语言模型（VLM）对图像中被完全遮挡的缺失物体的推理能力缺乏系统性量化评估，推理失效的具体瓶颈和优化方向不明确。
### 方法关键点
1. 构建人工标注的OccludeBench基准，拆分两类任务：从阴影、反射等直接物理线索恢复隐藏物体，从全局场景上下文推断缺失物体；
2. 提出四阶段OccludeTrace诊断框架，定位VLM视觉推理的失效节点；
3. 针对性能gap提出inpaint-then-confront干预策略，先生成隐藏物体候选再与可见物理线索校验。
### 关键结果
- 5款VLM直接线索任务平均准确率42.7%，较上下文推理任务低20.0个百分点，人类两类任务准确率63.4%/68.5%无显著差距；
- 核心瓶颈为全图场景下从投影恢复对应物体步骤，失败案例中仅50%可完成该环节，成功案例中该步准确率达91%；
- inpaint-then-confront方法可将两类任务的性能差缩小至统计不显著水平。
