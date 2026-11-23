---
title: 'From Acting to Learning: Experience Selection toward Continually Learning
  Agents'
title_zh: 面向持续学习Agent的交互经验选择机制研究
authors:
- Yaoyuan Yan
- Haoxiang Jie
- Zhiyou Heng
- Kailin Wang
- Yumiao Li
- Lifeng Liu
- Anwan Yan
affiliations:
- Country Garden Services AI Lab
- Omni AI
arxiv_id: '2611.27159'
url: https://arxiv.org/abs/2611.27159
pdf_url: https://arxiv.org/pdf/2611.27159
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: Agent持续学习 · 经验数据选择
tags:
- Continual Learning
- Experience Selection
- LoRA
- LLM Agent
- SFT
one_liner: 对比9种经验选择器，验证优化器感知梯度选择可显著提升4B语言Agent的任务成功率
practical_value: '- 电商导购/客服Agent做增量SFT时，可直接复用优化器感知的梯度筛选规则，比随机/高NLL筛选效果提升5~8pp，仅需几十GPU小时即可完成小样本微调，落地成本极低

  - 推荐系统做增量训练数据筛选时，可直接复用结论：低NLL易模仿样本的训练效果远差于随机样本，不要默认选择模型预测置信度高的样本做训练

  - 做数据采样时要匹配筛选规则和选择空间：梯度筛选适合放开任务/类目覆盖约束，随机/规则筛选则适合保留固定的类目分布约束，避免效果下跌'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent交互执行会积累大量成功经验，但增量训练的更新预算有限，并非所有成功经验都能带来下游效果增益。现有经验筛选规则（如按NLL排序、随机采样）没有验证样本对任务的实际价值，也未考虑筛选规则和选择空间的适配性，缺乏系统的对比验证。
### 方法关键点
- 基于Qwen3-4B-Instruct做LoRA微调，对比9种经验选择器，覆盖随机选择、低/中/高NLL选择、优化器感知梯度选择三类，同时控制「任务/动作匹配约束」「全局无约束」两种选择空间
- 梯度选择复用LESS风格打分规则：基于冻结的Adam状态计算样本梯度与40个公开基准动作梯度的余弦相似度排序，选Top256条去重样本
- 所有实验控制相同训练配置（192步优化器更新、768次样本呈现）、初始化种子、采样种子、评估执行器，排除无关变量干扰
### 关键结果
在ALFWorld的两个独立经验池（API/Generic）上验证，对比全局随机、全局高NLL两个基线：
- 梯度选择在开发集上成功率分别达81.45%、73.19%，比随机选择高8.25、5.96pp，比高NLL选择高4.10、4.05pp，8组初始化对照全为正向增益
- 预留任务集泛化验证中，梯度选择比随机、高NLL选择分别高7.03、5.03pp，增益稳定
- 放开覆盖约束后，梯度选择效果提升4.15pp，随机选择效果下降4.15pp，两者适配性差异显著

最值得记住的结论：经验筛选的效果同时取决于排序规则和选择空间，优化器感知的梯度选择配合全局无约束空间可获得最优增量训练效果，低NLL易模仿样本的训练效果最差。
