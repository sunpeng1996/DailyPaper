---
title: LLM Program Optimization via Retrieval Augmented Search
title_zh: 基于检索增强搜索的大语言模型程序优化方法
authors:
- Sagnik Anupam
- Alexander Shypula
- Osbert Bastani
affiliations:
- University of Pennsylvania
arxiv_id: '2501.18916'
url: https://arxiv.org/abs/2501.18916
pdf_url: https://arxiv.org/pdf/2501.18916
published: '2026-06-22'
collected: '2026-07-01'
category: LLM
direction: LLM代码优化 · 检索增强搜索
tags:
- Retrieval Augmented Search
- Code Optimization
- Beam Search
- In-context Learning
- Atomic Edits
one_liner: 提出检索增强搜索RAS与原子编辑引导搜索AEGIS，无需微调即可黑盒优化LLM生成代码的运行效率
practical_value: '- 做RAG召回时可参考上下文检索思路：先让LLM生成待处理内容的语义摘要（而非直接编码原始内容）再做向量检索，能提升召回匹配精准度，可用于推荐系统召回用户历史行为对应优化策略、Agent调用工具的历史案例等场景

  - 迭代式优化任务可复用RAS的beam search+逐轮检索优化框架：每轮基于当前最优结果召回最相关案例，生成候选后选最优进入下一轮，适用于生成式推荐文案迭代、Agent任务规划调优等场景

  - 若需优化结果可解释性、降低修改幅度，可参考AEGIS的原子编辑思路：先把历史优化案例拆成可复用的带语义描述的最小优化单元，每次只应用单个原子编辑，适合电商推荐规则迭代、广告文案精细化调优，改动能追溯、风险低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM原生做程序优化效果不佳，传统端到端动态代码检索的黑盒优化方案未借鉴编译器分步优化思路，召回依赖原始代码嵌入，匹配精准度低，且生成的优化改动幅度大、可解释性差。

### 方法关键点
- RAS框架：用上下文检索替代代码直接检索，先调用LLM生成待优化程序的核心算法、数据结构自然语言描述，再基于描述嵌入召回相似慢-快程序对作为in-context示例；每轮执行beam search，召回k个示例生成k份优化代码，筛选出最快且通过测试的版本进入下一轮，迭代m步输出最优结果
- AEGIS增强方案：预训练阶段将历史慢-快程序对拆解为带语义描述的原子优化编辑，每个编辑对应单步小改动+通用优化说明；推理时复用RAS框架召回原子编辑，引导LLM做增量优化，大幅提升结果可解释性

### 关键结果
在C++ PIE基准、Python Mercury基准测试，对比动态检索等SOTA黑盒优化方案：RAS在PIE上用DeepSeek 3.2达到9.18×平均加速，性能是SOTA动态检索的2.06倍；在Mercury上把Qwen2.5-7B-Instruct的平均运行时百分位提升10.27，显著缩小与大模型的性能差距。AEGIS用GPT-4o达到6.08×平均加速，性能是基线的1.37倍，相比RAS降低17%平均编辑距离，改动更小可追溯。

最值得记住：基于语义摘要的上下文检索+逐轮迭代搜索的思路，对所有需要召回历史案例做优化的生成任务都具备普适性，效果远优于直接对原始内容做召回的方案。
