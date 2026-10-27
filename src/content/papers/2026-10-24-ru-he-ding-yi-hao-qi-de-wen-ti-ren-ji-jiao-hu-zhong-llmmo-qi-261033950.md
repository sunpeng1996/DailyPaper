---
title: What Makes a Question Curious? Measuring Model Curiosity in Human-LLM Interactions
title_zh: 如何定义好奇的问题？人机交互中LLM模型好奇心的度量
authors:
- Angana Borah
- Rachana Ramchandar
- Inderjeet Nair
- Rada Mihalcea
affiliations:
- University of Michigan - Ann Arbor
- PES University, Bangalore
arxiv_id: '2610.33950'
url: https://arxiv.org/abs/2610.33950
pdf_url: https://arxiv.org/pdf/2610.33950
published: '2026-10-24'
collected: '2026-10-27'
category: LLM
direction: LLM人机交互 · 好奇心度量
tags:
- LLM
- Human-AI Interaction
- Curiosity Measurement
- Question Taxonomy
- User Engagement
- Annotation
one_liner: 提出理论驱动的LLM好奇心问题分类体系，验证其对提升用户探索参与的价值
practical_value: '- 电商导购Agent、学习类AI助手可复用论文的好奇心问题分类体系，优先在商品选购决策、文案创作、咨询类场景投放反思/探索型问题，提升用户停留时长和探索深度

  - 可复用「规则预过滤+LLM-judge分类」的标注流程，对大模型生成的提问做自动筛选，过滤无效、隐私试探类问题，降低用户反感

  - 借鉴有用好奇心预测框架，基于用户query的场景属性动态选择直接回答还是提问，平衡即时需求满足和长期参与度提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM已广泛作为协作伙伴应用于咨询、创作、学习等场景，现有研究大多聚焦其回答能力，对主动提问的价值研究不足。不同类型的提问对用户的影响差异极大，但目前缺乏统一的分类框架区分任务类提问和能激发探索的好奇心导向提问，也不清楚何时提问不会增加用户负担，反而能提升人机协作效率。

### 方法关键点
- 构建理论驱动的提问分类体系：将LLM向用户的提问划分为6类好奇心导向问题（信息缺口、因果解释、探索拓展、反思元认知等）、4类非好奇心任务/交互类问题、2类高风险问题，明确不同提问的功能边界
- 三级标注流程：规则预过滤生成类artifact → LLM-judge上下文分类 → 人工校验，标注准确率达87%以上
- 关联分析+用户实验：通过匹配分析、回归、IPW加权验证好奇心提问与用户参与的关联，再通过众包用户实验明确不同场景下的好奇心提问接受度，最后实现有用好奇心预测的POC模型

### 关键实验
基于WildChat、OASST1、LMSYS-Chat-1M、ShareGPT 4个公开对话数据集的分析显示：好奇心导向提问仅占所有LLM提问的17%~28%；对比匹配的非好奇心提问组，好奇心提问后用户的认知类表达提升7.2%~16.5%，LLM判定的用户好奇心提升9.5%~13.7%；用户实验显示反思、探索类提问在咨询、创意、研究场景接受度最高，而60%以上的场景用户更偏好直接回答。

### 核心结论
大模型不需要问更多问题，而是要学会在合适的场景提出低负担的高质量好奇心问题，平衡直接响应用户需求和激发深度探索的价值。
