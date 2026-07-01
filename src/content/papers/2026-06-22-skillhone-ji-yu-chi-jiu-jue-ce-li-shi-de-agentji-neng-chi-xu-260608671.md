---
title: 'SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent
  Decision History'
title_zh: SkillHone：基于持久决策历史的Agent技能持续进化框架
authors:
- Zhiwei Li
- Yong Hu
affiliations:
- WeChat, Tencent Inc., China
arxiv_id: '2606.08671'
url: https://arxiv.org/abs/2606.08671
pdf_url: https://arxiv.org/pdf/2606.08671
published: '2026-06-22'
collected: '2026-07-01'
category: Agent
direction: Agent 技能持续进化优化
tags:
- Agent Skill Evolution
- Continual Learning
- Multi-Agent
- Decision History
- LLM Agent
one_liner: 提出带角色分离子Agent、持久决策历史的Agent技能迭代框架，效果超越现有基线与商业深度研究Agent
practical_value: '- 电商/搜索推荐场景的Agent技能（如查询改写、商品导购、工具调用技能）迭代可复用持久决策历史设计，存储每次修改的诊断、证据、结果，避免重复踩坑降低迭代效率

  - 角色分离的子Agent设计可直接落地到内部技能优化流程，优化侧与评估侧权限隔离，评估仅返回脱敏失败报告，防止技能过拟合测试用例

  - 可直接复用GitHub式工作流（Issue记录故障、PR存修改、Merge记录结果）落地决策历史存储，无需重新设计底层存储结构

  - 重复度高的固定工具调用类业务场景（如运营数据分析、用户画像查询）可直接用该框架迭代技能，实测平均准确率提升可达18%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能优化方法仅在单次迭代内优化，最终只保留最优技能产物，丢弃了修改原因、失败尝试、评估证据等核心决策上下文，后续迭代时会重复验证已经失败的方案、无法快速适配环境变化（如API更新、业务规则调整），无法支撑长生命周期的Agent技能维护。
### 方法关键点
- 双仓库权限隔离架构：技能仓库存储可加载的技能包（含任务指令、执行脚本、参考资料、输出规范），评估仓库存储测试用例、验证器、执行轨迹等资产，优化侧仅能获取脱敏的失败报告，无法接触原始测试集
- 角色分离动态子Agent调度：优化侧子Agent负责故障诊断、技能修改、结果审核，评估侧子Agent负责技能执行、故障分析、脱敏报告生成，调度器仅负责消息路由与决策记录存储，不参与直接决策
- 结构化持久决策历史：每次迭代存储四元组（故障诊断、修改方案、评估证据、结果状态），后续迭代可直接检索历史决策，快速判断故障是否出现过、方案是否已验证，避免冗余尝试
### 关键结果
在GAIA、WebWalkerQA-EN公开深度研究基准上，无预集成搜索栈的前提下，比商业深度研究Agent分别高15.8分、3.2分，比现有最优技能进化基线Hermes-SE分别高14.2分、13.4分；内部7个工具介导分析场景平均准确率提升18.8分，生成的技能包可跨LLM backbone直接迁移，无需额外优化。
最值得记住的一句话：长生命周期的Agent技能核心资产不是单个最优产物，而是完整可追溯的决策历史，让后续迭代无需从零开始。
