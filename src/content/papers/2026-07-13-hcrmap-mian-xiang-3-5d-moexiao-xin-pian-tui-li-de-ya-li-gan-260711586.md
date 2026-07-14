---
title: 'HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference'
title_zh: HCRMap：面向3.5D MoE小芯片推理的压力感知热专家驻留映射框架
authors:
- Yongqin Zhang
affiliations:
- Nanjing Vocational College of Information Technology
arxiv_id: '2607.11586'
url: https://arxiv.org/abs/2607.11586
pdf_url: https://arxiv.org/pdf/2607.11586
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: MoE LLM推理 · 3.5D小芯片架构优化
tags:
- MoE
- LLM Inference
- Chiplet
- Hierarchical Memory
- Dynamic Scheduling
one_liner: 提出双时间尺度压力感知热专家驻留映射框架，大幅降低3.5D架构下MoE推理端到端延迟
practical_value: '- 部署MoE-based推荐/Agent服务时，可借鉴热专家分层驻留思路：将高频调用的expert、热门商品Embedding、高频Prompt模板等资源按热度分层存储到SRAM、HBM、DRAM层级，减少反复加载的带宽开销

  - 可复用双时间尺度调度逻辑：慢路径做低频的热资源生命周期管理（升降级、副本扩缩），快路径做实时请求路由，平衡调度开销与资源利用率

  - 多维度压力感知的副本调度思路可迁移到热门广告/内容的服务实例调度：综合队列负载、链路带宽、存储压力分配请求，避免热点宕机'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MoE LLM推理时存在显著的专家热度倾斜：少量热专家承载绝大多数token请求，在3.5D多小芯片架构下，该倾斜不仅导致计算不均衡，还会放大通信、内存带宽、I/O、执行队列的压力。现有方案仅单独优化通信、副本复制或异构执行，未结合3.5D分层内存特性和多维度运行时压力，无法充分降低端到端延迟。
### 方法关键点
- 双时间尺度控制架构：慢路径用带可行性掩码的Double DQN做跨层专家驻留决策，根据专家热度、权重加载成本、迁移开销、资源压力决定专家的晋升、保留、降级、驱逐；快路径用归一化压力代理为每个token组选择最优专家副本，响应实时压力变化。
- 多维度压力感知：同时监控计算负载、链路、内存bank、层级容量、迁移五大类压力，避免单维度优化导致的其他资源瓶颈。
- 版本化目录与迁移限流：专家权重迁移采用分块拷贝、版本更新机制，避免影响前台请求，仅当链路空闲率达标时才执行迁移。
### 关键结果
基于LEGOSim仿真平台，在8个主流MoE模型（DeepSeekMoE、Mixtral、DBRX等）上对比3个业界基线：prefill阶段端到端延迟较Hydra、MoEntwine、PIMoE分别降低43.6%、34.5%、46.7%，decode阶段分别降低43.0%、33.1%、46.0%，EDP提升约20%。
> 核心启示：热资源管理的核心不是单纯减少通信或者最大化副本，而是在多维度资源约束下平衡长期收益与短期开销。
