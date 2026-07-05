---
title: A Good Talk Does not Look Like a Summary, It Teaches You! Measuring Takeaways
  from Paper-to-Video Talks
title_zh: 面向论文转讲解视频的教学价值度量与评估框架
authors:
- Ishani Mondal
- Aparna Garimella
- Ananya Sai
- Pannaga Shivaswamy
- Jordan Boyd-Graber
affiliations:
- University of Maryland, College Park
- Adobe Research
arxiv_id: '2606.28531'
url: https://arxiv.org/abs/2606.28531
pdf_url: https://arxiv.org/pdf/2606.28531
published: '2026-06-26'
collected: '2026-07-05'
category: Eval
direction: 生成内容评估 · 讲解视频教学质量度量
tags:
- Evaluation Metric
- Generative Content
- Instructional Video
- Content Quality
- LLM Application
one_liner: 提出EffectivePresentationScorer框架，从教学有效性维度度量论文生成讲解视频质量
practical_value: '- 可迁移评估思路到电商生成类内容（商品讲解视频、种草文案）：放弃仅命中关键词的评估逻辑，新增用户理解度维度，衡量内容是否能传递核心卖点、打消决策疑问

  - 可直接复用4维评估框架（概念落地/前置知识满足/连贯性/可回答性），优化RAG问答、Agent客服回复的效果评估体系，替代单一相关性指标

  - 可基于论文结论优化生成prompt：强制要求生成内容补充必要前置背景、补充因果逻辑链，避免仅堆砌信息，提升用户接受度'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有论文自动生成讲解视频的评估指标仅关注视觉质量、核心内容点是否出现，完全不衡量观众是否能真正理解内容，无法对视频的教学传递价值进行有效评估。
### 方法关键点
提出EffectivePresentationScorer评估框架，从4个核心维度衡量教学质量：1）概念落地度：核心观点是否解释清晰；2）前置知识满足度：是否补充必要的背景概念；3）逻辑连贯性：技术细节是否与论文核心贡献建立关联；4）可回答性：是否能清晰解答核心方法的生效逻辑。
### 关键结果
对现有主流论文转视频系统测试显示：传统评估指标给分普遍达0.85+，但新框架发现生成视频普遍存在前置概念缺失、未解释方法底层逻辑的问题，这类影响用户理解的缺陷完全被传统指标忽略。
