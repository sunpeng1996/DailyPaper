---
title: 'Firepool: Brokering Warm GPU Capacity for Agentic and RL Workloads at LinkedIn'
title_zh: Firepool：LinkedIn面向Agent与RL工作负载的暖GPU容量调度代理
authors:
- Ankit Goyal
- Santosh Jha
- Zhuo Zhi
- Youmin Han
- Cong Gu
- Chen Xie
- Animesh Singh
affiliations:
- LinkedIn
arxiv_id: '2611.10832'
url: https://arxiv.org/abs/2611.10832
pdf_url: https://arxiv.org/pdf/2611.10832
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: Agent工作负载GPU资源调度优化
tags:
- GPU Scheduling
- Agent Serving
- Warm Pool
- RL Training
- Resource Orchestration
one_liner: 面向Agent/RL短GPU任务，通过暖池复用将启动延迟从数十秒降至秒级，提10倍以上执行效率
practical_value: '- 做LLM4Rec/Agent工具调用等短GPU任务调度时，可复用owner-only暖池策略：同一会话的请求复用同一暖pod，冷启动延迟从20+s降至<1s，无需为每个请求创建新pod

  - 多业务线共享GPU集群可采用晚绑定设计：统一基础镜像，业务代码/依赖在任务启动时动态注入，避免暖池碎片化，暖命中率可提升至90%以上

  - 多租户GPU服务可借鉴零VRAM standby设计：同物理GPU上放置3个左右无CUDA上下文的空闲standby pod，跨租户/会话切换延迟从51s降至0.94s

  - 短任务GPU集群扩缩容采用队列驱动而非利用率驱动，配合keep-alive时长配置，可在保障延迟的前提下，暖池GPU占用仅为常亮池的50%'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent、RL工作负载多为秒级短任务（工具调用、rollout、验证），但GPU pod冷启动即使镜像已缓存也要20~35s，无缓存时需数分钟，启动延迟占比远超任务执行时间。现有方案要么静态占GPU导致严重idle浪费，要么跨任务无法安全复用暖资源，没有同时兼顾启动速度、资源利用率、任务隔离的落地方案。
### 方法关键点
- 晚绑定架构：同SKU的GPU pod共用统一基础镜像，任务启动时再动态注入代码、依赖、集群拓扑，避免暖池碎片化，不同任务可共享少量暖池
- 安全复用机制：pod仅复用上一调用方的任务，会话切换时自动退役pod，任务间强制校验重置进程树、显存、临时目录，避免状态泄露
- 零VRAM standby机制：同物理GPU上与active pod共存3个无CUDA上下文、不占显存的standby pod，跨调用方/会话切换时直接晋升standby为active，无需新建pod
- 队列驱动扩缩容：基于排队任务数而非GPU利用率做暖池扩缩，通过floor/ceiling/keep-alive参数平衡延迟与资源成本
### 关键结果
生产H200集群上，94.7%的pod请求命中暖池或standby；Agent、RL任务端到端速度比每任务新建pod快13×、10.8×；p90启动延迟从59.1s降至3.5s；跨会话切换延迟从51s降至0.94s；匹配任务间隔的keep-alive配置下，暖池GPU占用仅为常亮池的一半。
### 核心结论
当Agent代替人进入ML工作流循环时，资源调度延迟会成为每轮迭代的关键瓶颈，暖池复用是短GPU任务性价比最高的延迟优化手段
