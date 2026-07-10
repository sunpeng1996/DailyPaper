---
title: Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language
  Models
title_zh: 预算感知的大语言模型测试时重采样与重路由决策方法
authors:
- Teng-Ruei Chen
affiliations:
- National Yang Ming Chiao Tung University
- Krixvon
arxiv_id: '2607.08665'
url: https://arxiv.org/abs/2607.08665
pdf_url: https://arxiv.org/pdf/2607.08665
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM推理优化 · 成本感知调度
tags:
- LLM inference
- cost optimization
- model routing
- test-time compute
- budget allocation
one_liner: 提出边际收益驱动的RoR策略，在单查询预算下权衡重采样与重路由，优化LLM推理成本质量帕累托表现
practical_value: '- 电商客服、商品文案生成、Agent任务调度等LLM服务场景可直接复用RoR的边际收益贪心逻辑，量化重采样当前模型、切换大/专用模型的单位成本收益，在固定推理预算下优化效果与成本

  - 可根据业务场景选择适配的verifier：开放答案场景（如客服问答、创意文案）用自一致性作为无标注verifier；规则类场景（如营销规则校验、商品属性抽取）用部分测试用例作为高可靠verifier，最大化调度收益

  - 对 latency 要求高的业务可先做极简评估：饱和场景（如通用文案改写）用单模型best-of-K即可覆盖大部分收益，异构模型池+高难度场景（如复杂商品咨询、多步Agent推理）再引入RoR策略'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理调度方案要么聚焦单查询单模型路由，要么只做单模型重采样，均未在实际部署的有限单查询预算、非完美校验器（verifier）约束下，将重采样与重路由作为互相竞争的预算消耗选项，无法达到最优的成本-质量帕累托平衡。
### 方法关键点
- 形式化预算感知测试时模型选择问题：在单查询成本不超过B的约束下最大化答案正确率，决策空间包含「重采样已使用模型」「重路由到未使用新模型」两类动作
- 提出RoR（Resample-or-Reroute）策略：维护每个模型在当前查询的成功率后验估计，每步选择单位成本边际正确率最高的动作执行，默认贪心变体表现优于UCB探索变体，单查询计算开销可忽略
- 以模型离线准确率为先验，通过伪计数s控制先验权重，算法对s取值鲁棒，无需精细调参
### 关键结果
在4个难度梯度的基准（GSM8K、MATH-500、GPQA-Diamond、HumanEval+）、11个开源模型的池子上测试，对比单路由、单提交路由器、预算感知best-of-K、FrugalGPT式级联等基线：
- 饱和场景GSM8K下，RoR达到0.993准确率的成本比级联低24%，比单路由最佳模型低3.5倍，准确率还高2.7个百分点
- 高异构难场景GPQA-Diamond下，同成本RoR比best-of-K高10.7个百分点，比级联高4.1个百分点
- 增益完全受verifier质量约束：verifier质量q从1降到0.6时，GPQA上RoR相对best-of-K的增益从10.7个点降到2.7个点，甚至在部分场景反超

> 最值得记住的结论：LLM测试时预算分配的收益上限由verifier的可靠性决定，无可靠verifier的场景下，集中预算单模型重采样通常优于盲目切换模型
