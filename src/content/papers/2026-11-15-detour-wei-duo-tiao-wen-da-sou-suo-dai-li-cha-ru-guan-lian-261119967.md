---
title: 'DetouR: Plugging Association Routes into Search Agents for Multi-hop Question
  Answering'
title_zh: DetouR：为多跳问答搜索代理插入关联路径的轻量插件
authors:
- Tingwei Chen
- Yunxiao Shi
- Zhendong Chu
- Zhiying Deng
- Min Xu
- Qingsong Wen
arxiv_id: '2611.19967'
url: https://arxiv.org/abs/2611.19967
pdf_url: https://arxiv.org/pdf/2611.19967
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: 搜索Agent · 多跳问答优化
tags:
- Search Agent
- Multi-hop QA
- RAG
- PageRank
- LightGBM
one_liner: 无额外搜索/LLM调用的搜索代理插件，利用关联路径提升多跳问答准确率
practical_value: '- 多轮交互类Agent（电商导购、售后答疑、商品咨询Agent）可复用近重复查询检测逻辑，把冗余查询替换为已召回结果的关联链接跳转，不增加调用成本即可提升召回覆盖率

  - RAG上下文构建环节可抛弃传统RRF融合策略，改用「轮询排序+个性化PageRank」的无模型融合方案，多跳关联证据保留率优于8B reranker，还可省去大模型重排序成本

  - 关联路径选择无需部署大模型，轻量LightGBM排序器即可达到最优效果，甚至无训练的标题匹配策略也能实现接近的收益，适合快速落地

  - 电商现有商品/内容关联结构（详情页相关推荐、看了又看、实体共现关系）可直接作为关联路径使用，无需额外构建离线知识图谱，降低接入成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索Agent仅依赖语义路径生成检索query，只能召回模型可明确命名的证据，53%-73%的多跳问答缺失黄金页仅和已召回结果隔一个超链接；同时多轮检索常用的RRF融合会惩罚仅单次召回的关联证据，导致已召回的黄金证据被丢弃，额外检索反而降低上下文完整度。

### 方法关键点
- 完全无侵入插件设计，无需额外搜索或LLM调用，可直接接入任意现有搜索Agent
- Link Rerouting：以内容词Jaccard相似度≥0.8判定近重复查询，用轻量LightGBM排序器选择已召回页面的关联链接作为替换query，提升召回覆盖率
- Chain-aware Context Selection：以问题提及的实体页面为种子运行个性化PageRank，结合轮询排序的先验分数生成最终上下文，完整保留多跳证据链

### 关键结果
在HotpotQA、2Wiki两个多跳问答数据集上，接入IRCoT、ReAct、Search-R1、Plan四种主流搜索Agent，平均提升EM 4.0个点（2Wiki）、1.4个点（HotpotQA）；上下文选择模块无任何模型调用，在2Wiki上完整上下文占比达64.5%，优于7B LLM judge的53.8%和8B reranker的57.9%。

### 核心结论
固定检索和LLM调用预算下，挖掘已召回结果的隐含关联结构带来的收益，远高于使用更大的重排序模型或增加检索次数。
