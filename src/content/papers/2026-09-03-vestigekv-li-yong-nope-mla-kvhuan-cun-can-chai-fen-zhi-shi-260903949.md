---
title: 'VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial
  Branch'
title_zh: VestigeKV：利用NoPE-MLA KV缓存残差分支实现无训练压缩
authors:
- WenJie Fan
affiliations:
- Yotta Labs
- University of Science and Technology of China
arxiv_id: '2609.03949'
url: https://arxiv.org/abs/2609.03949
pdf_url: https://arxiv.org/pdf/2609.03949
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM推理优化 · KV Cache压缩
tags:
- KV Cache
- NoPE
- MLA
- LLM Inference
- Cache Eviction
one_liner: 无需修改模型或训练，基于NoPE-MLA残差分支实现KV缓存8-128倍低损压缩
practical_value: '- 若业务使用NoPE架构大模型（如Kimi系列）做Agent/生成式推荐推理，可直接复用VestigeKV缓存策略，无需改模型/训练即可降低VRAM占用、提升长上下文推理吞吐

  - KV分级存储思路可迁移：高重要性token放高速访问层，低重要性token归档到GPU/主机存储按需召回，平衡长上下文推理的成本与效果

  - RoPE架构下无全局静态token重要性信号，不要尝试在RoPE模型上做预查询的全局静态缓存驱逐，效果会严重下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理的KV缓存占用极高，现有基于观测注意力的驱逐方法（H2O、SnapKV等）需要查询存在时才能判断token重要性，在缓存需提前压缩（查询未到达）的场景下效果完全失效，NoPE-MLA架构下缺少低开销、无侵入的缓存压缩方案。

### 方法关键点
- 利用NoPE-MLA模型中原为RoPE设计的64维残差分支（NoPE训练后被重用于显著性编码），仅读取11%的缓存行即可计算token重要性，无需查询参与
- 缓存分为两层：top-m高重要性token留在高速访问层，其余token完整归档到GPU/主机存储，不做删除避免信息损失
- 自研召回层索引：基于残差分支和内容草图构建轻量索引，每步仅扫描索引召回可能竞争注意力的归档token，保证效果无损

### 关键结果
- 8倍压缩下needle检索率100%，32倍压缩下检索率92%（覆盖8k-65k上下文），叠加召回层后128倍压缩仍保持100%检索率
- 对比H2O、SnapKV等基线，在预查询压缩场景下基线检索率几乎降为0，VestigeKV保持92%以上效果
- 仅增加可忽略的计算开销，KV路径读带宽降低4倍，无需修改模型权重、算子或训练流程

**最值得记住的一句话**：NoPE架构下token重要性是全局静态的，RoPE架构下重要性随位置动态变化，二者的缓存优化路线完全不通用。
