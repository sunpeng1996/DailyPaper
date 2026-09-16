---
title: 'VideoMM: Adaptive Macro-Micro Inference for Efficient Video MLLMs'
title_zh: VideoMM：面向高效视频多模态大模型的自适应宏微推理框架
authors:
- Haoyu Guo
- Yuan Feng
- Junlin Lv
- Mingjun Xiao
- S Kevin Zhou
- Xike Xie
affiliations:
- 中国科学技术大学生物医学工程学院
- 中国科学技术大学计算机学院
- 苏州高等研究院MIRACLE中心Data Darkness Lab
arxiv_id: '2609.16722'
url: https://arxiv.org/abs/2609.16722
pdf_url: https://arxiv.org/pdf/2609.16722
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态大模型 · 长视频推理优化
tags:
- MLLM
- Video Understanding
- Inference Acceleration
- Token Reduction
- Long Context
one_liner: 模仿人类粗到细感知的宏微推理范式，实现长视频MLLM精度与效率双突破
practical_value: '- 电商直播/短视频内容理解场景可复用宏微分层思路：先用低分辨率粗粒度特征做初筛，仅对候选片段调用高分辨率精细推理，算力成本可降低60%以上

  - 分组共识早停机制可迁移到多模态召回/排序场景：对高置信度样本直接输出结果，减少大模型调用比例，提升吞吐

  - 下采样因子k可作为业务调优旋钮：高QPS场景用k=3换取7.9×加速，高精度场景用k=2兼顾效果，无需重构架构'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
长视频MLLM推理的核心瓶颈是视觉token爆炸，现有token压缩方案陷入两难：轻量编码器驱动的方法易丢失关键语义，MLLM驱动的压缩方法开销过大抵消效率收益，无法兼顾精度与效率。

### 方法关键点
- 第一阶段（粗筛）：构建空间下采样的Macro Proxy，将token量压缩为原有的1/k²，基于MLLM中间层的跨模态注意力权重对视频帧分组打分，仅保留top 50%高相关性帧的核心token，大幅降低后续计算量
- 第二阶段（自适应推理）：采用分组共识投票机制做宏粒度推理，若多组结果一致则直接输出早停；若存在分歧则将选中的宏token映射回对应高分辨率Micro Token做精细推理，仅对歧义样本调用高算力路径

### 关键实验
在LongVideoBench、LVBench、VideoMME三个基准上测试，对比VidCom、VisionZip、FlexSelect等SOTA方法：相比全上下文基线，实现6.13×推理加速的同时精度提升7.4%；相比当前SOTA FlexSelect，推理速度提升2.73×且精度无损失；下采样因子k设为3时，可实现7.9×加速，仅出现1.6%的精度下降。

### 最值得记住的一句话
从模型中心的token压缩转向感知粒度自适应调度，是兼顾长序列多模态推理精度与效率的更优范式。
