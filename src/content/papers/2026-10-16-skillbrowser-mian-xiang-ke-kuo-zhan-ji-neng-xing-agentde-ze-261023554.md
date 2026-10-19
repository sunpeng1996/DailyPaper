---
title: 'SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents'
title_zh: SkillBrowser：面向可扩展技能型Agent的选择性技能曝光框架
authors:
- Jin Ye
- Yifan Jiang
- Lan-zhe Guo
affiliations:
- Nanjing University
arxiv_id: '2610.23554'
url: https://arxiv.org/abs/2610.23554
pdf_url: https://arxiv.org/pdf/2610.23554
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能管理与按需调用优化
tags:
- LLM Agent
- Skill Retrieval
- Meta Skill
- On-Demand Loading
- Selective Exposure
one_liner: 提出元技能管控的按需技能检索框架，解决大技能库下上下文污染与静态检索匹配错位问题
practical_value: '- 电商导购Agent/智能客服的大技能库（活动规则、售后流程、商品参数库等）可复用该框架，避免全量技能元数据挤占上下文预算，减少回答错误

  - 生成式推荐的prompt技能库（穿搭规则、优惠计算、文案模板等）可适配SkillGrep的多视图混合检索架构，提升技能召回准确率

  - 无需重新训练模型，仅通过植入固定Meta-Skill即可实现技能按需调用，可快速落地到现有Agent系统'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent依赖外部可复用技能扩展复杂任务能力，但主流范式存在核心缺陷：渐进式曝光会随技能库增长暴露大量元数据，挤占上下文预算并引入语义噪声；静态检索仅基于初始任务查询召回技能，易与推理过程中涌现的能力需求错位，还可能注入不必要技能干扰原本正确的推理。

### 方法关键点
- 植入训练无关的固定Meta-Skill：Agent可在推理过程中自主判断是否需要外部技能支持，生成包含能力描述、任务上下文、约束条件的结构化检索query
- 设计SkillGrep混合检索系统：离线为每个技能构建多维度可搜索视图（能力描述、使用条件、示例、输入输出Schema等），在线融合BM25 lexical匹配、多视图稀疏匹配、BGE dense匹配的排序结果，精准召回符合需求的技能
- 仅在Agent主动发起检索时才注入技能内容，完全解耦技能库规模与Agent可见上下文大小

### 关键实验
在SRA-Bench 6个子集（含定理应用、临床计算、多步工具调用等任务）、5种不同规模LLM上测试，对比静态BM25、静态SkillGrep、LLM Selection等基线：
- 整体准确率在26/30个测试设置下优于静态BM25，23/30个设置优于静态SkillGrep；在多步工具调用的ToolQA任务上准确率达43~61%，远超静态检索的17~39%
- 对Agent无需外部技能即可正确解决的样本，可降低不必要技能曝光，准确率平均提升4~10个百分点

最值得记住的一句话：技能库的可扩展性核心不是单纯提升检索准确率，而是要让Agent自主控制技能的加载时机与内容，避免不必要的上下文注入。
