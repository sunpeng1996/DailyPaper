---
title: 'AVQ-Attention-2: Adaptive Vector-Quantized Attention with Exact Local Blocks
  and Linear-Cost Training'
title_zh: AVQ-Attention-2：带精确局部块与线性训练代价的自适应矢量量化注意力
authors:
- Winfried van den Dool
- Patrick Forré
- Amir Habibian
- Yuki M. Asano
- Max Welling
affiliations:
- University of Amsterdam
- University of Technology Nuremberg
- Qualcomm AI Research
arxiv_id: '2611.32989'
url: https://arxiv.org/abs/2611.32989
pdf_url: https://arxiv.org/pdf/2611.32989
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 高效注意力 · 线性代价Transformer优化
tags:
- Efficient-Attention
- Transformer
- Vector-Quantization
- Linear-Time-Computation
- FlashAttention
one_liner: 融合精确局部注意力与矢量量化注意力，实现线性训练推理代价的通用注意力替换层
practical_value: '- 可直接将AVQ-Attention-2作为FlashAttention的替代品，用于长序列用户行为建模的召回/排序Transformer训练，短序列下获得1.3~2倍加速，长序列（>9k
  tokens）下加速可达3.5倍，精度损失小于1%

  - 借鉴「精确局部块+全局量化聚类」的混合注意力设计，在用户序列建模中，对近1个月的高价值行为做精确注意力计算，对更早的低价值行为做聚类量化注意力，平衡精度与计算开销

  - 参考硬件感知的token分块优化方法，在多模态推荐的视觉/文本特征处理中，预先针对GPU tile计算特性优化token分块，无需额外运行时开销即可获得免费精度收益

  - 对于需要复用预训练Transformer的推荐场景，可直接drop-in替换原有注意力层，仅需用少量batch数据完成codebook初始化，无需全量微调即可保证效果稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
标准Attention的O(N²)复杂度随序列长度增长急剧升高，FlashAttention仅解决内存瓶颈未消除计算量的二次项；现有矢量量化注意力需额外消耗预算拟合局部近邻，且训练仍为二次复杂度，无法直接替换预训练模型的注意力层。
### 方法关键点
- 混合注意力架构：每个查询对近邻token块做精确注意力计算，对全局token通过聚类均值做量化注意力，通过计数修正避免重复计算，二者融合为单趟attention pass无需中间存储
- 训练代价优化：用聚类键均值替代固定codeword做注意力计算，梯度可通过聚类均值回传，将训练代价从O(N²)降低到O(NM)线性复杂度
- 工程优化：提出硬件感知的token分块策略，提前针对GPU tile特性优化分块无运行时开销；新增排序预处理逻辑，将量化预计算速度提升1.5~2.7倍
### 关键结果
在ImageNet-1k（N=785）、ADE20K（N=901）、Diving-48（N=9216/18432）三个任务上对比FlashAttention-2、MRA、Agent Attention等基线：drop-in替换无需微调时精度损失<2%，微调后精度几乎与精确注意力持平；短序列下推理加速1.3~2倍，18k长序列下训练推理加速可达3.5倍。
### 核心结论
AVQ-Attention-2是首个可直接drop-in替换预训练Transformer注意力层、训练推理均为线性复杂度、精度接近精确注意力的通用高效注意力实现
