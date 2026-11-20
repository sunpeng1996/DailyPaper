---
title: 'TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management
  and Layer-Wise Streaming'
title_zh: TideCache：支持透明缓存管理与层流式的高效混合LLM服务系统
authors:
- Jinbin Luo
- Xiaozhe Yao
- Shang Yang
- Zhijian Liu
- Song Han
- Qinghao Hu
affiliations:
- Massachusetts Institute of Technology
- ETH Zurich
- University of California, San Diego
arxiv_id: '2611.26619'
url: https://arxiv.org/abs/2611.26619
pdf_url: https://arxiv.org/pdf/2611.26619
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理服务 · KV cache优化
tags:
- KV cache
- LLM serving
- hybrid LLM
- cache management
- streaming inference
one_liner: 为混合架构LLM设计的高效服务系统，较SGLang+HiCache最高提升2.04倍agent turns处理能力
practical_value: '- 混合架构LLM服务可复用透明缓存池设计：基于CUDA虚拟内存API做物理页动态映射，无需修改上层注意力后端，即可动态调整全局KV、bounded
  state缓存的HBM配额，适配电商大促/平峰期不同流量特征（短请求多/长上下文Agent请求多），避免静态分区的资源浪费。

  - 长上下文Agent场景可复用层流式KV预取逻辑：利用滑动窗口/SSM层的计算间隙预取下一层全局注意力KV，无需全量保留长上下文KV在HBM，可提升单卡同时服务的电商客服Agent、商品文档问答Agent的会话数。

  - 请求调度可借鉴分级策略：高优广告/推荐召回请求走常驻KV保证低延迟，普通用户行为分析、离线特征计算请求走流式KV提升吞吐量，平衡业务SLA和资源利用率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前混合架构LLM（全局注意力+滑动窗口/SSM层）成为开源大模型主流，现有服务系统静态分配不同类型缓存的HBM空间，容易出现一类缓存不足另一类闲置的资源浪费问题；同时CPU-GPU高速链路在解码阶段带宽大量闲置，未利用混合模型的层间计算间隙做KV传输，限制了长上下文Agent场景的服务吞吐量和延迟表现。

### 方法关键点
- 透明缓存池：基于CUDA虚拟内存API，在固定虚拟地址下动态调整物理页在全局KV、窗口KV、循环状态三类缓存之间的分配，无需修改上层注意力后端和KV缓存接口，无数据拷贝完成重分区。
- 缓存流控器：利用混合层的计算间隙，将全局注意力层的历史KV做层间流式预取，共享跨层的GPU插槽，仅保留新生成的KV在HBM常驻，通过双缓冲和图兼容握手机制实现传输与计算重叠，不破坏CUDA图的低启动开销。
- 请求调度器：根据队列状态和请求长度，动态选择请求走常驻KV还是流式KV，触发缓存池的容量调整，优先给阻塞的缓存组件分配空间。

### 关键实验
在GB300、GH200平台测试7种主流混合LLM配置，对比基线为带HiCache的SGLang：最高完成2.04倍的Agent turns，P50 per-token latency降低20%~59%，Agent P50 TTFT提升1.40~3.05倍；动态缓存池达到手工调优最优静态分区96.3%~113.6%的吞吐量，单步解码开销不超过6.3%。

### 核心结论
混合架构LLM的服务优化要同时利用内存空间的动态复用和CPU-GPU链路的闲置带宽，即可在不修改模型的前提下大幅提升长上下文Agent场景的服务效率。
