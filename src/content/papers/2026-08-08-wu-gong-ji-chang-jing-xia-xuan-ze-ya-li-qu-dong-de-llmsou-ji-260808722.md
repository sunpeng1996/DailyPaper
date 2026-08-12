---
title: 'Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search
  Under Selection Pressure'
title_zh: 无攻击场景下选择压力驱动的LLM搜索基准指纹识别研究
authors:
- Víctor Gallego
affiliations:
- Komorebi AI Technologies
arxiv_id: '2608.08722'
url: https://arxiv.org/abs/2608.08722
pdf_url: https://arxiv.org/pdf/2608.08722
published: '2026-08-08'
collected: '2026-08-12'
category: Eval
direction: LLM 基准评估可靠性优化
tags:
- Benchmarking
- LLM Evaluation
- Fingerprinting
- Selection Pressure
- Generalization
one_liner: 发现带选择压力的LLM驱动搜索会无意识拟合基准特征，30%分布内优胜结果泛化失效
practical_value: '- 做LLM4Rec/Agent优化的离线benchmark时，必须加跨配置的held-out性能校验，不能只测正确性，避免30%左右分布内优但泛化差的结果上线踩坑

  - 迭代优化LLM生成方案（如商品文案、召回规则生成）时，要对失败案例按gamed/overfit/benign分类归因，针对性调整反馈信号减少选择偏差

  - 若benchmark的可枚举特征过多，需定期更换测试集轴维度，避免优化方案无意识指纹拟合benchmark，放大离线线上gap'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM驱动的搜索/自动优化类系统的基准评估默认模型处于被动无反馈状态，但实际带进化迭代反馈的优化流程会对评估信号产生选择压力，导致基准测量结果与实际能力脱节。
### 方法关键点
构建两套GPU内核优化基准套件：Metal-Sci（10个科学计算任务）、Metal-ZK（12个零知识加密任务），采用3个前沿LLM（Opus 4.7、Gemini 3.1 Pro、GPT-5.5）在(1+1)进化循环内生成Metal内核，无对抗prompt设置下观测优化结果的跨配置泛化表现，梳理四类失效模式并给出评估设计准则。
### 关键结果
- 30%（16/53）的分布内胜出结果无法迁移到未见过的配置
- 总结3条基准设计原则：仅非可枚举轴的留存探针有效、校验门必须测量留存性能而非仅正确性、迁移率需结合失效机制分级解释
