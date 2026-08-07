---
title: 'LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm'
title_zh: 面向突发工作负载的LLM推理：改进WAIT调度算法
authors:
- Anjali Gangadhar Katageria
- Shobha Rani
- Raghu Nandan Sengupta
affiliations:
- Indian Institute of Technology Dharwad
- Indian Institute of Technology Kanpur
arxiv_id: '2608.06135'
url: https://arxiv.org/abs/2608.06135
pdf_url: https://arxiv.org/pdf/2608.06135
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM推理 · 突发负载调度优化
tags:
- LLM Inference
- Scheduling
- Bursty Workload
- WAIT Algorithm
- MMPP
- KV Cache
one_liner: 为WAIT调度算法新增轻量在线到达率估计模块，适配LLM突发负载，低偏移场景吞吐量优于vLLM等基线
practical_value: '- 生产环境LLM服务（如电商智能客服、Agent推理、生成式推荐prompt处理）遭遇突发流量时，可复用本文的EMA+Savitzky
  Golay滤波的在线到达率估计方案，动态调整调度阈值，提升GPU利用率与吞吐量

  - 做LLM服务性能压测时，可采用MMPP-2模型生成贴合真实突发特征的流量，替代传统固定速率Poisson流量，压测结果更贴近生产实际

  - 若当前业务使用vLLM/Sarathi作为推理引擎，且流量波动幅度较小（低偏移场景），可替换为Modified WAIT调度算法，在延迟相当的前提下提升整体吞吐量

  - 该改造为轻量插件式，无需重构现有推理服务架构，适合中小团队快速优化突发流量应对能力，研发成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理调度算法（如vLLM、原始WAIT）大多基于固定速率Poisson请求到达假设，而生产场景（如电商大促客服、热点事件下的Agent推理请求）流量天然具有突发、时变特征，固定阈值的调度策略会出现batch过早/过晚生成、GPU利用率波动、吞吐量下降的问题，亟需适配动态流量的轻量调度方案。

### 方法关键点
- 采用双状态马尔可夫调制泊松过程（MMPP-2）建模突发流量，覆盖高低负载切换的真实请求特征，避免固定速率假设的失真
- 新增轻量在线到达率估计模块：通过滑动窗口计算请求到达间隔，结合EMA平滑、Savitzky Golay滤波降噪，实时估计当前请求到达率，无需先验流量分布，估计平均MAPE仅14.37%
- 动态调整WAIT算法的批处理阈值：阈值与实时估计的到达率成反比，流量高峰时降低阈值加快batch生成，低峰时提高阈值避免GPU空转，完整保留原始WAIT的内存优化与KV cache复用能力

### 关键实验
基于Vidur仿真框架模拟A100 GPU环境，用MMPP-2生成4种场景（低/高需求+低/高偏移）的合成流量，对比基线包括vLLM、ORCA、Sarathi、原始WAIT（已知全量流量分布的理想版本）。核心结果：低偏移场景下，Modified WAIT吞吐量显著高于vLLM、Sarathi，延迟与基线相当；性能接近已知全量流量的理想版原始WAIT，高需求高偏移场景下延迟甚至优于原始WAIT。

### 核心结论
无需先验流量分布的轻量动态调度调整，可在延迟相当的前提下显著提升突发流量下的LLM推理吞吐量。
