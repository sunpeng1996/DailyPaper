---
title: 'Evolving Infra: Agent-Adaptive LLM Serving at Scale'
title_zh: 面向大规模Agent场景的自适应LLM服务框架Evolving Infra
authors:
- Hao Kang
- Weili Xu
- Ziyang Li
- Zheng Du
- Hanchen Li
- Tian Xia
- Song Bian
- Tushar Krishna
- Huizi Mao
- Ion Stoica
affiliations:
- Georgia Institute of Technology
- University of Illinois Urbana-Champaign
- University of California, Berkeley
- NVIDIA
- OpenAI
arxiv_id: '2611.12304'
url: https://arxiv.org/abs/2611.12304
pdf_url: https://arxiv.org/pdf/2611.12304
published: '2026-11-08'
collected: '2026-11-12'
category: LLM
direction: LLM推理服务 · Agent适配优化
tags:
- LLM Serving
- KV Cache
- Prefill Decode Disaggregation
- Agent Workload
- Inference Optimization
one_liner: 解耦计算分配与KV缓存管理，实现Agent场景低延迟高吞吐的大规模LLM服务
practical_value: '- Agent服务端KV缓存优化可复用其按active branch引用计数的淘汰策略，替代LRU减少长等待Agent上下文误删，实测KV复用损失降低90%+，大幅降低TTFT

  - PD混部集群可借鉴对称引擎设计，节点无需重启即可切换prefill/decode角色，切换耗时从分钟级降到秒级，大幅提升集群弹性适配峰谷流量波动

  - 动态流量下的资源分配可复用其online迭代耗时模型+窗口增益校验的调优逻辑，避免突发流量触发无效切流，比基于队列深度的粗粒度调度提升20%+吞吐

  - 大模型推荐重排序、Agent导购等上下文复用场景可复用请求排队期间异步拉取远程KV的设计，隐藏IO延迟，降低端到端耗时'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent类LLM推理请求占比持续提升，传统prefill-decode（PD）分离的服务架构存在三大痛点：1）节点切换PD角色成本极高（分钟级重启+KV缓存丢失）；2）基于队列深度等粗信号的资源调度无法适配Agent workload在prefill/decode占比的动态变化，静态PD分流最高损失24%吞吐；3）LRU缓存淘汰策略无法感知Agent上下文管理（分支、压缩、子Agent），大量可复用KV被误删，TTFT升高明显。

### 方法关键点
- 解耦计算与KV管理：设计支持prefill/decode双角色的对称引擎，节点切换角色无需重启；构建跨节点共享的主机内存KV池，切换角色时KV不丢失，单节点切换耗时仅0.7s
- 自适应PD分流：在线学习prefill/decode迭代耗时模型，区分缓存/非缓存token精准估算算力需求，基于10分钟窗口的统计增益判断是否切换分流比，避免突发流量触发无效切换
- 感知Agent的KV管理：集群级KV目录跟踪每个缓存块被active branch的引用计数，优先淘汰无引用的缓存（压缩丢弃的上下文、结束的子Agent缓存等）；请求排队期间异步拉取远程KV，路由选择预测TTFT最低的节点，平衡负载与缓存命中率

### 关键结果
在36张GB300 GPU上测试coding、数学、计算机操作三类Agent workload，对比NVIDIA生产级框架Dynamo：静态负载下mean E2E latency最高降4.1×，P95 TTFT最高降14×，吞吐最高提2.73×；动态混合负载下mean E2E latency比最优静态分流低33%，比Dynamo低2.15×。

> 最值得记住的一句话：Agent场景下LLM服务的核心优化方向是感知上层Agent的上下文管理逻辑，而不是仅依赖底层请求的统计特征
