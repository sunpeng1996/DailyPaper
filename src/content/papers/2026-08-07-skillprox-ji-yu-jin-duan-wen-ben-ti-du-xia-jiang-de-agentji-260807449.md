---
title: 'SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent'
title_zh: SkillProx：基于近端文本梯度下降的Agent技能自演化框架
authors:
- Mingxuan Zheng
- Yujin Zhou
- Chuxue Cao
- Boqin Yin
- Yuyao Zhang
- Jiapeng Sun
- Shuaishuai Gong
- Sirui Han
- Yike Guo
affiliations:
- Hong Kong University of Science and Technology
- Macau University
arxiv_id: '2608.07449'
url: https://arxiv.org/abs/2608.07449
pdf_url: https://arxiv.org/pdf/2608.07449
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent技能优化 · 文本空间自演化
tags:
- LLM Agent
- Skill Evolution
- Textual Gradient
- Proximal Gradient
- Self-optimization
one_liner: 结合闭环诊断更新与效用感知近端剪枝，在文本空间优化Agent可复用技能，兼顾效果与复杂度
practical_value: '- 迭代优化Agent业务技能（如客服应答规则、选品判定逻辑）时，可加同批次重执行校验门：补丁生成后回刷同批历史任务，仅保留效果不下降的更新，避免看似合理的语义补丁导致线上效果退化

  - 定期对RAG知识库、Agent技能库做留一法效用审计：将内容拆分为独立知识单元，逐一移除测试对效果的影响，删除负效用、零效用单元，既能缩短上下文长度降低推理成本，还能提升跨场景泛化性

  - 小模型部署Agent时可适当保留更多参考规则：实验显示同任务下4B模型需要的参考内容长度是27B模型的2倍，小模型对辅助规则的依赖更强，无需强行对齐大模型的技能压缩率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent技能演化方法存在两大痛点：一是技能补丁仅通过语义合理性判定就直接合并，未验证实际执行效果，易引入负向规则；二是迭代补丁持续扩张技能长度，积累重复、冲突、过拟合单任务的内容，既增加上下文成本，又会干扰正常推理，降低技能泛化性。
### 方法关键点
- 前向闭环更新：每生成候选补丁后，在同批次训练任务上重执行，仅当硬准确率、单元准确率均不低于原技能时才保留更新，否则回滚并将失败原因反馈给后续诊断，从源头拦截负向更新。
- 后向近端剪枝：将技能拆解为独立知识单元，通过留一法在验证集上计算每个单元的边际效用，按效用从低到高尝试合并、降级、删除操作，仅保留满足准确率约束且降低复杂度的操作，清理冗余内容。
- 整体受近端梯度下降启发，前向阶段优化任务效果，后向阶段做复杂度正则，全程无需更新LLM权重，仅在文本空间迭代优化可复用技能。
### 关键实验
在SpreadsheetBench（域内）、WikiTableQuestions、HiTab（跨域）三个基准上测试，对比SkillGrad、SkillOpt等6个基线，覆盖3个不同量级Qwen backbone，平均准确率比最强基线高3.0pp；通过效用剪枝最多可压缩75%的技能长度，同时准确率仅下降1pp以内，移除负效用单元最多可提升准确率8pp。
### 核心结论
Agent技能并非越长越好，语义合理的补丁不一定能带来实际效果提升，必须结合执行反馈和效用审计才能得到轻量、泛化性好的可复用技能。
