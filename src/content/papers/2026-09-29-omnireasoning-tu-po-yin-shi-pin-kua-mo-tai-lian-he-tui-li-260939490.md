---
title: 'OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning'
title_zh: OmniReasoning：突破音视频跨模态联合推理性能上限
authors:
- Junming Lin
- Yuxuan Wang
- Zhenxin Lei
- Yuxin Liu
- Ruixun Liu
- Yinsong Yan
- Ling Wang
- Minghao Han
- Yunfei Chu
- Shun Lei
affiliations:
- 北京大学智能科学与技术学院
- 北京大学通用人工智能国家重点实验室
- 阿里巴巴集团Alibaba Token Hub
arxiv_id: '2609.39490'
url: https://arxiv.org/abs/2609.39490
pdf_url: https://arxiv.org/pdf/2609.39490
published: '2026-09-29'
collected: '2026-10-06'
category: Multimodal
direction: 多模态大模型 · 音视频联合推理
tags:
- Multimodal-Reasoning
- Audio-Visual-Model
- Self-Distillation
- Benchmark
- Data-Engine
one_liner: 提出音视频联合推理基准、数据引擎与模态因子自蒸馏方法，大幅提升多模态模型推理性能
practical_value: '- 直播/短视频内容理解场景可复用OmniQA数据引擎思路，自动构造带时间戳证据链的音视频QA对，降低多模态训练数据标注成本

  - 多模态推荐场景需跨模态信息融合推理时，可借鉴Modality-Factored Self-Distillation（MFSD）方法，拆分各模态贡献做token级信用分配，提升模型推理精度

  - 短视频/直播相关多模态Agent能力评估时，可复用OmniReasoningBench的评估范式，确保任务要求音视频双模态联合推理，避免模态shortcut'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型研究普遍独立处理各模态，音视频联合推理能力缺乏针对性评估，能力挖掘不充分，缺少配套基准、训练数据与优化方法。
### 方法关键点
1. 发布OmniReasoningBench基准，包含1150道必须同时依赖音视频证据的多选/开放题，覆盖视频内推理、跨场景推理两类任务
2. 搭建OmniQA数据引擎，自动生成带时间戳线索链的音视频联合推理QA对，产出112K SFT训练数据、19K RL训练数据
3. 提出MFSD自蒸馏方法，在各模态专属线索上下文下评估采样响应，解耦单模态线索与跨模态交互贡献，实现token级信用分配
### 关键结果
基于Qwen3-Omni-30B底座训练的OmniReasoning-30B-A3B在OmniReasoningBench上准确率达42.5%，较底座提升9.3pp；在OmniVideoBench上准确率达50.0%，较底座提升12.8pp，同时在Video-MME-v2等通用、长视频基准上均获得显著增益。
