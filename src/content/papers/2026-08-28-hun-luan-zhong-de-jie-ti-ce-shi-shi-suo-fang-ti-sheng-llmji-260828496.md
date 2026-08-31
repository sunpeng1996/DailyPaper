---
title: 'Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve
  LLM Machine Translation'
title_zh: 《混乱中的阶梯：测试时缩放提升LLM机器翻译的时机、方式与机制》
authors:
- Di Wu
- Sergey Troshin
- Christof Monz
- Antske Fokkens
- Vlad Niculae
affiliations:
- University of Amsterdam
- Vrije Universiteit Amsterdam
arxiv_id: '2608.28496'
url: https://arxiv.org/abs/2608.28496
pdf_url: https://arxiv.org/pdf/2608.28496
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM测试时优化 · 机器翻译
tags:
- Test-Time Scaling
- Large Language Models
- Machine Translation
- Sequential Sampling
- Best-of-N
one_liner: 对比LLM机器翻译场景下两类测试时缩放范式的效果，拆解顺序采样的优劣与底层作用机制
practical_value: '- 做多语种电商业务（商品文案翻译、多语种标题生成）时，小采样预算优先选顺序采样范式，可获得更优的生成流畅度与多样性

  - 顺序迭代生成的优化逻辑可迁移到Agent输出精炼流程，优先保障生成自然度的场景可直接复用该范式

  - 高推理预算下使用顺序采样要额外增加准确性校验环节，避免过度润色引发事实性错误'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM测试时缩放的顺序、并行两类范式在机器翻译任务中的效果差异、作用机制尚不明确，现有复杂实现无法隔离单个组件的贡献，难以指导落地选型。
### 方法关键点
1. 对比并行i.i.d采样+重排序、顺序迭代采样两类范式的翻译表现，结合人工多维度评估、控制变量消融实验拆解底层机制；
2. 控制采样预算、温度、上下文构造等变量做对照验证。
### 关键结果
- 小采样预算下顺序采样性能天花板更高，样本多样性、有效性显著优于并行范式；
- 顺序采样可大幅提升翻译流畅度与自然度，但推理预算过大时会降低翻译准确率；
- 顺序自提升的效果部分来自模型可访问更大的目标侧上下文，对不同采样温度鲁棒，但对上下文构造高度敏感。
