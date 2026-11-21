---
title: 'SpecWM: Turning Verification into Refinement for Streaming World Models'
title_zh: SpecWM：面向流式世界模型的验证转精修推理框架
authors:
- Jiaming Li
- Lingzhen Li
- Xiaze Yang
- Chenyu Zhu
- Kaiqi Liu
- Xiaotong Zhao
- Songlian Li
- Toyota Li
- Alan Zhao
- Haobin Zhong
affiliations:
- Huazhong University of Science and Technology
- Tencent
- Peking University
- The Hong Kong University of Science and Technology
arxiv_id: '2611.26211'
url: https://arxiv.org/abs/2611.26211
pdf_url: https://arxiv.org/pdf/2611.26211
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 多模态流式世界模型推理优化
tags:
- Speculative Decoding
- World Model
- Streaming Generation
- Inference Optimization
- Multimodal Generation
one_liner: 免训练流式世界模型推理框架，复用验证信号为修正项，实现质量速度控制最优权衡
practical_value: '- 投机解码的「验证转修正」思路可迁移到生成式推荐/多轮Agent交互场景，无需全量重生成错误候选，复用验证阶段修正信号降低推理成本，提升响应速度

  - 双阈值三分支（Accept/Refine/Reject）的候选处理策略可复用在RAG/LLM4Rec的候选召回后处理环节，根据置信度匹配不同精调成本，平衡效果与时延

  - 免训练的推理优化范式适合业务落地，不需要重新训练大模型，仅通过推理链路改造即可获得速度/效果提升，可快速上线验证'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流式世界模型的投机推理方案仅依赖外部打分验证生成草稿，仅输出接受/拒绝二分类结果，无修正信号，被拒草稿需要全量重生成，额外增加解码、打分开销，质量与速度的权衡效果不佳。
### 方法关键点
1. 提出免训练的SpecWM统一推理框架，基于目标模型隐层速度场验证草稿块，验证过程同时产出可复用的修正信号；
2. 采用双阈值划分三个处理分支：Accept直接输出、Refine复用修正信号优化、Reject触发重生成；
3. 1步精修路径提升感知质量，3步精修路径强化相机跟随、轨迹一致性。
### 关键结果
WBench Navigation任务上，相较纯目标模型推理提速1.63倍，NavScore从草稿的75.99提升至85.63，实现最优质量-速度-控制权衡；LongSpecBench长序列多轮测试中质量、控制效果稳定，跨不同backbone、去噪预算均有效。
