---
title: 'TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge
  Editing against Memory Hallucination'
title_zh: TASK Memory：融合激活引导与知识编辑对抗使用阶段记忆幻觉
authors:
- Jinkun Zhao
- Wenjun Wu
affiliations:
- 北京航空航天大学人工智能研究所SKLCCSE
- 北京未来区块链与隐私计算高精尖创新中心
arxiv_id: '2611.34762'
url: https://arxiv.org/abs/2611.34762
pdf_url: https://arxiv.org/pdf/2611.34762
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: LLM Agent 记忆架构优化
tags:
- LLM_Agent
- Memory_Hallucination
- Activation_Steering
- Knowledge_Editing
- RAG
one_liner: 绑定文本、激活引导、知识编辑为记忆单元，大幅降低LLM Agent使用时记忆幻觉
practical_value: '- 电商导购/客服Agent场景可复用门控逻辑：对召回的用户/商品记忆，用模型内部表征做相关性校验，避免错误应用历史记忆给出错误推荐/答复，降低误导用户概率

  - 优化RAG系统可借鉴双激活引导向量设计：相关query加v+提升记忆采纳率，无关query加v-抑制记忆滥用，比全局强制上下文优先的方案同时兼顾准确率和泛化性

  - 动态更新场景（商品价格/库存变更、用户偏好更新）可复用版本自动淘汰机制：无需额外维护事实ID，用地址校验+模型自动判断新旧版本，同时卸载旧记忆的编辑补丁和引导向量，避免版本混淆幻觉

  - 低算力落地可优先使用T+S（文本+引导向量）配置，无需做知识编辑即可获得大部分性能收益，降低工程复杂度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent依赖的纯文本记忆/RAG即使召回了正确内容，仍会因模型参数知识与外部记忆冲突出现使用时幻觉：最多46%场景忽略正确记忆返回 stale 参数知识，最多24%把记忆错用给无关实体，53%的更新类查询返回旧版本内容，现有方案仅能解决单类幻觉，无法同时兼顾记忆采纳率和不滥用。

### 方法关键点
- 每个记忆单元绑定3个组件共享同一模型内部地址：文本T存储事实内容，可解释可追溯；可移除低秩知识编辑E提供内部地址并支撑多跳推理；双激活引导向量S（v+引导采纳记忆，v-引导抑制无关记忆）控制记忆使用策略，不存储事实内容
- 读时用同一内部地址门控三类组件：相关query加载T、E并加v+，无关query不加载T、E并加v-，保证决策一致
- 版本更新时自动校验旧记忆地址，同时淘汰旧版T、E、S，无需维护额外事实ID

### 关键结果
跨5个开源模型（8B-27B）测试：记忆忽略幻觉降至≤1.5%，记忆错用率从39.2%降至7.5%，CounterFact数据集综合分提升10.8pp；300条记忆库场景比BM25 RAG综合分提升16.4pp，优势在3000条记忆时仍保持，多跳推理MQuAKE数据集提升7.5pp，9/10的模型-数据集组合优于现有上下文引导方法。

### 核心结论
记忆系统不能只优化存储和召回，还要显式控制记忆的使用决策，从「告诉模型有什么事实」升级为「告诉模型什么时候用这个事实」
