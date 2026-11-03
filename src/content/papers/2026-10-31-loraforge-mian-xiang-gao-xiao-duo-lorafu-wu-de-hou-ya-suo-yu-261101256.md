---
title: 'LoRAForge: Co-Designing Post-Hoc Compression and Execution for Efficient Multi-LoRA
  Serving'
title_zh: LoRAForge：面向高效多LoRA服务的后压缩与执行协同设计系统
authors:
- Shenghui Li
- Thiemo Voigt
affiliations:
- Uppsala University
- Research Institutes of Sweden
arxiv_id: '2611.01256'
url: https://arxiv.org/abs/2611.01256
pdf_url: https://arxiv.org/pdf/2611.01256
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: 多LoRA服务 · 推理性能优化
tags:
- LoRA
- Multi-LoRA Serving
- Inference Optimization
- Compression
- GPU Kernel
one_liner: 联合设计多LoRA后压缩管线与秩感知执行后端，大幅提升推理吞吐量与存储效率
practical_value: '- 若业务持有大量垂直域LoRA（如不同品类商品文案生成、不同用户群个性化推荐Prompt适配），可直接复用LoRAForge的光谱能量预算分配策略，仅保留7.7%参数时任务质量损失不超过1.2分（0-100分制），大幅降低GPU显存占用

  - 多LoRA推理服务可复用其秩感知执行核心优化：针对小批量decode的直接归约shrink内核、针对小秩场景的RowExpand内核，实测可提升1.2倍左右吞吐量，无需修改原有LoRA结构

  - 离线批量压缩上百个业务LoRA时，可复用FlashTSQR并行因子构造方法，相比标准库QR压缩速度提升2.28倍'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多LoRA服务是当前LLM落地垂直场景的主流方案，但随着LoRA数量增多，显存占用过高、加载开销大、小秩LoRA无法适配通用内核导致性能损失等问题突出，现有后压缩方法仅关注参数减少，未匹配执行侧优化，无法转化为实际吞吐量提升。

### 方法关键点
- 两种秩分配策略：均匀保留（LoRAForge-U）按统一比例截断所有LoRA的秩；光谱能量分配（LoRAForge-S）根据奇异值能量按预算动态分配每个LoRA的保留秩，优先保留高能量方向
- 设计FlashTSQR并行因子构造原语，跨LoRA模块和行块并行执行QR分解，大幅降低批量LoRA压缩的计算开销
- 秩感知执行后端：针对小批量decode设计直接归约shrink内核，针对小秩场景设计RowExpand内核，通过阶段、秩、形状感知的调度策略自动选择最优执行路径

### 关键结果
基于85个开源Qwen、Llama训练完成的LoRA测试，对比原生SGLang多LoRA服务：
1. LoRAForge-S仅保留7.7%的LoRA参数时，任务平均得分最多下降1.2分（0-100分制）
2. 推理吞吐量相比原生服务在AMD MI250X提升1.59倍，在NVIDIA GH200提升1.92倍，TPOT P99从222.4ms降至40.8ms
3. FlashTSQR相比标准库QR压缩速度提升2.28倍

最值得记住的一句话：LoRA压缩的收益不能只看参数减少比例，必须匹配执行侧的秩感知优化才能转化为实际的吞吐量提升，光谱能量分配是兼顾质量和效率的最优预算分配策略。
