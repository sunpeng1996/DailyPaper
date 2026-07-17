---
title: 'MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video
  Generation'
title_zh: MultiRef-Compass：多参考条件音视频生成综合评估基准
authors:
- Xiaohan Zhang
- Yuqing Wen
- Junlin Chen
- Yuqi Tang
- Yiting He
- Lizhuo Shao
- Weiming Zhu
- Tengfei Liu
- Yang Shi
- Jialu Chen
affiliations:
- Nanjing University
- Kling Team
- National University of Singapore
- Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
arxiv_id: '2607.14189'
url: https://arxiv.org/abs/2607.14189
pdf_url: https://arxiv.org/pdf/2607.14189
published: '2026-07-14'
collected: '2026-07-17'
category: Eval
direction: 多模态生成 · 评估基准
tags:
- Multimodal
- Evaluation
- Benchmark
- LLM-as-a-Judge
- VideoGeneration
one_liner: 推出面向多参考驱动音视频生成的统一基准，含350个标注样本与4维度14子项的评估协议
practical_value: '- 电商AI短视频生成等多模态生成业务，可直接复用其「基础质量+参考一致性+音视频对齐+指令遵循」四维评估框架，替代零散人工评估

  - LLM-as-a-Judge类评测可复用其重校验增强流程，降低大模型打分偏差，同时提升评估结果的可审计性

  - 多约束条件生成任务的业务评测集搭建，可参考其可控资产组合式样本构建pipeline，低成本快速产出自定义标注样本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频生成基准多聚焦文本驱动、单参考主体保留或孤立音视频对齐场景，未覆盖多参考+文本指令驱动的音视频生成（MR2AV）场景，该场景要求模型同时完成多参考信息推理、同步音视频生成、参考特征保留、多实体组合，现有评测体系无法适配需求。
### 方法关键点
1. 通过可扩展可控的资产组合pipeline构建350个高质量评测样本，覆盖多视角主体保留、多实体绑定、人-物-场景组合三类核心场景；
2. 定义基础质量、参考一致性、音视频一致性、指令遵循4大维度共14个子指标的可解释评估协议；
3. 融合自动指标与重校验增强的MLLM-as-a-Judge框架，兼顾感知保真度与参考约束组合能力的可扩展、可审计评估。
### 关键结果数字
对8款主流MR2AV系统的评测显示，所有模型在各评估维度均存在大幅优化空间，验证了该基准的必要性。
