---
title: Valid Stopping in Adaptive Generator-Verifier Loops
title_zh: 自适应生成器-验证器循环的有效停止策略
authors:
- Mahmoud Hegazy
- Michael I. Jordan
- Aymeric Dieuleveut
affiliations:
- École polytechnique, IP Paris
- Inria Paris
- UC Berkeley
arxiv_id: '2610.06432'
url: https://arxiv.org/abs/2610.06432
pdf_url: https://arxiv.org/pdf/2610.06432
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 生成验证循环停止策略优化
tags:
- Generator-Verifier Loop
- e-value
- Conformal Risk Control
- FDR Control
- Online Multiple Testing
one_liner: 结合指数投注e值、鲁棒CRC与在线e-BH实现生成验证循环FDR可控停止
practical_value: '- 电商生成式推荐/Agent生成文案/物料的生成-校验循环可直接复用该停止框架，将最终输出的bad case率控制在预设阈值内，无需跑满所有迭代，最高可节省40%以上的推理算力

  - 非单调损失的鲁棒核CRC方法可迁移到业务超参数校准场景，比如召回阈值、排序截断规则的校准，解决传统单调CRC无法适配非单调损失的问题

  - 指数投注e值归一化方法可用于代理指标有效性校准，解决推荐/广告场景中代理指标（如点击率、停留时长）和业务真实目标（如复购、GMV）偏差导致的策略过拟合问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
大量Agent工作流、生成式任务采用生成器-验证器循环架构：用低成本验证器筛选候选，避免反复调用昂贵的ground-truth oracle（如人工审核、业务长链路指标计算）。但生成器会自适应拟合验证器的弱点，反复迭代后假阳性结果会不断积累，最终输出集合的真实错误率远高于验证器给出的结果，此前没有方法能在不限制生成器自适应策略的前提下，控制停止后输出结果的假发现率（FDR）。
### 方法关键点
- 基于指数投注框架构建每轮候选的有效e值，将当前验证器分数和历史负样本分数做归一化，无需对生成器的自适应策略做任何假设，保证e值在「候选不合格」的原假设下期望≤1
- 提出鲁棒核共形风险控制（Robust-core CRC），通过将参数校准问题提升到集合空间恢复单调性，解决传统CRC要求损失随参数单调的限制，适配在线e-BH超参数校准的非单调损失场景
- 结合加权在线e-BH多检验流程，实现任意停止时刻下输出集合的FDR不超过用户预设的阈值α，支持同时收集κ个合格候选的业务场景
### 关键结果
- 合成数据实验：对比unscaled在线e-BH、包络CRC基线，目标α=0.1时本方法输出FDP为0.082，接近理论上限，比基线少浪费60%以上的误差预算
- 蛋白设计真实场景：在RFdiffusion/Proteina生成器的30轮循环中，α=0.1、κ=10时本方法输出FDP严格低于0.1，同时平均返回9个以上合格候选，比固定跑满30轮的策略减少40%以上的算力开销
### 核心结论
生成-验证循环的停止策略不能仅依赖廉价代理指标，必须通过统计校准将真实业务目标的误差率严格控制在预设水平，避免过拟合校验器带来的业务损失
