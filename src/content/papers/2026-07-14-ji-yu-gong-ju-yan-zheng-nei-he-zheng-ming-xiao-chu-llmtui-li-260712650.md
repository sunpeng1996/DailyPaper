---
title: 'Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM
  Hallucination in Empirical Inference via Tool-Attested Kernel Proofs'
title_zh: 基于工具验证内核证明消除LLM推理幻觉的证据锚定可验证智能体推理
authors:
- Junyu Ren
arxiv_id: '2607.12650'
url: https://arxiv.org/abs/2607.12650
pdf_url: https://arxiv.org/pdf/2607.12650
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 可验证推理与幻觉抑制
tags:
- Agentic Reasoning
- Hallucination Mitigation
- Tool Calling
- Formal Verification
- Lean 4
one_liner: 提出基于Lean4的EG-VAR智能体推理架构，通过工具验证内核证明消除LLM实证推理幻觉
practical_value: '- 高风险电商/广告场景可复用证据锚定逻辑，所有生成的营销文案、价格计算、商品参数说明必须绑定可溯源的商品/活动数据源，避免虚假宣传类幻觉

  - 智能体调用工具（如商品检索、订单查询、库存校验）的结果可引入形式化校验内核，仅内核验证通过的工具调用结论允许输出，显著降低工具调用结果错用风险

  - 可落地审计链路设计，所有无法验证的请求明确返回Abstain而非编造结果，同时留存全链路操作日志满足电商合规审核要求'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 动机
仅为LLM开放工具调用能力无法实现可控的实证推理：输出内容可能未锚定可信证据，推导逻辑也未经过严谨形式化校验，存在幻觉风险，无法满足高风险场景的可信要求。
### 方法关键点
提出EG-VAR架构，基于Lean 4构建工具调用范式，仅Lean内核有权限输出验证通过的结论，所有结论必须同时满足：1）推导起点是经工具认证的公理/可信数据源；2）全链路推理逻辑经内核形式化校验；未通过验证的请求明确返回Abstain，同时留存可复现的全链路审计轨迹。
### 关键结果
- TableBench 120条数值推理任务准确率100%，优于同工具基线的95%
- 5领域反事实压力测试源数据保真度保持100%，同工具基线仅80-90%，无工具基线仅50-80%
- Claude Sonnet语义转形式化错误率3.3%，Opus仅1.7%
