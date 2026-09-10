---
title: 'GANDR: Claim Auditing for Verifiable Legal Answer Generation'
title_zh: GANDR：面向可验证法律答案生成的主张审计框架
authors:
- Chen Qian
- Yimeng Wang
- Yu Chen
- Lingfei Wu
- Andreas Stathopoulos
affiliations:
- William & Mary
- Anytime AI
arxiv_id: '2609.10293'
url: https://arxiv.org/abs/2609.10293
pdf_url: https://arxiv.org/pdf/2609.10293
published: '2026-09-09'
collected: '2026-09-10'
category: MultiAgent
direction: 多Agent 可验证RAG生成与引用审计
tags:
- Multi-Agent
- RAG
- Citation Verification
- Grounded Generation
- Hallucination Mitigation
one_liner: 双Agent隔离架构结合逐主张审计，提升高风险RAG生成的引用合规性
practical_value: '- 高风险RAG场景（电商合规话术、广告文案生成）可复用双Agent隔离架构：生成器与审核器使用独立KV cache上下文，避免审核被生成链路思维锚定，提升审核准确率

  - 结构化输出契约（如强制分块、引用标记规则）+ 正则预校验，可大幅降低大模型生成内容的格式/引用错误率，比纯LLM自检查成本更低、确定性更高

  - 逐断言级审计机制可直接迁移到营销文案、商品卖点生成场景：拆分到单句粒度匹配知识库依据，自动标记无依据主张，降低合规风险

  - 避免盲目堆叠多Agent调用：默认同上下文多Agent自校正反而会提升错误率，必须配套明确校验规则和隔离机制才能生效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高风险领域（法律、金融、电商合规）现有RAG生成方案采用整体评分，结论正确的答案也可能存在虚构引用、依据不匹配问题，单一严格指标不足以解决风险，可验证性需要内置到系统架构而非事后补校验；通用LLM在法律类开放问题幻觉率达58%-88%，商用RAG产品也有17%-43%的幻觉率，合规风险极高。
### 方法关键点
- 双Agent隔离架构：Drafter按CREAC结构化法律推理格式生成答案，所有主张强制带引用标记；Critic运行在独立KV cache上下文，仅能访问问题、检索片段、生成终稿，看不到Drafter思维链，模拟人类审核视角逐主张审计引用有效性
- 协议锚定提交规则：优先用正则做格式和引用有效性的结构化检查，通过即直接提交，98.6%的请求第一轮即可提交，Critic的审核结果仅作为审计trace留存，不触发不必要改写
- 严格正确性判定：答案不仅需结论正确，所有引用必须匹配检索返回片段，单个虚构引用即判定不合格
### 关键结果
在185条法律基准数据集上，与5个共享相同backbone、检索资源、引用指令的基线对比，GANDR严格准确率达70.8%，领先最强基线11.3个百分点（p<0.01）；移除协议锚定规则后严格准确率下降22.7个百分点；逐主张审计标记无依据主张的F1达0.84，与法律专业标注员对齐度高。
### 核心结论
多Agent的价值不在于盲目增加调用次数，而在于通过上下文隔离、结构化契约、确定性校验规则的组合，把可验证性内置到生成全链路。
