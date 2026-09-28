---
title: Block Sparse Attention with Log-Linear Complexity
title_zh: 对数线性复杂度的块稀疏注意力机制PISA
authors:
- Bohao Tang
- Zhen Qin
- Yuqi Pan
- Zheng Li
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- ByteDance Seed
arxiv_id: '2609.31093'
url: https://arxiv.org/abs/2609.31093
pdf_url: https://arxiv.org/pdf/2609.31093
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: 长上下文LLM · 稀疏注意力优化
tags:
- Sparse Attention
- Long Context LLM
- Triton Kernel
- Block Attention
- Inference Optimization
one_liner: 提出金字塔层级Top-K+LSE打分的块稀疏注意力PISA，预填充复杂度降至O(N log N)
practical_value: '- 长上下文LLM服务（如电商商品长文档理解、用户全生命周期行为建模用大模型）可直接复用PISA的金字塔层级Top-K选择逻辑，将块选择复杂度从O(N²)降至O(N
  log N)，降低长序列推理延迟

  - 块匹配打分可借鉴LogSumExp（LSE）替代传统平均池化，实验显示该方案块选择召回率更高，注意力质量保留更好，适合推荐召回、RAG检索等匹配场景

  - 工程上可复用其硬件感知Triton核设计：训练/预填充用两阶段核跨查询复用Key块降低IO，解码用单阶段核减少启动开销，32K以上长序列下相比传统BSA有几倍速度提升

  - 长序列用户行为匹配场景可复用粗到细筛选逻辑：先选粗粒度行为时段，再选细粒度单个行为，降低全序列匹配的复杂度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM落地的核心瓶颈是自注意力的O(N²)复杂度，传统块稀疏注意力（BSA）虽然后续注意力计算复杂度为线性，但块选择阶段需要遍历所有候选块，复杂度仍达O(N²/C)，在32K以上长序列下成为核心性能瓶颈。

### 方法关键点
- 构造粗到细的Key块金字塔：通过平均池化聚合相邻块生成多层级摘要，层级越高覆盖序列范围越大、候选块数量越少，总层级数为O(log N)
- 层级Top-K筛选：从最粗层级开始选Top-K候选块，展开到下一层细粒度块后再次筛选，直到最细的原始块层级；每个query每层仅处理固定数量候选，单query块选择复杂度降至O(log N)，整体预填充复杂度为O(N log N)
- 采用LogSumExp（LSE）做块打分：相比传统平均池化打分，能更准确反映块的真实匹配度，块选择召回率更高
- 硬件感知Triton核实现：训练/预填充用两阶段核，跨查询复用加载的Key块降低IO开销；解码用单阶段核，避免多轮核启动开销，全程不实例化完整QK得分矩阵，大幅降低内存占用

### 关键结果
在418M/1.47B/2.67B三个尺度的Decoder-only LLM上对比BSA、NSA、HiLS等基线：
1. 常识推理任务性能与基线相当，6类包含式检索任务平均精度为所有稀疏方法最高
2. 长序列块选择延迟：64K/128K/256K序列长度下，相对BSA分别取得2.86×/5.31×/9.95×的加速比
3. 块选择质量：Recall@8和注意力质量占比均优于BSA等基线

### 核心结论
序列长度≥32K时，粗到细层级筛选的块稀疏注意力，在不损失效果的前提下，延迟远低于传统全量遍历的块稀疏方案。
