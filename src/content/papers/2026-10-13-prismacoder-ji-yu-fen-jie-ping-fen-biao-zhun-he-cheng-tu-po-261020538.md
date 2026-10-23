---
title: 'PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through
  Decomposed Rubric Synthesis'
title_zh: PrismaCoder：基于分解评分标准合成突破开放多模态代码智能边界
authors:
- Qiushi Sun
- Jingyang Gong
- Yang Liu
- Qiaosheng Chen
- Zhangyue Yin
- Zixian Huang
- Hanxu Hu
- Jing Xiong
- Fangzhi Xu
- Haochen Tan
affiliations:
- The University of Hong Kong
- Nanjing University
- Fudan University
- Huawei Foundation Model Department
- University of Zurich
arxiv_id: '2610.20538'
url: https://arxiv.org/abs/2610.20538
pdf_url: https://arxiv.org/pdf/2610.20538
published: '2026-10-13'
collected: '2026-10-23'
category: Multimodal
direction: 多模态代码大模型 · 数据合成流水线
tags:
- Multimodal LLM
- Code Generation
- Data Synthesis
- Reinforcement Learning
- Open Source
one_liner: 提出分层数据流水线PrismaForge，构建开源最大多模态代码数据集，训练SOTA的9B/35B多模态代码模型
practical_value: '- 分解式rubric评分框架可直接迁移到电商营销可视化图表、商品落地页代码生成的质量校验场景，同时支持作为RL的奖励信号优化生成效果

  - 分层数据合成+过滤流水线的设计思路可复用在多模态推荐/生成任务的训练数据构建流程，降低标注成本提升数据质量

  - 开源的PrismaCoder系列模型可作为电商运营Agent的代码生成底座，快速搭建从需求描述到可运行前端页面/可视化报表的工具链'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态代码生成任务面临数据质量瓶颈，校验信号无法同时覆盖代码正确性、结构合理性、渲染后视觉效果三个核心维度，闭源模型技术领先但数据与训练流程不开放，阻碍开源生态发展。
### 方法关键点
1. 提出PrismaForge分层数据流水线，核心是合成可分解的评分rubric，同时作为监督语料的过滤规则和强化学习训练的奖励信号；
2. 基于流水线构建PrismaCoder-2M数据集，是目前规模最大、多样性最高的开源多模态代码数据集；
3. 基于该数据集训练9B、35B参数的PrismaCoder系列模型并完全开源。
### 关键结果数字
- 模型大幅领先现有开源SOTA，性能对齐头部闭源多模态代码系统；
- 基于rubric的流水线可跨不同模型底座稳定提升多模态代码生成性能。
