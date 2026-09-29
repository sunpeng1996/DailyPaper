---
title: 'Nereus: Adaptive Parallelism for LLM Post-Training'
title_zh: Nereus：面向LLM后训练的自适应并行调度框架
authors:
- Songlin Jiang
- Tuo Shi
- Sitong Zhang
- Zeke Wang
- Mario Di Francesco
- Bo Zhao
affiliations:
- Aalto University
- Shenzhen University of Advanced Technology
- Zhejiang University
arxiv_id: '2609.34645'
url: https://arxiv.org/abs/2609.34645
pdf_url: https://arxiv.org/pdf/2609.34645
published: '2026-09-27'
collected: '2026-09-29'
category: Training
direction: LLM训练 · 分布式自适应并行优化
tags:
- LLM
- distributed_training
- parallel_computing
- RLHF
- elastic_training
- GPU_cluster
one_liner: 提出成本感知的自适应并行runtime Nereus，大幅提升LLM RL后训练的吞吐与资源利用率
practical_value: '- 垂直领域LLM RL后训练（如电商文案生成、推荐多轮交互Agent对齐）可直接集成Nereus，相比现有框架可获得2~7倍的端到端训练效率提升，降低GPU资源成本

  - 其成本感知切换策略可复用在搜索推荐系统的弹性扩缩容场景，大促/平峰流量波动时评估扩缩容成本与收益比，避免无价值的调度调整

  - EMU状态抽象思路可复用在多模型协同的推荐/广告推理服务弹性调度中，将TP/PP逻辑封装在单元内，DP维度灵活扩缩，可降低状态迁移开销90%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM RL后训练（如RLHF、GRPO等）需要跨生成、推理、训练多阶段协调多个模型，运行过程中序列长度动态增长、GPU资源波动、阶段瓶颈漂移，静态并行策略要么提前预留资源造成浪费，要么后续OOM无法运行，现有弹性框架仅支持单模型或者checkpoint重启开销极大，未适配多模型多阶段耦合的RL后训练场景。

### 方法关键点
- 成本感知自适应策略：实时监控序列长度、GPU资源、内存压力等漂移信号，基于在线校准的成本模型判断切换收益是否覆盖迁移开销，仅当收益足够或者当前计划不可行时才触发切换
- 提出Elastic Model Unit (EMU) 状态抽象：将每个模型-阶段副本的TP/PP逻辑封装在单元内部，DP维度作为独立副本，通过Split、Merge、Extend、Destroy四个原语覆盖所有并行配置调整，无需全量重加载状态
- 安全并发迁移编排：将多模型多阶段的并行配置变更转化为全局迁移DAG，优先执行资源释放操作避免死锁，最大化并发状态传输效率，基于GPU direct RDMA降低数据传输开销

### 关键结果
- 对比OpenRLHF、Verl等主流RL后训练框架，8B参数PPO任务端到端吞吐提升2.14~7.27×（对比OpenRLHF）、1.10~1.47×（对比Verl）
- 真实漂移trace下，相比固定TP/PP配置平均步延迟降低27.7%；1000步扩展到1024 GPU的6次切换仅占总运行时间的0.079%
- EMU迁移比checkpoint重启快115~284倍，比单模型shard级迁移快3.8~16.2倍

### 核心结论
多阶段耦合的分布式任务弹性调度，核心是对齐状态边界与任务依赖，用成本收益判断替代盲目切换，可以用极低的overhead换来数倍的效率提升
