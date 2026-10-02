---
title: Optimizing Effective Training Time for Large-Scale Recommendation Systems
title_zh: 大规模推荐系统有效训练时长优化实践
authors:
- Mingming Ding
- Ruilin Chen
- Yuzhen Huang
- Hang Qi
- Menglu Yu
- San Tan
- Damian Reeves
- Boris Sarana
- Kevin Tang
- Satendra Gera
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2610.02057'
url: https://arxiv.org/abs/2610.02057
pdf_url: https://arxiv.org/pdf/2610.02057
published: '2026-10-01'
collected: '2026-10-02'
category: RecSys
direction: 推荐系统 · 大规模训练效率优化
tags:
- Training Efficiency
- Recommendation Systems
- Distributed Training
- PyTorch
- GPU Utilization
one_liner: 提出ETT%两级度量框架，全栈优化推荐训练生命周期开销，集群有效训练占比提至90%+
practical_value: '- 引入ETT%两级度量体系，拆解训练全链路（调度、初始化、编译、checkpoint、恢复）的时间损耗，精准定位对应负责模块优化，避免仅参考MFU的评估片面性

  - 训练初始化阶段用合成batch替代真实数据供PyTorch 2编译，让编译、数据流预热、模型初始化并行执行，可直接降低冷启动耗时27%左右

  - 将模型发布阶段从GPU训练任务中剥离，训练完成后立即释放GPU，单独用CPU任务完成checkpoint转推理快照，单任务可减少约30分钟GPU空置浪费

  - 训练阶段采用异步checkpoint+动态调整checkpoint间隔策略，平衡故障重训损耗与checkpoint阻塞损耗，可降低77%的checkpoint阻塞时间'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模推荐模型需高频迭代新鲜用户行为数据，任务周期短、重启频率高，传统MFU仅统计训练步内效率，Goodput无法拆解损耗到具体负责模块，Meta原推荐训练集群GPU仅50~60%的时间在处理新数据，大量算力浪费在初始化、编译、故障恢复等生命周期环节，优化空间极大。
### 方法关键点
- 提出ETT%（有效训练时长占比）作为核心度量，两级拆解损耗：L1层拆解为首次启动耗时TTS、单故障恢复耗时TTR、故障次数NoF；L2层拆解为调度、初始化、PT2编译、无效训练、关机5类可优化损耗，每类对应明确负责团队
- 全栈优化覆盖5个核心环节：初始化阶段删除冗余通信、用合成batch让编译与数据流预热并行、组件并行初始化，TTS降低41%；PT2编译层面标记动态shape、裁剪自动调优搜索空间、复用编译缓存，冷启动编译耗时降87.6%；异步checkpoint+动态调整间隔，平衡重训损耗与阻塞耗时，checkpoint阻塞时间降77%；模型发布与训练解耦，GPU任务完成训练即释放，用CPU做快照生成，关机耗时降近30分钟；调度层面优化抢占策略，优先抢占刚完成checkpoint的任务，减少无效重跑
### 关键结果
在7个覆盖8~256GPU的推荐模型上测试，ETT%从基线的59~85%提升至80~93%，平均提升15.5个百分点，故障恢复耗时下降1.8~8.6倍；全集群上线后，整体ETT%从80%提升至90%以上。
### 核心洞见
对于短周期、高重启频率的推荐训练任务，生命周期开销占比远高于LLM预训练，优化全链路损耗的收益远高于仅优化训练步内效率。
