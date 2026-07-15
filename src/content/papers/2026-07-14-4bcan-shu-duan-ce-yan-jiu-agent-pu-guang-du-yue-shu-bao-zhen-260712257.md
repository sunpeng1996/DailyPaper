---
title: 'On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds
  Coverage'
title_zh: 4B参数端侧研究Agent：曝光度约束保真度，检索质量约束覆盖率
authors:
- Vinay Kumar Chaganti
arxiv_id: '2607.12257'
url: https://arxiv.org/abs/2607.12257
pdf_url: https://arxiv.org/pdf/2607.12257
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 端侧Agent 引用可信度优化
tags:
- On-Device Agent
- Citation Faithfulness
- Retrieval Coverage
- Small LLM
- RAG
one_liner: 拆解4B参数端侧研究Agent引用保真、覆盖度的独立影响因子，给出落地优化优先级
practical_value: '- 做端侧RAG/Agent时可优先提升单条召回chunk的上下文长度（曝光量），可低成本快速提升回答与引用源的保真度，无需先优化召回准确率

  - 引用覆盖率/答案完整性仅由召回recall决定，单源曝光量提升对该指标无增益，优化召回阶段是唯一可行路径

  - 4B级端侧小模型部署成本可参考：单条源曝光从400字符提升到1500字符，仅额外增加约235个输出token的推理开销'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
端侧小模型研究Agent的引用保真度、覆盖度无统一量化标准，两类指标的影响因子长期被混淆，缺乏可落地的优化优先级指引。
### 方法
固定部署于24GB笔记本的4B生成模型，控制两组变量：单条源曝光字符数（400 vs 1500）、源质量（标注黄金源/检索召回源），拆分度量两个独立指标：引用保真度（被引内容是否支撑输出结论）、可信覆盖率（是否覆盖所有应引用的正确源）。
### 关键结果
1. 保真度仅由单源曝光度约束：提升单源字符数可将召回源保真度从0.45提升至0.58，黄金源保真度从0.37提升至0.58，两类场景保真度收敛，与源本身正确性无关；
2. 可信覆盖率仅由检索质量约束：无论曝光度如何调整，召回源的覆盖率稳定在0.22，仅与召回recall（约0.4）强相关；
3. 单源曝光从400字符提升至1500字符，仅额外消耗约235个输出token的推理成本。
