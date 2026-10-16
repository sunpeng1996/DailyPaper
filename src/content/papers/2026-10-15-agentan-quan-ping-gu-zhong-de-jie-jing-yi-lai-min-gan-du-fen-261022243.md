---
title: Shortcut Sensitivity in Agent-Safety Evaluations
title_zh: Agent安全评估中的捷径依赖敏感度分析
authors:
- Hasan Demirkiran
- Jens Ernstberger
affiliations:
- Kontext
arxiv_id: '2610.22243'
url: https://arxiv.org/abs/2610.22243
pdf_url: https://arxiv.org/pdf/2610.22243
published: '2026-10-15'
collected: '2026-10-16'
category: Eval
direction: Agent 安全评估方法优化
tags:
- Agent Safety
- Shortcut Learning
- Benchmark Audit
- Guardrail
- Evaluation
one_liner: 提出三级捷径审计框架，量化Agent安全评估中基准表征对安全Guard决策的影响
practical_value: '- 内部Agent（电商导购Agent、推荐策略调优Agent、广告投放Agent）的安全Guardrail评估可直接复用三级审计框架，先排查简单特征是否能预测标注，再验证特征和Guard决策的关联，最后做配对扰动测试，避免上线后出现大量误拦漏拦

  - 评估模型/策略性能时必须明确统计单元，电商场景下的用户粒度、会话粒度、点击粒度的指标差异极大，不要仅选择对结果有利的统计单元报性能，类似论文中行粒度切换为交互粒度后TS-GUARD
  F1下降近20pp

  - 设计安全规则或Prompt Guard时，必须测试表面特征的鲁棒性：比如电商Agent调用下单、退款、优惠券发放等高风险工具时，不要仅依赖工具名判断风险，要做别名、格式扰动、标签改写测试，避免被攻击者利用表面特征绕过

  - 跨业务域迁移安全规则或小模型Guard时，必须提前做跨域Holdout测试，论文中精确工具名规则跨域F1从0.901跌至0.495，对应电商服饰/3C/生鲜等不同业务域的规则迁移要提前验证泛化性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent安全Guard的评估高度依赖基准数据集，但数据集中的标注惯例、模板结构、统计单元偏差等捷径特征，会让Guard的评估性能虚高，无法反映真实部署后的安全能力，亟需系统化方法定位这类捷径对评估结果的干扰。
### 方法关键点
- 三级捷径审计框架：Level1测试无语义理解能力的简单规则对基准标签的预测性，筛选候选捷径特征；Level2测试候选特征与Guard决策的观测相关性，锁定待验证特征；Level3做配对编辑（仅修改目标特征，保留安全语义不变），直接测试Guard决策对特征的敏感度。
- 针对随机性Guard新增重复调用、交错请求、格式安慰剂对照，排除模型不稳定、时序漂移等干扰因素，确保敏感度测试结果可信。
### 关键实验结果
- 覆盖3个公开Agent安全基准：LINUXARENA、AGENTDOJO-TRAJ、AGENTHARM-TRAJ
- Level1测试：LINUXARENA中命令长度特征预测攻击的AUC达0.910；AGENTDOJO-TRAJ的精确工具名匹配规则混合域F1=0.901，跨域Holdout下F1骤降至0.495；AGENTHARM-TRAJ中TS-GUARD行粒度F1=0.902，切换为等交互权重后F1降至0.719，仅统计单元变化就带来近20pp的性能差异。
- Level3测试：Claude Haiku作为Guard时，将<INFORMATION>标记重写会降低拦截率8.33pp，工具名替换为不透明别名会提升拦截率11.46pp，所有不安全调用仍被拦截，变化全部来自对合法请求的误判；该效应在GPT-5.6 Luna和8bit量化TS-GUARD中未复现，说明捷径依赖和模型配置强相关。

基准的预测性特征只是待验证的假设，不能直接证明Guard依赖该特征，只有配对扰动测试才能确认评估结论的鲁棒性。
