---
title: Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture
  for Multi-Agent AI in Regulated Finance
title_zh: 受监管金融领域多Agent AI治理架构：应对局部合规但整体歧视风险
authors:
- Jose Manuel de la Chica Rodriguez
- Juan Manuel Vera Diaz
- Pablo Delgado Romero
affiliations:
- Santander AI Lab, Grupo Santander
arxiv_id: '2609.27994'
url: https://arxiv.org/abs/2609.27994
pdf_url: https://arxiv.org/pdf/2609.27994
published: '2026-09-23'
collected: '2026-09-24'
category: MultiAgent
direction: 多Agent 金融场景合规治理架构
tags:
- Multi-Agent
- AI Governance
- Fair Lending
- Runtime Monitoring
- Regulated Finance
one_liner: 提出金融专属多Agent治理架构ARIA，弥补局部合规不保障整体合规的管控缺口
practical_value: '- 多Agent部署需补充全局层管控：不能仅做单Agent的局部合规校验，需新增群体维度的统计指标监控，避免局部合规但整体出现歧视、流量倾斜等不可接受的业务/合规问题，可直接迁移至电商多推荐Agent、多导购Agent的治理场景

  - 漂移预警可复用M2观测-预期分布对比思路：基于JS散度计算群体决策行为和基线分布的差异，能比单维度违规指标提前捕捉漂移，适配推荐、广告系统的异常行为早发现需求

  - Agent权限管控可复用BDA分级思路：将Agent的执行能力与授权权限解耦，按合规表现、场景风险做分级授权，异常时自动降级权限，降低多Agent协同的违规风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前受监管金融机构大量部署多Agent工作流，但传统治理仅做单模型/单Agent的局部合规校验，存在「宪法非组合性」问题：所有Agent局部合规的情况下，群体行为仍可能产生歧视、系统性风险等不可接受的整体结果，无法满足公平借贷、EU AI Act等监管要求，现有模型中心的治理方案无法覆盖群体层面的管控缺口。

### 方法关键点
提出金融专属多Agent治理参考架构ARIA，分为三个平面六大能力：
1. 规范问责平面：包含政策规范、人类 oversight 能力留存，明确跨司法辖区的合规映射、版本化管理规则，定期校准人类审核人员的业务能力避免自动化导致的能力退化；
2. 执行控制平面：包含边界化授权、运行时遏制，将Agent能力与权限解耦，按风险分级授权，异常时自动触发权限降级、沙箱等遏制操作；
3. 保障学习平面：包含群体行为监控、自适应策略更新，提出M2指标（基于JS散度对比群体决策观测分布与预期基线的差异）做漂移预警，将红蓝队、异常事件输出转化为合规策略的迭代输入。

### 关键实验
两组仿真验证：第一组200个信贷Agent的仿真中，局部合规无违规的前提下，无全局管控时群体对薄文件用户的审批率差达到0.41，是合规阈值0.05的8倍；加入ARIA管控后审批率差稳定在0.052，仅超出阈值4%。第二组两阶段漂移仿真中，M2指标比单维度违规指标提前53步（中位数65步vs12步）预警漂移，且二者假阳性率均控制在5%以内。

### 最值得记住的一句话
局部合规的简单叠加不代表整体合规，多Agent系统治理必须补充群体层面的监控、管控能力，才能覆盖结构性的合规缺口。
