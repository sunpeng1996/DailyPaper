---
title: 'KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints'
title_zh: KVShareArena：跨上下文与模型检查点的KV缓存复用基准
authors:
- Xi Shi
- Qian Lou
affiliations:
- University of Central Florida
arxiv_id: '2609.10266'
url: https://arxiv.org/abs/2609.10266
pdf_url: https://arxiv.org/pdf/2609.10266
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: LLM推理优化 · KV cache 复用评测
tags:
- KV-cache
- Benchmark
- LLM Serving
- RAG
- Multi-Agent
one_liner: 首个覆盖RAG、多智能体场景的跨上下文/跨检查点KV缓存复用评测基准，配套统一评分体系与公开榜单
practical_value: '- 搭建RAG/多Agent系统的KV缓存复用能力时，优先实现免费的位置重对齐，单源场景下可恢复93%+性能，几乎无额外开销，无需直接上复杂方案

  - 多源拼接的RAG导购、多Agent报告生成等需要跨块联合推理的场景，优先选择选择性重计算方案（如LegoLink仅重算0.4% payload就能恢复40%+性能缺口），效果远好于压缩类方案

  - 跨同架构模型检查点复用KV缓存时，避免使用和特定检查点绑定的训练类修复方案，易出现显著性能下降，训练无关的重计算类方案稳定性更高，波动小于0.02

  - 严禁直接复用未对齐的KV缓存，多Agent报告场景下未对齐缓存的效果比不用缓存还差（PGR=-0.82），反而损害输出质量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有KV缓存复用仅支持精确前缀匹配，无法适配RAG（多检索块动态拼接）、多Agent（跨模型/上下文传递报告）这两类高速增长的生产场景；同时零散分布在RAG、多Agent等社区的KV修复方案缺乏统一评测标准，无法横向对比效果与成本，无法指导生产选型。

### 方法关键点
- 两因子评测框架：覆盖「上下文变化」「跨同架构模型检查点复用」两大核心场景，包含Retrieved Evidence（RAG检索块）、Agent Reports（多Agent生成报告）两个赛道
- 统一质量指标PGR（性能缺口恢复率）：以无缓存为底、全重算为顶，量化修复方案恢复的上下文价值比例，可跨任务横向对比
- 三维成本度量：从计算量、内存占用、首包延迟（TTFT）三个维度统一统计效率，单独统计缓存构建一次性成本，不摊薄到单请求，适配不同业务的缓存复用频次特征
- 配套可pip安装的评测框架、固定查询集、公开榜单，支持自动化提交复现

### 关键结果
在LongBench、FRAMES等公开数据集上评测10+主流KV修复方案，核心结论：
1. 免费位置重对齐在单源场景下恢复93%+性能，多源联合推理场景仅能恢复25%，未对齐缓存效果比无缓存差（PGR=-0.82）
2. 多源场景下选择性重计算方案LegoLink仅重算0.4% payload就能恢复41.6%的多跳QA性能缺口，KVPacket零重算恢复36.5%
3. 压缩类方案在精确前缀场景下无损，但跨上下文拼接场景效果显著低于免费位置对齐，甚至低于无缓存
4. 跨检查点复用场景下，训练类修复方案性能下降最高0.23，重计算类方案波动小于0.02

**最值得记住的一句话：KV缓存复用的效果损失=位置错位损失+跨源互盲损失，仅当任务需要多源联合推理时，付费修复方案的投入才值得**
