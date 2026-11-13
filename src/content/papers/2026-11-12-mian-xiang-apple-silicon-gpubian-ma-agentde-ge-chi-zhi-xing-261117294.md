---
title: 'Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents
  on Apple Silicon'
title_zh: 面向Apple Silicon GPU编码Agent的隔离执行与命令调度框架Metal Sandbox
authors:
- Haozhe Wang
- Lina Chen
- Fanqi Wan
- Qi Han
- Yinmin Zhang
- Zheng Ge
- Daxin Jiang
- Junchi Yan
affiliations:
- 上海交通大学
- 北京中关村学院
- StepFun
arxiv_id: '2611.17294'
url: https://arxiv.org/abs/2611.17294
pdf_url: https://arxiv.org/pdf/2611.17294
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: 编码Agent · 集群资源调度
tags:
- Agent
- GPU Scheduling
- Resource Isolation
- Cluster Scheduling
- Apple Silicon
one_liner: 实现Apple Silicon集群多编码Agent的资源隔离、命令调度与跨节点迁移，提升GPU利用率
practical_value: '- 多Agent集群调度可借鉴「并行/串行命令拆分」思路：将GPU密集型、CPU密集型任务分队列调度，避免GPU资源抢占，可直接复用在LLM微调、生成式推荐离线素材生产等场景的集群管理中

  - 跨节点任务迁移的「预留-认领-提交」三阶段协议开销仅约1s，适合长耗时任务的负载均衡，可迁移到语义ID生成、RAG知识库构建等离线任务的集群调度设计

  - 基于系统原生沙箱的轻量实例隔离方案，比VM/容器性能损耗更低，可参考用于端侧推荐Agent、边缘Agent的执行环境设计'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Apple Silicon端侧推理依赖高效Metal kernel优化，用编码Agent生成kernel时，单Agent会话的GPU利用率仅2.32%，大部分时间消耗在模型请求、代码编辑等CPU侧操作，多Agent并发时GPU资源浪费严重。现有执行环境要么缺乏实例间文件隔离，要么不支持原生Metal GPU访问，缺乏适配Apple Silicon集群的多Agent调度基础设施。

### 方法关键点
- 基于Apple App Sandbox实现轻量实例隔离：每个Agent拥有独立工作区与私有环境，仅允许访问授权路径，原生支持Metal API调用，性能优于容器/VM方案
- 命令分级调度：将文件编辑、编译等CPU密集型任务归为并行命令直接执行，将GPU执行类任务归为串行命令进入单节点FIFO队列，避免GPU资源冲突
- 跨节点动态迁移：符合共享存储、无本地依赖条件的等待中串行命令，通过「预留-认领-提交」三阶段协议迁移到空闲节点执行，无需迁移运行时GPU状态

### 关键结果
在4台Mac mini M4集群上测试，对比无迁移的静态调度基线：
1. 集中负载场景下，2s短任务吞吐量提升1.68倍，6s长任务吞吐量提升2.05倍，p95队列等待时间降低45.5%
2. 16个编码Agent真实轨迹回放显示，动态调度平均工具等待时间降低18.8%，批次总耗时降低22.3%，单节点多Agent并发的持续吞吐量提升2.14倍

### 核心启示
多Agent集群的资源利用率提升，核心不在于复杂的全局调度，而在于按资源需求拆分任务、辅以轻量跨节点负载迁移，以极低开销盘活闲置硬件。
