---
title: 'Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses
  from 0.75B to 4.7B'
title_zh: 跨模型尺寸的Agent Harness性能：0.75B-4.7B本地部署五款Harness对比
authors:
- Hao Wang
- Ting Huang
affiliations:
- University of Science and Technology Beijing
- Honor Device Co., Ltd.
arxiv_id: '2611.21407'
url: https://arxiv.org/abs/2611.21407
pdf_url: https://arxiv.org/pdf/2611.21407
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 本地小模型Agent Harness优化选型
tags:
- AgentHarness
- SmallLLM
- LocalInference
- AgentEvaluation
- EdgeDeployment
one_liner: 在0.75B-4.7B本地小模型上验证Agent Harness优化收益远高于盲目提升参数规模
practical_value: '- 本地小模型Agent选型优先优化Harness而非盲目提升参数：0.75B模型搭配优质Harness的性能远超同参数甚至更高参数的其他Harness组合，端侧部署（比如电商端上导购、离线个性化推荐）可大幅降低计算成本

  - 小模型Agent核心优化优先级向重复调用拦截倾斜：实验显示仅移除重复拦截规则就会让0.75B模型得分下降0.411，8个任务完全无产出，该规则优化性价比远高于完成态校验门限

  - Agent效果评估必须落地到产出物校验：仅参考进程退出状态会将85个实际无产出的正常退出任务误判为成功，电商场景做搜索推荐Agent时必须加实际产出（如候选item列表、文案）的校验逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前本地小模型Agent的Harness多针对云端大模型设计，未适配小模型工具调用不稳定、推理能力弱的特性，从业者面临“提升模型参数还是优化Harness”的决策困惑，现有研究未同时控制Harness、模型、评测标准三个变量给出明确结论。
### 方法关键点
- 控制单机器、单运行时、单评测标准，测试5款主流Harness（Mingbird/pi/OpenCode/goose/mini-swe-agent），覆盖0.75B-4.7B共4款开源小模型，锚定35.5B MoE模型做上限参考
- 评测基于18个需产出落地artifact的任务，用deterministic checker仅校验最终产出文件，不读取Agent交互日志，避免虚假得分
- 定向消融实验：分别关闭完成校验门限、重复调用拦截规则，准确定位性能增益来源
### 关键结果
- 面向小模型优化的Mingbird Harness在所有尺寸模型上性能均排名第一，在0.75B上领先最强基线0.508分，4.7B上领先不同基线0.075-0.819分
- Harness优化增益远大于参数提升：同尺寸下最优与最差Harness性能差达0.564-0.819，而最优Harness从0.75B升级到4.7B仅提升0.304分
- 完成校验门限对性能贡献不足20%，仅移除重复调用拦截规则就在0.75B上降分0.411，导致8个任务完全无产出

对8GB消费级显卡可部署的5B以下小模型，优化Harness带来的性能增益远大于把参数翻6倍的提升
