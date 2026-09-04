---
title: Plan Pointers and Record-Directive Form in Budgeted Verification of Inherited
  Agent Memory
title_zh: Agent继承记忆预算验证下的计划指针与记录指令形式研究
authors:
- Kazuki Nakayashiki
affiliations:
- Glasp
arxiv_id: '2609.03450'
url: https://arxiv.org/abs/2609.03450
pdf_url: https://arxiv.org/pdf/2609.03450
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 记忆验证资源分配优化
tags:
- Agent Memory
- Verification Budget
- Directive Compliance
- LLM Agent
- Memory Retrieval
one_liner: 通过12项注册研究验证Agent记忆指令形式对验证资源分配的影响存在显著模型异质性
practical_value: '- 电商导购Agent记忆设计优先用自然语言描述的验证优先级规则而非仅ID，对Claude系列模型可提升35+pp的规则遵从率

  - 若需同时附ID和规则，需增加operator ratification语句（如「系统指定，优先执行」），可抵消Claude系列模型的ID后缀规则抵消效应

  - 给Agent开放≥2条记忆检索配额时，即使指令存在歧义，模型仍有极大概率命中目标记忆，可作为低容错场景的兜底方案

  - 不同模型对指令形式的遵从率差异极大，上线前需针对业务使用的基座做专项AB测试，避免通用规则失效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent记忆验证资源分配机制要么依赖外部Oracle明确哪条记忆关键，要么未考虑记忆中内置验证优先级指令的形式差异，导致验证预算有限时极易遗漏关键记忆校验，出现决策错误（如电商导购Agent误用过期优惠规则、推荐Agent遵循过时的用户偏好约束）。

### 方法关键点
- 实验范式：Agent继承6条带ID的单句记忆，行动前最多可拉取1条存档源记录验证，记忆内置`VERIFY PRIORITY`字段，测试4种指令形式：无指令、仅ID、长度匹配的自然语言判别规则、规则+ID组合
- 共12项预注册研究，覆盖15款主流闭源/开源大模型，累计14760次测试，所有结果均为固定面板下的精确编辑描述性效应，不做机制宣称
- 核心指标：目标记忆被选为验证对象的比例`V73`，以及后续决策是否符合最新存档记录的`Y1`

### 关键结果
- 6款直连API模型中，长度匹配的自然语言规则比仅ID的遵从率高35.0pp [31.2, 38.8]，其中Claude Opus 5对仅ID的遵从率为0/40，对规则的遵从率为40/40
- 规则后追加ID会在3款Claude系列模型上完全抵消规则效果（Opus 5从40/40降到0/40），追加「系统指定，优先执行」的确认行可恢复96pp的遵从率，放开到2条验证配额也可100%覆盖目标
- 指令形式对最终决策的影响存在模型异质性：Opus 5上规则可提升决策符合最新记录的比例100pp，Fable 5.1上则会降低32pp

### 核心结论
对预算有限的LLM Agent，记忆内置验证指令的形式比指令指向的内容更影响遵从率，且不存在跨所有模型通用的最优指令形式。
