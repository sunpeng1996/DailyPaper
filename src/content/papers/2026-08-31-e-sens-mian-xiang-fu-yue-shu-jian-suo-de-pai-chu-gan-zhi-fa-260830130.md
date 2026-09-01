---
title: 'E-SENS: Exclusion-Sensitive Penalization for Negative-Constraint Retrieval'
title_zh: E-SENS：面向负约束检索的排除感知惩罚方法
authors:
- Yerang Kim
- Jiyoon Myung
- Joohyung Han
affiliations:
- Independent Researchers
arxiv_id: '2608.30130'
url: https://arxiv.org/abs/2608.30130
pdf_url: https://arxiv.org/pdf/2608.30130
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: RAG检索优化 · 负约束检索重排
tags:
- Negative Constraint Retrieval
- Reranking
- Training-free
- Query Decomposition
- RAG
one_liner: 提出无训练的负约束检索重排方法E-SENS，通过查询分解减分规则降低排除内容召回
practical_value: '- 电商搜索/推荐的负约束场景可直接复用该架构：对用户明确排除的需求（如「连衣裙 不要雪纺」），拆解为正向目标和排除陷阱查询，对召回结果的相似度做β加权扣减，无需重训embedding模型，改造门槛极低

  - β参数可根据业务场景灵活调优：负约束容忍度高的场景用β=0.1~0.2，仅损失<0.4%召回即可降低19%+违规召回；对合规、儿童内容推荐等负约束敏感场景用更高β，优先保障排除内容不被召回

  - Agent工具调用的检索环节可复用该方法，处理用户明确排除的需求（如「找2024年后的论文不要综述」），避免违规内容进入LLM上下文导致生成错误'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前密集检索模型无法区分查询中的包含与排除语义，用户明确要求排除的内容常因语义相似被高召回，进入RAG的LLM上下文后会导致生成结果违反用户约束；现有方案大多需要重训检索模型或修改embedding，不适用于文档embedding预计算、闭源embedding API的业务场景。

### 方法关键点
- 无训练的推理端重排架构，不改动检索索引、文档embedding和底座检索模型，仅修改最终排序分数
- 用轻量LLM（如GPT-4o mini）将带负约束的原查询拆解为两个子查询：q_target（保留正向需求，移除排除规则）、q_trap（仅包含要排除的实体/概念/属性）
- 最终得分公式为 `S(d) = s(d, 原查询) - β * s(d, q_trap)`，β为惩罚权重可灵活权衡召回与违规率，所有分数先做min-max归一化保证可比性

### 关键结果
在ExcluIR数据集3452条负约束查询、9万+文档上测试4款主流embedding模型（OpenAI text-embedding-3系列、Qwen3-Embedding系列），以β=0（原生检索）为基准：
- β=0.1时，平均召回波动仅±0.0014，平均违规率下降7.4%~10.6%
- β=0.2时，平均召回最多损失0.0038，平均违规率下降19.3%~21.7%
- β=0.3时，平均违规率下降29.7%~33.3%，仅最小的Qwen3-Embedding-0.6B出现0.0071的召回损失

> 最值得记住：带负约束的检索需求无需重训模型，仅通过查询拆解+分数惩罚即可在几乎不损失召回的前提下大幅降低违规内容召回率
