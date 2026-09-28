---
title: 'EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language
  Models'
title_zh: EAServe：面向多模态大模型的编码感知解离式服务框架
authors:
- Kunxiong Zhu
- Zhihao Shu
- Hangyu Zheng
- Minghai Qin
- Miao Yin
- Gagan Agrawal
- Wei Niu
affiliations:
- University of Georgia
- Western Digital
- University of Texas at Arlington
arxiv_id: '2609.31551'
url: https://arxiv.org/abs/2609.31551
pdf_url: https://arxiv.org/pdf/2609.31551
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: 多模态大模型 · 推理服务优化
tags:
- MLLM serving
- disaggregated inference
- GPU resource allocation
- SM partitioning
- request scheduling
one_liner: 提出编码感知MLLM解离式服务框架，相同SLO下goodput较vLLM高1.7倍、Dynamo高4.3倍
practical_value: '- 部署多模态导购Agent、商品理解等MLLM服务时，可直接复用Poisson-gap微批次调度策略，无需手动调整批次超时参数，自动适配流量波动，平衡延迟与GPU利用率

  - GPU资源紧张的业务场景，可参考动态SM分区+Encode侧空闲算力卸载给Prefill的设计，无需新增硬件即可提升服务吞吐量30%以上

  - 多阶段推理服务的部署配置调优可复用HAS框架，先通过单阶段性能profiling剪枝无效配置，再用贝叶斯优化搜索最优参数，大幅降低手动调参成本

  - 电商多模态搜索的离线大规模商品特征编码任务，可借鉴负载自适应微批次设计，提升GPU利用率同时控制编码延迟波动'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前文本LLM解离式服务已将Prefill、Decode拆分到独立GPU池实现资源优化，但多模态大模型（MLLM）新增了Encode阶段，形成Encode-Prefill-Decode（EPD）三阶段流水线。现有方案要么不支持Encode阶段，要么将Encode作为独立透传服务，缺乏全链路调度，导致Encode GPU利用率不足10%，下游Prefill/Decode算力闲置，整体SLO达标率低，goodput难以提升。

### 方法关键点
- 核心思路：将Encode作为EPD流水线的全局控制点，设计两层协同架构：上层Hybrid Auto Selection（HAS）离线搜索最优部署配置，下层三个运行时机制动态适配在线流量
- HAS优化：先通过单阶段容量profiling剪枝存在明显瓶颈的GPU分配配置，再用TPE贝叶斯优化搜索GPU分配、Encode批次上限、Prefill卸载率的最优组合，搜索效率较随机采样提升数倍
- 运行时机制：Poisson-gap负载自适应微批次调度，自动根据流量调整批次下发阈值；赤字计数器路由实现精准的Prefill部分卸载，无额外调参；动态SM分区，按当前Encode批次大小动态分配GPU算力给Encode和本地Prefill，保障latency无干扰

### 关键结果
在8卡RTX 6000 Ada环境测试LLaVA-v1.6-34B（图像）、Qwen2.5-VL-32B（视频）、Ultravox-v0.6-27B（音频）三类MLLM，对比NVIDIA Dynamo、vLLM等主流基线，相同SLO约束下goodput最高比Dynamo高4.3×，比vLLM高1.7×，Encode GPU利用率从基线的10%提升至80%左右，P99 TTFT最高降低95%。

### 核心结论
多阶段推理服务的入口阶段是天然的全局调度控制点，通过入口侧的调度优化、空闲算力复用、配置自动调优，可在无额外硬件成本的前提下大幅提升全链路服务效率
