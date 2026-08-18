---
title: 'Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored
  Supervised Fine-Tuning'
title_zh: Palmyra x6技术报告：基于锚定SFT的工具调用智能体大模型
authors:
- Peng Du
- Kiran Kamble
- Rakshith Vasudev
- Zhizhuo Yang
- Rohith Nadimpally
- Arjun Krishna
- Waseem Alshikh
- Daniel M. Bikel
affiliations:
- Writer AI Research, Writer, Inc.
arxiv_id: '2608.16620'
url: https://arxiv.org/abs/2608.16620
pdf_url: https://arxiv.org/pdf/2608.16620
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent 工具调用 · 大模型微调
tags:
- Agent
- Tool Calling
- SFT
- MoE
- Muon Optimizer
one_liner: 基于744B MoE基座，用626条合成轨迹+锚定SFT训练出SOTA级工具调用智能体模型
practical_value: '- 做业务垂直Agent微调时，无需海量标注数据，几百条高质量、过验证的领域轨迹+锚定SFT（KL权重0.1左右）即可在不损害基座原有能力的前提下，大幅提升工具调用性能，降低数据成本

  - 大参数MoE模型微调可采用Muon+Adam混合优化策略：2D权重矩阵用Muon、1D/非矩阵参数用Adam，能降低显存占用，同时提升训练效率和效果

  - 合成训练数据时，可复用「策略级示范注入+作弊过滤+多轮验证」流程：仅保留工具调用逻辑、屏蔽参数和结果，强制模型自主调用工具生成结果，避免数据泄露，提升轨迹质量

  - 电商导购Agent、商品查询Agent微调可直接复用这套框架：先构造电商专属工具（商品检索、库存查询、优惠计算等）的轨迹集，用锚定SFT微调，可控成本下得到垂直领域可用的Agent'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型做智能体工具调用微调时，常规SFT容易导致基座原有能力退化，且需要海量标注数据，成本极高；面向企业级Agent场景，需要兼顾能力提升、基座能力保留、训练成本可控的微调方案。
### 方法关键点
- 基座选择：采用GLM-5.2 MoE基座，总参744B，单token激活参约40B，原生支持DSA IndexShare稀疏注意力，上下文长度达65536 tokens
- 数据构造：仅用626条高质量合成轨迹，覆盖金融研究、数据分析、MCP工具、RAG等6大类任务；生成采用策略级示范注入（仅保留工具调用顺序、屏蔽具体参数和结果）+作弊过滤（防直接抄示范）+多轮LLM验证，严格保障轨迹质量
- 训练策略：采用锚定SFT（ASFT）损失，加入与冻结基座的KL散度惩罚（K=0.1），避免模型分布漂移；优化器采用Muon+Adam混合策略，降低显存占用、提升训练效率
- 训练配置：单epoch训练，学习率5e-7，全局batch size 16，全程离线训练无RL采样，训练复杂度极低
### 关键结果
- 对比Writer Agent原有默认模型，6个评测基准全部领先，MCP-Atlas提升0.32、FinanceBench提升0.305、IFBench提升0.304
- 对比5款前沿大模型，6个基准平均得分0.765位列第一，BFCL Core得分0.785登顶
- 安全表现优异：80%政治相关问题中立呈现双方观点，FORTRESS安全评测比基座提升8.6分，仅损失0.8分良性友好度
### 核心结论
几百条高质量垂直领域轨迹+锚定SFT，就可以在几乎不损失基座原有能力的前提下，把大模型的对应垂直Agent能力提升到SOTA水平，真正实现「少即是多」的微调范式
