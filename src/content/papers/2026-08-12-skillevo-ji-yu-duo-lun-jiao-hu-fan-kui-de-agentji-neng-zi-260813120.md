---
title: 'SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback'
title_zh: SkillEvo：基于多轮交互反馈的Agent技能自更新进化框架
authors:
- Qianxi Yan
- Chunrong Chen
- Jiuzhou Zhao
- Min Zhang
- Yongzhou Xu
- Xiaochuan Xu
affiliations:
- Tencent Cloud Andon
- Zhejiang University
arxiv_id: '2608.13120'
url: https://arxiv.org/abs/2608.13120
pdf_url: https://arxiv.org/pdf/2608.13120
published: '2026-08-12'
collected: '2026-08-21'
category: Agent
direction: Agent 技能持续自进化框架设计
tags:
- Agent Skill Evolution
- Multi-turn Interaction
- User Simulation
- Feedback Generation
- Controllable Governance
one_liner: 将多轮用户模拟从评估端点转为反馈生成器，搭配可控治理层实现Agent技能持续进化
practical_value: '- 多轮用户模拟改造方案可直接复用在电商客服、导购Agent的技能迭代中，将历史用户会话转化为自进化反馈信号，降低人工标注成本

  - 双锚点事实一致性校验+结构化治理方案，可解决RAG知识库迭代时的知识漂移、冗余膨胀问题，避免多轮更新后旧知识丢失、新知识冲突

  - 失败归因分类（知识缺口/能力限制/评估噪声）逻辑可套用到推荐系统badcase归因流程，过滤不可修复的噪声样本，提升迭代效率

  - 全闭环流程已在生产环境落地，可直接迁移到所有依赖领域知识库的用户-facing Agent场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能要么人工编写要么单轮生成，没有从交互失败中迭代的闭环；已有的闭环方案依赖单轮QA反馈，第一轮补完可见缺口后进化梯度就会衰减，多轮交互才会暴露的深层缺陷无法被捕捉，同时仅靠标量分数的治理只能拒退劣质候选，不能定位修复结构性问题，最终导致技能进化停滞甚至退化。

### 方法关键点
- **可信反馈生成**：将多轮用户模拟从评估端点改造成反馈生成器，从历史工单提取意图议程、行为事实、情绪轨迹重建约束型模拟用户；用意图状态机保证所有关键意图都被触达，双端正交评估分离模拟器失真和Agent技能缺陷，集体归因仅保留可修复的知识缺口作为进化梯度。
- **可控技能治理**：将技能视为结构化知识系统，双锚点（初始稳定版本S0+上一迭代版本St-1）校验事实一致性，硬约束阻止现有稳定知识丢失、新增事实错误；结构一致性软约束主动修复知识膨胀、引用断裂、事实过度泛化三类结构退化，避免梯度漂移。

### 关键实验
在腾讯云6类云服务、9个生产技能、98个参考文件的数据集上测试，对比基线包括初始人工技能、自反射进化、单轮QA驱动进化。最终SkillEvo的任务解决率（TSR）达81.8%，比初始技能提升51.8个点，比自反射方案高23.0个点，比单轮QA驱动方案高15.4个点；带治理层的情况下知识膨胀率仅2.8%，远低于无治理的16.2%，跨轮回归率逐轮下降。

### 核心洞察
持续技能进化的瓶颈既不是编辑能力也不是迭代次数，而是评估反馈能否持续提供可信的进化梯度。
