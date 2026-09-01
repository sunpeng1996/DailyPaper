---
title: 'Beyond Surface Alignment: Grounding the Dynamics of Situational Understanding
  and Generative Control in LLMs'
title_zh: 超越表面对齐：大语言模型情境理解与生成控制的落地机制
authors:
- Chenghao Yang
affiliations:
- The University of Chicago
arxiv_id: '2608.29610'
url: https://arxiv.org/abs/2608.29610
pdf_url: https://arxiv.org/pdf/2608.29610
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: LLM对齐优化 · 生成控制与Agent落地
tags:
- LLM Alignment
- Situational Grounding
- Generative Control
- Agent
- Evaluation
one_liner: 系统性揭示LLM对齐的深层局限，提出情境/生成/控制三层落地框架与配套优化方法
practical_value: '- 电商商品/广告文案生成可复用AI Realtor架构：先做商品特征接地避免幻觉，再对齐用户偏好，最后用RAG引入差异化卖点，提升转化

  - 搭建LLM驱动的推荐Agent时，可参考分支因子（BF）指标衡量生成多样性，优先在生成早期高熵阶段做探索，后期收敛保证质量

  - 多模型生成推荐话术/搜索Query时，可复用BACO框架：基模型保多样性，对齐模型保质量，token级动态路由，比单纯调温度效果更稳定

  - 评估LLM生成内容鲁棒性时，可借鉴ReCode的扰动方法，对prompt做语义不变改写，测试输出一致性，降低线上bad case'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM经SFT、RLHF等表面对齐后，仍存在情境理解偏差、幻觉严重、生成多样性不足、鲁棒性弱等问题，无法支撑Agent、生成式推荐等落地场景对可控性、真实性、个性化的要求，缺乏系统性的评估框架与可落地的优化方案。
### 方法关键点
- 构建三层研究体系：情境接地评估、生成接地机制分析、动态控制优化
- 推出SITTEST、ReCode等基准，分别测试LLM多轮状态跟踪能力、代码生成在语义不变扰动下的鲁棒性
- 揭示分支因子（BF）变化规律：对齐后LLM生成概率随输出长度快速收敛，多样性（BF）大幅降低，其中SFT对BF的压缩贡献最大
- 提出系列落地方法：三模块接地式文案生成框架AI Realtor、基模型+对齐模型token级路由协作方案BACO、退火采样方法EAD优化RL训练探索效率
### 关键结果
在MMLU、GSM8K、代码生成、房产文案生成等任务上验证：BACO相比单对齐模型，语义多样性提升42%，质量评分提升11%，人类偏好win率达68%；EAD相比固定温度采样，RL训练Pass@16提升27%，适配PPO、DPO等所有主流RL算法；AI Realtor生成的文案相比人工撰写，说服性Elo评分高23分，幻觉率低18%。
### 核心结论
对齐不是LLM落地的终点，而是需要结合场景动态控制生成过程，平衡多样性、质量、真实性的起点。
