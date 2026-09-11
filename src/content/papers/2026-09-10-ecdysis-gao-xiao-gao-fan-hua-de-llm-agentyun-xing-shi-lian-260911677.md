---
title: 'Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents'
title_zh: Ecdysis：高效高泛化的LLM Agent运行时Harness训练框架
authors:
- Ruiqing Yue
- Yu Cui
- Zhuoyu Sun
- Sicheng Pan
- Xianhong Xue
- Tingyu Li
- Ting Li
- Wenzhuo Zhu
- Yi Chen
- Yifei Liu
affiliations:
- Chinese Academy of Sciences, Chengdu Institute of Computer Applications
- University of Chinese Academy of Sciences
- Beijing Institute of Technology
- Beijing University of Technology
- Yangtze Delta Region Institute of Tsinghua University, Zhejiang
arxiv_id: '2609.11677'
url: https://arxiv.org/abs/2609.11677
pdf_url: https://arxiv.org/pdf/2609.11677
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 运行时Harness自进化优化
tags:
- LLM Agent
- Runtime Harness
- Self-Evolution
- Failure Diagnosis
- Multi-Agent Collaboration
one_liner: 通过跨任务失败聚合与多角色诊断优化Agent Harness进化，训练提速1.84×精度提升18.56%
practical_value: '- 做电商导购Agent、推荐系统执行框架迭代时，可复用跨失败案例聚合逻辑，避免针对单个查询/Case修改框架，减少过拟合提升跨场景泛化性

  - 多角色协同诊断的机制可直接迁移到Agent工作流缺陷排查场景，替代部分人工校验环节，降低迭代的人力成本

  - 训练数据选择可采用失败感知策略，优先筛选能暴露新执行路径的任务，仅需1/4训练数据即可达到全量训练效果，大幅降低Harness迭代成本

  - Harness优化时主动区分模型特性适配与框架级缺陷修复，减少模型绑定逻辑，一套Harness可适配多LLM，降低切换大模型的迁移成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent运行时Harness自进化方法依赖单失败实例迭代修改，一方面重复执行、代码修改带来极高训练开销，另一方面容易过拟合观测任务和特定失败模式，泛化到未见过的任务或其他LLM时性能显著下降，核心瓶颈是未对失败原因做归因，无法区分是模型本身缺陷还是Harness系统性问题，盲目修改会引入大量不必要的模型适配逻辑。
### 方法关键点
- 批级跨实例失败聚合：每轮迭代聚合多个任务的失败轨迹，将跨2个以上任务复现的失败模式判定为高优先级Harness系统性缺陷，大幅减少编码Agent调用次数
- 失败驱动协同精炼（FDCR）：设计分析师（定位缺陷提修改）、批评家（评估修改风险）、工程师（对齐共识）三个角色迭代分析失败模式，最终由仲裁者生成结构化Harness修改规范，再交给编码Agent实现
- 失败感知训练数据选择：优先筛选能暴露新执行路径、新Harness缺陷的任务，减少冗余失败信号，用少量数据即可完成训练
### 关键结果
在τ²-Bench的Airline、Retail子集和AgentBench上，对比Self-Evolution、人工优化Harness等基线，用5款LLM测试：训练速度最高提升1.84×，Harness推理精度平均提升18.56%，推理时token消耗降低12.19%，仅用1/4训练数据即可达到全量训练效果，训练好的Harness可直接迁移到未参与训练的LLM上，泛化性显著优于基线。
### 核心洞见
Agent Harness进化不要对单个失败直接修改，只有跨任务复现的失败模式才是可靠的框架级修复依据，能同时兼顾效率和泛化性
