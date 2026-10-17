---
title: 'Two Sample Sizes in Test-Time LLM Ensembling: Buffered ERM and Minimax Theory'
title_zh: 测试时LLM集成中的两类样本量：缓冲ERM与极小极大理论
authors:
- Zhi Zhang
- Arash A. Amini
affiliations:
- Department of Statistics and Data Science, UCLA
arxiv_id: '2610.21363'
url: https://arxiv.org/abs/2610.21363
pdf_url: https://arxiv.org/pdf/2610.21363
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: LLM测试时集成优化
tags:
- LLM Ensembling
- Test-time Scaling
- Empirical Risk Minimization
- Minimax Theory
- Model Ensemble
one_liner: 量化LLM测试时集成的两类样本量权衡，提出最优缓冲ERM并证明其极小极大误差边界
practical_value: '- 做多LLM生成内容（如电商文案、Agent回复）集成时，可参考两类样本量的权衡公式分配标注预算：标注数据不足时优先扩充标注问题数Q，标注充足后优先提升单问题生成数N

  - 集成权重学习可直接复用带校准边际缓冲的ERM方法，比普通ERM效果更稳定更优

  - 业务场景标注预算有限时，可参考三类性能区间划分选择采样策略，避免无意义的资源投入'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM测试时通过多生成结果聚合/多模型加权集成提升效果，但权重学习依赖两类核心样本量：标注问题数Q、单问题单模型生成数N，两者的权衡关系、最优采样策略未被量化。

### 方法关键点
从集成无限生成投票规则的群体误差切入，引入带校准边际缓冲的ERM方法学习集成权重，基于带指数β的边际条件推导误差上界，通过双模型双答案简化子模型的极小极大分析验证方法最优性。

### 关键结果数字
缓冲ERM的excess risk阶为$Q^{-1/2} + N^{-\beta/2}$（忽略对数因子）；存在三个性能区间：Q稀缺时误差由$Q^{-1/2}$主导，缓冲ERM为最优方法；中间区间跨问题pooling生成数收益更高，新增标注仅带来对数级提升；Q足够多时误差进入$N^{-\beta}$的下限，即使无限增加标注也无法进一步降低误差。
