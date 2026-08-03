---
title: Evaluation-Verification Reward for Consistent Multi-Reference Image Editing
title_zh: 基于评估-验证奖励机制的一致性多参考图像编辑方法
authors:
- Yingmao Miao
- Pengfei Zhang
- Xiaochen Lv
- Meng Yu
- Lei Sun
- Xiangxiang Chu
- Chao Shen
- Chenhao Lin
affiliations:
- Xi'an Jiaotong University
- Amap, Alibaba
- Shanghai Jiao Tong University
arxiv_id: '2607.29025'
url: https://arxiv.org/abs/2607.29025
pdf_url: https://arxiv.org/pdf/2607.29025
published: '2026-07-30'
collected: '2026-08-03'
category: Multimodal
direction: 多模态生成 · RL奖励对齐优化
tags:
- MLLM
- Reinforcement Learning
- Image Editing
- Reward Modeling
- Multimodal Generation
one_liner: 设计多维度EVR双阶段评估框架，过滤MLLM幻觉，提升多参考图像编辑的一致性与和谐度
practical_value: '- 电商商品合成（虚拟试穿、商品换背景等）场景可直接复用EVR双阶段MLLM评估框架，分维度生成打分理由再做视觉校验，大幅降低MLLM作为奖励的幻觉，替代昂贵人工标注做RL优化

  - 生成类任务奖励建模可复用维度拆分+几何平均聚合的设计，避免模型为单维度高分牺牲其他核心指标，有效防范奖励黑客

  - 生成任务训练数据构造可参考本文半自动化合成pipeline，自动生成语义对齐的参考对与编辑指令，低成本快速构造万级训练样本，无需标注ground truth目标图

  - 小算力场景下，给小参数MLLM增加EVR验证流程，即可达到甚至超过无验证大参数MLLM的奖励对齐效果，降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多参考图像编辑面临跨参考一致性差、整体和谐度低的痛点，RL在单图编辑、文生图场景已验证有效，但多参考场景下缺乏可捕捉多图关系约束的合适奖励模型；直接复用MLLM做零样本评估时，存在长CoT易诱发幻觉、短CoT推理能力不足的核心矛盾，无法输出稳定可靠的奖励信号。

### 方法关键点
- 评估维度拆分：将编辑效果评估拆分为参考一致性、场景一致性、视觉和谐度、指令一致性、整体视觉质量5个独立维度，降低MLLM单次评估的认知负载，减少幻觉
- 双阶段评估流程：Evaluator对每个维度生成K个带推理理由的候选打分，Verifier逐个校验每个理由是否有实际视觉证据支撑，仅保留符合事实的打分计算最终奖励
- 奖励聚合规则：采用几何平均计算多维度综合得分，避免单维度高分掩盖其他维度缺陷，有效防范奖励黑客
- 可扩展数据pipeline：自动生成语义对齐的参考对象、参考场景、编辑指令三元组，无需ground truth目标图即可支持RL训练

### 关键实验
基于开源Qwen-Image-Edit做基座，用10K合成三元组训练，对比基线、Edit-R1等奖励方案，EVR的人类偏好对齐度达0.707，比基线高7pct；相对基座模型人类偏好胜率达67%，性能匹配甚至超过闭源NanoBanana系统；8B小参数MLLM加EVR后效果超过无验证的32B MLLM。

**最值得记住的一句话**：对具体事实断言的校验远简单于开放式评估，给MLLM的输出增加证据校验环节，即可用更低成本获得更可靠的反馈信号，大幅缓解幻觉问题
