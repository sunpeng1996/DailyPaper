---
title: 'Page-EntroKV: Hardware-Aligned, Entropy-Weighted KV-Cache Eviction under Grouped-Query
  Attention'
title_zh: Page-EntroKV：GQA场景下硬件对齐的熵加权KV缓存淘汰机制
authors:
- Inbasekaran S
affiliations:
- SRM Institute of Science and Technology, India
arxiv_id: '2610.03135'
url: https://arxiv.org/abs/2610.03135
pdf_url: https://arxiv.org/pdf/2610.03135
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM推理优化 · KV cache 淘汰
tags:
- KV cache
- Grouped-Query Attention
- PagedAttention
- Entropy
- Inference Serving
one_liner: 针对GQA架构KV缓存独立淘汰的膨胀问题，提出熵加权组池化+页粒度淘汰实现零union开销
practical_value: '- 部署GQA架构大模型的Agent/推理服务（如电商导购Agent、搜索query理解服务）可直接复用组池化思路：同一GQA组的头先聚合再淘汰，完全消除内存膨胀，相比H2O/SnapKV等策略最高可降低80%KV缓存占用

  - 熵加权trick可迁移到长序列推荐/召回场景：用sink-isolated Rényi-2熵给attention头加权，自动放大检索头信号、抑制注意力sink，无需额外标定，可提升长用户序列的语义召回准确率

  - 工程上可直接适配vLLM现有PagedAttention架构，仅需新增2个fused kernel即可上线，额外内存开销低于1MB，不修改底层内存布局即可提升推理并发量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前主流大模型（Llama3、Qwen2等）普遍采用GQA降低KV缓存占用，但现有动态KV缓存淘汰策略均按query头独立计算token重要性，同一GQA组内头的选中token存在分歧，引擎需存储所有选中token的并集，缓存最多膨胀至组比例r倍；算术平均池化又会稀释检索头的事实信号，导致长上下文召回失效，KV缓存已成为长上下文推理的核心内存瓶颈，直接限制服务并发和吞吐量。

### 方法关键点
- 组级熵加权池化：同一GQA组内的头采用sink-isolated Rényi-2熵计算权重，低熵检索头权重指数级放大，高熵注意力sink、弥散头被抑制，从根源消除union开销，UOR恒等于1
- 硬件对齐页粒度淘汰：将聚合后的token重要性映射到PagedAttention物理页帧，按页粒度做max-reduction后淘汰，避免内存碎片，完全适配vLLM现有内存布局
- 理论证明：严格保证缓存预算不超支，有限上下文下needle retention比算术平均池化高几个数量级，无需额外离线标定

### 关键结果
基于Qwen2.5-1.5B-Instruct（r=6）的实验显示：原有按头独立淘汰策略在2%缓存预算下最多膨胀5.1倍，Page-EntroKV在1008次测量中UOR恒为1.0；sink隔离机制将sink头的权重优势从2.10x转为0.66x劣势；20%缓存预算下，熵加权池化的needle召回率100%，算术平均池化召回率为0，QA、代码任务性能保持可用。

**最值得记住的一句话**：GQA下KV缓存优化必须对齐硬件物理内存布局，仅在算法层做token级筛选必然引入额外内存开销。
