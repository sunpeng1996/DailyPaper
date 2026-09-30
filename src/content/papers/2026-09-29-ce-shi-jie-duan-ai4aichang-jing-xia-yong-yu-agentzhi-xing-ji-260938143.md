---
title: Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI
title_zh: 测试阶段AI4AI场景下用于Agent执行环境设计的元技能学习
authors:
- Cheng Qian
- Kunlun Zhu
- Beibin Li
- Zhenhailong Wang
- Heng Ji
affiliations:
- Apodex
- University of Illinois Urbana Champaign
arxiv_id: '2609.38143'
url: https://arxiv.org/abs/2609.38143
pdf_url: https://arxiv.org/pdf/2609.38143
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 元技能学习与执行环境优化
tags:
- Meta-Skill
- AI4AI
- Agent Harness
- Test-Time Learning
- Agent Self-Improvement
one_liner: 在模型权重固定的测试阶段AI4AI场景下，通过Builder学习可复用元技能构造执行环境提升目标Agent表现
practical_value: '- 电商导购/选品/文案生成等业务Agent可复用「when-provide-use」三元组格式沉淀元技能，无需微调LLM权重即可将过往执行失败/优化经验转化为可复用的环境设计规则，快速迭代Agent能力

  - 推荐系统侧的Agent集群可采用Builder+Target双角色架构，由专门的Builder Agent基于元技能为每个任务生成定制化工具、验证逻辑、执行流程，避免直接给Target
  Agent投喂长prompt带来的推理负担与理解偏差

  - 需自迭代的业务Agent（如活动运营、用户服务Agent）可复用同模型自改进思路：同一模型同时承担Builder和Target角色，通过沉淀执行经验优化自身执行环境，在权重固定的前提下实现效果提升'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agent优化多聚焦模型权重微调或直接向目标Agent投喂技能prompt，忽略执行环境对Agent能力发挥的影响，测试阶段权重固定的场景下缺乏可复用的环境优化手段，无法将过往执行经验转化为结构化的支持能力，导致目标Agent的固有能力无法充分释放。
### 方法关键点
- 定义元技能为「when（触发条件）-provide（需提供的资源/能力）-use（使用规则与Target权责边界）」三元组，作为Builder设计执行环境的可复用原则
- 开发阶段Builder基于Target在开发集任务的执行反馈迭代更新元技能库，全程Builder与Target的模型权重均保持固定
- 测试阶段冻结元技能库，Builder针对每个新任务选取适配元技能，构造包含指令、内存、工具、执行控制、验证逻辑的定制化harness供Target执行
### 关键实验
在Harness-Bench（106个任务）、NewtonBench（324个任务）上验证，对比原生环境、无技能Builder、直接向Target投喂元技能等6类基线，全量元技能库方案相比无技能Builder的宏观平均表现提升8.95个百分点，相比直接向Target投喂同一份元技能库平均提升12.02个百分点；同模型同时承担Builder和Target角色时，相比无技能方案平均提升18.71个百分点。
### 核心结论
与其直接给目标Agent灌输大量技能prompt，不如让专门的Builder将经验转化为可执行的环境支持，降低目标Agent的推理负担，是权重固定场景下Agent优化的高效路径。
