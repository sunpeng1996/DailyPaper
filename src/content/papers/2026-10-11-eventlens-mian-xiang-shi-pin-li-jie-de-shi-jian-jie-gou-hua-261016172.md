---
title: 'EventLens: Event-Structure Reinforcement Learning for Video Understanding'
title_zh: EventLens：面向视频理解的事件结构强化学习框架
authors:
- Guowen Zhang
- Boshen Xu
- Zihao Yue
- Ziheng Wang
- Xiaokun Liu
- Xin Tao
- Wenyu Qin
- Pengfei Wan
- Qin Jin
affiliations:
- Renmin University of China
- Kling AI
arxiv_id: '2610.16172'
url: https://arxiv.org/abs/2610.16172
pdf_url: https://arxiv.org/pdf/2610.16172
published: '2026-10-11'
collected: '2026-10-14'
category: Multimodal
direction: 多模态大模型 · 视频时序理解强化
tags:
- MLLM
- Video Understanding
- Reinforcement Learning
- GRPO
- Knowledge Distillation
one_liner: 通过事件结构恢复的强化学习范式提升视频MLLM时序理解能力，同时保留通用视频QA性能
practical_value: '- 电商短视频/直播内容结构化场景可复用「时序扰动-恢复」RL范式，无需人工偏好标签，直接用确定性奖励训练，大幅降低标注成本

  - 多任务RL训练可借鉴「单任务专家预训+多教师同策略蒸馏」架构，解决异构奖励信号冲突问题，训练效率相比混合RL提升近3倍

  - 短视频高光提取、直播片段切割等业务可复用三级时序本体（主题阶段/语义事件/原子动作）的分层设计，适配不同粒度的时序分割需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频MLLM多依赖字幕式文本监督训练，易依赖语言shortcut而非视觉时序证据，在事件边界识别、时序推理等任务上表现糟糕；现有多任务RL训练方案存在异构奖励信号冲突、训练不稳定、效率低的问题。

### 方法关键点
- 定义三级时序本体（L1主题阶段/L2语义事件/L3原子动作），基于「扰动-恢复」思路构造三类无需人工标注的确定性奖励RL任务：分层事件分割、单事件时序方向判别、多事件关系推理（含下一个事件预测、补全、重排）
- 采用两阶段训练范式：第一阶段用GRPO分别训练三类单任务专家模型，第二阶段用多教师同策略蒸馏（MT-OPD）将多专家能力合并为单个部署模型，避免混合奖励训练的不稳定问题

### 关键结果
在Qwen3-VL 4B/8B、Qwen2.5-VL 7B三个backbone上验证：时序定位任务mIoU最高提升16.13pp（QVHighlights上从27.66升至43.79），事件敏感推理基准E.T. Bench最高提升4.89pp，通用视频QA性能保留率达98%以上；相比直接混合RL优化，达到相同下游效果的训练时间从37小时压缩至13小时，效率提升近3倍。

### 核心洞察
提升MLLM时序理解的核心不是让它匹配文本描述，而是让它从原生视觉信号中恢复被扰动的时序结构，该范式的迁移性远优于传统文本监督。
