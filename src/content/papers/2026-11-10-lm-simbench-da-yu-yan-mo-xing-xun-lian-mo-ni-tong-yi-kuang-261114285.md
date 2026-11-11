---
title: 'LM-SimBench: A Unified Framework, Dataset, and Benchmark for Large Language
  Model Training Simulation'
title_zh: LM-SimBench：大语言模型训练模拟统一框架、数据集与基准
authors:
- Yu Dong
- Hong Li
- Qiang Sun
- Xu Zhou
- Jinbiao Huo
- Qixiu Cheng
- Zhiyuan Liu
affiliations:
- Southeast University
- The Hong Kong Polytechnic University
arxiv_id: '2611.14285'
url: https://arxiv.org/abs/2611.14285
pdf_url: https://arxiv.org/pdf/2611.14285
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 大语言模型训练模拟 · 基准构建
tags:
- LLM Training
- Distributed Training
- Simulation
- Benchmark
- MoE
one_liner: 推出覆盖稠密/MoE LLM多粒度profiling的训练模拟统一基准，解决模拟器横向对比难问题
practical_value: '- 训自有垂域LLM/GenRec模型时，可复用其多并行维度+激活重计算的配置搜索逻辑，提前筛除OOM、低利用率配置，降低全量跑测的算力浪费

  - 跨硬件平台（如NPU转GPU训模型）时，可参考NPU指导GPU选配置的思路，先在成本更低的硬件上筛选Top3候选，再到目标硬件验证，节省GPU资源

  - 自研训练性能预估工具时，可直接复用其公开的348组多粒度profiling数据集做校准，无需自行跑大量测试任务'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前分布式LLM训练的并行配置选择依赖全量跑测，成本极高（如DeepSeek-V3训练耗278.8万H800 GPU小时，对应成本超500万美元）；而现有训练模拟器的评估无统一基准，不同硬件、workload下的预测误差无法横向对比，难以有效指导配置优化。
### 方法关键点
- 提出统一训练模拟框架，将流程拆解为模型编译、设备绑定、执行表示、算子级耗时预估、调度层聚合5个阶段，统一模拟器的输入输出与评估目标
- 采集10个稠密/MoE LLM家族共23种模型设置的profiling数据，覆盖5种并行维度（DP/TP/PP/CP/EP）+激活重计算的348种可行配置，包含配置、单卡、算子、事件、内核6个粒度的测量视图
- 设计三级评估体系：系统级评估耗时/内存预测准确率、组件级评估算子/通信预估误差、策略级评估配置排序效果，同时支持跨平台验证
### 关键实验
基于昇腾NPU集群的实测数据，对比Calculon、vTrain两个主流模拟器：vTrain迭代耗时预测sMAPE低至1.86%，配置排序Spearman ρ达1.0；Calculon模拟速度比vTrain快14.3倍。跨平台实验中，用NPU实测排序筛选的Top3配置100%包含GPU最优配置，Top3候选集的GPU训练regret为0。
### 核心结论
训练模拟的配置排序准确度比绝对误差更重要，跨硬件平台的性能、内存排序一致性远高于绝对值一致性，可低成本实现跨平台配置筛选
