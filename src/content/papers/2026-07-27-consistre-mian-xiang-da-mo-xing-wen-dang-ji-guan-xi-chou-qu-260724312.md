---
title: 'CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation
  Extraction with Large Language Models'
title_zh: CONSISTRE：面向大模型文档级关系抽取的统一一致性感知框架
authors:
- Mingxuan Sun
affiliations:
- Université de Sherbrooke
arxiv_id: '2607.24312'
url: https://arxiv.org/abs/2607.24312
pdf_url: https://arxiv.org/pdf/2607.24312
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 大模型关系抽取 · 一致性优化
tags:
- Document-Level RE
- Knowledge Distillation
- GRPO
- Self-Reflection
- Consistency Modeling
one_liner: 提出双轨一致性感知框架，同时覆盖黑盒LLM推理优化和小模型蒸馏对齐的文档级关系抽取场景
practical_value: '- 电商商品/评论/订单的结构化信息抽取场景，可直接复用推理侧方案：先把业务规则（如产地传递性、属性唯一性）转成结构化约束，加进Prompt+迭代校验，无需微调即可降低抽取结果的矛盾率

  - 小模型落地抽取类任务时，可复用蒸馏+GRPO对齐的pipeline：用大模型生成带推理过程的标注，黄金标签对齐输出后做SFT，再把业务规则约束加入奖励函数做RL对齐，仅需少量标注即可缩小和大模型的性能gap

  - Agent的工具调用/信息抽取结果校验场景，可复用本文的一致性评分逻辑：把业务互斥/依赖规则转成可量化的校验项，替代无边界的自反思，大幅减少幻觉导致的错误输出

  - 知识蒸馏阶段可复用「黄金标签对齐大模型推理轨迹」的trick：既能让小模型学到正确的推理逻辑，又能保证输出严格符合业务标注规范，避免大模型幻觉污染训练数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型做文档级关系抽取（DocRE）时默认逐三元组独立预测，普遍违反传递性、逆关系对称、函数唯一性等基础关系约束，输出矛盾不可靠；同时业界缺乏统一的一致性优化方案，无法同时覆盖黑盒大模型API调用、小模型本地部署两类主流场景。
### 方法关键点
- 统一一致性建模：定义三类通用关系约束，计算0-1的一致性评分，作为推理侧校验信号和训练侧奖励项，跨双轨通用
- 推理侧优化（面向黑盒LLM）：先通过带约束提示的Prompt生成初始三元组，再用约束校验模块定位具体矛盾类型，引导LLM做针对性迭代修正，全程无需微调
- 训练侧优化（面向小模型落地）：先由大模型教师生成带一致性校验过程的推理轨迹，用数据集黄金标签对齐输出后做SFT蒸馏；再基于GRPO做RL对齐，奖励函数同时加权抽取F1、一致性得分、格式合规性，把约束能力注入小模型
### 关键结果
在DocRE基准数据集DocRED上测试：
1. 推理侧方案用Gemini-2.5 Pro 5-shot+CoT+自修正F1达0.543，比Reflexion、CoVe等通用自反思方法F1高0.2左右，无规则锚点的通用自反思反而会降低抽取效果
2. 训练侧方案蒸馏得到的Qwen3-8B模型F1达0.492，仅比GPT-5.2推理侧结果低0.038，推理成本仅为proprietary大模型的1%量级
> 最值得记住：结构化规则驱动的针对性校验修正效果远好于无边界的通用自反思，一致性约束既能在推理侧零成本提效，也能通过蒸馏对齐注入小模型，兼顾效果和部署性价比
