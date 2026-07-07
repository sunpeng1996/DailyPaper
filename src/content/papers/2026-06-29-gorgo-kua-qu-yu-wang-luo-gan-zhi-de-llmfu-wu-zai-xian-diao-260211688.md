---
title: 'GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving'
title_zh: GORGO：跨区域网络感知的LLM服务在线调优框架
authors:
- Alessio Ricci Toniolo
- Rome Thorstenson
- Abinaya Dinesh
affiliations:
- Carnegie Mellon University
- Arcadia Research Team
arxiv_id: '2602.11688'
url: https://arxiv.org/abs/2602.11688
pdf_url: https://arxiv.org/pdf/2602.11688
published: '2026-06-29'
collected: '2026-07-07'
category: LLM
direction: LLM服务 · 跨区域路由调优
tags:
- LLM Serving
- KV Cache
- Load Balancing
- Online Tuning
- Evolution Strategy
one_liner: 提出跨区域LLM服务路由框架GORGO，结合多维度成本在线调优，显著降低TTFT与端到端延迟
practical_value: '- 跨区域部署LLM类业务（如电商智能客服、生成式推荐prompt服务）可复用GORGO三因素成本模型：加权网络RTT、队列等待、未缓存prefill长度，替代单一启发式路由策略，平衡TTFT与端到端延迟

  - 在线调优权重可采用轻量(1+1)进化策略，仅2个参数调优空间，收敛快、无额外推理开销，适合生产环境实时迭代，无需复杂贝叶斯优化方案

  - 长上下文、高会话复用场景（如多轮导购对话）的LLM服务压测可复用开源ART-Chat-2.5M数据集，比通用LMSYS/WildChat更贴近高KV缓存复用的生产负载

  - 若业务对首包响应优先级极高（如实时对话Agent）可适当调低队列权重，优先路由到近区域高缓存命中节点，容忍一定后端饱和带来的长尾E2E延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有跨区域LLM服务的负载均衡策略仅考虑KV缓存复用、节点负载等单一或部分因素，忽略跨区域网络延迟差异，导致长上下文、高会话复用场景下TTFT（首token时间）和端到端延迟偏高，无法兼顾缓存命中、负载均衡、网络开销的平衡。此外现有公开对话数据集缺乏长上下文、高前缀复用的生产级流量，无法有效验证缓存感知路由策略的效果。

### 方法关键点
- 成本模型统一融合三个核心TTFT影响因子：加权跨区域网络RTT、加权节点队列等待延迟、未命中KV缓存的prefill计算成本，通过权重归一化不同单位的指标，选择总路由成本最低的副本
- 采用轻量(1+1)进化策略在线调优RTT和队列延迟的权重，以p95 TTFT为优化目标，遵循1/5成功规则动态调整步长，收敛快、无额外计算开销，小窗口调优的权重可泛化到多天流量
- 构造并开源ART-Chat-2.5M数据集，基于生产长上下文多轮对话流量生成，平均输入token达17964，用户内前缀复用率89.4%，符合高KV缓存复用的生产场景特征

### 关键结果
在跨3区域的SGLang集群上部署Qwen3.5-35B模型测试，对比会话亲和、前缀缓存、最小负载等基线，GORGO在未知流量窗口下p95 TTFT降低6.9%~15.5%，p95端到端延迟降低14.3%~30.9%；仅在短上下文、低前缀复用的公开数据集上效果不及基线。

**最值得记住的话**：路由策略的收益高度依赖负载特征，长上下文高复用场景下多因素加权的动态调优策略显著优于单一启发式规则，短上下文低复用场景下简单路由规则即可满足需求
