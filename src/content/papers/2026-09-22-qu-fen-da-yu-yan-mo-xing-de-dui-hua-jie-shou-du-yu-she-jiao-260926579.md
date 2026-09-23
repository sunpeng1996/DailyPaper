---
title: 'Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in
  Language Models'
title_zh: 区分大语言模型的对话接受度与社交阿谀行为
authors:
- Calvin Isley
- Johann Gaebler
- Max Lamparth
- Julia Minson
- Sharad Goel
affiliations:
- Harvard University
- Stanford University
arxiv_id: '2609.26579'
url: https://arxiv.org/abs/2609.26579
pdf_url: https://arxiv.org/pdf/2609.26579
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM对齐 · 阿谀行为评测与优化
tags:
- LLM Alignment
- Sycophancy
- Evaluation
- Conversational Receptiveness
- Prompt Engineering
one_liner: 揭示现有社交阿谀评测混淆有益接受性表达的问题，提出兼顾独立判断与友好表达的方案
practical_value: '- 电商客服、咨询类Agent可直接复用「先锚定核心业务规则/结论，再改写为接受性表达」的生成范式，既不偏离业务要求，又大幅提升用户沟通体验，降低负反馈

  - 优化LLM回答的友好度、共情能力时，避免直接使用“请友好回答”这类笼统prompt，容易导致模型为了迎合用户违背业务规则/事实，先生成核心判断再改写的架构可完全规避该问题

  - 构建LLM行为对齐的评测指标时，需明确区分表层语言特征（共情、认可视角、委婉表达）与实质判断偏差，避免将对提升转化率、用户满意度有益的表达误判为有害的阿谀行为'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM社交阿谀（sycophancy）评测普遍将共情、认可用户视角、委婉表达等特征判定为阿谀行为，而这些特征恰恰是社会心理学中证实能大幅提升分歧场景沟通效果的对话接受性特征。两类行为的混淆会导致对齐工作错误惩罚有益的交互表达，甚至降低用户对LLM回答的接受度，既影响体验又可能提升用户流失率。
### 方法关键点
- 基于社会心理学H.E.A.R框架构建对话接受度自动评测指标，通过GPT-5.6 Luna对10项正负向语言特征打分后拟合人类标注结果，与人类评分相关度达0.48，优于现有politeness工具的0.34
- 设计控制变量实验：将人类/模型生成的回答改写为更具接受性的版本，但完全保留原实质判断，验证现有社交阿谀评测的构造效度问题
- 提出「接受性独立」的对齐方案：先让LLM输出独立的实质判断，再调用改写工具将回答调整为符合接受性特征的表达，完全隔离表达风格与实质判断
### 关键实验
基于Reddit r/AmITheAsshole（AITA-YTA）道德建议场景数据集开展实验：
1. 现有社交阿谀评分与接受度评分相关度达0.64，仅提升回答接受度、保留核心判断的改写，会使社交阿谀评分大幅上升，验证评测混淆问题
2. 预注册用户实验显示，用户对保留核心判断的高接受度回答偏好显著更高：人类回答改写后质量评分提升1.5分（7分制），用户认为提问者更愿意听取的评分提升1.0分（5分制）
3. 采用先锚定判断再改写的方案，可让Gemini 3.7 Flash、Claude Sonnet 5的接受度分别提升2.1、1.4个标准差，同时实质判断的偏差几乎无变化
### 核心结论
LLM的对话友好性与实质判断独立性完全可以兼顾，不需要为了保持判断中立牺牲用户交互体验
