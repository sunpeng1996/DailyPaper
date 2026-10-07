---
title: 'The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in
  Long-Term Agent Memory'
title_zh: Agent长时记忆检索可采纳性验证：解决正确记忆放错上下文问题
authors:
- Zi Wang
- Xingqiao Wang
- Emmanuel Addai
- Devika Ambekar
- Xiaowei Xu
affiliations:
- University of Arkansas at Little Rock
arxiv_id: '2610.07309'
url: https://arxiv.org/abs/2610.07309
pdf_url: https://arxiv.org/pdf/2610.07309
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent 长时记忆检索可采纳性验证
tags:
- Agent Memory
- Retrieval Admissibility
- RAG Governance
- Long-term Memory
- Audit Framework
one_liner: 提出三值决策+匹配召回边界+ID全链路追踪的Agent长时记忆检索可采纳性验证框架
practical_value: '- 做电商多租户Agent/个性化推荐RAG时，优先在检索前加用户/租户namespace预过滤，可将Top20记忆召回提升0.101，同时减少98%的相似度计算量，兼顾效果和效率

  - 记忆准入校验不要仅依赖文本相似度，需额外增加主体归属、合规政策、生命周期状态三个维度的校验，同时保留unresolved标识避免误删必要证据，适配电商用户隐私、订单状态等动态合规场景

  - 落地时需实现记忆ID全链路追踪，覆盖存储、召回、Prompt注入、答案生成全环节，可快速定位隐私泄露、违规信息使用等问题，满足合规审计要求

  - 不要使用纯文本LLM做记忆准入校验，实验显示其在1%必要证据误拒率限制下完全无法检出违规，优先用结构化元数据做确定性规则校验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent长时记忆系统仅考核召回相关性与最终答案准确率，完全无法检出「语义相关但上下文不合规」的记忆错误：比如属于其他用户的隐私数据、已过期的订单/优惠状态、用户明确要求遗忘的信息，即使能匹配query语义也不能被使用，这类错误会导致隐私泄露、结果错误等严重业务风险。
### 方法关键点
1. 定义三值（合规/不合规/待确认）可采纳性判定规则，从主体归属、政策权限、生命周期状态三个维度做强 Kleene 与运算，与语义相关性完全解耦；
2. 采用匹配召回边界评估方案，在相同的证据召回率要求下对比不同检索链路的风险，避免低召回链路因返回信息少假装更安全；
3. 实现记忆ID全链路追踪，从存储、召回、Prompt注入到最终答案披露全环节绑定ID，可精准定位违规泄露的具体环节。
### 关键实验
在RHELM、MemOps两个公开长时记忆基准共3767个query上测试，对比全局检索基线：
- 信任域（namespace）预过滤方案将Top20锚点召回从0.432提升至0.533，80%召回的可行性从0.237提升至0.311，相似度计算量减少98.3%；
- 结构化元数据规则校验可在不损失证据召回的前提下过滤违规记录，而GPT-5.6、Gemini等纯文本校验器在1%必要证据误拒率要求下完全无法检出违规。
### 核心结论
记忆的相关性只回答「能不能回答问题」，可采纳性才回答「能不能用这个信息回答问题」，二者是完全独立的评估维度。
