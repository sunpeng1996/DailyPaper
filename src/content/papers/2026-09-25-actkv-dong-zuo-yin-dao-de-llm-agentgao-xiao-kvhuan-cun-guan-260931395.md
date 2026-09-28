---
title: 'ActKV: Efficient LLM Agents through Action-Guided KV Cache Management'
title_zh: ActKV：动作引导的LLM Agent高效KV缓存管理框架
authors:
- Zihan Wang
- Cheng Tang
- Lei Gong
- Chao Wang
- Wenqi Lou
- Teng Wang
- Xuehai Zhou
affiliations:
- University of Science and Technology of China
- Suzhou Institute for Advanced Research, University of Science and Technology of
  China
arxiv_id: '2609.31395'
url: https://arxiv.org/abs/2609.31395
pdf_url: https://arxiv.org/pdf/2609.31395
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: LLM Agent · KV缓存推理优化
tags:
- LLM Agent
- KV Cache
- Cache Compression
- Inference Optimization
- Serving Throughput
one_liner: 首个面向LLM Agent推理的KV缓存压缩框架，以26%内存保留98.5%精度，吞吐量提升3.9倍
practical_value: '- 电商导购Agent、多轮交互推荐Agent可复用Action-oriented KV驱逐思路，优先保留工具调用、下单决策等动作相关KV条目，压缩内存的同时不影响核心任务成功率

  - 多轮交互场景可复用置信度驱动的自适应预算分配逻辑，通过LLM输出token置信度变化动态调整缓存容量，无需离线预设不同任务的压缩比，适配动态交互需求

  - 工程侧可复用分页感知压缩的两个定制内核，基于softmax LSE恢复注意力分数、无冲突原地KV压缩，无需额外缓存空间，可快速接入vLLM等主流serving框架提升部署吞吐量

  - 长轮次推荐/导购Agent可参考「过滤无效推理/观测KV、仅保留动作相关KV」的设计思路，解决context膨胀、推理延迟高的问题，降低GPU部署成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent采用迭代观测-推理-行动范式，多轮交互中KV缓存随历史快速膨胀，单WebShop电商导购任务用Qwen3-30B就需3.2GB KV缓存，其中99%为观测、推理类非核心条目。现有KV压缩方法默认所有token重要性一致，未考虑Agent场景下仅动作决定任务进展的不对称性，易误删动作相关关键KV导致任务失败；同时现有方法难以适配vLLM等主流框架的分页内存管理，压缩收益被拷贝开销抵消。
### 方法关键点
- 动作导向KV驱逐：基于同一任务下动作相关KV跨轮次注意力模式稳定的观测，设计注意力感知LRFU策略，优先保留对当前及未来动作贡献高的KV
- 置信度驱动自适应预算分配：利用LLM输出token置信度与KV预算充足性的强相关性，通过滑动窗口监测置信度下降趋势动态调整缓存容量，无需离线预设压缩比
- 分页感知压缩管理：抽象出注意力计算、条目驱逐、缓存压缩三个通用原语，定制两个内核：基于softmax LSE副产品恢复注意力分数，无需全量重计算；无冲突原地压缩内核，无需额外缓存适配分页内存
### 关键结果
在4个Agent大模型（Qwen3-30B/235B、GPT-OSS-20B/120B）、3个Agent基准（ALFWorld、HotpotQA、WebShop）上测试：平均保留98.53%的FullKV任务精度，仅占用25.98%的峰值KV内存；token吞吐量为FullKV的3.97倍，任务吞吐量为3.58倍，较现有压缩基线精度平均提升27%以上。
### 核心洞见
Agent场景的系统优化要优先对齐核心任务目标（动作正确性），而非通用场景的整体输出质量，可同时获得精度和效率的双重收益
