---
title: 'Δτ-Bench: Pushing Agents Toward a Moving Capability'
title_zh: Δτ-Bench：面向动态工具生态的Agent能力评测基准
authors:
- Shuofei Qiao
- Xuanguang Pan
- Yijun Chen
- Wendi Feng
- Bin Wu
- Runnan Fang
- Yuqi Zhu
- Shumin Deng
- Emine Yilmaz
affiliations:
- Zhejiang University
- University College London
arxiv_id: '2610.34238'
url: https://arxiv.org/abs/2610.34238
pdf_url: https://arxiv.org/pdf/2610.34238
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 动态工具生态适配与评测
tags:
- Agent Benchmark
- Tool Use
- Evolving Ecosystem
- Skill Maintenance
- Dynamic Provisioning
one_liner: 提出首个动态演进工具生态Agent评测基准Δτ-Bench及工具技能协同管理框架STEWARD
practical_value: '- 电商/企业内部Agent场景下，工具API迭代频繁时，可复用STEWARD的增量技能维护方案，仅更新工具变动对应的关联技能，无需全量重构技能库，降低维护成本30%+，同时避免旧技能失效

  - 做Agent工具调用模块时，不要单独做工具检索或技能召回，可借鉴协同供给机制，给Agent同时返回匹配的工具集合与对应的流程指导，能同时提升任务成功率和执行效率

  - 内部Agent效果验收时，可复用Δτ-Bench的IDR/DAR评测指标，除静态成功率外，额外评估工具升级/下线时的新路径发现能力与旧流程适配能力，避免业务迭代时Agent性能跳水'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测基准普遍基于静态工具生态假设，无法覆盖真实业务场景中工具持续迭代、下线、合并，重叠功能+噪声文档导致Agent既有工作流失效、错过更优执行路径的问题，也无法评测Agent的主动能力发现与知识动态更新能力。

### 方法关键点
- 构建Δτ-Bench：覆盖42个领域共1588个多轮可执行任务，通过1对1接口修改、1对多能力拆分、多对1流程合并三类能力保留变换，生成6个连续演进的工具生态状态，每个状态配套生成步骤最优、成本最优两条参考路径
- 提出STEWARD生态管理器：增量维护「规划技能-原子技能-工具技能」三层结构化技能库，跟踪技能与工具的依赖关系，工具迭代时仅编辑关联技能；任务执行时协同提供匹配的工具集合与流程指导，出现能力缺口时动态补充资源

### 关键结果
现有最强模型在Δτ-Bench上任务成功率仅42.3%，步长/成本效率SPE不足30%；现有技能学习方法的初始性能增益无法在生态演进时持续保留，部分版本性能低于无技能基线。STEWARD相比最优基线平均SR提升2.68pct，技能维护成本降低20%~82%，新路径发现率IDR平均提升4pct，退化场景适配率DAR平均提升5pct。

### 核心结论
工具与流程知识是高度耦合的依赖资源，必须协同管理才能让Agent在动态业务生态中持续保持高效执行能力
