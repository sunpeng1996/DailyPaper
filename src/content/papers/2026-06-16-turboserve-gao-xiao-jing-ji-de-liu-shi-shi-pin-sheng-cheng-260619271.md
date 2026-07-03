---
title: 'TurboServe: Serving Streaming Video Generation Efficiently and Economically'
title_zh: TurboServe：高效经济的流式视频生成服务系统
authors:
- Youhe Jiang
- Haoxu Wang
- Haotong Bao
- Kai Jiang
- Jianfei Chen
- Jun Zhu
- Fangcheng Fu
- Jintao Zhang
affiliations:
- Shanghai Jiao Tong University
- Shengshu Technology
- Tsinghua University
arxiv_id: '2606.19271'
url: https://arxiv.org/abs/2606.19271
pdf_url: https://arxiv.org/pdf/2606.19271
published: '2026-06-16'
collected: '2026-07-03'
category: Other
direction: 流式视频生成 · 服务调度优化
tags:
- Video Generation Serving
- GPU Scheduling
- Autoscaling
- Session Migration
- Cost Optimization
one_liner: 首个面向流式视频生成的服务系统，联合调度会话放置与GPU扩缩容实现降本提效
practical_value: '- 长会话生成服务（如多轮Agent交互、长文本/多模态内容生成）可复用迁移感知的会话放置调度逻辑，跨GPU重平衡降低长尾延迟

  - 流量波动大的生成类服务（如大促期间生成式文案/商品视频生成）可借鉴负载驱动的GPU自动扩缩容机制，平均降GPU成本30%+

  - 会话状态管理可复用GPU-CPU卸载+NCCL跨GPU迁移的工程实现，解决长会话状态持久化与动态调度问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流式视频生成作为新兴长会话生成服务，需跨活跃/空闲期保留会话状态、分块输出满足低延迟要求，现有框架面临两大痛点：一是会话时长异构，长会话导致初始放置策略随时间劣化；二是用户需求时间异构，活跃会话数峰谷波动剧烈，易出现算力利用率低/延迟不达标矛盾。
### 方法关键点
将服务转化为在线调度问题，联合优化会话放置与GPU资源供给：1. 闭环调度包含两个核心组件：迁移感知放置控制器跨GPU重平衡会话降低延迟，负载驱动自动扩缩容控制器适配负载波动降成本；2. 工程实现合并块处理批化同GPU并发会话、GPU-CPU卸载支持会话挂起恢复、NCCL跨GPU迁移支持在线重平衡。
### 关键结果
基于生数科技生产trace测试，最多64张NVIDIA B300 GPU集群下，相比基线配置最坏分块延迟降低37.5%，GPU总运营成本平均降低37.2%
