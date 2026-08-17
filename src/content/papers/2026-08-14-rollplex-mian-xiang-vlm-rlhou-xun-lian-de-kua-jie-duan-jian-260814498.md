---
title: 'Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training'
title_zh: Rollplex：面向VLM RL后训练的跨阶段GPU空间共享运行时
authors:
- Hanfeng Lu
- Tianyu Feng
- Suyi Li
- Yuheng Zhao
- Wei Gao
- Shaopan Xiong
- Ju Huang
- Siran Yang
- Jiamang Wang
- Lin Qu
affiliations:
- HKUST
- Alibaba Inc
arxiv_id: '2608.14498'
url: https://arxiv.org/abs/2608.14498
pdf_url: https://arxiv.org/pdf/2608.14498
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 大模型训练优化 · GPU资源调度
tags:
- VLM
- RL Post-Training
- GPU Scheduling
- Memory Optimization
- Tensor Parallelism
one_liner: 通过跨阶段前缀与rollout解码重叠，零精度损失提升VLM RL后训练1.23~2.24倍效率
practical_value: '- 做电商多模态Agent/搜广推模型RL微调（如GRPO/RLHF）时，可直接复用跨阶段并行思路：将不依赖rollout生成结果的多模态prompt预填充、reference模型前缀推理和rollout解码并行，无需修改训练逻辑即可获得20%+的训练提速

  - 内存优化trick可复用在大模型微调场景：基于CUDA VMM的按生命周期内存调度+chunked流式优化器更新方案，可将单卡峰值内存占用降低50%以上，解决70B+大模型微调单卡内存不足问题

  - 不同TP度权重共享方案适合训练推理同池部署的在线系统：92.8%的参数可通过物理地址共享避免重复存储，无需每次模型更新全量拷贝权重，降低在线RL微调的权重同步开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有VLM的RL后训练（如RLHF、GRPO）默认串行执行rollout、reference打分、actor训练三个阶段，对多模态任务来说，视频/图像编码+长prompt预填充占单步时间的79%~98%，远高于纯文本任务的11%~19%，而这部分前缀计算完全不依赖rollout生成的响应，串行执行会浪费大量GPU空闲算力（rollout解码时SM利用率仅19%）；同时rollout和训练偏好不同TP度，权重复制、内存不足的问题进一步制约效率。

### 方法关键点
- 跨阶段调度：将reference打分、actor训练的前缀计算拆分出来，和rollout解码并行执行，保留KV cache边界状态，后缀计算等rollout完成后继续，完全不改变同步on-policy RL的语义
- 阶段感知内存管理：基于CUDA VMM实现虚拟地址与物理内存解绑，按张量生命周期调度HBM驻留，仅保留 latency 敏感的KV cache，训练激活/优化器状态分块流式加载/卸载，峰值内存从165GiB降到低于80GiB（单张H800容量）
- 并行感知权重共享：对不同TP度的训练/rollout引擎，按张量布局分三类处理：相同分片直接共享、转置兼容的通过元数据转置共享、仅不兼容的张量做拷贝，92.8%的参数无需重复存储，允许训练/rollout用各自最优TP度

### 关键实验结果
基于Qwen2.5-VL-32B在32张H800上测试4个视频推理任务，对比串行同池、分池部署两个主流基线：
- 比串行同池部署快1.23×~1.30×，比分池部署快1.57×~2.24×，训练reward曲线与基线完全一致，无精度损失
- 权重共享支持rollout使用最优TP=4，比强制与训练同TP=8时rollout速度提升1.17×~1.31×，端到端提效1.06×~1.17×

### 核心结论
对于输入密集的多模态RL训练，无需修改算法逻辑，仅通过跨阶段调度独立计算任务+精细化内存/权重管理，就能在相同GPU预算下实现最高2倍以上的训练提速。
