---
title: Explicit Style Extraction for Personalized Long-Form Text Generation
title_zh: 面向个性化长文本生成的显式风格提取框架
authors:
- Jenitha Reddy Patel
- Sameeksha Kini
- Amulya Rayasam
- Anisa Dye
- Abhinav Sharma
- Sai Karthik Navuluru
- Bo Ni
- Li Li
- Junda Wu
- Tong Yu
affiliations:
- University of Chicago
- Adobe Research
- Amazon
- Vanderbilt University
- University of Southern California
arxiv_id: '2611.27211'
url: https://arxiv.org/abs/2611.27211
pdf_url: https://arxiv.org/pdf/2611.27211
published: '2026-11-19'
collected: '2026-11-23'
category: LLM
direction: 个性化长文本生成 · 显式风格建模
tags:
- PersonalizedGeneration
- StyleExtraction
- LongFormText
- LLMInference
- PromptEngineering
one_liner: 提出7大类28维风格分类体系与推理时风格引导方案，大幅提升个性化长文本生成效果
practical_value: '- 电商个性化文案（商品评论、种草内容、商家回复）生成场景，可直接复用STYLEPRISM的28维风格标签体系构建可解释的用户/品牌风格画像，无需自行梳理维度

  - 推理侧优化可借鉴SP-REFINE两阶段修订逻辑：先从用户历史样本显式抽取结构化风格Profile，再基于风格得分定向修订，无需微调即可提升风格匹配度，适合快速上线场景

  - 算力受限或高QPS场景可采用轻量SP-INFER单调用方案，风格保真度损失<5%的前提下推理成本降低75%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化长文本生成主流采用RAG思路，将用户历史文本直接塞入prompt让模型隐式学习风格，存在风格对齐不稳定、结果不可解释、无法定向修正风格问题的缺陷，无法满足电商评论、品牌文案、客服回复等对风格一致性要求高的场景需求。

### 方法关键点
- 提出STYLEPRISM风格分类体系，覆盖词汇选择、句法模式、语用 tone、结构组织、话语标记、格式布局、跨任务一致性7大类共28个可量化维度，每个维度提取时附带原文引用证据、禁用习惯字段，保证风格画像可验证
- 提出推理时优化方法SP-REFINE，分四步：先从top4检索到的用户历史样本中提取结构化风格Profile，再基于样本生成初稿，接着对照Profile修订初稿并给5类风格维度打分，最后针对得分≤3分的维度做定向二次修订，全程不修改内容事实
- 提供轻量变体SP-INFER，仅用单调用隐式学习风格，无需显式提取和修订，平衡效果和成本

### 关键实验
在LongLaMP基准的3个长文本任务（摘要生成、评论撰写、话题写作）上，用3款LLM（DeepSeek-V4-Flash、Grok-4.1-Fast、GPT-5.4-nano）测试，对比LongLaMP原生RAG基线：SP-REFINE在27组ROUGE、METEOR对比中25组胜出，平均相对提升10.2%，最高提升35.8%；LLM打分的风格保真度在8/9的模型-任务组合上优于基线，平均提升0.21分，且不损失内容质量。

最值得记住的结论：显式风格画像仅可作为修订引导，无法替代原始用户样本作为生成输入，直接用画像生成的效果在所有任务上均劣于基于样本生成的效果。
