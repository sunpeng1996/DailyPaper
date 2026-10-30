---
title: 'Read More, Reason Deeper: Latent Workspaces for Long-Sequence Recommendation'
title_zh: 基于隐式工作区的长序列推荐：解耦证据扩展与推理扩展
authors:
- Renzhi Wu
- Li Sheng
- Zikun Cui
- Junjie Yang
- Tai Guo
- Keke Zhai
- Yan Li
- Jerry Fu
- Nipun Mathur
- Sri Reddy
affiliations:
- Meta MRS
- Facebook Discovery
arxiv_id: '2610.39188'
url: https://arxiv.org/abs/2610.39188
pdf_url: https://arxiv.org/pdf/2610.39188
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 长序列推荐 · 算力效率优化
tags:
- Long-sequence Recommendation
- CTR Prediction
- Ranking
- Efficiency
- Scaling
one_liner: 隐式工作区排序器LWR解耦长序列推荐的证据与推理扩展，兼顾效果与算力效率
practical_value: '- 长序列推荐架构设计可参考LWR的解耦思路：将用户历史/上下文等证据存入静态共享银行，仅传递固定大小的候选相关工作区跨层计算，大幅降低前向算力开销

  - 多轮推理的长序列建模可复用层间condensate archive设计：每层压缩当前推理状态存入归档，后续层可同时访问原始证据和历史推理结果，避免早期证据选择不可逆的问题

  - 算力调优可借鉴双维度缩放评估方法：分别做固定推理深度下的历史长度调优、固定历史长度下的推理深度调优，再拟合帕累托前沿选择最优算力分配方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长序列推荐架构将证据扩展（拉长用户历史）和推理扩展（加深模型层数）强耦合：要么全序列跨层传递导致算力随历史长度线性暴涨，要么提前做单次池化/检索过滤证据，导致深层无法访问被过滤的历史信息，限制了长序列和深层模型的收益。

### 方法关键点
- 核心解耦设计：将用户长历史、请求上下文、候选匹配事件三类证据存入静态持久化银行，仅用固定大小的候选专属工作区跨层传递状态，历史长度和模型深度调整互不影响
- 每层执行四步操作：协调（工作区自注意力更新状态）→ 查询（基于当前工作区+历史推理归档生成各证据源的查询）→ 重读（跨注意力检索对应证据源）→ 交互（融合检索结果与排序特征更新工作区）
- 层间condensate归档机制：非最后一层压缩当前工作区生成少量condensate令牌存入归档，后续层可同时访问原始证据和所有层的历史推理结果

### 关键实验
基于Meta两个十亿级推荐场景数据集，对比HSTU等主流基线：10K长历史下，LWR较HSTU NE提升0.19%，前向GFLOP/请求降低69.6%；双维度缩放测试中，LWR的算力效率前沿斜率最高（α=0.845，显著高于基线的0.424~0.599），在12K~65K历史区间效果领先所有基线。

### 核心结论
长序列推荐不需要把全量历史塞进每一层的计算流，解耦可访问证据和传递状态能同时实现「读更长历史」和「做更深推理」的双重收益。
