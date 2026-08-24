---
title: 'Graph Engineering in the Era of LLM Agents: From Individual Intelligence to
  System Intelligence'
title_zh: LLM Agent时代的图工程：从个体智能到系统智能
authors:
- Yuyuan Feng
- Zhishang Xiang
- Chaobin Yang
- Qichao Ma
- Zerui Chen
- Yujing Zhang
- Ke Huang
- Chuanjie Wu
- Zhaoxu Liu
- Yili Wang
affiliations:
- 吉林大学
arxiv_id: '2608.21156'
url: https://arxiv.org/abs/2608.21156
pdf_url: https://arxiv.org/pdf/2608.21156
published: '2026-08-20'
collected: '2026-08-24'
category: Agent
direction: 多Agent系统 · 图工程协同范式
tags:
- Multi-Agent
- Graph Engineering
- System Intelligence
- LLM Agent
- Agent Coordination
one_liner: 系统性提出图工程范式，通过图结构实现多Agent协同的系统级智能
practical_value: '- 电商多Agent运营/导购系统可直接复用图工程三层架构：先将大促活动策划、用户全生命周期运营等复杂任务拆分为带依赖的子任务图，再匹配文案/选品/风控/投放等不同专长Agent，最后做全局状态管理，解决单Agent串行效率低、角色混淆的问题

  - 推荐系统全链路Agent化改造可借鉴任务组织模块的依赖调度逻辑，将召回/粗排/精排/重排各环节的Agent用有向图做并行调度、结果交叉校验，提升全链路吞吐和效果稳定性

  - 多Agent线上系统的运维可参考Runtime State Management方案，用图结构记录每步Agent的执行状态、输入输出、依赖关系，实现故障快速定位和局部回滚，降低线上事故影响范围'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
单Agent架构已无法适配复杂长周期任务的需求：这类任务需要异构专业能力、子任务并行执行、独立结果校验、持久状态维护，仅提升单Agent的上下文窗口或工具调用能力无法解决架构层面的 mismatch，而现有多Agent系统缺乏统一的组织范式，普遍存在协调混乱、效率低下、故障难排查、扩展性差的问题。
### 方法关键点
- Graph Engineering被作为系统级智能的核心范式提出，用显式、动态演化的图结构统一建模任务、Agent、系统状态三大核心要素，作为多Agent系统组织的统一基础
- 核心分为三大模块：任务组织（目标拆解、工作流优化，定义子任务的依赖、执行顺序/并行规则、校验条件）、Agent协同（Agent能力建模、团队拓扑组织、通信路由机制，实现子任务与专长Agent的精准匹配）、运行时状态管理（全链路状态记录、故障定位、异常恢复，支持执行进度跟踪、局部回滚、系统迭代进化）
- 系统性梳理了从模型智能→个体智能→系统智能的完整技术演进路径，配套上线开源资源库，收录数百篇相关论文、数据集、开源项目
### 关键结果
为综述类研究，无定制实验，梳理了近五年百余项Agent领域核心研究成果，开源资源库地址：https://github.com/DEEP-JLU/Awesome-Graph-Engineering
### 核心结论
系统智能的核心不是单纯增加Agent数量，而是用结构化机制统一组织任务、协调Agent、维护全局状态；个体Agent可抽象为 `Agent = Loop(LLM + Harness)`
