---
title: Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict
  Typing in RAG
title_zh: RAG知识冲突类型检测：是否需要用大模型？决策模型方案全评测
authors:
- Parv Khatri
- Harshul Jain
- Mehak Kapoor
- Tanya Sah
affiliations:
- Independent Researcher
arxiv_id: '2610.36915'
url: https://arxiv.org/abs/2610.36915
pdf_url: https://arxiv.org/pdf/2610.36915
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: RAG 知识冲突分类优化
tags:
- RAG
- Knowledge Conflict
- Decision Model
- Cost Optimization
- Latency Reduction
one_liner: 评测11款商用决策模型实现RAG冲突分类，效果对标Gemini 2.5 Flash，成本降4-39倍、延迟降2.6-6倍
practical_value: '- 电商/广告RAG场景下的多源内容冲突分类（比如商品参数多源冲突、用户评价观点冲突、促销信息过时）可优先采用typed decision模型替代通用LLM，在不损失效果的前提下大幅降低推理成本与延迟，尤其适合高QPS的生产环境

  - 可复用「轻量决策模型+低置信度请求路由到高阶LLM」的级联架构：仅需把25%低置信度请求转发给Gemini 3.8 Flash级别的高阶模型，即可达到与全量用高阶LLM相当的准确率，成本仅为后者的25%-37%

  - 决策模型做分类任务时优先采用直接多选问题的prompt设计，不要拆成多个yes/no子问题，后者会显著降低所有决策模型的准确率，且单模型适配的树状问题结构无法迁移到其他模型

  - 做信息过时类冲突检测时无需单独依赖源的发布日期，决策模型可从文本内容（比如“former”“截至XX年”等表述）识别过时信息，降低数据预处理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG系统中召回的多源信息经常出现冲突，不同冲突类型（无冲突、互补信息、观点冲突、信息过时、错误信息）对应完全不同的生成策略，已有研究证明给生成器输入冲突类型可提升回答质量24个点，但此前仅用通用LLM做冲突分类，成本高、延迟大，无法适配高QPS生产场景。
### 方法关键点
- 任务定义：5分类的RAG知识冲突类型检测，采用公开CONFLICTS基准数据集，共458条标注query，平均每条对应9.2条检索结果
- 对比方案：对比11款商用typed decision模型（单前向传播输出分类概率，无需生成文本）、Gemini 2.5 Flash（原SOTA方案）、Gemini 3.8 Flash（当前最新SOTA）三类方案
- 架构创新：提出基于决策模型置信度的级联路由方案，将决策模型最低置信度的一定比例请求转发给高阶LLM，平衡成本与效果
- 诊断实验：测试发布日期、检索源排序、植入错误信息三类变量对模型效果的影响
### 关键结果
- 10款决策模型的准确率（50.0%-67.0%）匹配或超过Gemini 2.5 Flash的61.3%，计费模型成本仅为后者的1/4-1/39，延迟仅为1/2.6-1/6
- 采用25%低置信度请求转发给Gemini 3.8 Flash的级联方案，8款决策模型的级联系统准确率与全量用Gemini 3.8 Flash（70.0%）统计持平，成本仅为后者的25%-37%
- 拆分为多个yes/no子问题的prompt设计会使所有决策模型准确率显著下降，单模型适配的树状结构无法迁移到其他模型
### 核心结论
typed decision模型是结构化分类类任务的首选方案，级联架构可在不损失效果的前提下大幅降低RAG系统的推理成本与延迟
