---
title: 'ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving'
title_zh: 面向Prefill-Decode拆分MoE服务的专家局部性感知解码路由ELDR
authors:
- Sangjin Choi
- Sukmin Cho
- Yifan Xiong
- Ziyue Yang
- Youngjin Kwon
- Peng Cheng
affiliations:
- KAIST
- Microsoft Research
- Shanghai Xingyunzhili Artificial Intelligence Institute
arxiv_id: '2607.00466'
url: https://arxiv.org/abs/2607.00466
pdf_url: https://arxiv.org/pdf/2607.00466
published: '2026-06-30'
collected: '2026-07-03'
category: LLM
direction: LLM服务 · MoE PD拆分路由优化
tags:
- MoE
- LLM Serving
- PD Disaggregation
- Decode Routing
- vLLM
- KV Cache
one_liner: 基于Prefill阶段专家激活特征设计感知路由，降低PD拆分MoE服务的生成时延TPOT
practical_value: '- 若业务使用MoE LLM做生成（如电商文案生成、Agent推理、推荐场景个性化生成）且采用PD拆分部署，可直接复用ELDR的「专家签名+离线均衡聚类+在线locality带路由」架构，在不改变模型输出的前提下降低TPOT
  5%以上

  - 块级绑定KV cache与专家签名缓存的设计可直接迁移到所有带前缀缓存的LLM服务场景，无需修改原有缓存逻辑，额外内存开销不到KV cache的1%

  - 做MoE模型服务负载调度时，不要仅以请求数/并发数为指标，需将每批请求激活的distinct专家数纳入核心调度维度，尤其是内存带宽瓶颈的decode阶段'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Prefill-Decode（PD）拆分的LLM服务架构中，decode侧路由仅做负载均衡，完全忽略MoE模型的核心特性：decode阶段时延由每批请求激活的不同专家数决定，而非仅由batch size决定；同领域/同语言请求激活的专家重叠度高，随机混部会大幅拉高专家权重加载的内存带宽开销。同时观测到Prefill阶段的专家激活和decode阶段的相关度高达0.7~0.92，存在可提前利用的路由信号。

### 方法关键点
- 专家签名设计：基于Prefill阶段每个专家的激活计数，用IDF加权降低通用专家权重、筛选高信号层，生成归一化的紧凑签名，签名距离可直接预测decode阶段的专家重叠度
- 离线路由规划：带均衡约束的K-means对签名空间聚类，每个decode worker对应一个聚类中心，保证各集群流量规模均衡，避免热点
- 在线路由：locality带路由策略，在与请求签名相似度落在阈值τ范围内的worker中选择负载最低的，同时保障专家locality和实时负载均衡
- 前缀缓存兼容：与KV cache块级绑定存储专家签名缓存，前缀命中时直接拼接缓存块的签名即可得到完整请求签名，无需重算

### 关键实验
在vLLM上实现，测试Qwen3-30B、GPT-OSS-120B、Gemma-4-26B三个主流MoE模型，覆盖多领域任务、多语言两类真实数据集，对比四类传统负载均衡baseline与基于领域标签的静态路由baseline：ELDR降低中位TPOT 5.9~13.9%，尾TPOT最多降低6.8%，额外开销仅占TTFT的1.2%，与前缀缓存的收益完全叠加。

最值得记住的结论：MoE decode阶段的核心时延瓶颈是每步激活的不同专家数而非batch size，利用Prefill阶段的专家激活信号做路由可以在零精度损失的前提下显著降低生成时延。
