---
title: 'Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in
  Scientific Claims'
title_zh: 相同表述不同解读：LLM Agent如何解决科学主张的歧义问题
authors:
- Delip Rao
- Ahmed Muharram
- Chris Callison-Burch
affiliations:
- University of Pennsylvania
arxiv_id: '2610.20457'
url: https://arxiv.org/abs/2610.20457
pdf_url: https://arxiv.org/pdf/2610.20457
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 科学主张验证歧义消解
tags:
- LLM Agent
- Ambiguity Resolution
- Claim Verification
- Structured Interpretation
- ReAct
one_liner: 提出Claim Card结构化记录Agent对科学主张的前置解读，证实解读调整可大幅改变验证结论
practical_value: '- 电商/广告合规校验类Agent可复用Claim Card思路，把「该商品可抗过敏」等歧义性claim的隐式假设拆分为判定阈值、适用人群、对比基线等显式字段，标注来源，降低误判率

  - 用户query理解场景可借鉴前置解读结构化的方案，对模糊query先输出系统解读字段（如「苹果」是水果还是数码产品），匹配用户预期后再执行召回，减少badcase

  - Agent输出不稳定排查可优先冻结解读类字段，再定位工具调用、证据检索、推理环节的波动来源，大幅缩小排障范围'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前科学主张验证类Agent普遍默认选择一种隐式解读执行验证，基准评测仅比对最终结论与专家标签，不记录专家与Agent的解读差异，导致结论不一致无法归因，还会浪费算力在未经验证的解读上，甚至工具调用的内容都会受隐式解读的影响。
### 方法关键点
1. 设计Claim Card结构化模板，包含系统定义、干预措施、评估标准三类共9个字段，每个字段标注来源为声明原文给出、领域知识推理、系统默认假设三类
2. 验证流程新增前置解读步骤：Agent先输出自然语言解读，由独立Parser转换为Claim Card，在工具调用前对外暴露，支持用户编辑字段后冻结解读重新运行
3. 基于ReAct架构搭建ClaimSpy验证Agent，支持网页搜索、材料科学专业计算工具调用，骨干模型采用GPT-5.4
### 关键结果
实验覆盖30条材料科学SFBench claims、30条生物医学SciFact claims，设置带Claim Card、不带Card、冻结统一Card三组对照，共900次运行：
- 42%~44%的Claim Card字段不是原文明确给出，多为单位、对比基线、判定阈值等直接影响验证结果的核心字段
- 仅修改量化词为全称、或收紧判定阈值两种单字段编辑，就能让约1/3的claim验证结论发生反转，远高于随机预期的1/7（p<0.001）
- 加入Claim Card仅增加10%左右的token消耗和运行耗时，对与专家标注的一致性无显著影响
### 核心结论
任何验证结论都是基于特定解读的结论，脱离解读的结果比对没有实际意义。
