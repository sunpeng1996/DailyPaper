---
title: 'Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse
  for Rolling Agents'
title_zh: 滚动Agent场景下选择性KV缓存复用的请求顺序敏感性研究
authors:
- Tiffany Gu
- Annie Guan
- Manshu Huang
- Nitin Rao
- Siddhant Shah
- Margaret Capetz
affiliations:
- Carnegie Mellon University
- Capital One
- University of Chicago
- University of California, Berkeley
- University of Southern California
arxiv_id: '2610.05833'
url: https://arxiv.org/abs/2610.05833
pdf_url: https://arxiv.org/pdf/2610.05833
published: '2026-10-05'
collected: '2026-10-06'
category: LLM
direction: Agent 推理KV缓存优化
tags:
- KV cache
- Rolling Agent
- LLM Serving
- Selective Recomputation
- Inference Optimization
one_liner: 发现滚动Agent场景KV缓存复用的输出受请求顺序影响，提出连续段重计算策略降低输出波动
practical_value: '- 电商导购、RAG问答类Agent业务做LLM推理优化时，优先选择连续段重计算策略，相同算力预算下输出一致性比token top-k提升3倍，且不损失TTFT加速比

  - KV缓存复用策略的上线前评估必须模拟真实业务的连续请求序列，仅测试孤立请求会高估输出稳定性，容易引发相同prompt返回不同结果的业务故障

  - 若业务prompt本身有天然段落/文档边界（如RAG召回的商品块、用户历史会话块），可直接采用文档对齐的连续段选择，无需额外开发分段逻辑，落地成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
滚动Agent（如金融监控、科研检索、电商RAG导购）需要频繁更新上下文窗口，剔除旧文档、加入新文档的操作会打破传统前缀缓存的匹配条件，现有非前缀KV缓存复用的token级top-k重计算策略仅针对孤立请求优化，未考虑跨请求持久化缓存状态的影响，相同prompt在不同请求顺序下可能输出不同结果，无法满足业务确定性要求。
### 方法关键点
- 控制两类策略的重计算预算均为5%：token top-k选择KV偏差最大的散列token重计算，连续段重计算选择连续区域的token重计算，后者包含单窗口、固定块、随机文档、文档对齐4种实现
- 连续段策略基于span的平均KV偏差排序，相同预算下保证重计算token的连续性
- 实验固定Qwen3-8B、贪心解码、随机种子，排除无关变量干扰
### 关键结果
- 数据集采用美股8995条真实行情、新闻、SEC公告，模拟84个文档的滚动窗口工作流，共7735次滚动更新请求
- 跨5种请求顺序测试：token top-k的答案变异率为69.0%，文档对齐策略降至26.1%；乱序场景下token top-k的全预填保真度仅19.8%~41.5%，文档对齐策略提升至54.3%~91.7%，增益34.5~52.5个百分点
- 两类策略的TTFT中位数加速比均约为5.7×，无显著性能差异；ablation证明连续性是鲁棒性提升的核心因素，是否对齐文档边界、是否按偏差排序无显著额外增益

> 最值得记住的结论：KV缓存复用策略的评估不能仅基于孤立请求，必须结合真实业务的连续请求序列，相同算力预算下连续段重计算的鲁棒性远高于散列高偏差token选择。
