---
title: A knowledge-guided agentic framework for mitigating patient-context ambiguity
  in health queries
title_zh: 知识引导的Agent框架缓解健康查询的患者上下文歧义
authors:
- Mahyar Abbasian
- Saba A. Farahani
- Arshia Ilaty
- Hung Cao
- Ramesh Jain
- Amir M. Rahmani
arxiv_id: '2608.19875'
url: https://arxiv.org/abs/2608.19875
pdf_url: https://arxiv.org/pdf/2608.19875
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 上下文歧义消解框架设计
tags:
- Agent
- Knowledge Graph
- Context Disambiguation
- LLM
- Question Answering
one_liner: 在用户与下游LLM间插入知识引导Agent层，主动采集缺失的个性化上下文，无需微调即可提升问答准确率
practical_value: '- 可复用「中间Agent层+下游LLM解耦」架构，用于电商导购/客服场景的用户查询歧义消解，无需微调业务在用的下游LLM即可上线

  - 用领域知识图谱约束Agent的追问逻辑，而非让LLM自由生成问题，可大幅减少无效交互、提升上下文采集的精准度，适合商品咨询、售后等标准化场景

  - 补全用户上下文后可大幅降低下游LLM的性能波动，无需盲目追用最贵的大模型，搭配中小尺寸LLM即可拿到稳定的业务效果，显著降本

  - 上下文补全后下游生成的一致性提升近100%，适合对输出合规性、稳定性要求高的场景，比如医药健康类商品咨询、高客单价商品导购'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：健康类查询用户常提交表述清晰但缺失个性化上下文（如过敏史、基础病、妊娠状态）的短查询，现有方法无论是微调LLM、RAG增强还是重写Query，都无法获取用户未披露的专属信息，直接回答会依赖错误假设导致结果出错。
**方法关键点**：
- 架构上在用户与下游LLM之间插入独立的Agent中间层，完全不修改、不微调下游LLM，可直接对接任意主流LLM
- 基于任务专属知识图谱解析用户初始Query，生成符合逻辑的候选假设集，定位能区分不同假设的缺失上下文变量，生成精准的定向追问
- 多轮交互采集用户回复，迭代缩小假设空间，直到假设收敛或确认无法获取足够信息，再将原Query+采集到的上下文拼接为明确Prompt传给下游LLM
**关键结果**：在两个受控医疗基准数据集上测试：① 1034条症状诊断查询（平均缺失49.5%的关键症状）；② 487条饮食安全查询（缺失决定结果的患者健康上下文），对比直接回答、重写Query两个Baseline，覆盖5款主流LLM。结果：诊断任务Exact Top-1准确率较Baseline至少提升57.1个百分点，Exact Recall@5至少提升77.7个百分点；饮食安全任务在4/5的测试LLM上拿到最高MCC，不同LLM的性能波动降低60%以上，下游生成的不确定性几乎降为0。
**最值得记住的结论**：用户侧未披露的个性化上下文歧义，无法通过优化模型知识或重写Query解决，必须通过明确的主动交互获取，且这一过程与下游生成解耦能大幅降低业务对大模型能力的依赖。
