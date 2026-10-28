---
title: 'CRISP: Co-designing Pruning and Scheduling for Efficient MoE Inference on
  Edge Servers'
title_zh: CRISP：面向边缘服务器高效MoE推理的剪枝与调度协同设计
authors:
- Congwei Zhang
- Youming Tao
- Yifei Zou
- Yu Yang
- Ruirui Zhang
- Xiaoyu Zhang
- Falko Dressler
- Xiuzhen Cheng
- Dongxiao Yu
affiliations:
- 山东大学
- 柏林工业大学
- 香港城市大学
arxiv_id: '2610.37442'
url: https://arxiv.org/abs/2610.37442
pdf_url: https://arxiv.org/pdf/2610.37442
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 边缘MoE推理 · 剪枝调度协同优化
tags:
- MoE
- Edge Inference
- Structured Pruning
- Scheduling
- Inference Optimization
one_liner: 通过组合感知的剪枝与调度协同优化，边缘端MoE推理吞吐量最高提2.1倍，精度损失控制在3.6%以内
practical_value: '- 端侧电商导购Agent、端侧推荐场景部署MoE时，可复用神经元重排序方法，单个权重副本支持多宽度截断，无需存储多份剪枝模型，大幅降低存储开销

  - 推荐系统的MoE召回/排序模型优化可借鉴分层执行策略，按用户/query的专家组合激活频率分Tier，高频组合保全量精度，低频组合激进剪枝，平衡性能和效果

  - 异构模型推理调度可复用宽度优先调度策略，优先加载计算宽专家，用宽专家的计算窗口掩盖窄专家的IO开销，降低整体推理延迟

  - 该剪枝方案可与GPTQ/AWQ等量化技术叠加使用，进一步压缩端侧MoE的内存占用，适配更低配置的边缘设备'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
边缘端部署MoE大模型时，GPU内存通常无法容纳全部专家权重，需将权重存于主机内存按需加载，IO延迟占总推理延迟的70%以上，成为性能瓶颈。现有均匀剪枝、专家丢弃等优化方法未考虑MoE的两大特性：一是专家组合激活频率呈幂律分布，少量高频组合承载绝大多数流量；二是同一组合内专家贡献不对称，存在主/辅专家差异，导致精度损失大、性能提升有限；且剪枝与调度独立设计，未利用剪枝带来的执行异构性做进一步优化。
### 方法关键点
1. 重要性感知神经元重排序：基于校准集的激活幅度计算神经元重要性，物理重排专家权重矩阵，仅存1份权重即可通过前缀截断实现任意宽度的推理，无冗余存储开销
2. 热度分层执行策略：将专家组合按激活频率分为Hot（前60%累积激活）、Warm（中间30%）、Cold（后10%）三层，Hot层双专家全宽执行，Warm层主专家全宽、辅专家半宽执行，Cold层仅保留主专家执行
3. 剪枝感知IO调度：优先调度宽度更大的专家加载与计算，利用宽专家更长的计算窗口重叠窄专家的IO加载，降低IO空泡
### 关键结果
在Mixtral-8x7B、DeepSeek-MoE-16B上测试，对比Full Offloading、Uniform Pruning、EdgeMoE等基线：相同内存预算下吞吐量最高提升2.1倍，WikiText-103数据集上PPL仅上升3.6%，下游任务平均保留97.4%的原精度，边缘端单token能耗最高降低76.7%。
> 最值得记住的结论：MoE剪枝应该基于专家组合而非单个专家设计，剪枝带来的执行异构性是系统优化的机会而非副作用。
