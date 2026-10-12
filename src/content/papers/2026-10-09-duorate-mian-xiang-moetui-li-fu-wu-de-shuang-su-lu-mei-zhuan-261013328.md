---
title: 'DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving'
title_zh: DuoRate：面向MoE推理服务的双速率每专家精度分配机制
authors:
- Mengqi Guo
- Zhe Wei
- Yuan Yuan
- Jiunn Bin Lim
- Boyi Pan
- Michael Bi Mi
affiliations:
- Huawei Technologies Ltd.
arxiv_id: '2610.13328'
url: https://arxiv.org/abs/2610.13328
pdf_url: https://arxiv.org/pdf/2610.13328
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: MoE推理优化 · 混合精度量化
tags:
- MoE
- Quantization
- Inference Optimization
- Rate Distortion
- Serving
one_liner: 针对MoE服务存储-读取带宽gap，提出单份权重双速率的每专家精度分配机制
practical_value: '- 落地MoE架构的生成式推荐/Agent推理时，可复用双速率精度分配思路，区分prefill与decode的位宽需求，无需多份量化checkpoint即可适配不同业务负载，同时降低显存占用与解码带宽消耗

  - MoE路由频率在解码侧精度分配时可完全抵消，仅需无标签prefill数据做统计即可快速生成适配业务的精度表，计算量仅为每个专家一次点积+全局二分查找，线上动态调整成本极低

  - 对低延迟要求高的电商实时场景（如会话式推荐、Agent导购长输出），该方案可在精度损失<1%的前提下降低解码带宽3倍以上，尤其适配batch=1的长尾推理场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE模型推理存在严重的存储-读取带宽gap：现有MoE量化方案仅约束存储位宽，未考虑解码阶段仅激活少量专家的特性，导致解码时实际读取带宽远高于存储标称位宽，例如公开BITSMOE 2bit checkpoint存储仅2.54bpw，但batch=1解码时实际读取带宽达7.5bpw，浪费大量解码资源。

### 方法关键点
- 离线阶段仅存储1份前缀可读的多精度权重流，预计算每个专家不同位宽下的失真张量S，所有负载复用同一份checkpoint
- 线上适配新负载时，仅需无标签prefill数据统计专家激活二阶矩，通过一次点积即可计算每个专家不同位宽的失真，基于拉格朗日率失真优化分配读取位宽，路由频率在分配决策中完全抵消，仅需全局二分查找λ即可满足解码带宽预算
- 推理阶段prefill读取全量存储位宽，decode仅读取每个专家分配的前缀位宽，切换负载仅需更新KB级的位宽分配表，无需重新量化权重

### 关键实验结果
在Qwen3-30B-A3B MoE模型上验证：2.9bpw读取位宽下精度匹配读取位宽高1.4-1.6bpw的4bit格式，GSM8K长解码场景下仅比BF16低0.25个点；对比2bit类基线，2.3bpw读取位宽下平均精度领先6.3-47个点；精度分配策略本身可带来0.07-0.11bpw的读率收益。

### 最值得记住的结论
MoE服务的精度成本有两个独立维度——存储占用与解码带宽，仅优化存储位宽反而可能大幅提升解码阶段的实际带宽消耗，双速率设计可在两者间找到最优平衡。
