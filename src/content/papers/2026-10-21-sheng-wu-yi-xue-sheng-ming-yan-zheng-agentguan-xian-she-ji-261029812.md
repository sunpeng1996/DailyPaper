---
title: 'Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification
  Agents'
title_zh: 生物医学声明验证Agent管线设计：真实PMID未必对应相关论文
authors:
- Mohammed Saqlain
affiliations:
- Independent Researcher, Bangalore, India
arxiv_id: '2610.29812'
url: https://arxiv.org/abs/2610.29812
pdf_url: https://arxiv.org/pdf/2610.29812
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 生物医学事实核验Agent管线优化
tags:
- Agent
- Fact-Checking
- Retrieval
- Biomedical
- ReAct
- Citation Evaluation
one_liner: 控制变量对比4种生物医学文献Agent管线，证明检索而非推理是核心性能瓶颈
practical_value: '- 做搜索类Agent时不要直接用原始query做one-shot检索，让LLM生成实体聚焦的短查询改写，可提升3倍黄金召回率，可直接复用在电商搜索query改写、导购Agent检索链路

  - 验证检索而非LLM推理是RAG/Agent的核心性能瓶颈，业务优化优先投入检索链路（召回、query改写），比调整prompt、更换大模型性价比更高

  - 不要信任闭卷LLM生成的ID类内容（如商品ID、文献ID），哪怕ID真实存在也大概率不相关，必须新增召回内容与用户需求的相关性校验环节

  - Agent普遍用不满分配的搜索预算，可新增最小证据阈值规则强制用够预算，提升召回覆盖率，可复用在信息查询、导购类Agent设计'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前面向生物医学文献的检索Agent已成为科研助手的标准组件，但不同管线（Harness）设计的效果差异缺乏控制变量下的量化验证，三个核心问题悬而未决：PubMed检索是否比闭卷回答效果更优？ReAct式多轮检索的额外成本是否值得？Agent生成的引用是否可信？

### 方法关键点
- 固定骨干模型、输出格式、任务规则，仅变量为4种管线：闭卷回答、以原声明为query的one-shot RAG、可自主生成检索词的ReAct式Agent、直接获取黄金摘要的Oracle
- 骨干用gemini-3.1-flash-lite、gemini-3.5-flash-lite两个低延迟前沿模型，测试集为SciFact验证集采样的100条专家标注生物医学声明，任务为三分类（支持/反对/信息不足）
- 新增引用可信度评估：区分PMID不存在、存在但不相关两种错误，用跨家族LLM Qwen3.8-27B做相关性盲审

### 关键结果
- one-shot RAG黄金摘要召回率仅6%，准确率比闭卷回答低1~10个百分点，仅将过自信错误转为无信息判断，无实际增益
- ReAct式Agent黄金摘要召回率提升至19~20%，是one-shot RAG的3倍，准确率达62%，为所有非Oracle管线最高
- Oracle管线准确率达79~86%，比最优非Oracle管线高17~24个百分点，差距统计显著
- 闭卷生成的PMID 97%以上真实存在，但仅0.5~1%与声明相关；Agent生成的PMID相关性达66~70%

> 最值得记住的结论：对于依赖外部知识的Agent，检索质量是远大于推理能力的性能瓶颈，仅校验引用ID的真实性完全无法保障内容可信度。
