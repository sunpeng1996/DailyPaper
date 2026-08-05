---
title: 'SITA: Semantic Interest Tokens for Target-Aware Compression in Long-Sequence
  Recommendation'
title_zh: SITA：长序列推荐中支持目标感知压缩的语义兴趣令牌方法
authors:
- Rui Zhou
- Bo Chen
- Qinglin Jia
- Jiezhou Ji
- Chaoyi Ma
- Ruiming Tang
- Hao Wang
- Enhong Chen
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
arxiv_id: '2608.03692'
url: https://arxiv.org/abs/2608.03692
pdf_url: https://arxiv.org/pdf/2608.03692
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 长序列推荐 · 兴趣压缩与语义ID
tags:
- Long-Sequence Recommendation
- Semantic ID
- Interest Compression
- CTR Prediction
- Industrial Recommendation
one_liner: 提出基于Semantic ID的长序列推荐压缩框架，同时兼顾全局兴趣建模、目标感知与工业可部署性
practical_value: '- 语义ID生成可直接复用Balanced Parallel Quantization（BPQ）思路，新增码本使用均衡正则缓解坍塌，大幅降低用户兴趣存储复杂度，适配亿级用户长序列场景

  - 兴趣压缩模块可直接替换现有长序列建模方案：离线用Structured Interest Compression（SIC）块生成按语义分组的兴趣令牌，在线仅需根据候选item的Semantic
  ID查表选对应令牌，推理复杂度仅O(BNd)，和现有压缩类方案持平

  - 工业落地可直接复用离线预计算+在线查表范式：快手生产环境仅替换长序列建模模块，就获得最高0.078%的AUC提升，大规模场景下收益显著

  - 超参调优可直接参考验证结论：语义码本配置(N,K)取平衡值（如总令牌数128时选(8,16)），SIC块数取4即可达到最优效果，无需过多堆叠增加计算量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长序列推荐分为两类范式：检索类（如SIM、TWIN）需在线与全量长序列交互，推理成本高，且仅能捕捉局部相关兴趣；压缩类（如C-Former、VISTA）生成的用户表征全局共享，无法适配不同候选item的目标感知需求，两类方案均无法同时满足全局兴趣建模、目标感知、工业可部署三个核心要求。

### 方法关键点
- **Balanced Parallel Quantization（BPQ）**：基于item多模态表征学习Semantic ID（SID），引入码本使用均衡正则缓解码本坍塌，将item空间映射为N个并行码本、每个K个码词的紧凑型语义空间，存储复杂度从O(|U||V|)降至O(|U|*N*K)
- **Structured Interest Compression（SIC）**：离线堆叠SIC块，通过组内SwiGLU建模细粒度语义组内兴趣、组间自注意力实现跨语义组信息交互，将全量行为序列压缩为按语义分组的N*K个兴趣令牌，支持离线预计算存储
- **SID-Guided Selection（SGS）**：在线推理时仅需根据候选item的SID，从预存的兴趣令牌中选对应组的令牌聚合，得到目标感知的用户兴趣表征，无需访问原始长序列

### 关键实验
在Taobao-MM、XLong公开数据集对比SIM、TWIN、C-Former、LONGER等10个基线，AUC最高提升3.77%，GAUC最高提升3.82%；快手生产环境两个场景下，AUC最高提升0.078%，GAUC最高提升0.076%，均达到统计显著。

最值得记住的结论：长序列推荐的核心优化方向是在不损失推理效率的前提下，实现全局兴趣的结构化存储与目标感知的动态适配。
