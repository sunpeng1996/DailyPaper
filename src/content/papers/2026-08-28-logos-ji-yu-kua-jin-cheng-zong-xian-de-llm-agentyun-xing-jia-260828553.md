---
title: 'Logos: An Agent Harness on a Cross-Process Bus'
title_zh: Logos：基于跨进程总线的LLM Agent运行框架
authors:
- Hanzhang Jia
- Liheng Zeng
- Hao Cheng
- Yi Gao
- Bo Ma
affiliations:
- University of Sussex
- Zhejiang Gongshang University
- Shanghai Shuyuan Information Technology Co., Ltd.
arxiv_id: '2608.28553'
url: https://arxiv.org/abs/2608.28553
pdf_url: https://arxiv.org/pdf/2608.28553
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: LLM Agent 分布式运行基础设施
tags:
- LLM Agent
- Fault Tolerance
- Distributed System
- Cross-Process
- Plugin System
one_liner: 提出基于ROS架构的跨进程LLM Agent运行框架，解决单进程架构单点故障问题，支持故障无感恢复
practical_value: '- 对于电商多Agent导购、广告投放Agent集群，可复用跨进程隔离设计，单Agent节点故障不影响其他会话，大幅降低全链路故障率

  - 可复用append-only transcript的状态持久化方案，故障恢复时仅重放未记录步骤，避免重复执行已完成的下单、扣券等敏感操作

  - 多语言工具集成方案可直接复用，不同语言开发的召回、排序、权益计算工具可作为独立节点挂载总线，无需统一技术栈

  - 热插拔工具设计可用于推荐系统的AB实验，新的召回/排序插件可在线挂载/下线，无需重启整个Agent服务，降低实验成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有单进程Agent框架（如LangGraph、AutoGen）将所有插件、会话、状态托管在同一进程内，存在单点故障、重启影响全服务、多语言兼容差三大问题，单进程故障会导致所有在跑会话中断，插件升级需要全服务重启，无法满足电商、广告等生产环境高可用要求。
### 方法关键点
- 基于4个核心引理扩展时空可组合性演算到跨进程场景：LLM推理天然无状态、跨步骤状态可外置到持久化存储、各组件故障恢复无需协同、依赖解析可外置到路由表
- 参考ROS架构设计跨进程总线：每个插件/Agent/工具都是独立进程，路由器仅维护路由表不持有业务状态，唯一共享状态是全局append-only的transcript日志
- 故障恢复采用cold switching机制：进程挂掉后新进程直接从transcript重建会话状态，已记录的操作不会重复执行
- 天然支持多语言，Python/Go/Node.js开发的节点只要符合协议即可挂载到总线
### 关键实验
对比单进程Agent框架作为baseline：
1. 80个会话在工具调用全周期4个kill点测试，100%恢复且无重复执行
2. 总线单次跳数延迟中位数0.215ms，仅为LLM首token延迟的1/823，对业务无感知
3. 单进程框架下1个节点故障会中断所有共驻会话，Logos架构下故障仅影响单个节点，其余服务零冻结
4. 路由器进程kill后恢复中位数仅858ms，所有会话不受影响
### 核心结论
LLM推理的天然无状态特性是Agent系统做分布式高可用改造的核心前提，仅靠业务状态外置到append-only日志就能实现极低复杂度的故障无感恢复
