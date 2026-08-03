---
title: 'Zero-Mem: Zero-Token Memory Operations for LLM Agents'
title_zh: Zero-Mem：面向LLM Agent的零Token内存操作框架
authors:
- Yilin Xiao
- Zhehan Zhu
- Yujing Zhang
- Jin Chen
- Zijin Hong
- Luyao Zhuang
- Qinggang Zhang
- Shengyuan Chen
- Xiaocao Ouyang
- Lingfei Ren
affiliations:
- The Hong Kong Polytechnic University
- Southwestern University of Finance and Economics
- Jilin University
arxiv_id: '2607.29377'
url: https://arxiv.org/abs/2607.29377
pdf_url: https://arxiv.org/pdf/2607.29377
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 长交互内存优化
tags:
- LLM Agent
- Memory System
- Zero Token
- Graph Retrieval
- Temporal Retrieval
one_liner: 提出零Token内存操作范式，仅最终QA调用LLM，大幅降低内存链路时延同时效果优于现有方案
practical_value: '- 电商客服/导购Agent可直接复用该零Token内存架构，取消记忆摘要/整理环节的LLM调用，单query内存处理时延可降50%+，同时避免生成摘要丢失用户历史偏好细节

  - 长周期用户建模场景可借鉴双视图检索设计：实体-上下文图关联用户跨会话浏览/购买的同实体商品，时间层级保留单会话内的浏览上下文，提升召回准确率

  - 确定性证据校准逻辑可复用到RAG链路，无需额外LLM调用即可完成证据冲突过滤、答案合法性校验，降低RAG环节的Token开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent内存系统大多依赖LLM生成记忆摘要/中间表示，不仅产生大量额外Token开销、增加时延，还会丢失原始交互细节；而直接检索原始文本的方案又容易混淆不同会话/时间的相似内容，无法兼顾准确性、效率和信息保真性。

### 方法关键点
- 零Token操作范式：除最终QA环节外，内存构建、检索、校准全流程不调用LLM，不产生LLM Token消耗，仅用NER、Embedding编码器等小模型和确定性规则完成所有操作
- 双视图内存结构：保留原始交互trace作为唯一数据源，一方面基于NER结果构建实体-上下文共现图支持跨会话关系检索，另一方面按「turn-窗口-会话-事件」层级组织时间序列，保留会话局部上下文
- Query感知路由与校准：根据Query的实体、时间等特征自动加权双视图的检索结果，补充关联证据和局部上下文后，经确定性规则过滤冲突、不符合边界的证据，最终送入QA LLM

### 关键实验结果
在LoCoMo多会话对话内存基准、HotpotQA长文本多跳推理基准上测试，对比Mem0、LightMem、GAM等主流内存方案：① 以GPT-4o-mini为基座时，LoCoMo平均F1达59.15，比最优基线GAM高5.4个点；② HotpotQA 448K长上下文场景F1达65.04，超最优基线5个点以上；③ 内存操作时延比最快基线LightMem降低57.6%，Token消耗直接降为0。

最值得记住的结论：结构化Agent内存完全不需要生成中间记忆表示，基于原始trace的结构化证据选择即可同时实现更高准确率和更低成本。
