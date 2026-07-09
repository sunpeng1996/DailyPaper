---
title: Infinite Worlds with Versatile Interactions
title_zh: LingBot-World 2.0：支持无限交互的开源世界生成系统
authors:
- Zelin Gao
- Qiuyu Wang
- Jiapeng Zhu
- Jingye Chen
- Zichen Liu
- Qingyan Bai
- Jiahao Wang
- Yufeng Yuan
- Hanlin Wang
- Yichong Lu
arxiv_id: '2607.07534'
url: https://arxiv.org/abs/2607.07534
pdf_url: https://arxiv.org/pdf/2607.07534
published: '2026-07-07'
collected: '2026-07-09'
category: MultiAgent
direction: 多智体协作 · 实时交互式世界生成
tags:
- MultiAgent
- WorldModel
- CausalPretraining
- KnowledgeDistillation
- Real-timeGeneration
one_liner: 提出支持小时级无漂移、720p 60fps实时生成的双Agent架构开源交互式世界模型
practical_value: '- 双Agent（决策层+执行层）解耦架构可直接迁移到电商虚拟导购、商品互动展示场景：用VLM作为Director识别用户交互意图、规划展示内容，生成模型作为Pilot输出对应的商品3D场景、交互视频，实现沉浸式导购体验

  - MoBA混合注意力掩码+动态KV cache调度的工程方案，可复用到长序列生成类业务（比如用户长行为序列建模、长直播文案生成），在保证因果性的同时降低推理延迟、缓解长序列输出漂移

  - 一致性蒸馏+分布匹配蒸馏的两阶段后训练策略，可用于压缩生成类大模型（比如商品图生视频、文案生成模型），在损失可控的前提下将多步扩散压缩为少步生成，满足业务毫秒级响应要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有交互式世界模型存在两大核心瓶颈：一是长时序生成过程中误差持续累积，场景易发生漂移，稳定生成时长仅能维持数分钟，远达不到沉浸式交互所需的持久性要求；二是高保真交互生成算力开销极高，现有方案通常需要牺牲分辨率、帧率或控制自由度才能实现实时响应，仅支持简单的视角移动类交互，无法支撑丰富的动作控制和场景动态调整需求。
### 方法关键点
- 数据层：搭建多源异构数据引擎，融合第一人称交互视频、游戏合成数据、大规模网络视频，配套全局+分块多粒度标注体系，解决训练阶段全局条件、推理阶段局部交互条件的分布 mismatch 问题
- 预训练层：提出MoBA混合注意力掩码，将双向注意力块嵌入自回归因果掩码，既保证生成的因果性，又缓解长上下文过拟合导致的质量衰减，采用条件流匹配目标训练14B参数因果世界模型骨干
- 后训练层：结合一致性蒸馏和分布匹配蒸馏，将多步扩散模型压缩为少步生成模型，同时针对长自回归滚出场景做分布对齐，从根源抑制误差累积漂移
- 部署层：设计Director-Pilot双Agent脚手架，VLM作为Director负责场景理解、事件规划和因果推理，视频生成模型作为Pilot负责物理动态模拟和高保真渲染，配套动态KV cache、异步流水线优化将延迟压到实时要求
### 关键结果
对比Genie 3、HappyOyster等SOTA基线，是唯一实现小时级（>60分钟）无质量衰减生成的开源模型；蒸馏后版本支持720p 60fps实时生成，覆盖攻击、射箭、施法、环境切换等10+类交互动作；同时提供1.3B轻量化版本，单GPU即可部署。

> 最值得记住的一句话：给基础生成模型套上Agent决策脚手架，是将被动生成能力转化为可交互、自持续业务系统的核心路径。
