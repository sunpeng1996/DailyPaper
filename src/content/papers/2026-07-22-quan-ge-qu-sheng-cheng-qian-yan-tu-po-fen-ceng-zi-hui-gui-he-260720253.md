---
title: 'Pushing the Frontier of Full-Song Generation: Hierarchical Autoregressive
  Planning Meets Flow-Matching Rendering'
title_zh: 全歌曲生成前沿突破：分层自回归规划结合流匹配渲染
authors:
- Junyu Dai
- Xinyue Fan
- Weiqin Li
- Xiangang Li
- Yunjia Li
- Bin Ma
- Yukun Ma
- Chongjia Ni
- Yufei Shi
- Haoxu Wang
affiliations:
- Alibaba Token Foundry
arxiv_id: '2607.20253'
url: https://arxiv.org/abs/2607.20253
pdf_url: https://arxiv.org/pdf/2607.20253
published: '2026-07-22'
collected: '2026-07-23'
category: Other
direction: 多模态生成 · 全歌曲统一生成框架
tags:
- Music Generation
- Flow Matching
- Autoregressive Modeling
- GRPO
- DiT
one_liner: 提出分层自回归规划+流匹配渲染的统一框架，支持三类全歌曲生成任务，性能达业界领先水平
practical_value: '- 分层自回归离散建模+连续空间流匹配的两阶段生成架构，可迁移到电商长文案、商品短视频等长序列生成场景，先做结构规划再优化保真度

  - 基于GRPO的奖励后训练适配流匹配模型的思路，可复用在生成式推荐的偏好对齐环节，提升生成内容和用户需求的匹配度

  - 参考信息提取+离散线索引导的生成范式，可用于电商内容二创场景，实现风格重绘的同时保留商品核心特征信息'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有全歌曲生成普遍存在结构连贯性不足、音频保真度低、风格迁移时核心旋律易丢失的问题，且缺乏同时适配歌词转歌曲、纯音乐生成、翻唱生成三类场景的统一方案。
### 方法关键点
架构包含四大核心组件：语义感知tokenizer将音频编码为8码本RVQ离散token，实现高效音乐表示；hybrid-LM完成分层自回归音频token建模，支撑长时长全歌曲结构规划；FullDiT在连续VAE隐空间基于codec token、歌词、文本描述做全歌曲流匹配，提升音频保真度；两级旋律模块提取参考音频的离散旋律线索，引导翻唱生成时保留原始旋律。同时探索DPO/GRPO/OPD等奖励后训练策略，适配hybrid-LM和FullDiT优化生成音乐性。
### 关键结果
在多语言自动评测基准、Artificial Analysis带人声音乐榜单上均取得竞争力性能表现。
