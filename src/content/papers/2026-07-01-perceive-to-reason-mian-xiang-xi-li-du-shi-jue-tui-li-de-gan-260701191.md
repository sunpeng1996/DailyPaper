---
title: 'Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual
  Reasoning'
title_zh: Perceive-to-Reason：面向细粒度视觉推理的感知与推理解耦框架
authors:
- Hongxing Li
- Xiufeng Huang
- Dingming Li
- Wenjing Jiang
- Zixuan Wang
- Haolei Xu
- Hanrong Zhang
- Haiwen Hong
- Longtao Huang
- Hui Xue
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2607.01191'
url: https://arxiv.org/abs/2607.01191
pdf_url: https://arxiv.org/pdf/2607.01191
published: '2026-07-01'
collected: '2026-07-02'
category: Multimodal
direction: 多模态视觉推理 · 感知推理解耦
tags:
- VLM
- Fine-grained Reasoning
- GRPO
- Multimodal
- Reinforcement Learning
one_liner: 提出感知-推理解耦的P2R框架与交替RL训练策略，提升多尺度VLM细粒度视觉推理性能
practical_value: '- 电商多模态搜索/商品理解场景可复用感知-推理解耦架构，先定位商品图中关键特征（吊牌价、成分标、细微瑕疵等）再做推理，降低高分辨率图噪声干扰

  - 多阶段任务训练可借鉴PRA-GRPO交替训练策略，仅用最终结果监督即可分别优化不同阶段模块，大幅降低细粒度标注成本

  - 多模态Agent的视觉查询应答流程可参考该架构，拆分图像信息检索（感知）与逻辑推理模块，提升复杂视觉问题的准确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前VLMs在细粒度视觉推理任务上表现不佳，高分辨率图像中微小关键视觉线索容易被忽略，现有方法未显式区分感知与推理环节，存在上下文噪声大、pipeline难优化等问题。
### 方法关键点
1. P2R统一框架将细粒度视觉推理拆分为两阶段：Perceiver阶段定位与查询相关的视觉证据并裁剪对应区域，Reasoner阶段基于原图+裁剪区域输出答案。
2. 配套PRA-GRPO角色感知强化学习策略，仅依赖最终答案监督，交替开展感知导向和推理导向的模型更新，解决解耦架构的训练对齐问题。
### 关键结果
基于Qwen3-VL-Instruct 2B/4B/8B不同尺度搭建的P2R模型均实现一致性能提升，其中P2R-4B在V-Star基准达93.2%、HR-Bench-4K达81.9%、HR-Bench-8K达80.5%，大幅超越对应基线，效果可泛化到通用多模态推理任务。
