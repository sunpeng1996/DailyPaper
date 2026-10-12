---
title: 'Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy'
title_zh: Adaptive DHiSparse：基于负载自适应分层KV的投机解码
authors:
- Naji Alazhar
- Wassel Alazhar
affiliations:
- Umans AI
arxiv_id: '2610.13708'
url: https://arxiv.org/abs/2610.13708
pdf_url: https://arxiv.org/pdf/2610.13708
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM推理优化 · 分层KV与投机解码
tags:
- KV_cache
- Speculative_Decoding
- Long-Context_Serving
- Hierarchical_Caching
- LLM_Inference
one_liner: 在负载自适应分层稀疏KV缓存上支持投机解码，大幅提升长上下文大模型并发推理性能
practical_value: '- 长上下文导购Agent、用户全生命周期会话推荐等场景，可复用分层KV+负载自适应调度方案，将冷历史KV落主机内存，仅热KV留GPU
  HBM，在不损失效果前提下提升单卡并发会话数3~4倍，降低部署成本

  - 业务若用投机解码加速LLM推理（比如生成推荐文案、多轮Agent回复），可复用跨query去重KV拉取逻辑，同一请求多步投机验证共享历史KV拉取结果，降低PCIe带宽占用30%左右

  - 投机解码block size可按负载动态调整：低负载用大block最大化单步出数，高负载用小block降低单会话资源占用，平衡吞吐量和端到端延迟

  - 配置KV热缓存大小时不要盲目追高命中率，过大的热缓存会占用会话配额导致吞吐量下降，需结合模型KV共享特性、业务并发要求找最优值'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM服务中，KV cache 占用GPU HBM过高，往往先于计算资源成为瓶颈。现有分层KV方案HiSparse采用固定缓存预算，无法适配动态负载，也不支持 speculative decoding 的多query验证KV需求，无法充分释放硬件性能。

### 方法关键点
- 负载自适应KV驻留策略：保留固定大小的热缓存+可回收可选历史缓存，低负载时将更多历史KV存于GPU HBM减少主机拉取，高负载时回收可选缓存释放空间承接更多会话，全量KV均可从主机恢复无精度损失
- 适配投机解码的KV管理：同一请求的多步验证query共享历史KV拉取结果，去重减少PCIe传输；draft模型KV采用窗口受限的环形缓存，占用不随上下文长度增长；验证临时KV staging按层组复用，降低临时内存开销
- 兼容DSpark、DFlash2等主流投机解码框架，不修改原有提案生成与接受逻辑

### 关键实验结果
在B300 GPU上测试GLM-5.3（100K上下文）、DeepSeek-V4.1-Flash（500K上下文），对比baseline包括HiSparse、全驻留KV服务：1. 100K上下文并发128时，GLM-5.3+DFlash2方案吞吐量达793 tokens/s/卡，为HiSparse的1.45倍、非投机自适应服务的1.27倍，同latency约束下可承载4倍并发、2.3~3.7倍吞吐量；2. 500K上下文并发512时，DeepSeek+DSpark方案吞吐量为全驻留+DSpark的1.85倍；3. 低负载时可选缓存将主机拉取KV比例从14.2%降至1.4%。

> 最值得记住：长上下文LLM服务的KV缓存优化不能只追求命中率，要平衡缓存开销、会话并发数、计算利用率三者的关系，投机解码必须和KV分层调度结合才能发挥最大收益
