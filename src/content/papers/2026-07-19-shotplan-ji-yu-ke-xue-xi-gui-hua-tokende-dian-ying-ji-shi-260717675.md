---
title: 'ShotPlan: Cinematic Video Generation with Learnable Planning Token'
title_zh: ShotPlan：基于可学习规划Token的电影级视频生成框架
authors:
- Su Guo
- Guangce Liu
- Haosen Yang
- Jiepeng Wang
- Cong Liu
- Junqi Liu
- Haibin Huang
- Hongxun Yao
- Chi Zhang
- Xuelong Li
affiliations:
- Institute of Artificial Intelligence (TeleAI), China Telecom
- Harbin Institute of Technology
arxiv_id: '2607.17675'
url: https://arxiv.org/abs/2607.17675
pdf_url: https://arxiv.org/pdf/2607.17675
published: '2026-07-19'
collected: '2026-07-22'
category: Multimodal
direction: 多模态生成 · 可控视频生成
tags:
- Video Generation
- Diffusion Model
- Position Embedding
- Controllable Generation
- Token Learning
one_liner: 引入带分数时间旋转位置编码的可学习规划Token，实现可控高一致性多镜头电影级视频生成
practical_value: '- 可借鉴可学习规划Token思路，在电商商品短视频生成中插入可控转场、运镜控制，无需重训视频生成基座即可提升成片质感，降低人工剪辑成本

  - FRoPE帧级时间位置编码方法可复用到多片段内容拼接生成场景，解决不同素材/片段的时间对齐、过渡一致性问题

  - 规划Token与原生生成Token无缝融合的架构，可迁移到多轮Agent生成任务的过程控制，实现生成节点的精准干预，无需修改基座模型逻辑'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型仅能实现效果较好的单镜头生成，无法满足电影级多镜头视频对叙事连贯性、镜头组合合理性的要求，缺乏显式的镜头规划能力，转场、运镜控制精度不足。
### 方法关键点
1. 基于视频扩散基座搭建ShotPlan框架，新增可学习规划Token，捕获镜头级转场特征，与原生生成Token无缝融合即可实现转场时间戳的精准控制；
2. 为规划Token设计Fractional Temporal Rotary Position Embedding (FRoPE)，支持帧级粒度的镜头切换建模，统一兼容硬切、渐变转场、局部运镜控制等多类生成需求。
### 关键结果
实验显示ShotPlan效果显著优于现有电影级视频生成方案，镜头管理灵活性大幅提升，跨镜头一致性表现明显领先现有基线方法
