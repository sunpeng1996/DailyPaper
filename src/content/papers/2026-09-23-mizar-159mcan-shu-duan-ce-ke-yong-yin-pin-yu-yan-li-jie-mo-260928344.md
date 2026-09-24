---
title: 'Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding'
title_zh: Mizar：159M参数端侧可用音频语言理解模型
authors:
- Kaiyang Li
- Shaobo Han
- Yue Tian
- Shihao Ji
affiliations:
- NEC Laboratories America, Inc, USA
- School of Computing, University of Connecticut, USA
arxiv_id: '2609.28344'
url: https://arxiv.org/abs/2609.28344
pdf_url: https://arxiv.org/pdf/2609.28344
published: '2026-09-23'
collected: '2026-09-24'
category: Multimodal
direction: 多模态 · 小体量音频语言模型
tags:
- Audio-Language-Model
- Compact-Model
- Edge-Deployment
- Multimodal
- Three-Stage-Training
one_liner: 提出架构+数据+三阶段训练方案的159M音频语言模型，超同规模SOTA，支持单CPU端侧推理
practical_value: '- 小体量跨模态模型的三阶段训练范式可直接复用：先做跨模态对齐、再下游任务微调、最后定向补弱，平衡新能力注入与已有知识保留，适合落地时快速迭代小模型

  - 轻量跨模态衔接方案可借鉴：用频率融合映射层连接预训练单模态编码器与小参数基座LM，大幅降低跨模态模型的训练与部署成本

  - 端侧多模态Agent选型参考：159M规模多模态模型可实现单CPU 1s级推理延迟，适合离线语音客服、商品音频导购等电商场景端侧落地'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有音频语言模型（ALM）参数量普遍偏大，无法满足内存、算力受限的端侧设备本地部署需求，亟需200M参数以内的小体量、高性能ALM支撑离线音频理解场景。
### 方法关键点
1. 架构层面：将紧凑型CED-Small音频编码器通过频率融合映射器连接135M参数的SmolLM2-135M基座，总参数量仅159.3M；
2. 训练流程：采用三阶段训练范式，Stage1完成音频-语言对齐，Stage2做音频相关任务微调，Stage3做post-training定向补强薄弱技能同时保留已有能力；
3. 监督数据：混合ReasonAQA、AudioMCQ、AVQA多类音频问答数据集做训练监督。
### 关键结果
在MMAU、MMAR、ADQA-clean三个基准测试集上平均准确率分别达52.92%、42.42%、36.02%，全面超越同参数规模（<200M）此前的SOTA ALM；单CPU本地推理MMAU基准问题的平均延迟仅1.09s，端侧部署友好
