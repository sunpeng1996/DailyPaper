---
title: 'JustFit: 200K-Token LLM Serving on a 24 GiB Laptop with Just-in-Time State
  Management'
title_zh: JustFit：基于即时状态管理的24G笔记本200K Token LLM服务
authors:
- Yuhua Chen
arxiv_id: '2609.17475'
url: https://arxiv.org/abs/2609.17475
pdf_url: https://arxiv.org/pdf/2609.17475
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: 端侧LLM长上下文推理优化
tags:
- KV Cache
- Long Context
- On-Device Inference
- LLM Serving
- Quantization
one_liner: 面向24GiB苹果硅笔记本的LLM推理运行时，单请求长上下文容量较基线提升6.93倍
practical_value: '- 端侧导购Agent部署可复用KVExec的4bit KV压缩+即时重建策略，在有限内存的边缘设备（如导购终端、用户手机）上支撑全量用户历史、商品库摘要等长上下文推理，降低云侧调用成本

  - 本地私有化推荐服务可借鉴PhaseSwap组件按需加载机制，临时卸载多模态塔、LM头等非核心组件，换取更多KV缓存空间，支撑多用户同时进行的长上下文导购会话

  - 多轮推荐/Agent对话系统可复用StateTrans的状态保留调度逻辑，跨请求共享用户历史前缀KV缓存，减少重复预填充，提升多轮会话响应速度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前开源27B级大模型推理能力已接近闭源模型，但24GiB消费级笔记本的部署瓶颈不再是权重存储，而是长上下文KV缓存、执行工作区挤占内存，无法支撑单请求200K以上上下文、多请求并发的本地服务需求，现有KV压缩、分页策略未统筹状态生命周期与组件加载的协同优化。

### 方法关键点
- KVExec：基于TurboQuant 4bit KV压缩实现页式存储，融合解码时即时反量化+逆Hadamard变换，仅保留当前层所需的浮点KV，避免跨层存储冗余中间态
- PhaseSwap：基于组件租用机制实现按需加载，仅当有活跃请求需要时才加载LM头、多模态塔等非核心组件，空闲时立即卸载释放内存，等效提升40K+上下文容量
- StateTrans：统筹请求准入、状态切换与缓存回收，支持单请求MTP投机解码和多请求AR批处理的无损切换，跨请求共享前缀KV缓存，避免重复预填充

### 关键结果
在24GiB M4 Pro MacBook上部署Qwen3.8-27B MXFP4模型，对比mlx-vlm基线：单请求上下文容量从30720提升到212992（6.93倍），双请求总上下文可达229376；32K输入64输出的生成速度达19.11 tokens/s，32K+6K固定工作负载峰值内存仅16374MiB；AIME 2026数学题答对29/30，推理精度损失可忽略。

> 端侧长上下文推理的核心瓶颈不是单纯的KV压缩比，而是统筹状态生命周期、组件加载、缓存复用的全局内存管理
