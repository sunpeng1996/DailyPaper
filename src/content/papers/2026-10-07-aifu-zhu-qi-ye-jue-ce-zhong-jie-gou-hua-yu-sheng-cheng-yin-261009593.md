---
title: 'Structured pre-generation elicitation versus single-shot prompting in AI-assisted
  enterprise decision-making: a randomised online experiment'
title_zh: AI辅助企业决策中结构化预生成引导与单次提示的随机在线实验
authors:
- William Scott-Jackson
affiliations:
- Oxford Centre for Impact Research
arxiv_id: '2610.09593'
url: https://arxiv.org/abs/2610.09593
pdf_url: https://arxiv.org/pdf/2610.09593
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM prompt优化 · 企业决策辅助
tags:
- PromptEngineering
- Metacognition
- AIDecisionMaking
- EnterpriseAI
- UserEngagement
one_liner: 验证生成前结构化元认知引导层可大幅提升AI辅助企业决策的输出质量与用户参与度
practical_value: '- 做Agent决策模块、LLM辅助商家运营工具时，可在调用LLM生成内容前加入结构化引导步骤，先让用户明确上下文、核心诉求、策略方向，可大幅降低离题输出比例，兜底弱prompt效果

  - 针对普通用户prompt质量参差不齐的场景（比如商家用AI写商品详情页、运营用AI做活动方案），预生成引导环节可将离题输出占比从34%降至5%，兜底收益显著

  - 对响应速度要求不高的非实时场景（比如商家开店指导、中长期运营策略生成），可接受23%左右的耗时增加，换取32%的输出质量提升，投入产出比可观'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成式AI辅助专业工作时易出现用户认知 surrender 问题：用户同时委托AI生成与评估答案，易接受低质量输出、减少对底层逻辑的参与，现有干预方案均脱离工作任务本身，落地性差。
### 方法关键点
在AI生成前增加交互式元认知引导层，要求用户先完成三步操作：澄清上下文、选择策略方向、解释自身推理，再触发AI生成；通过400人随机在线实验对比单次prompt与该引导方案的效果，输出由2名LLM评分员+1名人类评分员按4个维度打分。
### 关键结果
平均综合质量提升32%，离题输出占比从34%降至5%；若用户原始prompt已明确核心问题，质量仍可提升21%；用户参与度更高，平均耗时仅增加2.4分钟（总耗时10.46分钟）；质量提升集中在权衡表述、战略一致性维度，技术特异性无明显增益。
