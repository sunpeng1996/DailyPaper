---
title: 'All Explanations are Wrong, But Many Are Useful: Exploring the Rashomon Explanation
  Set with Large Language Models'
title_zh: 所有解释都有偏差但多数有用：基于LLM的Rashomon解释集探索
authors:
- Pan Li
affiliations:
- Georgia Tech
arxiv_id: '2607.09502'
url: https://arxiv.org/abs/2607.09502
pdf_url: https://arxiv.org/pdf/2607.09502
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: LLM多智能体·可解释AI性能优化
tags:
- XAI
- Agentic Workflow
- Rashomon Set
- LLM
- CTR Prediction
one_liner: 提出RashomonLLM智能体工作流，同时提升预测精度与XAI解释质量，打破精度-可解释性权衡
practical_value: '- 可直接复用Explanation-Prediction-Reflection三智能体迭代架构，解决LLM生成解释的幻觉与不稳定性问题，同时提升下游预测任务精度，适用于电商CTR预测、用户
  churn 预测等业务场景

  - LLM Feature Dropout 技巧可直接迁移：每次迭代随机隐藏20%输入特征引导LLM生成多样化解释，替代传统ensemble的特征采样，无需修改数据输入仅调整Prompt即可实现

  - Batch LLM Learning 机制解决大模型处理大规模工业数据的长上下文退化问题，通过分批次处理+哨兵行校验的方案，可低成本落地到千万级样本的推荐/广告业务中

  - 解释集聚合的多数投票策略可直接复用：对多轮生成的解释做语义级聚合提取共识规则，生成的解释可直接用于推荐理由生成、风控规则挖掘等需可解释性的业务环节'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有XAI方法普遍存在精度-可解释性权衡，三大缺陷限制落地：1）单一种解释在分布偏移下易失效；2）SHAP等标量归因无法捕捉非线性、条件依赖关系；3）事后解释与预测流程割裂，无法反哺预测性能。业务中既要可解释性满足合规、用户信任要求，又要保障预测精度不下降的需求长期无法被满足。

### 方法关键点
- 提出Rashomon解释范式：不追求单一最优解释，而是构造一组保真度高、可指导预测的解释集合，理论证明该集合非空，且解释保真度直接约束预测模型性能上限
- 设计RashomonLLM三智能体工作流：Explanation Agent通过随机特征dropout生成多样化自然语言解释；Prediction Agent基于解释做预测；Reflection Agent根据预测误差迭代优化解释Prompt，三者交替优化直至收敛
- 配套工程优化：Batch LLM Learning分批次处理大规模数据+哨兵行校验避免长上下文退化；多轮解释通过语义级多数投票聚合为最终可解释结果

### 关键实验
在客户流失分类、临床生存回归、快手直播大规模CTR预测三个任务上测试，对比SOTA XAI方法、专用深度CTR模型：CTR任务上比强基线DeepFM AUC提升2.1%，解释保真度提升37%；分布偏移下性能下降幅度仅为单解释方法的1/3，同时可输出全局特征重要性与单样本自然语言解释。

### 核心结论
可解释性与预测性能不是对立的trade-off，将解释与预测流程耦合迭代，二者可以形成互补，同时提升业务效果与用户信任
