---
title: 'Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in
  AI Contact Centers'
title_zh: 分阶段语言种子：AI客服验证单元问答的接地查询扩展方法
authors:
- Hyeonseop Yoon
- Jeong-Eun Park
affiliations:
- OpenMined
- MaumAI, Inc.
- Independent Researcher
arxiv_id: '2609.00844'
url: https://arxiv.org/abs/2609.00844
pdf_url: https://arxiv.org/pdf/2609.00844
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: 智能客服Agent · 离线索引扩展
tags:
- Query Expansion
- FAQ Retrieval
- RAG
- LLM Agent
- Offline Augmentation
one_liner: 通过离线分阶段人类接地槽位配方+LLM生成扩展FAQ索引，零推理代价提升召回消除RAG幻觉
practical_value: '- 电商智能客服、售后QA场景可直接复用SLS流程：离线为每个标准QA对编写世界接地槽位配方（如将“怎么查物流”拆解为[查询动作,
  物流类术语, 人称/语气变体]），调用低成本小模型生成问法变体后做轻量人工过滤，将变体加入索引，完全不增加推理时延，可大幅解决用户口语化、多样化问法的匹配难题

  - 对时延要求极高的语音客服、实时问答场景，可直接放弃带query-time生成的RAG架构，采用「检索预定义验证单元+返回标准答案原文」的方案，从构造上消除生成幻觉，实测可将无依据回答率从7-13%降至接近0

  - FAQ检索系统优化优先级：优先做离线索引扩展，再调向量模型。论文实测BGE-M3加SLS的效果远好于更大的Qwen3、域内微调向量模型，无需盲目堆大向量模型，先补召回的问法覆盖度ROI更高

  - 做FAQ召回评估需严格规避数据泄漏：不能用标准问题当测试集，需用实际用户的变体问法做holdout，否则BM25等方法的R@1会虚高8倍左右，评估结果完全失真'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
AI语音客服等落地场景有两个核心约束被通用QA benchmark完全忽略：一是时延要求极高，query-time调用LLM生成会产生约1s延迟，无法满足语音热线的实时交互要求；二是错误回答成本极高，普通RAG即使召回了正确的上下文，自由生成的回答仍有7-13%的无依据内容，会严重激怒已有不满情绪的用户，错误回答的负面影响远高于转人工的成本。

### 方法关键点
- 架构上采用无生成的验证单元QA pipeline：所有回答只能从预定义、人类验证过的QA单元库中选取，要么返回匹配到的单元答案原文，要么路由到澄清/弃权/人工流程，从构造上完全消除无依据回答的可能
- 离线执行分阶段语言种子（SLS）扩展索引：①人类为每个QA单元编写世界接地的槽位配方，将标准问题拆解为带领域知识的可替换槽位；②用GPT-4.1-mini基于槽位组合生成多样化问法变体；③轻量人工过滤掉无效变体，将所有变体和标准问题共同加入索引，推理时仅做单次检索，无额外开销

### 关键实验
在两个工业域数据集（汽车领域90个QA单元、消费电子领域229个QA单元，共7947个query变体）上测试，对比doc2query、HyDE、query2doc等所有基线方法，在使用相同GPT-4.1-mini生成相同数量变体的条件下，SLS将混合检索（BM25+BGE-M3）的R@1提升到0.881（消费电子）/0.930（汽车），比最优自动基线高+0.20/+0.32，比仅用标准问题索引高+0.27/+0.34；推理时延仅14ms，比query-time生成方案快两个数量级；无依据回答率从7-13%降至接近0。

### 最值得记住的一句话
FAQ检索的优化核心是覆盖用户的多样化问法，注入人类接地知识的离线扩展效果远好于纯自动生成方案，且完全不增加推理成本
