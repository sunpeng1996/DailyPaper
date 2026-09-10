---
title: 'AuK Technical Report: An Open-Source Foundational Model for Speech Generation
  and Editing'
title_zh: AuK技术报告：面向语音生成与编辑的开源基础模型
authors:
- Ziyang Ma
- Zhikang Niu
- Wenming Tu
- Tianrui Wang
- Ruiqi Yan
- Junxi Liu
- Yanru Huo
- Nickk Huang
- Yang Liu
- Qicong Xie
arxiv_id: '2609.08936'
url: https://arxiv.org/abs/2609.08936
pdf_url: https://arxiv.org/pdf/2609.08936
published: '2026-09-07'
collected: '2026-09-10'
category: Multimodal
direction: 多模态基础模型 · 语音生成编辑
tags:
- Multimodal LLM
- Speech Generation
- Model Distillation
- Foundation Model
- Instruction Tuning
one_liner: 开源统一指令驱动语音生成编辑基础模型，配套蒸馏提速方案性能超SOTA
practical_value: '- 电商广告语音物料、直播口播文案可基于该模型快速生成编辑，通过文本指令调整音色、内容，降低素材生产成本

  - 语音交互类Agent的语音模块可参考其「多模态LLM语义分支+跨域VAE声学分支」的融合架构

  - 生成类大模型推理降本可复用其蒸馏策略：一致性初始化+任务路由Decoupled DMD实现多倍提速'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有语音生成、编辑、增强类模型能力分散，缺乏统一指令驱动的开源基础模型，且全量模型推理延迟高难以落地到业务场景。
### 方法关键点
1. 构建覆盖语音生成、内容编辑、增强分离等5大类任务的30.3亿指令-音频样本、195万小时监督数据；
2. 架构融合多模态LLM语义条件模块、跨语音/通用音频/音乐训练的VAE声学条件模块、混合整流流Transformer生成模块；
3. 训练分生成任务预热、生成编辑联合预训练、偏好优化/奖励强化学习后训练多阶段，后续用一致性初始化+任务路由Decoupled DMD蒸馏得到轻量版。
### 关键结果
蒸馏后的AuK-Flash仅需4步推理，速度为全量模型的4.5倍，在零样本语音生成、指令驱动编辑任务上性能达SOTA，信号级修复任务表现具备竞争力。
