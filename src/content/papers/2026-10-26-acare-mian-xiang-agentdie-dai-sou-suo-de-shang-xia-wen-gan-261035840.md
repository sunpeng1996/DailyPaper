---
title: 'ACARE: Agent-Context-Aware Reranker for Iterative Search'
title_zh: ACARE：面向Agent迭代搜索的上下文感知重排模型
authors:
- Sahel Sharifymoghaddam
- Yauhen Babakhin
- Reza Esfandiarpoor
- Oliver Holworthy
- Jimmy Lin
- Bo Liu
affiliations:
- University of Waterloo
- NVIDIA
arxiv_id: '2610.35840'
url: https://arxiv.org/abs/2610.35840
pdf_url: https://arxiv.org/pdf/2610.35840
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent 迭代搜索工具优化
tags:
- Reranker
- Agentic Search
- Iterative Retrieval
- LLM4IR
- Context-Aware
one_liner: 基于Qwen3-Reranker-4B微调的4B Agent上下文感知重排器，提升迭代搜索效率与效果
practical_value: '- Agent搜索/导购场景可直接复用4种上下文模式设计，适配开源（可获取推理轨迹）/闭源（仅可获取原始问题）Agent，无需维护多套重排模型

  - 训练时加入独立上下文dropout策略，对多类可选输入字段各自按概率丢弃，单checkpoint兼容多种输入场景，大幅降低训练与部署成本

  - 电商/广告Agent导购场景可将用户原始需求、Agent当前推理上下文、生成的搜索子Query结合重排商品/广告，减少无效交互轮次，降低大模型调用成本

  - 成本敏感的业务场景可优先选择小Agent+上下文感知重排器的架构，仅用大Agent 8%~38%的成本就能达到接近大Agent的检索效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统迭代搜索重排器仅基于Agent生成的子Query计算相关性，忽略用户原始问题、Agent推理轨迹等上下文，容易召回匹配子Query但无助于解决原始任务的文档，大幅提升无效搜索轮次与Agent调用成本；而上下文感知的一阶检索要求本地持有全量语料，无法适配调用公开搜索API的无语料权限场景。

### 方法关键点
- 基于Qwen3-Reranker-4B微调得到4B参数的ACARE，单checkpoint支持4种输入模式：仅子Query、子Query+推理轨迹、子Query+原始问题、子Query+推理轨迹+原始问题，兼容开源（暴露推理轨迹）/闭源（不暴露轨迹）各类Agent
- 训练时对原始问题、推理轨迹两个字段做独立50%概率的dropout，避免模型依赖某类上下文，提升不同输入场景下的泛化性，采用LCE损失区分正负样本
- 扩展DR-Synth标注数据集，重新挖掘负例并新增Agent轨迹样本，最终得到16601条标注实例用于训练

### 关键结果
- 覆盖3个基准、5类Agent的实验中，ACARE的数据集平均nDCG@10比基础Qwen3重排器高0.9~2.0pp，每Query搜索次数减少0.3~1.0次，Agent API成本降低5.1%~20.1%
- 小Agent搭配ACARE可缩小51%~74%与大Agent的nDCG@10差距，成本仅为同场景大Agent的8%~38%
- 端到端问答场景下，ACARE比无重排方案准确率高8.2~9.1pp，同时证据精度更高、搜索次数更少

### 核心结论
给Agent用的检索工具不要局限于子Query特征，复用已有的原始任务、推理上下文信息，仅需微调轻量重排器就能同时实现效果提升与成本下降。
