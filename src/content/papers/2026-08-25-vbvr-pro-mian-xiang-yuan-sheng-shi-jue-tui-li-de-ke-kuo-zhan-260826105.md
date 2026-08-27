---
title: 'VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning'
title_zh: VBVR-Pro：面向原生视觉推理的可扩展可验证测试套件
authors:
- Junxiang Xu
- Ruisi Wang
- Fanyi Pu
- Maijunxian Wang
- Ran Ji
- Tongxi Zhou
- Chenyang Gu
- Jing Zuo
- Hongcan Xiao
- Yimeng Geng
affiliations:
- Nanyang Technological University
- University of California, Berkeley
- The Chinese University of Hong Kong
- University of Oxford
- Stanford University
arxiv_id: '2608.26105'
url: https://arxiv.org/abs/2608.26105
pdf_url: https://arxiv.org/pdf/2608.26105
published: '2026-08-25'
collected: '2026-08-27'
category: Reasoning
direction: 多模态原生视觉推理评估与训练基准
tags:
- Visual Reasoning
- Testbed
- Reward Scoring
- MLLM Evaluation
- Generative Vision
one_liner: 推出包含300个生成任务、可验证奖励的原生视觉推理闭环测试基准
practical_value: '- 电商/广告多模态内容生成的效果评估环节，可复用其基于任务规则的确定性奖励打分器，替代不稳定的VLM-as-judge范式，降低评估方差

  - 开发商品搭配、空间布局推理等多模态Agent时，可引入VBVR-Pro的任务集做预训练，提升视觉空间与时序推理的迁移能力

  - 短视频/直播内容生成优化场景，可直接复用其「视频生成适配时序状态跟踪、interleaved生成计算效率更高」的结论做架构选型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
原生视觉推理将生成的视觉状态（图像/视频）作为问题求解的核心载体，现有研究受限于训练任务规模小、评估反馈不可靠、跨生成基底对比无统一基准的瓶颈。
### 方法关键点
1. 构造300个程序化生成的可控视觉推理任务空间，统一支持图像、视频、交错生成等多类生成基底的对照实验
2. 设计基于确定性任务规则的可验证奖励打分器，替代传统VLM-as-judge的评估范式
3. 支持闭环训练，打分器可直接作为多任务强化学习的奖励信号
### 关键结果
- 在VBVR-Pro上训练的模型可迁移到RISE-Video等7个外部视觉推理基准，泛化性优异
- 自带打分器与人类判断细粒度对齐，作为RL奖励信号时，视觉推理任务微调后性能显著优于VLM-as-judge方案
- 实验验证视频生成最适合持久时空状态跟踪任务，交错生成是计算效率更优的替代方案
