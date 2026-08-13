---
title: Persona Conditioning as an Assessor-Sensitivity Probe for LLM-Based IR Evaluation
title_zh: 面向LLM信息检索评估的人设条件化评估者敏感性探测研究
authors:
- Samaneh Mohtadi
- Pietro Bernardelle
- Joel Mackenzie
- Gianluca Demartini
affiliations:
- The University of Queensland
arxiv_id: '2608.10385'
url: https://arxiv.org/abs/2608.10385
pdf_url: https://arxiv.org/pdf/2608.10385
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: LLM-as-Judge 评估 · 鲁棒性探测
tags:
- LLM-as-Judge
- Relevance Assessment
- Persona Conditioning
- IR Evaluation
- Sensitivity Probe
one_liner: 通过人设条件化探针揭示LLM作为IR评估者的敏感性规律，为评估pipeline鲁棒性测试提供方法
practical_value: '- 做搜索/推荐/Agent系统的LLM-as-Judge离线评估时，可引入多角色人设探针做压力测试，提前识别评估结果不稳定的候选模型，降低上线效果波动风险

  - 优先选择高容量LLM作为离线评估器，其受人设诱导的排序稳定性远优于小模型，可降低评估偏差对系统选型的干扰

  - 针对RAG类检索管道、神经排序/重排序模块的评估需额外关注人设敏感性，这类系统结果易受评估视角影响，可引入多角色投票机制校准评估结果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
LLM作为信息检索（IR）领域的相关性评估器应用越来越广泛，但评估者的人设框架对判断可靠性、下游系统对比结果的影响尚不明确，缺乏可控的敏感性探测方法。
### 方法关键点
从PersonaHub、NVIDIA Nemotron-Personas-USA两个来源引入5类任务导向评估者人设（意图理解、领域专家、对比判断、证据验证、全局搜索质量评估），对比标准UMBRELA基线，在TREC DL20、RAG24两个数据集上测试6种不同规模的LLM backbone的评估表现。
### 关键结果
1. 人设调整主要改变评估严格度、证据阈值、理解侧重，未出现大面积相关性反转，判断结果与基线整体接近
2. 系统层面，高容量LLM可保持稳定的系统排序一致性，小模型会显著放大人设诱导的不稳定性
3. 敏感性集中在特定系统类型：DL20数据集上的神经排序/重排序系统、RAG24数据集上的RAG类管道，人设来源对结果的影响远小于评估角色与模型容量
