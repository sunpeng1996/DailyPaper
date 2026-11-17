---
title: 'Revisiting What Makes a Good Context Subset: A Sparse Latent Basis Perspective'
title_zh: 从稀疏隐基视角重新审视大模型上下文子集的选择标准
authors:
- Cen-Jhih Li
- Siddhant Chaudhary
- Aditya Bhaskara
affiliations:
- University of Utah
arxiv_id: '2611.19220'
url: https://arxiv.org/abs/2611.19220
pdf_url: https://arxiv.org/pdf/2611.19220
published: '2026-11-14'
collected: '2026-11-17'
category: LLM
direction: 大模型ICL演示样本选择优化
tags:
- In-Context Learning
- Demonstration Selection
- Sparse Reconstruction
- LLM Inference
- Retrieval Strategy
one_liner: 提出稀疏隐基视角的RES上下文选择方法，明确不同检索目标的适用边界与表征适配规律
practical_value: '- 电商情感分析、用户意图分类等query可暴露需求的任务，可直接替换MMR为RES选择ICL演示样本，情感类任务实测可提升1-3pct准确率，工程实现复杂度与MMR持平

  - 检索表征可按需选择：Top-k语义检索优先用LLM中层隐态，RES/MMR这类互补性检索优先用LLM最后一层隐态，无需盲目引入第三方通用语义编码器

  - 模板化强的业务任务（如电商活动规则问答、结构化属性抽取）直接用Top-k相关性检索即可，无需复杂互补性选择，降低工程成本

  - 知识密集型Agent任务若query未暴露所需推理路径（如常识问答、多跳推理），直接放弃基于query的demo检索，改用零样本或工具调用，避免性能反而下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM推理中上下文子集选择对效果影响显著，但现有ICL演示选择方法的有效原理不明，相关性、多样性等优化目标的适用边界模糊，不同任务、表征下的策略适配无明确指导，落地时存在大量试错成本。

### 方法关键点
- 提出稀疏隐基假设：有效演示子集的表征线性组合可近似重构目标query表征，用集合对query的解释度衡量互补性，替代传统成对样本相似度的多样性度量。
- 设计RES贪心检索流程：迭代选择与当前query残差余弦相似度最高的样本，减去已解释分量更新残差，复杂度与MMR持平，无需额外预计算。
- 覆盖三类表征对比：通用Sentence Transformer embedding、LLM中层隐态、LLM最后一层隐态，验证不同检索目标的表征适配性。

### 关键结果
实验覆盖7个基准（情感分类、NLI、推理任务）、8个2B-8B参数开源LLM，对比BM25、Top-k、MMR、随机选择基线：
1. RES在56组模型-数据集配对中34组优于MMR，情感类任务准确率比MMR平均高1pct左右。
2. 模板化推理任务（MathQA/AQUA）上Top-k相关性检索效果最优，准确率增益比RES高2-6pct。
3. 知识密集型任务StrategyQA上所有检索方法平均准确率低于零样本，验证query未暴露所需推理链时检索会降效。
4. 表征适配规律：中层隐态对Top-k检索效果最优，最后一层隐态对RES/MMR等互补性检索效果最优。

最值得记住的结论：不存在通用最优的上下文选择策略，需根据任务特征、所用表征匹配对应检索目标。
