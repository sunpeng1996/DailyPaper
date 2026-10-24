---
title: 'Local Evidence, Global Failure: Diagnosing Speech-Vision Temporal Composition
  in Audio-Visual Language Models'
title_zh: 局部证据全局失效：视听大模型语音-视觉时序组合问题诊断
authors:
- Jaehong Myung
- Seunghun Oh
- Unsang Park
affiliations:
- Department of Artificial Intelligence, Sogang University, Seoul, Republic of Korea
- Department of Computer Science and Engineering, Sogang University, Seoul, Republic
  of Korea
arxiv_id: '2610.25352'
url: https://arxiv.org/abs/2610.25352
pdf_url: https://arxiv.org/pdf/2610.25352
published: '2026-10-18'
collected: '2026-10-24'
category: Multimodal
direction: 视听多模态大模型 时序组合能力诊断
tags:
- Multimodal-LLM
- Temporal-Reasoning
- Training-free
- Audio-Visual-Understanding
- Diagnostic-Framework
one_liner: 提出免训练TED诊断框架，拆分局部视觉验证与语音关联聚合，大幅提升AV-LLM时序任务准确率
practical_value: '- 多模态内容理解场景可复用TED的「时序拆分+局部证据聚合」思路，解决长视频/长时序多模态推理精度低的问题

  - 免训练优化思路可直接迁移到冻结大模型的多模态业务场景，无需重新训练即可提升时序相关推理效果

  - 时序锚定+分窗查询的设计可复用在直播/短视频内容理解、多模态商品检索等业务的推理链路中'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有AV-LLM执行全视频语音-视觉决策时，即使局部可提取有效视觉证据，也常出现决策错误，核心缺陷是时序组合能力不足。
### 方法关键点
提出免训练Temporal Evidence Decomposition (TED)诊断框架：先通过ASR获取语音转录文本与发声时间区间，针对无音频的视频窗口，要么用转录文本查询完成时序对齐、时序预测任务，要么用答案候选查询完成跨模态时序绑定任务，最终基于发声区间聚合所有局部证据输出结果。
### 关键结果
在SVHalluc数据集上测试4个冻结AV-LLM，时序预测准确率从原生全视频提问的29.3%~33.7%提升至79.3%~82.2%；固定时序区域可用条件下，锚定发声区间的设计仍能带来明确收益。
