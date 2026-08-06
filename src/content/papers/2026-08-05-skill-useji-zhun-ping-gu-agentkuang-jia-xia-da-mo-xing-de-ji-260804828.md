---
title: 'Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?'
title_zh: SKILL-USE基准：评估Agent框架下大模型的技能调用能力
authors:
- Jinyi Han
- Yuanjian Xu
- Ying Liao
- Xinyi Wang
- Zishang Jiang
- Zixiang Di
- Fanyang Lu
- Zhichao Hu
- Yanghua Xiao
affiliations:
- East China Normal University
- Hong Kong University of Science and Technology
- Fudan University
- Tencent Hunyuan
arxiv_id: '2608.04828'
url: https://arxiv.org/abs/2608.04828
pdf_url: https://arxiv.org/pdf/2608.04828
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 技能调用能力评估
tags:
- Agent
- LLM
- Benchmark
- Skill Invocation
- Evaluation
one_liner: 提出覆盖9领域79个真实技能的SKILL-USE基准，拆解三维度评估Agent技能调用能力并揭示瓶颈
practical_value: '- 搭建电商/运营类Agent技能库时，技能的名称+短描述需尽量精准，优先给高频任务Agent预加载全量技能内容，可大幅提升触发率，避免渐进式披露的检索瓶颈

  - 评估自有Agent的技能使用能力时，可复用Trigger/Compliance/Boundary三维度拆分框架，无需仅依赖最终任务成功率，可精准定位是触发、执行还是越界的问题

  - 若Agent的Skill-Use（SU）得分低于0.5，不要贸然上线技能库，该场景下调用技能反而会比无技能的基线任务完成率更低

  - 技能库扩容到10个以上时，触发率不会持续线性下降，主要失败原因是未触发任何技能而非选错技能，可新增兜底触发规则优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent已广泛依赖结构化技能完成复杂任务，但现有评估要么仅关注技能本身质量、要么仅看最终任务成功率，完全未覆盖渐进式披露（仅给技能名+短描述，需主动检索完整流程）场景下，Agent主动识别、检索、正确使用技能的全流程，也无法定位技能使用的具体瓶颈。

### 方法关键点
- 将技能使用拆解为三个独立维度：Trigger（是否主动检索到正确技能）、Compliance（是否严格遵循技能规定流程）、Boundary（是否规避技能禁止操作），组合为 gated SU 得分，仅触发正确技能后才计算执行分
- 构建SKILL-USE基准，覆盖9个领域79个真实社区技能，对应177个可执行任务，所有任务在Docker沙箱运行，基于全执行轨迹打分，剔除不用技能也能完成的通用要求，保证评估的是纯技能使用能力
- 测试8个主流SOTA大模型，分别在Claude Code和Codex两个Agent框架下运行，对比不同技能注入方式、技能库大小对效果的影响

### 关键结果
当前最优配置（GPT-5.5 + Claude Code）的SU得分仅0.613，技能使用能力远未达可用水平；触发和流程合规是两个独立瓶颈，很多模型能合规执行但触发率极低，或能触发但执行不符合要求。技能预加载最多可提升弱触发模型SU得分0.24，但触发后执行质量几乎不变，检索是渐进式披露的核心瓶颈。技能库从1个扩容到10个时触发率明显下降，继续扩容到30个降幅很小，主要失败原因是未触发任何技能而非选错技能。SU得分低于0.5时，调用技能反而会降低任务完成率，超过0.5才会带来正向收益。

最值得记住的结论：Agent的技能使用能力是模型和框架共同决定的，不是大模型的固定属性，单一框架下的模型排名无法迁移到其他框架。
