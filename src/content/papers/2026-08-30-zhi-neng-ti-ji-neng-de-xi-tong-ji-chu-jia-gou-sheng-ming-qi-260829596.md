---
title: 'Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle,
  and Security'
title_zh: 智能体技能的系统基础：架构、生命周期与安全框架
authors:
- Sanket Badhe
- Deep Shah
- Priyanka Tiwari
- Nehal Kathrotia
affiliations:
- Google LLC
- Purdue University
arxiv_id: '2608.29596'
url: https://arxiv.org/abs/2608.29596
pdf_url: https://arxiv.org/pdf/2608.29596
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 技能模块化架构与生命周期治理
tags:
- Agentic Skill
- LLM Agent
- Skill Lifecycle
- Agent Security
- Modular Agent
one_liner: 形式化Agentic Skill六元组抽象，建立覆盖全生命周期的技能系统参考架构与安全防护体系
practical_value: '- 可复用Agentic Skill六元组（A/I/C/T/π/E）抽象，把电商推荐/营销Agent的常用操作（如用户偏好查询、商品检索排序、优惠券发放流程）封装成可复用的模块化技能，避免每次任务都重新生成执行逻辑，降低推理成本和出错率

  - 参考9阶段技能生命周期设计，搭建业务Agent技能库的全流程管理体系：从对话/执行轨迹中自动合成新技能，经过单元测试/LLM评审/HITL三道校验后入库，定期按实用度淘汰冗余技能，避免检索污染

  - 落地技能安全防护时，采用「元数据先验校验+沙箱执行+权限最小化」机制：技能激活时先校验其工具集合是否属于当前上下文允许的权限子集，防止越权操作（如误调用用户隐私查询接口、超额发放优惠券）

  - 技能存储优先采用混合分层架构，轻量元数据（激活条件、适用场景）用向量库存储用于快速检索，完整执行代码/流程仅在激活时加载，降低上下文token消耗，提升Agent响应速度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent在长周期复杂任务下存在三大瓶颈：一是任务长度增加时性能骤降，早期执行错误会向下游传导且无法自修复；二是无知识沉淀机制，成功执行过的任务下次执行仍需重新推导，效率极低；三是现有解决方案存在缺陷：把执行逻辑放上下文会增加token成本，微调又跟不上工具、API、业务规则的快速迭代，亟需模块化、可复用、易迭代的技能抽象支撑Agent规模化落地。

### 方法关键点
- Agentic Skill被形式化为六元组抽象`s=(A,I,C,T,π,E)`，明确三大判定标准：封装模块化、动态晚绑定调用、可执行状态转换，清晰区分技能与普通Prompt、原子工具、工作流、episodic memory的边界
- 覆盖9阶段的技能全生命周期参考架构：自主发现、创作与表示、存储、动态检索路由、组合编排、执行与修复、终身适配、评估、安全治理，每个阶段给出业界现有方案的对比与选型建议
- 建立技能安全威胁taxonomy与防护体系，提出基于能力的权限校验规则：技能激活的前提是其声明的工具集合是当前上下文允许工具集的严格子集，从架构层面避免权限越界

### 关键结论
作为Agentic Skill领域的系统性梳理，覆盖超过60个现有技能相关系统的架构选型、优劣势与适用场景，总结出核心设计trade-off：技能的预执行可验证性越高，跨Agent框架的可移植性越低，需根据业务场景平衡两者。

### 核心洞见
模块化、可沉淀、动态调用的Agentic Skill是解决长周期任务可靠性与可扩展性瓶颈的核心范式，比单一的Prompt工程、工具调用架构更适合规模化落地。
