---
title: 'Skill Issue: Are Skills Language-Invariant in LLMs?'
title_zh: 技能差异：大语言模型的技能是否具备语言不变性？
authors:
- Bobby Cheng
- Adam Gaber
- Zhengyuan Liu
- Catherine Arnett
- Omer Goldman
- Cheston Tan
- Leshem Choshen
affiliations:
- NA*STAR
- Weizmann Institute of Science
- MIT-IBM Watson AI Lab
- University of Cambridge
- EleutherAI
arxiv_id: '2608.25832'
url: https://arxiv.org/abs/2608.25832
pdf_url: https://arxiv.org/pdf/2608.25832
published: '2026-08-25'
collected: '2026-08-27'
category: LLM
direction: 大语言模型 · 跨语言能力评估
tags:
- LLM
- Cross-lingual Evaluation
- Self-play
- Reasoning
- Skill Assessment
one_liner: 通过多语言自博弈框架量化LLM跨语言技能差异，证明语言选择显著影响模型决策与推理能力
practical_value: '- 跨境多语言电商/推荐Agent落地时，可将小语种用户请求的中间CoT推理环节切换为模型表现更优的语言（如英语），快速提升推理准确率，降低无效决策占比

  - 评估多语言LLM业务能力时，不能仅参考通用基准分数，需结合自身场景（如商品属性理解、营销活动决策）做分语言的专项技能测试，避免线上效果落差

  - 开发多语言Agent时可复用文中多语言自博弈对比框架，低成本隔离语言变量对模型能力的影响，快速验证优化方案的效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM跨语言差异研究多聚焦知识一致性，缺少对推理、决策等通用技能层面差异的量化分析，难以为多语言模型业务落地提供可靠依据。
### 方法关键点
提出多语言自博弈评估框架，固定模型、对手、规则、状态空间、可选动作等所有变量，仅改变交互语言，完全隔离语言对模型实际技能表现的影响；扩展多语言版本TextArena benchmark，覆盖8种语言、6类博弈场景（空间推理、不完全信息决策、资源分配等），测试3款主流开源LLM。
### 关键结果
同一模型跨语言博弈胜率差异最高超70%，无效动作率差异超30%；空间推理、条件决策类技能的语言特异性损失最明显；仅将CoT中间推理语言切换为模型高表现语言，即可恢复80%以上的性能损失。
