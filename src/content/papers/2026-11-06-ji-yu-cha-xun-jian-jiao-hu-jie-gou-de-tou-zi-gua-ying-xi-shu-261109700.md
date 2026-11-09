---
title: 'Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key
  Interaction Structure'
title_zh: 基于查询-键交互结构的头自适应稀疏注意力框架HASA
authors:
- Wajih Hassan Raza
- Ahsan Bilal
- Yidan Shen
- Renjie Hu
- Xin Fu
- Yu Wen
affiliations:
- University of Houston
- University of Oklahoma
arxiv_id: '2611.09700'
url: https://arxiv.org/abs/2611.09700
pdf_url: https://arxiv.org/pdf/2611.09700
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM推理优化 · 稀疏注意力
tags:
- Sparse Attention
- Long Context LLM
- Inference Optimization
- Training Free
- KV Cache
one_liner: 无需训练的头自适应稀疏注意力框架，为每个注意力头适配特征与序列维度的选择分辨率
practical_value: '- 电商长上下文LLM应用（如多轮导购、长用户行为序列生成推荐）可直接集成HASA，无需微调即可获得最高14倍稠密注意力加速，精度损失小于1%，适配高并发推理场景

  - 推荐系统中LLM4Rec模块可复用头自适应思路：对负责局部行为匹配、全局兴趣建模的不同注意力头分别设置KV缓存粒度和特征维度，实测可降低KV内存占用30%以上

  - 可复用HASA的「低维特征粗筛+全维特征精算」架构，在商品召回/粗排阶段用低维语义特征快速筛选候选，后续用全维特征做精准打分，平衡筛选效率与精度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长上下文LLM推理场景下，稠密注意力的O(n²)计算量与KV缓存访问开销成为性能瓶颈，现有稀疏注意力方案多采用固定粒度的上下文选择规则，未适配不同注意力头的内在交互结构，要么粗粒度筛选漏选关键token导致精度下降，要么细粒度筛选引入过高的前置计算开销，难以同时满足精度与推理效率要求。
### 方法关键点
- 特征维度自适应：离线对每个注意力头的Q-K权重矩阵做SVD分解，结合谱熵和截断误差阈值确定每个头的有效秩，构造头专属的低维响应空间，用于轻量相关性预打分
- 序列维度自适应：在每个头的低维响应空间中，基于token响应的方向一致性渐进合并相邻上下文块，响应高度一致的块合并为大粒度区域，异质性高的块保留细粒度，合并过程仅依赖预计算的块统计量，无需回溯原始token
- 稀疏选择执行：用低维特征计算候选区域的相关性得分，筛选Top-K高相关区域后加载原始全维KV做精确注意力计算，仅在最终计算阶段引入全维特征开销
### 关键实验
基于Ministral-3-8B、Qwen3-8B两个开源模型验证，对比H2O、Quest、InfLLM、UNIQUE等主流训练-free稀疏注意力基线，在LongBench-Pro、RULER-32K长上下文基准上：精度超过最优基线UNIQUE最高3.47个百分点（RULER）、2.57个百分点（LongBench-Pro），512 token KV预算下精度仅比稠密注意力低0.27个点；效率层面，32K上下文下自注意力速度比稠密注意力快14.07倍，比UNIQUE快1.32倍，同时保留88.1%的稠密注意力质量。
### 核心结论
不同注意力头的Q-K交互结构差异极大，自适应为每个头匹配特征和序列粒度，比统一固定粒度的稀疏策略能同时获得更高的精度和效率。
