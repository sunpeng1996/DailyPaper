---
title: 'OmniReasoner: Thinking with Long Audio-Video via Native Tool Use'
title_zh: OmniReasoner：基于原生工具调用的长音视频推理框架
authors:
- Yu Chen
- Caorui Li
- Ziyu Xiong
- Yidong Wang
- Mingqi Gao
- Shuman Liu
- Biao Liu
- Chunfeng Yang
- Anxiang Zeng
- Haibo Zhang
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation CAS
- Southeast University
- Shopee
- Tsinghua University
arxiv_id: '2607.19339'
url: https://arxiv.org/abs/2607.19339
pdf_url: https://arxiv.org/pdf/2607.19339
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: 多模态Agent · 原生工具调用优化
tags:
- Omni-modal LLM
- Tool Use
- Long Video Reasoning
- SFT
- Reinforcement Learning
one_liner: 通过SFT+RL训练全模态大模型自主调用时序缩放工具，解决长音视频推理的稀疏证据定位难题
practical_value: '- 做商品长直播、种草短视频合集等长内容多模态理解时，可借鉴TimeAnchor方案，用绝对时间戳绑定不同采样粒度的音视频token，避免时序对齐偏差

  - 大模型自主调用感知类工具的场景，可复用「SFT冷启动学习工具调用格式+GRPO强化学习优化决策精度」的两阶段训练范式，避免直接RL的策略漂移问题

  - 缺乏工具调用标注数据时，可通过内容拼接、异常插入等编辑操作自动生成带真值的工具调用轨迹，大幅降低标注成本

  - 长内容召回/推理场景，可参考「低分辨率全局预览过滤候选区间+高分辨率局部细查」的算力分配策略，在成本可控的前提下提升理解精度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
长音视频推理中关键证据通常稀疏、跨模态，全量高保真处理算力成本极高，均匀降采样又会丢失细粒度关键信息；现有工具调用方案大多仅适配视觉模态，时序索引绑定特定采样率，跨粒度调用时易出现对齐偏差，同时缺乏低成本的工具调用标注数据生产方案。

### 方法关键点
- 整体框架：先构建全量音视频的低分辨率全局预览，模型自主决策直接回答或调用zoom-in工具获取指定时间段的高保真音视频片段，结合全局上下文和局部片段输出答案
- TimeAnchor：给每2秒的音视频块前置普通文本时间戳`<t seconds>`，工具调用参数采用绝对秒数，无需新增特殊token或改动模型架构，即可保证不同采样粒度下的时序索引一致性
- Temporal Augmented Data Engine：通过多片段拼接、异常插入两种编辑方式自动生成带证据区间真值的长音视频任务，再合成直接回答、工具调用两类训练轨迹，无需人工标注区间
- 训练范式：先SFT让模型学习工具调用格式和基础决策逻辑，再用GRPO强化学习优化决策质量，奖励仅包含答案准确率和格式合规性，不额外增加区间定位奖励

### 关键结果
基于Qwen-Omni-7B基座测试：OmniVideoBench相对基线提升5.5pp，LVOmniBench提升3.4pp，VideoHolmes（强依赖稀疏证据定位的任务）提升15.6pp；视频越长收益越高，10-30分钟长视频上OmniVideoBench准确率比基线提升9.9pp。

### 核心记忆点
感知类工具调用的核心是对齐不同模态、不同分辨率下的统一时空坐标系，用尽可能低成本的机制解决本质问题，而非叠加复杂的定制化模块
