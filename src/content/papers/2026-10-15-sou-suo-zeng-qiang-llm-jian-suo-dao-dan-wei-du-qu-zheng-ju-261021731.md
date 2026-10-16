---
title: 'Retrieved but Not Read: Understanding Why Search-Augmented LLMs Fail to Use
  Available Evidence'
title_zh: 搜索增强LLM「检索到但未读取」证据使用失效问题研究
authors:
- Owen Walters
- Lihu Chen
- Francesca Toni
affiliations:
- Department of Computing, Imperial College London
arxiv_id: '2610.21731'
url: https://arxiv.org/abs/2610.21731
pdf_url: https://arxiv.org/pdf/2610.21731
published: '2026-10-15'
collected: '2026-10-16'
category: RAG
direction: RAG 证据使用失效分析与机制研究
tags:
- RAG
- Search-Augmented LLM
- Evidence Utilization
- Citation Faithfulness
- Temporal Knowledge
one_liner: 揭示搜索增强LLM依赖摘要不打开源页的失效模式及内部知识竞争机制
practical_value: '- 电商导购Agent、商品问答RAG系统中，针对时效性强的查询（价格、库存、促销规则），强制工具调用逻辑必须打开高相关源页，禁止仅依赖搜索摘要输出答案，可将过时信息错误率降低60%以上

  - 工程实现可直接复用验证过的trick：检索到源内容后，将用户原始Query重新拼接在源内容末尾再送入LLM生成，可恢复26.1%的证据使用失效case

  - 时效性强的推荐/问答场景（新品发布、大促规则更新），优先将关键证据直接注入Prompt上下文，不要让LLM自主决策是否打开源页，可将主流开源LLM的过时答案错误率从20%+降至5%以内'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
搜索增强LLM已广泛用于时效敏感场景，但即使检索到最新相关证据，仍常输出过时答案、引用与结论矛盾的来源，现有研究多聚焦检索准确率提升，对模型为何无法有效使用已有证据的机理研究不足，直接限制RAG系统在电商、金融、医疗等场景的落地可靠性。

### 方法关键点
- 构造225条模型训练cutoff后发生变更的跨领域时序事实集（覆盖体育、金融、FDA药品、高管变动等6个领域），每条明确标注过时值、当前值，可精准判定答案时效性与引用忠实度
- 测试两种场景：1个闭源模型的原生搜索流程，6个开源/半开源模型的受控检索流程（所有模型拿到完全相同的10条固定搜索结果，统一开放搜索、开页、页内查找工具）
- 结合行为层面的工具调用轨迹分析，与logit lens、J-lens层间探针技术，拆解证据使用失效的外显模式与内部机理

### 关键结果
- 原生搜索场景下53.6%的请求仅依赖搜索摘要不打开源页，这类请求的过时答案、不忠实引用率达6.4%，是打开源页并引用场景的3~5倍
- 直接将源页内容注入Prompt时，gemma-4-31b、gpt-oss-20b的过时答案错误率从28%、23%降至0和2%；在返回开页结果后重述完整用户Query，可恢复26.1%的失效case
- 层间分析显示：即使失效case中模型已在中间层识别到最新检索证据，最终输出层仍会被过时的参数知识覆盖，核心原因是旧知识未被充分抑制

> 最值得记住的结论：RAG系统的可靠性瓶颈不止在检索准确率，更在模型对检索到证据的有效使用，仅依赖摘要不读取源页是当前最容易优化的共性失效点。
