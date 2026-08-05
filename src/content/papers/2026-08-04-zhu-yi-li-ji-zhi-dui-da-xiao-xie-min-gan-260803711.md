---
title: Attention is Case-Sensitive
title_zh: 注意力机制对大小写敏感
authors:
- Maximilian Dillitzer
- Tin Stribor Sohn
- Jason J. Corso
- Michael Auerbach
affiliations:
- University of Applied Science Esslingen
- Karlsruhe Institute of Technology
- Dr. Ing. h.c. F. Porsche AG
- University of Michigan
arxiv_id: '2608.03711'
url: https://arxiv.org/abs/2608.03711
pdf_url: https://arxiv.org/pdf/2608.03711
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM特性研究 · 零样本注意力调控
tags:
- attention_mechanism
- zero_shot
- LLM_characteristic
- VLM
- prompt_engineering
one_liner: 通过13款LLM/VLM实验验证字母大小写可零样本调控模型内部注意力并揭示效果边界
practical_value: '- Prompt工程层面：可将用户核心诉求、推荐规则等关键内容转大写格式，零成本提升LLM对关键指令的注意力权重，无需微调

  - RAG场景增强：给返回的TopN高优先级商品/内容的标题核心字段加大写格式强调，提升生成式推荐/问答对高相关内容的采纳率

  - 多模态商品理解场景：对VLM输入prompt里的目标检测/属性抽取关键词做大写调整，可引导跨模态注意力向目标商品区域偏移，降低无关图像干扰

  - 注意适用边界：推理类LLM的CoT思考阶段会抵消大小写效应，不要在推理类Agent流程中用大小写做强调，无收益甚至负向'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
人类视觉感知中大写文本是天然的显著性线索，可从上下文中捕获注意力，此前无系统研究验证LLM/VLM是否存在类似的大小写调控注意力的效应，也未明确其对下游任务的影响边界。
### 方法关键点
覆盖9款LLM、4款VLM共13个采用不同分词方案的模型，对比小写上下文下目标文本采用全大写、交替大小写等格式时的内部注意力权重变化、下游任务准确率差异，同时探索推理模型、VLM场景下的效应边界。
### 关键结果
1. 所有非推理类LLM普遍存在大小写效应：目标文本转大写/交替大小写可显著提升其注意力权重，零样本无需任何模型修改
2. 注意力提升不必然带来准确率增益，高熵交替大小写场景甚至会降低任务精度
3. 推理类LLM的思考阶段会抵消大小写敏感性，效应消失
4. VLM中大小写调整一方面引导注意力从图像向文本偏移，另一方面让剩余视觉注意力集中到目标区域
