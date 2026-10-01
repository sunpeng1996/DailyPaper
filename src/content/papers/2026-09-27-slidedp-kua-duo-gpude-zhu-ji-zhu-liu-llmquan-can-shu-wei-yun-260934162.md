---
title: 'SlideDP: Scaling Host-Resident LLM Fine-Tuning Across Multiple GPUs'
title_zh: SlideDP：跨多GPU的主机驻留LLM全参数微调运行时扩展框架
authors:
- Ruijia Yang
- Shiyuan Lin
- Yulong Ao
- Zhiyu Li
- Yingli Zhao
- Xianduo Li
- Yonghua Lin
- Zeyi Wen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Beijing Academy of Artificial Intelligence
arxiv_id: '2609.34162'
url: https://arxiv.org/abs/2609.34162
pdf_url: https://arxiv.org/pdf/2609.34162
published: '2026-09-27'
collected: '2026-10-01'
category: Training
direction: 大模型训练 · 多GPU内存优化与并行加速
tags:
- LLM-FineTuning
- Multi-GPU-Training
- Host-Offload
- Data-Parallelism
- Memory-Optimization
one_liner: 通过共享主机状态和流水线调度将多GPU主机驻留LLM微调吞吐量提升1.46~2.64倍
practical_value: '- 多卡微调垂直领域LLM（如推荐文案生成、Agent工具调用模型）时，可复用共享主机状态+GPU侧梯度聚合设计，避免多卡重复传输导致的PCIe带宽瓶颈，降低主机资源竞争

  - 当GPU显存不足做7B以上模型全参数微调时，可直接集成SlideDP开源实现，无需修改训练逻辑即可在4张消费级RTX4090上完成72B模型微调

  - 长序列微调场景（如用户行为长序列建模、多轮对话Agent微调）可复用其弹性Checkpointing策略，根据显存动态调整激活存储/卸载比例，平衡吞吐与显存占用

  - AutoPolicy自动调优逻辑可直接迁移到业务微调pipeline，根据硬件拓扑和任务自动选最优通信、分块、激活策略，减少手动调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
主机驻留层流技术可突破GPU显存限制实现LLM全参数微调，但多卡数据并行时存在两个核心瓶颈：一是重复传输导致共享主机资源（CPU、内存、PCIe带宽）竞争放大，二是强缩放时计算窗口缩小导致主机侧任务无法被GPU计算隐藏，现有ZeRO-Offload、SlideFormer等方案吞吐低、支持的模型/序列长度有限。

### 方法关键点
- 共享主机状态设计：全量FP32主权重和Adam优化器状态仅存1份在主机内存，解耦状态布局与通信路径，支持复制/分片两种参数分发策略、CPU/GPU两种梯度聚合策略
- 跨卡流水线调度：将参数分发、梯度聚合、CPU更新按层和分块多流水线执行，重叠CPU计算、CPU-GPU传输与GPU计算，最小化暴露延迟
- 弹性Checkpointing：动态选择激活的保留、卸载、重计算策略，利用闲置GPU显存降低传输和重计算开销
- AutoPolicy自动调优：基于硬件拓扑和任务负载，自动选择最优通信路径、分块大小、激活策略，在显存约束下最大化吞吐

### 关键结果数字
在RTX4090、A800、H100三种平台测试，对比SlideFormer、MegaTrain、ZeRO-Offload等基线：相同batch下几何平均吞吐提升1.46~2.64倍；4张H100上Qwen3-14B大batch场景吞吐超GPU驻留FSDP2 11.2%；支持Qwen3-14B单步1M tokens、256K长序列微调；4张RTX4090可完成Qwen2.5-72B全参数微调；弱缩放效率达95~98%，主机内存占用比基线低14.5%~41.3%。

**最值得记住的一句话**：主机驻留多卡微调的核心瓶颈不是显存，而是共享主机资源的调度效率，合理的流水线重叠和路径选择可让离卡微调的吞吐接近甚至超过GPU驻留方案。
