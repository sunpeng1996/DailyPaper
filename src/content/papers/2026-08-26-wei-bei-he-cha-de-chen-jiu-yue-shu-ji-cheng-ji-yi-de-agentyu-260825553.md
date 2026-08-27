---
title: 'When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited
  Agent Memory'
title_zh: 《未被核查的陈旧约束：继承记忆的Agent预算验证失效问题》
authors:
- Kazuki Nakayashiki
affiliations:
- Glasp
arxiv_id: '2608.25553'
url: https://arxiv.org/abs/2608.25553
pdf_url: https://arxiv.org/pdf/2608.25553
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: Agent 记忆陈旧性验证优化
tags:
- Agent Memory
- Verification Budget
- Stale Constraint
- Provenance Path
- LLM Safety
one_liner: 固定验证预算下，将1个验证槽分配给关键来源路径可降低70%+的Agent陈旧记忆决策错误
practical_value: '- 开发电商导购、运营决策类Agent时，可给约束类记忆（如促销规则、库存限制、价保政策）标记高优先级验证位，固定分配1个验证槽检查其来源时效性，不额外增加预算即可降低70%+规则误用错误

  - 构建Agent记忆系统时，需单独设计freshness/supersession信号维度，不要和语义relevance绑定，避免语义相关的陈旧规则被漏检

  - 优化Agent验证策略时，可先统计各类型记忆的原生漏检率，针对性分配验证预算，对漏检率高的约束类记忆强制溯源，避免无意义的随机验证开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
带持久记忆的LLM Agent在继承历史沉淀的约束类记忆（如规则、限制、政策）时，其对应的源规则可能已被更新或废止，但推理阶段的验证预算有限，原生策略极少主动核查约束类记忆的来源有效性，会产生大量可避免的错误决策，现有研究未量化该场景下的错误占比与优化空间。
### 方法关键点
- 显式建模记忆的替代关系：历史来源记录不可篡改，仅标记当前生效的权威记录，单条记忆的溯源请求会返回全量历史版本及生效状态
- 控制变量实验设计：固定验证预算为2条记录，对比三种策略：原生分配、强制1个槽分配给关键约束的来源路径、强制1个槽分配给随机非关键记录
- 覆盖6个主流LLM（Claude Opus 5/Sonnet 5/Haiku 4.5、GPT-5.6 Sol/Terra/Luna）、2个业务场景（增长折扣、采购选商）、12种记忆表述，所有实验配置提前注册哈希确保可复现
### 关键结果
- 原生分配下仅约20%的episode会主动核查约束类记忆的来源，当约束已被废止时，74%~77%的决策会遵从陈旧记忆
- 相同预算下，强制1个槽分配给关键来源路径，符合当前生效规则的决策比例提升61.3~74.0个百分点，全模型全场景均正向生效；若记忆仍有效，该操作对决策无影响
- 修正跨域场景的上下文不一致问题后，提升幅度稳定在73.3个百分点，接近理论上限
### 最值得记住的一句话
Agent记忆系统需要独立于语义相关性的freshness、supersession信号，语义上越相关的陈旧约束，越容易被漏检
