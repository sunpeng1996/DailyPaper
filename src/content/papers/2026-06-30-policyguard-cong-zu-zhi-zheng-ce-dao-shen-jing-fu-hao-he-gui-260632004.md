---
title: 'PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review
  Engines'
title_zh: PolicyGuard：从组织政策到神经符号合规审核引擎
authors:
- Sameer Malik
- Ayush Singh
- Amar Prakash Azad
arxiv_id: '2606.32004'
url: https://arxiv.org/abs/2606.32004
pdf_url: https://arxiv.org/pdf/2606.32004
published: '2026-06-30'
collected: '2026-07-02'
category: LLM
direction: LLM · 神经符号合规审核
tags:
- Neuro-Symbolic
- LLM
- Compliance Review
- Policy Grounding
- Rule Engine
one_liner: 神经符号框架PolicyGuard将组织政策转化为可执行规则引擎，实现可解释可维护的合规审核
practical_value: '- 电商/广告合规场景可复用该架构：将平台合规政策拆解为原子级规则+抽取问题，LLM做局部信息抽取，符号引擎做规则判断，比端到端Prompt准确率更高、可解释性强，适合广告文案、商品详情页合规审核

  - Agent任务的合规校验模块可参考该设计：把Agent操作的内部约束拆解为可执行逻辑规则，每次执行后调用LLM抽取关键参数再做符号校验，大幅降低Agent幻觉导致的违规风险

  - 规则迭代效率显著提升：政策更新时只需修改符号规则无需重新微调LLM，适合平台规则频繁迭代的电商、广告业务场景，降低运营成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
端到端Prompt驱动的LLM政策合规审核逻辑隐式，决策结果不可解释、难更新、难测试，企业文档合规审核依赖专家人力，规模化落地成本高。
### 方法关键点
1. 神经符号框架PolicyGuard先将组织政策转化为带类型的关系逻辑规则+原子级抽取问题集合，生成可执行审核引擎；
2. 审核时先召回目标文档的相关证据片段，调用LLM回答原子抽取问题，再用符号评估器执行预定义规则，输出合规结论和违规依据。
### 关键结果
在企业定制化NDA（保密协议）合规审核场景完成验证，相比端到端LLM方案，审核决策可解释性、规则可维护性、系统可测试性均有显著提升，无需重新微调即可快速适配政策更新
