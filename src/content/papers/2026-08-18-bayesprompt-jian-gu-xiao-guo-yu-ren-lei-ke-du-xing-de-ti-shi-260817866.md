---
title: 'BayesPrompt: human readable prompts that make sense'
title_zh: BayesPrompt：兼顾效果与人类可读性的提示生成方法
authors:
- Franky Kevin Nando Tezoh
- Ali Hussaini Umar
- Alessandro Laio
- Guido Sanguinetti
- Riccardo Rende
affiliations:
- Scuola Internazionale Superiore di Studi Avanzati (SISSA)
- Flatiron Institute
arxiv_id: '2608.17866'
url: https://arxiv.org/abs/2608.17866
pdf_url: https://arxiv.org/pdf/2608.17866
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM提示优化 · 贝叶斯推理
tags:
- Prompt_Optimization
- Bayesian_Inference
- MCMC
- Reverse_LM
- LoRA
one_liner: 将提示优化重构为贝叶斯后验推理，生成低困惑度且高可读性的有效提示
practical_value: '- 做Agent/推荐场景的prompt优化时，可在目标函数中加入自然语言先验正则项，避免生成不可解释的伪提示，降低线上迭代的debug成本

  - 反向语言模型（reverse LM）做warm start的思路可复用，能大幅提升离散prompt搜索的初始质量，减少迭代步数

  - 离散prompt搜索时可借鉴MCMC的增删改采样策略，平衡任务效果和prompt可读性，适合需要人工审核prompt的业务场景

  - 电商搜索query生成/改写场景可复用该框架，从目标商品反向生成符合用户表达习惯的候选query，提升召回覆盖'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有prompt优化方法为了最小化目标输出的困惑度，往往生成人类完全无法理解的pseudoprompts，既不可控也无法调试，业务落地风险高；核心原因是优化目标仅考虑条件似然P(a|q)，忽略了自然语言的先验分布，属于病态优化问题。

### 方法关键点
- 重构prompt优化为贝叶斯后验推理问题，目标为最大化P(q|a) ∝ P(a|q)P(q)，其中P(q)是自然语言序列的先验分布，约束生成prompt的流畅性
- 采用Metropolis-Hastings (MCMC)采样算法探索prompt空间，支持替换、插入、删除三种token编辑操作，动态调整prompt长度，操作概率分别设为0.6、0.2、0.2
- 用LoRA微调反向语言模型（从右到左预测的Llama-3.2-1B）做MCMC的warm start初始化，大幅降低采样收敛成本

### 关键实验
在NQ-OPEN公开问答数据集上测试，对比GCG、GCG-Reg、GD-PEZ三个SOTA基线：
- 可读性（fluency）上MCMC的分布最接近人类标注的Ground Truth，比基线平均提升60%以上
- LLM评判的问答对合理性上，MCMC赢329次，远高于第二名GD-PEZ的23次
- 语法正确性得分集中在0.9-1.0区间，基线仅集中在0.4-0.5区间，仅存在不到5%的效果损失

### 核心结论
prompt优化的伪提示问题本质是未引入自然语言先验的病态优化问题，加入先验后可在效果损失极小的前提下大幅提升prompt可读性。
