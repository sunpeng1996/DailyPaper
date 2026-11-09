---
title: 'GroundWork: Bridging Human and LLM Reasoning Through a Structured Argumentation
  Model'
title_zh: 《GroundWork：基于结构化论辩模型打通人类与LLM推理》
authors:
- Sjoerd Vink
- Byungmoo Kim
- Michael Behrisch
- Adam Coscia
- Remco Chang
affiliations:
- Utrecht University
- Tufts University
- Stevens Institute of Technology
arxiv_id: '2611.09840'
url: https://arxiv.org/abs/2611.09840
pdf_url: https://arxiv.org/pdf/2611.09840
published: '2026-11-06'
collected: '2026-11-09'
category: Reasoning
direction: LLM人机协同 · 结构化论辩推理
tags:
- StructuredArgumentation
- HumanLLMCollaboration
- ToulminModel
- ReasoningSystem
- InteractiveAI
one_liner: 基于Toulmin论辩模型构建人-LLM共享结构化论辩图系统，支持可溯源可编辑协同推理
practical_value: '- 电商卖点梳理、合规校验、投放效果归因等需可解释的场景，可复用Toulmin模型将隐性论证逻辑从LLM对话中拆解为结构化组件，解决纯对话输出不可控、难追溯的问题

  - 商品评价分析、竞品对比类Agent系统可参考双层图架构：底层用不可变语料层存储原始证据，上层用可编辑推理层存储分析结论，平衡溯源性与分析灵活性

  - 多源信息核验类应用可复用权限设计：LLM仅输出候选编辑建议，经人类确认后再更新推理状态，避免LLM幻觉污染最终结论'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM与人类协同处理文档类推理任务时，交互以线性对话为主，论辩结构隐含在文本中，难以维护、对比、修订，专家需手动跟踪多来源证据的关联关系，易出现判断误差，缺乏统一的结构化共享状态支撑人机协同推理。

### 方法关键点
- 基于Toulmin论辩模型构建双层 typed 图架构：底层为不可变语料图，存储从文档提取的claim/grounds/warrant/backing/qualifier/rebuttal六类节点及关联边，完整保留原始溯源信息；上层为可编辑查询图，存储当前分析的推理状态
- 定义封闭操作集：人类可直接执行节点增删改、分组、评估等操作，LLM仅能输出候选编辑建议，需人类确认后才更新查询图，保证人类对推理过程的完全控制权
- 系统实现三类协同视图：语料面板溯源原始文档、论辩视图展示组件语义聚类、工作台支持论辩结构的编辑、对比、测试

### 关键实验
基于Qwen2.5 14B完成语料抽取，GPT-5.1-nano支撑交互推理，覆盖情报、法律、医疗3个真实场景验证，4名跨领域专家测试均认可系统论辩结构匹配现有工作流程，可大幅降低多源证据关联维护成本。

### 最值得记住的结论
将论辩结构本身作为人机共享的可交互状态，比纯文本对话交互更适合需要证据溯源、对比修订的复杂推理场景。
