---
title: 'KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems'
title_zh: KVCMAS：多智能体系统共享上下文的高效KV缓存修正框架
authors:
- Hyesung Jeon
- Hyeongju Ha
- Seoyoung Lee
- Beomseok Kang
- Jae-Joon Kim
affiliations:
- Seoul National University
arxiv_id: '2609.34060'
url: https://arxiv.org/abs/2609.34060
pdf_url: https://arxiv.org/pdf/2609.34060
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: 多智能体 · KV缓存推理优化
tags:
- MultiAgent
- KV cache
- Low Rank
- Inference Optimization
- Serving Efficiency
one_liner: 用低秩状态表示跨Agent缓存偏差+链式修正，实现低时延低内存的多Agent KV缓存共享
practical_value: '- 电商多Agent导购/广告策略生成场景可直接复用该方案，跨Agent共享的用户画像、检索结果等上下文无需重复预填充，峰值GPU内存可降低3.7×，高并发下TTFT提升2倍

  - 落地时优先对首个处理用户请求的Agent做全量预填充，后续角色Agent沿工作流链式复用修正后的KV缓存，无需额外构建无上下文参考缓存，可进一步降低34%的TTFT

  - 低秩delta修正的思路可迁移到长上下文RAG推荐、搜索Query理解场景的KV缓存优化，用rank=32的低秩因子存储缓存偏差，内存开销相比全量存储降低一个数量级以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Prompt驱动的多Agent系统中，不同Agent的角色前缀会导致相同共享上下文生成的KV缓存不兼容，每个Agent都要重复预填充上下文，计算和内存开销极高；现有KV缓存共享方法要么仅支持固定上下文关系，要么需要维护全量参考缓存，内存开销大，且首Agent的修正误差会沿工作流传播影响下游效果。

### 方法关键点
- 利用跨Agent KV缓存偏差的低秩特性，用截断SVD将base缓存和delta修正存储为低秩因子，锚点池内存从O(VNLD)降低到O(VNr(L+D))，r取32即可覆盖90%以上的奇异值能量
- 采用链式修正架构，首Agent完整预填充生成精确缓存，后续每个Agent直接基于前序Agent输出的缓存做修正，无需额外构建独立的无上下文参考缓存，避免额外预填充开销
- 基于锚点匹配的归一化熵做可靠性门控，匹配可靠时直接应用低秩delta修正，不可靠时回退到全量预填充，保证任务精度

### 关键实验
在MMLU、GSM8K、HumanEval、MathVista、Video-MME 5个基准上对比NonShared、FullShared、DroidSpeak、KVComm等7个基线：精度与KVComm相当（误差<0.7%），峰值GPU内存比KVComm低3.7×；32K共享上下文、8QPS高并发下，TTFT比无缓存共享方案快2.0×，比非链式修正快34%；多Agent交互轮次增加时，仍保持最低TTFT和最高吞吐量。

> 最值得记住：多Agent场景下跨角色的KV缓存偏差具有天然低秩特性，沿工作流链式复用修正缓存可在几乎不损失精度的前提下大幅降低推理时延和内存开销
