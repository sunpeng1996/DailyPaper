---
title: Knowledge That Is Linear Before Fine-Tuning Generalizes After It
title_zh: 微调前线性可读的知识在微调后具备更好的泛化能力
authors:
- Faridoun Mehri
- Hinrich Schütze
affiliations:
- LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.22300'
url: https://arxiv.org/abs/2610.22300
pdf_url: https://arxiv.org/pdf/2610.22300
published: '2026-10-15'
collected: '2026-10-16'
category: LLM
direction: 大模型知识表征 · 线性可探测性
tags:
- Knowledge Probing
- Linear Probe
- Fine-tuning
- Generalization
- Fact Representation
one_liner: 证明预训练模型中线性可读的事实知识更能支撑微调后新关联知识的泛化
practical_value: '- 领域LLM微调注入业务知识时，可先通过Linear Probe测试现有核心关联（如商品→品类、用户→消费等级）的线性可读性，优先选用线性度高的关联作为底座构建垂直领域规则映射，泛化效果更稳定

  - RAG/知识编辑的评估指标除了知识召回准确率，可新增线性探测得分作为补充，得分越高的知识越容易被模型复用支撑下游新任务

  - 构建用户/商品的Semantic ID表征时，优先保证核心属性（如价格带、适用人群）在隐空间线性可分，后续微调跨域推荐、个性化标签生成等任务时泛化性更强'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有研究多关注LLM的事实召回能力，但忽略了不同知识对新任务学习的支撑能力差异：部分知识可被准确召回，但无法支撑新关联知识的推导泛化（即惰性知识），区分主动/惰性知识对提升微调效率、降低幻觉、优化知识注入流程有重要价值。

### 方法关键点
- 基于70个预训练事实关联（如城市→所属大洲、明星→所属经纪公司），将每个原答案随机映射为全新无关标签（如欧洲→螃蟹）构造全新关联任务
- 定义三大核心指标：Pre-linearity（预训练模型上通过嵌套交叉验证Linear Probe测得的事实关联线性可读度）、Recall（预训练模型对原关联的召回准确率）、Generalization（微调后模型对未见过主体的新标签预测准确率）
- 微调仅在新关联的部分主体上训练，不告知模型原关联及映射规则，直接测试模型对未见过主体的标签推断能力

### 关键实验
在2B~27B参数的11个开源LLM上测试，70个事实关联的Pre-linearity与Generalization的皮尔逊相关系数达0.87~0.92；控制Recall、实体数量、实体预训练出现频次等变量后，相关系数仍保持0.70~0.82，Pre-linearity对泛化效果的预测能力比Recall高30%以上。

### 核心结论
判断LLM中知识的价值，不要只看它能不能被准确召回，其表征的线性可读度才是支撑新任务学习泛化的核心指标。
