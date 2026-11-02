---
title: 'SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding
  in Conversational XAI'
title_zh: SimXAI：可直接替换的轻量层提升对话式XAI的交互质量与理解
authors:
- Van Bach Nguyen
- Qianli Wang
- Nils Feldhus
- Jörg Schlötterer
- Christin Seifert
affiliations:
- University of Marburg
- Technische Universität Berlin
- University of Groningen
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2610.41856'
url: https://arxiv.org/abs/2610.41856
pdf_url: https://arxiv.org/pdf/2610.41856
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 对话式XAI · 可插拔Agent交互层
tags:
- ConvXAI
- Tool-Calling LLM
- Agent Architecture
- Faithfulness
- Conversational System
one_liner: 基于工具调用LLM的可插拔对话XAI交互层，替代传统GUS架构多模块，无需微调且保忠实度
practical_value: '- 电商/推荐场景下的规则/模板驱动对话机器人（比如推荐理由解释、商品答疑、广告效果咨询Agent）可直接复用该架构，用单工具调用LLM替换原有NLU+对话管理+NLG的多模块流水线，无需标注意图数据、开发规则与模板，大幅降低多轮对话能力的迭代成本

  - 对话Agent的评估可直接复用该三维框架：单/多轮意图解析准确率、响应与工具输出的忠实度、上下文连贯性，避免仅评估单轮效果导致的上线后多轮体验差问题

  - 可解释推荐的对话交互层可复用论文中的11个通用XAI函数定义，无需修改现有解释后台逻辑，即可快速升级支持自然语言多轮查询能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统对话式XAI（ConvXAI）普遍采用GUS架构，拆分NLU、规则对话管理、模板NLG三个独立模块，依赖大量手工标注的意图数据集、定制化对话规则与响应模板，上下文适配能力弱，无法灵活处理多轮对话中的指代、省略等需求，扩展到新场景成本极高，且难以平衡响应忠实度与交互体验。

### 方法关键点
- 仅用带工具调用能力的开源LLM（ToolACE-2.5-Llama-3.1-8B）作为唯一交互组件，替换原有三个模块，无需微调、无手工规则与模板，对接底层资源仅需提供函数定义
- 定义11个通用XAI函数接口，覆盖模型预测、局部/全局解释、反事实查询、模型/数据信息查询等核心需求，和底层XAI资源完全解耦，可按需扩展
- 交互逻辑自动处理上下文指代、参数补全，缺失参数主动询问用户，最终响应完全基于工具返回结果生成，避免编造信息

### 关键实验
在CoXQL、Compass等公开数据集+自制多轮/对话级数据集上测试，单轮函数选择准确率86%，多轮88%，长对话级最高96%；响应与工具输出的忠实度超91%，上下文连贯性超90%；用户研究替换TALKTOMODEL原有交互层后，用户任务准确率从59.0%提升到92.1%，每正确回答所需轮次从2.70降到1.32，80%用户更偏好SimXAI方案。

### 核心结论
对于已具备成熟后台能力的对话场景，用工具调用LLM搭建可插拔交互层替换传统多模块流水线，可在底层能力完全不变的前提下，大幅提升多轮对话体验同时有效控制幻觉风险。
