---
title: 'SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM
  Pre-Training'
title_zh: SCOUT：基于对称共识异常检测的LLM预训练故障定位框架
authors:
- Zhuang Wang
affiliations:
- Independent Researcher
arxiv_id: '2608.11034'
url: https://arxiv.org/abs/2608.11034
pdf_url: https://arxiv.org/pdf/2608.11034
published: '2026-08-11'
collected: '2026-08-12'
category: Training
direction: LLM预训练 · 分布式训练故障定位
tags:
- LLM Pre-training
- Failure Localization
- Distributed Training
- Outlier Detection
- SDC
one_liner: 基于等价副本多数共识的无侵入运行时框架，定位LLM预训练的挂起、慢节点、SDC故障
practical_value: '- 自研垂直/推荐大模型的预训练团队可直接集成开源SCOUT，无需修改PyTorch/Megatron/DeepSpeed训练代码，快速获得故障定位能力，将原本平均30分钟以上的手动排查缩短到秒级，降低大规模训练的GPU算力浪费

  - 分布式系统异常检测可复用「等价副本多数共识」思路，无需预设健康阈值或黄金样本，适配动态变化的训练/推理负载

  - 在线推理集群的故障巡检可复用SDC检测的轻量数值签名+in-situ重放方案，避免全量数据传输带来的性能开销

  - MoE模型训练/推理的故障检测可复用执行路径覆盖的形状压缩策略，用最少的重放样本覆盖所有执行路径，降低巡检 overhead'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大规模LLM预训练依赖数万GPU的同步分布式训练，单节点故障会导致全集群空闲，现有诊断方案要么训练进程挂死后无法上报，要么事后日志只能看到同步后的全局症状，离线健康测试又覆盖不到触发故障的真实负载，挂起、慢节点、静默数据损坏（SDC）三类隐性故障无法快速定位根因，手动定位平均耗时超30分钟甚至数天，生产环境慢节点影响42.5%的作业，浪费10.4%的GPU算力，可靠性直接决定训练吞吐量。

### 方法关键点
- 核心设计原则：利用分布式训练天然存在的等价数据并行副本，通过严格多数共识识别异常节点，无需预设阈值或黄金基准
- 三层架构：集成层适配主流训练框架，自动划分等价副本组；证据层结合带外CPU观测器（应对训练进程挂死）和原位重放（保留真实运行负载/压力/状态）采集特征；决策层通过Consensus Collective Communication(C3)原语对比副本的进度、耗时、数值哈希签名，输出异常节点定位
- 优化机制：重放采用层采样、可调间隔、紧凑签名降低开销，MoE场景通过执行路径覆盖压缩重放形状，避免全量重放的高昂成本；支持checkpoint数值完整性校验，避免从SDC污染的checkpoint恢复

### 关键结果
SCOUT兼容PyTorch、Megatron-Core、TorchTitan、DeepSpeed四大主流训练框架，无需修改训练逻辑或框架源码，典型场景下重放开销仅约0.3%，可在线实时定位挂起、慢节点、SDC三类隐性故障，已开源。

### 核心结论
分布式训练的隐性故障定位不需要复杂的故障规则建模，利用等价副本的多数共识就能以极低开销实现高精度根因定位。
