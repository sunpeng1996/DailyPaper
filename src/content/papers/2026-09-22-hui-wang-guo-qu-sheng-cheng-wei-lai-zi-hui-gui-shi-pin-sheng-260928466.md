---
title: 'The Past Frames the Future: Memory for Autoregressive Video Generation'
title_zh: 回望过去生成未来：自回归视频生成中的记忆机制综述
authors:
- Harold Haodong Chen
- Rongjin Guo
- Disen Lan
- Wen-Jie Shu
- Hongfei Zhang
- Hanzhe Hu
- Shengtao Yao
- Zixin Zhang
- Guibin Zhang
- Zhefan Rao
affiliations:
- HKUST
- CityUHK
- FDU
- CMU
- NVIDIA
arxiv_id: '2609.28466'
url: https://arxiv.org/abs/2609.28466
pdf_url: https://arxiv.org/pdf/2609.28466
published: '2026-09-22'
collected: '2026-09-24'
category: Multimodal
direction: 多模态生成 · 长时序记忆机制
tags:
- Autoregressive Generation
- Video Generation
- Memory Mechanism
- Long Context
- Survey
one_liner: 系统综述自回归视频生成的记忆机制，构建五维度研究框架并梳理前沿挑战
practical_value: '- 长序列生成任务（如电商商品展示视频生成、用户行为长序列建模）可复用本文提出的「读写-更新-管理-整合」五阶段记忆操作流程，优化长上下文信息留存效果

  - 涉因果时序依赖的Agent交互场景（如导购Agent多轮会话+视觉交互）可参考记忆功能分类思路，优先保留实体身份、状态变更、因果干预三类高价值历史信息，降低存储开销

  - 自回归生成类任务的记忆模块评估可借鉴本文提出的评估范式，验证记忆信息对后续生成的实际因果影响，避免伪记忆问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频生成支持长时序生成、交互式世界建模等任务，但受限于上下文窗口、存储和算力约束，实体身份、动态状态、因果变更等关键历史信息易在生成过程中丢失，时序一致性难以保障，是当前领域核心瓶颈。

### 方法关键点
将记忆定义为跨自回归步骤留存的持久化历史信息，在证据脱离局部上下文后仍可影响后续生成，从五个互补维度梳理现有研究：1）形式：历史信息的表征载体；2）功能：需留存的语义/物理信息类型；3）操作：记忆的读写、更新、管理、整合全生命周期；4）学习：闭环生成过程下的记忆行为优化；5）评估：真实记忆能力的诊断范式。

### 关键结果
总结了当前领域的核心开放挑战，包括可组合且资源感知的记忆架构、可信状态更新、自生成学习、标准化评估，为记忆增强的自回归生成系统构建提供结构化研究基础。
