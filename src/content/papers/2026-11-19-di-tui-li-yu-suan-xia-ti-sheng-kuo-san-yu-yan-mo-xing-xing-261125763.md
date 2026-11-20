---
title: Closing Performance Gap for Diffusion Language Models under Low Inference Budgets
title_zh: 低推理预算下提升扩散语言模型性能的无训练框架CaRR
authors:
- Hao Wu
- Sipeng Chen
- Jingwen Fu
- Yuwang Wang
affiliations:
- University of Wisconsin–Madison
- Northwestern University
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
- Tsinghua University
arxiv_id: '2611.25763'
url: https://arxiv.org/abs/2611.25763
pdf_url: https://arxiv.org/pdf/2611.25763
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 扩散语言模型 · 低推理预算优化
tags:
- Diffusion Language Model
- Inference Optimization
- Training-free
- Low Budget
- Text Generation
one_liner: 无训练框架CaRR在不增加骨干推理步数的前提下，大幅提升低预算下扩散语言模型生成准确率
practical_value: '- 生成式推荐/Agent代码调用场景可复用SCR轨迹回溯策略：保存生成中间状态，最终输出不合规时从近到远回溯有效状态，无需重跑推理即可降低输出错误率，额外
  latency 开销低于5%

  - 并行生成类模型（如营销文案/商品标题批量生成）可复用TCR延迟提交策略：对低置信度token先mask，利用下一次已调度前向的更新上下文填充，无需增加推理步数即可提升生成一致性

  - 结构化输出场景（如商品属性生成、广告文案合规校验）可复用任务专属轻量校验逻辑：在CPU侧做提交前的格式校验+恢复，几乎无额外成本即可提升输出合规率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持多token并行生成，理论上比逐token自回归解码推理成本更低，是低延迟生成场景的重要技术路线。但现有DLM在减少去噪步压缩推理预算时，生成质量会出现显著衰减；已有的 editable DLM 优化方案仅依赖最终输出，会浪费生成轨迹中的有效中间结果，低预算下的性能缺口一直没有低成本的解决方法。
### 方法关键点
- 训练-free的CaRR框架可直接挂载到现有ME-DLM等可编辑扩散模型上，全程复用原生推理调度，无额外骨干模型前向开销
- Token Commitment Remasking（TCR）：筛选原生编辑动作中旧token支持度低于阈值的纯替换位置，暂不直接替换为预测token，而是先填MASK，等下一次调度的前向时用更新后的上下文重新预测填充，避免并行编辑的上下文不一致问题
- Submission Commitment Recovery（SCR）：保存完整的生成轨迹，当最终输出不符合任务格式要求时，按从后往前的顺序回溯中间状态，通过任务专属规则（代码AST校验、数学答案等价性校验）恢复有效输出
### 关键结果
在代码生成（HumanEval、MBPP）和数学推理（GSM8K、MATH-500）4个基准数据集上，对比原生ME-DLM、CoRe、KLASS等同推理步数基线：1/8全量预算下，6项指标平均准确率提升7.44pp，其中MBPP、MBPP+分别提升11.37pp、10.05pp；1/4预算下平均提升4.97pp，收益随预算升高逐步降低，全量预算下仅提升0.36pp。
### 核心结论
低预算并行生成优化不需要修改模型训练，通过延迟提交低置信度token、复用中间生成轨迹做恢复，就能以可忽略的额外成本拿到大幅性能收益。
