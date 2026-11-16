---
title: 'Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated
  KV under Prefill-Decode Disaggregation'
title_zh: Callo：预填充-解码分离架构下基于失效KV的投机解码系统
authors:
- Jianjun Ou
- Matthew Lentz
affiliations:
- Duke University
arxiv_id: '2611.18459'
url: https://arxiv.org/abs/2611.18459
pdf_url: https://arxiv.org/pdf/2611.18459
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM服务优化 · 失效KV 投机解码
tags:
- KV cache
- Speculative Decoding
- Disaggregated Serving
- LLM Inference
- Agent Session
one_liner: 在预填充-解码分离架构下利用失效KV做投机解码，无损降低上下文编辑引发的缓存失效延迟
practical_value: '- 多轮Agent（如电商导购Agent、会话式推荐）服务中，上下文编辑导致的失效KV无需直接丢弃，可重定位后作为投机解码的草稿源，通过精确KV验证保证输出无损，可降低10%-20%的请求延迟

  - 预填充-解码分离部署架构下，可复用层粒度KV流式传输trick，无需等全量预填充完成再传输，既减少传输突刺，还能逐步提升投机草稿的接受率

  - 调度策略可参考CALLO设计：优先保障正常业务请求的解码资源，仅空闲时运行投机任务，投机任务累计接受概率低于阈值时提前终止，饱和负载下也不会劣化原有性能'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent多轮会话（如编码Agent、电商导购Agent）会频繁编辑上下文以优化效果、控制成本，这会导致KV缓存大量失效，需要重新完成全量预填充才能启动解码，产生显著延迟；现有预填充-解码分离架构仅能避免失效请求影响其他会话，无法降低失效请求本身的等待开销，直接影响Agent交互体验。

### 方法关键点
- 核心逻辑：在预填充阶段利用解码节点的空闲算力，对失效KV做位置重对齐后直接用目标模型做投机解码生成草稿，等精确KV全部生成后再统一验证草稿，仅提交符合要求的token，完全保证输出无损
- 流式KV更新：预填充节点每计算完一层的KV就实时写入解码节点的对应内存位置，无需等全量预填充完成，边更新边解码可逐步提升草稿接受率
- 自适应调度：优先调度普通业务解码请求，仅在有空闲槽位时准入投机任务；根据草稿token的top1-top2 logit gap计算累计接受概率，低于0.3阈值时提前终止投机，避免浪费资源

### 关键实验
基于SWE-agent真实会话数据集，在Llama-3.3-70B、Gemma-4-31B、Mistral-Small-3.2-24B三个模型上测试，对比基线为原生vLLM；中等负载下缓存失效请求速度提升1.06~1.24×，全请求速度提升1.05~1.19×；单请求场景下可隐藏49%的缓存失效惩罚，75%的投机token可通过验证。

最值得记住的一句话：失效的KV缓存不是无用垃圾，而是质量极高的投机解码状态源，仅需增加验证环节即可在无损输出质量的前提下显著降低缓存失效延迟。
