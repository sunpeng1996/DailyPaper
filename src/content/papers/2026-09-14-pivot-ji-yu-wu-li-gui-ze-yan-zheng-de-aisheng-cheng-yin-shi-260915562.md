---
title: 'PIVOT: Physics-Grounded Verification for AI-Generated Audio-Video Detection'
title_zh: PIVOT：基于物理规则验证的AI生成音视频检测方法
authors:
- Bo Zheng
- Kangran Zhao
- Xiaoyu Zhang
- Weinan Guan
- Zhiheng Li
- Yize Chen
- Haizhou Li
- Qingshan Liu
- Siwei Lyu
- Baoyuan Wu
affiliations:
- 香港中文大学（深圳）人工智能学院
- 南京大学
arxiv_id: '2609.15562'
url: https://arxiv.org/abs/2609.15562
pdf_url: https://arxiv.org/pdf/2609.15562
published: '2026-09-14'
collected: '2026-09-15'
category: Other
direction: AIGC内容检测 · 物理一致性校验
tags:
- AIGC-Detection
- Physical-Consistency
- Multimodal
- Benchmark
- Forensics
one_liner: 提出基于物理一致性校验的音视频AIGC检测框架PIVOT及配套基准，效果优于Gemini 3.1 Pro
practical_value: '- 电商UGC/AIGC内容风控场景可引入领域常识/物理规则作为独立校验维度，弥补纯黑盒多模态判别模型可解释性差、迭代成本高的问题

  - 多模态内容真实性校验可复用「特征量化-规则匹配-置信度输出」三段式架构，规则层可独立迭代适配不同业务场景要求

  - 自研业务评测数据集时可参考真实/生成内容配对的构造方式，降低人工标注成本，提升不同方案评测的公平性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前生成模型效果快速提升，传统AIGC检测器依赖的伪影特征逐渐消失，检测准确率持续下滑；但现有生成模型仍难以高保真复现真实世界事件的物理行为规律。
### 方法关键点
PIVOT检测框架采用三段式逻辑：从音视频中估算各类物理量，自动匹配当前片段适用的物理定律，校验约束条件是否满足；除真假判别结果外，还输出校验证据、对应时间窗口、支撑量化数值；配套发布PhysForensics-Bench基准，包含9类场景、2种主流音视频生成器产出的真实/生成配对数据。
### 关键结果
在Real+Seedance数据集上准确率达70.30%、F1 64.29%，Real+VEO数据集上准确率达72.16%、F1 65.82%，较Gemini 3.1 Pro准确率分别提升16.34、14.94个百分点。
