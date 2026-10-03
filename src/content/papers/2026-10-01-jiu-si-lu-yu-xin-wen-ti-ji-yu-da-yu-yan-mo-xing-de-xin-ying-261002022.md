---
title: 'Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation'
title_zh: 旧思路遇新问题：基于大语言模型的新颖性评估不稳定性研究
authors:
- Noy Sternlicht
- Simra Shahid
- Peter Jansen
- Daniel S. Weld
- Pao Siangliulue
- Tom Hope
affiliations:
- Hebrew University of Jerusalem
- Allen Institute for AI
- Microsoft
- University of Arizona
- University of Washington
arxiv_id: '2610.02022'
url: https://arxiv.org/abs/2610.02022
pdf_url: https://arxiv.org/pdf/2610.02022
published: '2026-10-01'
collected: '2026-10-03'
category: Eval
direction: LLM评测 · 新颖性评估
tags:
- LLM_Evaluation
- Novelty_Detection
- Prompt_Engineering
- Automated_Ideation
- Benchmark
one_liner: 系统揭示LLM新颖性评估的高不稳定性，微小prompt改动可导致准确率波动超50个点
practical_value: '- 做电商AI生成文案、商品创意、推荐策略的新颖性评估时，不能直接依赖单条prompt的LLM打分结果，必须固定prompt模板并做人工校准，避免结果大幅波动

  - 内部用LLM做创意筛选的pipeline中，不要盲目加检索、CoT推理模块提升新颖性评估准确率，实测增益极低，优先做prompt鲁棒性验证

  - 对外宣称的生成系统新颖性提升指标需要做跨prompt、跨LLM模型的鲁棒性测试，避免结果不可复现'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前自动化创意生成系统普遍用LLM做输出新颖性评估，但这类评估器大多临时搭建，仅在人工撰写文本上验证，未在待打分的生成内容上校准，效果存疑。

### 方法关键点
自动构建评测数据集，从OpenReview挖掘审稿人一致明确认可/否认原创性的论文摘要极值样本，匹配普通LLM生成的创意对；测试6种不同LLM新颖性评估器，控制prompt、是否加检索、推理预算等变量。

### 关键结果
微小prompt改动可导致超过50%的相同创意对评估结果反转，pairwise准确率波动超50个点，甚至低于随机水平；同类改动对不同评估器效果正负相反；新增检索模块、增加推理步长增益极小，专用新颖性评估器表现反而不如成本最低的prompt baseline。
