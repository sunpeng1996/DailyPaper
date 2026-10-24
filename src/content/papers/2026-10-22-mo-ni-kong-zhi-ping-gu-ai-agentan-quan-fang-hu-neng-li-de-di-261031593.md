---
title: Simulated Control Evals
title_zh: 模拟控制评估：AI Agent安全防护能力的低成高效仿真测评框架
authors:
- Jeffrey Olmo
- David Zhang
- Tyler Tracy
affiliations:
- Redwood Research
arxiv_id: '2610.31593'
url: https://arxiv.org/abs/2610.31593
pdf_url: https://arxiv.org/pdf/2610.31593
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: Agent安全评估 · 仿真环境模拟
tags:
- Agent Evaluation
- Safety Evaluation
- Simulation
- Control Eval
- LLM Application
one_liner: 提出用LLM模拟环境响应的SCE评估框架，大幅提升Agent安全防护测评的精度与样本效率
practical_value: '- 电商导购/客服Agent安全测评：无需搭建真实风险环境，用LLM模拟用户异常操作、系统响应即可低成本测试防护能力，如是否泄露用户隐私、诱导不合理消费

  - 推荐系统对抗鲁棒性测试：复用SCE思路模拟黑灰产刷榜、投毒攻击行为，无需真实发动攻击即可验证召回/排序模块抗攻击能力，样本成本可降低95%以上

  - 自研Agent安全监控模块优化：用SCE生成的攻击策略迭代监控规则，优化效果接近真实攻击得到的结果，大幅降低攻防测试的成本与风险'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统AI Agent控制评估依赖专用隔离控制环境，无法覆盖真实部署场景的环境、任务特征，评估结果和实际线上表现偏差大，且搭建专用环境、执行真实攻击的成本极高。
### 方法关键点
提出模拟控制评估（SCE）框架，直接用LLM模拟工具/环境的响应输出，替代真实环境运行攻击测试，无需搭建专用控制环境即可完成安全防护能力测评。
### 关键结果
在LinuxArena基准上，5%审计预算下SCE的安全预测RMSE为3.6个百分点，仅为传统BashArena方法的1/3；攻击策略、攻防推理分布的KL散度比BashArena低10倍以上；可解释78%~85%的跨环境攻击成功率、监控得分、安全度方差；样本效率提升20倍以上，仅需不到5%的任务样本即可获得比BashArena更高的预测精度；用SCE发现的攻击策略优化监控模块，效果接近真实执行策略的优化效果，显著优于BashArena。
