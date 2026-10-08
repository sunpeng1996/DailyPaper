---
title: 'Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for
  Regression Testing'
title_zh: 可复现的LLM推理基准测试：面向回归测试的顺序隔离协议
authors:
- Arnold Olympio
- Juan Manuel Servera Bondroit
- Wael Abdelmalek
- Guang Lu
- João Carvalho
affiliations:
- Lucerne University of Applied Sciences and Arts
- Microsoft
- Uthereal AG
- ETH Zurich
arxiv_id: '2610.09778'
url: https://arxiv.org/abs/2610.09778
pdf_url: https://arxiv.org/pdf/2610.09778
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: LLM推理 · 可复现基准测试
tags:
- LLM Inference
- Benchmarking
- Reproducibility
- Regression Testing
- Tail Latency
- Cost Analysis
one_liner: 提出顺序隔离基准测试协议，将LLM推理性能测量变异系数从15.2%降至2.2%
practical_value: '- 做LLM服务性能回归测试时，可直接复用顺序隔离协议的工程trick：按上下文长度重启服务、单配置顺序测试、每轮间隔10s、前置30s预热，将测量变异控制在3%以内，避免性能对比误判

  - 部署7B量级开源LLM做电商客服、商品文案生成、Agent推理服务时，可参考A100 + vLLM栈的性能数据：200并发内是稳定区间，超过500并发时延飙升133倍，提前做容量规划避免生产故障

  - LLM服务选型时可参考实测性能结论：低并发短上下文选Qwen2.5-7B压长尾，8k上下文选Llama3.1-8B，高并发吞吐量优先选Mistral-7B，减少选型测试成本

  - LLM服务成本核算时可复用给出的盈亏模型，结合业务token量级判断是调用API还是自托管更划算，单A100月吞吐2.88亿token远低于API盈亏阈值，小流量场景优先用API更省钱'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理基准测量变异大（平均15.2%），无法区分模型、框架、配置的真实性能差异，导致容量规划、回归测试、部署决策不可靠，急需可复现的标准化测试协议。

### 方法关键点
- 顺序隔离协议采用四层迭代设计：从基线并发测试逐步增加控制，最终版本按「单模型-上下文长度」维度重启服务，同上下文下按并发等级顺序测试，每轮间隔10s，单轮前置30s预热期排除初始化波动
- 实验严格控制变量：固定硬件为Azure A100 80GB，软件栈为vLLM 0.9.1 + CUDA 12.4，测试3款主流7-8B开源LLM，覆盖6种上下文长度（1k-32k）、8种并发等级（5-1000用户），每个配置重复5次取P50 TTFT计算变异系数
- 配套提供基础设施即代码脚本、成本盈亏分析模型，支持实验复现与部署成本核算

### 关键结果
最终协议将平均变异系数（CV）从无控制基线的15.2%降至2.2%，78.5%的配置CV低于3%；实测A100+vLLM栈的性能拐点在200-500并发之间，500并发时P50 TTFT从91ms飙升到12068ms，涨幅133倍；7B量级模型性能对比显示Qwen2.5-7B平均P99 TTFT比Mistral低12.1%，200并发内Mistral吞吐量最高达48.5 tok/s；单A100自托管盈亏点为月处理3.7-14.9亿token，远高于单卡实测月吞吐2.88亿token。

### 核心结论
LLM基准测试的核心价值是提供相对性能参考而非绝对生产性能预测，只有控制测量变异的对比结果才有决策意义。
