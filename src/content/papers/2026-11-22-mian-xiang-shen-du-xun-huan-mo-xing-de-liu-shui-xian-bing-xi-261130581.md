---
title: A Pipeline-Parallel System for Depth-Recurrent Models
title_zh: 面向深度循环模型的流水线并行训练系统Loop-PP
authors:
- Yunjia Xi
- Jiarui Qin
- Di Yin
- Xing Sun
affiliations:
- Tencent Youtu Lab
arxiv_id: '2611.30581'
url: https://arxiv.org/abs/2611.30581
pdf_url: https://arxiv.org/pdf/2611.30581
published: '2026-11-22'
collected: '2026-11-24'
category: Training
direction: 大模型训练 · 流水线并行优化
tags:
- Pipeline Parallelism
- Looped Transformer
- MoE
- Distributed Training
- Training System
one_liner: 针对深度循环Transformer设计的流水线并行系统，降低显存同时提升训练吞吐量
practical_value: '- 若业务需要训练垂类Looped Transformer（比如电商/推荐场景的轻量化推理大模型），可直接复用Loop-PP系统，在不修改模型语义的前提下最高降低32.8%显存占用，提升训练效率

  - 训练MoE类大模型（如大规模推荐排序/多任务模型）时，优先采用Loop-PP配合粗粒度流水线分区（如PP2/PP4），可获得最高7.2%的吞吐量提升

  - 自研分布式训练调度器的团队，可借鉴「语义逻辑展开+原生1F1B约束调度+通信拆分重叠」的架构思路，适配带循环依赖的特殊模型结构

  - 实操中训练循环类模型时，避免过细的流水线分区，尽量保证单阶段计算块厚度，降低循环依赖带来的通信 overhead'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
深度循环（Looped）Transformer通过复用同一组模块多次执行提升有效深度，不增加参数量即可强化推理、上下文学习能力，是大模型轻量化的重要方向。但传统流水线并行（PP）针对无环前向结构设计，无法适配循环模型跨阶段的反向依赖，原生1F1B调度会出现停滞、执行顺序错误，现有系统缺失对这类模型大规模训练的支持，显存占用和吞吐量无法满足生产需求。
### 方法关键点
- 语义图构建：将固定循环步骤逻辑展开，区分同一物理模块的不同逻辑访问，通过主边、反馈边、注入边捕捉跨步骤依赖，生成无环的调度无关语义图
- 原生引导调度合成：以Megatron原生交错1F1B为计算模板，叠加语义图的依赖约束，通过优先级引导的拓扑排序生成全局一致的计算顺序，保留原有调度的计算节奏
- 通信感知流编译：将跨阶段通信拆分为非阻塞POST和阻塞WAIT操作，调度本地计算填充通信窗口实现重叠，生成每个rank的静态执行流，避免运行时调度开销
- 工程优化：载荷本地化仅传输下游需要的张量字段，编译结果跨训练步缓存复用，进一步降低通信和编译开销
### 关键结果
在8B-60B MoE模型上测试，对比Unrolled（参数不共享展开）、Tied（参数共享展开）、Lockstep（保守依赖调度）三个基线：峰值显存最高降低32.8%，同等32卡资源预算下吞吐量最高提升12.7%；MoE场景PP2配置下吞吐量比Unrolled基线高7.2%，但过细的PP8分区会导致通信开销超过参数复用的收益，吞吐量低于基线。
### 核心结论
深度循环模型的流水线并行收益高度依赖单阶段计算块厚度，粗粒度分区下MoE场景的收益显著高于稠密模型。
