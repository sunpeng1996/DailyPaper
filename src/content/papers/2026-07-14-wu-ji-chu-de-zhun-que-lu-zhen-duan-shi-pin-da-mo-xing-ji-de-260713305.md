---
title: 'Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video
  LLM Benchmarks'
title_zh: 无基础的准确率：诊断视频大模型基准中的视觉依赖解离问题
authors:
- Jae Joong Lee
affiliations:
- Purdue University
arxiv_id: '2607.13305'
url: https://arxiv.org/abs/2607.13305
pdf_url: https://arxiv.org/pdf/2607.13305
published: '2026-07-14'
collected: '2026-07-18'
category: Eval
direction: 多模态大模型 · 视频理解评测
tags:
- Video-LLM
- Benchmark
- Evaluation
- Visual Understanding
- Multimodal
one_liner: 提出视觉依赖差距VDG指标，验证视频LLM基准高准确率不一定对应强视觉理解能力
practical_value: '- 短视频/商品视频类多模态推荐场景选型LLM时，可引入VDG指标审计模型是否真的依赖视觉信息而非语言先验，避免选到刷榜高但实际视觉理解能力弱的模型

  - 做视频时序相关的推荐/理解任务时，需针对性优化模型的时序信息利用能力，现有多数开源视频LLM的时序顺序对准确率贡献几乎为0

  - 多模态模型内部评测可复用「黑屏→单帧→乱序帧→原视频」的诊断阶梯，快速定位模型能力边界，避免评测结果误导业务迭代'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频LLM基准默认准确率越高代表视觉理解能力越强，该假设未被验证，易导致模型选型、架构优化方向偏离实际需求。
### 方法关键点
提出Visual Dependency Gap（VDG），量化模型在原视频与黑屏输入下的单题正确率差值；设计「黑屏→单帧→乱序帧→原视频」诊断阶梯，搭配McNemar检验、多帧率消融实验，验证准确率与视觉依赖的关联性。
### 关键结果
20款参数量2B-78B的视频LLM在MVBench上，原视频下正确率存在显著差异（p=0.0003），但黑屏下无差异（p=0.53）；属性感知任务强依赖视觉输入，时序推理任务表现接近纯语言基线；16款开源模型中，帧多样性贡献绝大多数视觉收益，时序顺序对准确率贡献接近0；API类视频LLM的VDG区间为0.025-0.315，能力差异显著。
