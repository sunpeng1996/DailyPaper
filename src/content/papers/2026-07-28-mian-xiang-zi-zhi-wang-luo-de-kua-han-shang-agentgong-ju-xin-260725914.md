---
title: Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous
  Networks
title_zh: 面向自治网络的跨厂商Agent工具信任管理标准化方案
authors:
- Ravi Kant Sharma
- Ashutosh Uttam
- Ajay Kumar
affiliations:
- Ericsson
arxiv_id: '2607.25914'
url: https://arxiv.org/abs/2607.25914
pdf_url: https://arxiv.org/pdf/2607.25914
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent工具跨域信任管理标准化
tags:
- Agent-Trust-Management
- 3GPP-Standard
- Autonomous-Network
- Trust-Propagation
- Multi-Vendor-System
one_liner: 提出兼容3GPP标准的AgentToolMO信息模型，实现跨厂商Agent工具信任互通与风险收敛
practical_value: '- 跨域/跨部门工具调用的信任管理可复用梯度状态机设计：将工具信任分为Learning/Trusted/Monitored/Restricted/Revoked五级，替代二元授权/封禁决策，降低误判对业务的影响，同时设置最小
  dwell time 避免状态频繁振荡

  - 依赖链风险传播可复用阻尼衰减机制：对调用链下游的信任惩罚按距离指数衰减，设置最大传播深度，既做到风险透传又避免雪崩式级联封禁，保证风险收敛性

  - 故障影响回溯可复用依赖图遍历方法：工具出问题后沿调用链回溯指定时间窗内的所有调用记录，精准定位受影响的业务实体，避免全量回滚的额外成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
自治网络L4-L5阶段AI Agent需要跨厂商边界无人工干预调用工具，但现有管理标准缺乏跨厂商信任状态透传机制，单一厂商的工具故障会导致其他厂商的Agent无感知持续调用，引发数小时级的级联服务故障，且多厂商两两对接需要O(n²)的定制化开发成本。

### 方法关键点
- 提出兼容3GPP NRM规范的AgentToolMO信息模型，新增工具身份、生命周期、信任属性等标准化管理对象，复用现有Management Services(MnS)接口实现跨厂商互通，对接成本降至O(n)
- 设计五级信任状态机，明确禁止从Trusted直接跳转到Restricted/Revoked等不安全跃迁，保证梯度管控的安全性
- 信任级联传播采用指数阻尼衰减机制，默认阻尼因子γ=0.5、最大传播深度3，从数学上保证风险收敛，避免级联风暴
- 配套基于NRM依赖图的回溯算法，支持配置时间窗，精准定位故障工具历史调用影响的业务范围

### 关键实验结果
多厂商拓扑仿真显示，标准化跨厂商通知将故障爆炸半径的 undetected 传播从小时级压缩到MnS通知交付的近实时水平，级联收敛在有限迭代内完成，通知开销跨厂商域呈亚线性扩展。

跨域多Agent系统的信任管理核心不是复杂的算法，而是标准化的状态表达、收敛的传播规则和兼容现有基础设施的落地路径。
