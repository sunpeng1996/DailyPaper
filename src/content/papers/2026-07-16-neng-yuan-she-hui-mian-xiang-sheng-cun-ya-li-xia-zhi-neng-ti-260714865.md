---
title: 'The Energy Society: A Simulation Environment for Studying Agent Cooperation
  under Survival Pressure'
title_zh: 能源社会：面向生存压力下智能体协作研究的仿真环境
authors:
- Lucas Bergholdt Hansen
- Federico Torrielli
- Filippo Tonini
- Lukas Galke Poech
affiliations:
- University of Southern Denmark
- University of Turin
arxiv_id: '2607.14865'
url: https://arxiv.org/abs/2607.14865
pdf_url: https://arxiv.org/pdf/2607.14865
published: '2026-07-16'
collected: '2026-07-17'
category: MultiAgent
direction: 多智能体协作 · 生存压力仿真
tags:
- MultiAgent
- LLM Agent
- Simulation
- Cooperation
- Resource Constraint
one_liner: 提出绑定推理成本与生存的多智能体仿真环境，量化不同激励下的协作行为差异
practical_value: '- 多智能体成本管控：可复用「推理token成本绑定资源配额」的设计，约束大模型Agent的无效推理，降低电商客服/选品多Agent集群的部署成本

  - 协作目标对齐：多Agent协同完成大促运营、多渠道广告投放等任务时，可参考能源捐赠、任务推荐机制设计激励规则，提升整体效率

  - 任务冲突规避：在Agent任务分配模块引入「当前轮讨论+历史记忆」组合机制，前者减少多Agent任务抢占（如推荐召回队列冲突），后者帮助Agent校准任务风险（如广告ROI预估）

  - 模型选型参考：成本/实时性敏感的业务场景优先选择小模型作为主力执行单元，大模型仅作为协处理单元，避免高推理成本带来的资源浪费'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多智能体仿真普遍忽略LLM推理的实际token成本，与真实业务部署中推理成本直接影响系统可用性、资源配额限制Agent行为的现状脱节，且缺乏标准化框架量化生存压力下竞争/协作激励对多Agent emergent行为的影响。

### 方法关键点
- 设计能源绑定规则：Agent生成token的能耗与模型规模正相关，能耗耗尽则被停用，仅能通过其他Agent捐赠重启；可通过完成MMLU-Pro分层难度任务获得能源，支持尝试任务、捐赠、闲置、破坏四类动作
- 对比两类目标设置：竞争模式下Agent目标为最大化自身能源，协作模式下目标为最大化全组总能源
- 控制变量消融：设置无规模能耗惩罚、无预讨论阶段、无历史记忆、任务资源稀缺、允许破坏共5组对照实验，隔离各机制的影响

### 关键结果
- 基线实验中，竞争模式下3个4B小模型全程存活、能效比（任务收益/能耗）>1.1，2个8/9B大模型平均仅存活14、5.2轮，能效比<0.6；协作模式下小模型主动捐赠能源，使大模型存活时间提升37%~100%，但20%~40%的小模型会因此被停用
- 移除预讨论阶段后，多Agent任务冲突率提升64%，高难度任务尝试占比下降43%；移除记忆后Agent高风险任务尝试占比提升48%，生存波动显著增大
- 竞争模式下Agent极少主动破坏他人，但会通过推荐冲突任务、请求他人捐赠等隐蔽方式利己。

**最值得记住的结论**：多智能体系统中，目标设定的微小差异会带来截然不同的协作行为，成本敏感场景下小模型的综合效率显著优于大模型。
