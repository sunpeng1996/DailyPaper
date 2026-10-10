---
title: Learning Probabilistic Logic Programs with Functional Gradient Guided Language
  Models
title_zh: 基于函数梯度引导语言模型的概率逻辑程序学习方法
authors:
- Saurabh Mathur
- Sahil Sidheekh
- Bhavan Vasu
- Farbod Tavakkoli
- Prasad Tadepalli
- Kristian Kersting
- Sriraam Natarajan
affiliations:
- Technische Universität Darmstadt
- The University of Texas at Dallas
- AT&T CDO
- Oregon State University
arxiv_id: '2610.12303'
url: https://arxiv.org/abs/2610.12303
pdf_url: https://arxiv.org/pdf/2610.12303
published: '2026-10-08'
collected: '2026-10-10'
category: Reasoning
direction: 神经符号推理 · 概率逻辑程序学习
tags:
- Neurosymbolic
- Probabilistic Logic Program
- Gradient Boosting
- LLM
- Program Synthesis
one_liner: 提出结合梯度提升与LLM的GRASP框架，解决概率逻辑程序学习的符号搜索空间爆炸问题
practical_value: '- 可借鉴梯度引导LLM生成候选的思路，替代推荐系统规则挖掘中传统的组合搜索，降低规则召回的计算开销

  - 对于需要可解释性的电商风控、广告合规场景，可复用「梯度提升+LLM生成符号规则」的框架，产出可审核的加权规则集合

  - 处理用户行为图、商品关联网络等关系型数据的规则挖掘任务时，可将弱学习器替换为业务域自定义的一阶规则，适配业务需求'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
概率逻辑程序可编码关系结构、实现可解释的神经符号推理，但从数据中学习时面临符号搜索空间组合爆炸瓶颈；单独使用LLM生成规则又缺乏系统归纳推理能力，难以生成适配复杂关系分布的有效程序。
### 方法关键点
提出GRASP神经符号框架，将关系结构学习建模为函数梯度提升过程，弱学习器定义为一阶规则，把原本难以求解的内部搜索任务交给LLM作为候选生成oracle，由梯度信号引导LLM输出符合优化方向的规则候选，最终生成加权规则集成。
### 关键结果
在分子毒性预测（Tox21）、诱变预测、引文匹配（Cora）共4个关系基准任务上，效果优于纯符号、纯神经网络、纯LLM基线，同时输出可解释的加权规则集合，保留梯度提升的理论保证且不牺牲符号输出的透明性。
