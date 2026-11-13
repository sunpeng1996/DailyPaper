---
title: 'When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems'
title_zh: 双向适配场景下交互式大语言模型系统的评估挑战
authors:
- Hannah Li
arxiv_id: '2611.17239'
url: https://arxiv.org/abs/2611.17239
pdf_url: https://arxiv.org/pdf/2611.17239
published: '2026-11-12'
collected: '2026-11-13'
category: Eval
direction: LLM交互式系统 · 评估方法校准
tags:
- LLM Evaluation
- A-B Testing
- Offline Benchmark
- User Adaptivity
- Distribution Shift
one_liner: 明确交互式LLM离线评测与A/B测试的估计量差异，给出两者模型排序一致的充分条件
practical_value: '- 上线LLM驱动的对话推荐、智能导购Agent前，可使用论文提出的预实验筛查规则，仅用离线数据判断离线评测与A/B测试的模型排序是否一致，降低线上实验成本与风险

  - 对话式推荐/Agent的评估不能仅依赖固定prompt集的离线指标，需额外统计不同模型诱导的用户query分布变化（如简单咨询/复杂定制需求占比），避免用户适配带来的评估偏差

  - 优化业务指标时需区分两类提升：一是模型对同类型query的性能提升，二是模型诱导用户转向简单query带来的指标注水，从机制上规避reward hacking

  - 长周期A/B测试不要盲目丢弃burn-in期数据：若目标是评估长期稳态效果保留全量数据，若需对齐离线评测结论可参考早期交互数据'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
交互式LLM（如对话推荐、智能客服、Agent）的评估长期存在离线与线上结论不一致的问题：用户会根据模型输出调整prompt策略、任务类型与难度，导致模型实际接收的query分布内生变化，现有评估框架未考虑这种用户-模型双向适配的影响，容易导致错误的上线决策。
### 方法关键点
- 定义两类核心估计量：common-distribution effect（相同prompt分布下的模型性能差，为离线Benchmark、历史prompt回放等方法的估计目标）；induced-distribution effect（各模型在自身交互诱导出的prompt分布下的性能差，为线上A/B测试的估计目标）
- 推导两类估计量的排序反转条件：当common-distribution effect的绝对值小于query分布的总变分距离乘以新模型跨不同query的性能波动范围时，离线与线上的模型排序会反转
- 提出无部署的预实验筛查启发式算法：仅用离线历史数据即可判断是否需要开展线上A/B测试，无需提前部署新模型
### 关键结果数字
构造的邮件写作任务示例中，M1在所有固定prompt分布下性能均优于M0，但线上A/B测试中M1的两回合平均成功率比M0低5.5pp，出现完全排序反转；当用户prompt对模型响应的敏感度与模型响应对prompt的敏感度乘积大于1时，评估指标的估计方差会随交互轮次指数级增长。
### 核心结论
评估交互式LLM系统，不仅要测模型如何响应用户，还要测用户如何响应模型。
