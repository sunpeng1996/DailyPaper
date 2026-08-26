---
title: 'Knowing When to Ask for Help: Bayesian Self-Escalation in Hierarchical LLM
  Agents'
title_zh: 分层LLM Agent的贝叶斯自升级机制：自主判断何时请求强模型协助
authors:
- Nadeem Shaikh
affiliations:
- Independent Researcher, Melbourne, Australia
arxiv_id: '2608.24087'
url: https://arxiv.org/abs/2608.24087
pdf_url: https://arxiv.org/pdf/2608.24087
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: 分层Agent协作 · 贝叶斯自升级决策
tags:
- LLM Agent
- Hierarchical Agents
- Optimal Stopping
- Uncertainty Quantification
- Model Cascade
one_liner: 将LLM生成中途的升级决策建模为贝叶斯最优停止问题，实现比预/后路由更高的成本效率
practical_value: '- 可直接复用在电商营销文案生成、推荐理由生成、智能客服等大小模型级联场景：小模型生成中途实时检测置信度，失败就提前切大模型，不用等全生成完成，既降算力成本又减响应延迟，文本级上下文切换兼容任意模型架构，无需改造现有推理栈

  - 路由优化优先级调整：优先优化能力后验的校准度（最小化Brier score，用等张回归/温度scaling做事后校准），收益远高于调整决策阈值，重点优化「自信错误」样本的识别，避免低置信度漏判和高置信度错判带来的业务损失

  - 工程落地门槛极低：推理阶段每步仅做O(1)的后验更新和阈值判断，开销可忽略；离线仅需少量标注的生成成败轨迹（百级样本即可）即可训练后验模型，无需重训大小模型，可快速适配不同业务场景'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有分层LLM部署的路由决策要么在请求前基于query选择模型，要么在全量生成完成后判断是否重跑，均无法在生成中途识别当前模型能力不足、提前切换强模型，既浪费算力也提升了响应延迟，缺乏可解释、有理论保障的中途升级决策框架。
### 方法关键点
- 将生成中途的升级决策建模为有限horizon的贝叶斯最优停止问题：小模型维护能力后验$B_t = P(自身最终生成正确|当前观测)$，每步更新，当继续生成的期望成本超过升级成本时触发切换
- 能力后验不从原始token熵直接计算，而是从标注的生成成败轨迹中学习得到，避免「自信错误」（熵低但生成结果错误）的核心失效问题
- 推导得到闭形式的近视升级阈值，以及动态规划的最优策略，证明最优策略为每步对$B_t$设置时变阈值，无需对原始信号做似然单调性假设
- 升级时仅传递文本级上下文（部分生成结果、工具调用记录、检索证据等），无需跨模型同步KV cache或隐状态，兼容任意模型架构
### 关键结果
- 模拟实验：同等计算成本下，最优策略准确率比固定熵阈值路由高5pct，比事后路由成本低20%+，仅需40%的升级率即可达到96%的准确率
- 真实代码生成任务（Qwen2.5-Coder 1.5B→7B，MBPP数据集）：要达到75%准确率，流式中途升级比事后路由省30.2%的总计算量，仅用小模型98%的算力就实现了12.7pct的准确率提升，升级率仅37%
### 核心结论
对于分层LLM系统的路由优化，能力后验的校准效果收益远高于决策规则的优化，「自信错误」是最核心的失效模式
