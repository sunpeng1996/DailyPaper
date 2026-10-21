---
title: 'AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent
  under Human-Gated and Autonomous Regimes'
title_zh: AllPath：人工/自主模式下自迭代LLM交易代理的分层校验机制
authors:
- Tian Zhang
- Meng Li
affiliations:
- Independent Researcher, USA
arxiv_id: '2610.26662'
url: https://arxiv.org/abs/2610.26662
pdf_url: https://arxiv.org/pdf/2610.26662
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 自迭代系统分层校验机制
tags:
- LLM Agent
- Human-in-the-loop
- Agent Oversight
- Self-Revising Agent
- Deployed System
one_liner: 提出三层分层校验架构，在实盘模拟环境验证两种自迭代管控模式的运行效果
practical_value: '- 自研自迭代Agent可复用三层校验架构：确定性代码层管控不可变规则（如推荐预算、广告风控阈值）、Agent自校验层限权（仅可提策略修改提案无直接上线权限）、人工层负责判断类决策，避免不可逆业务损失

  - 可借鉴自修改规则的管控方案：Agent迭代的策略必须过版本一致性校验，禁止修改权限/状态字段，避免自迭代Agent悄悄扩大操作权限引发故障

  - Agent部署的人机交互设计要显性化「沉默状态」：未生效的推荐策略、暂停的投放规则需加全局显眼标识，避免运营遗漏状态引发资损'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent几乎都在回测/模拟环境评测，上线后动作不可逆，现有方案未明确不同校验方的权责边界，无法避免自迭代Agent的故障扩散，尤其电商、广告这类涉及真金白银的场景，不可逆操作的校验机制是落地刚需。

### 方法关键点
- 三层分层校验架构：①代码层：纯逻辑实现风控阈值、策略版本一致性、权限字段冻结等不可变规则，无模型参与；②Agent自校验层：限定自迭代会话仅能提交策略修改提案，无直接操作权限、工具调用次数设上限、输入全部为可信结构化数据；③人工层：负责所有判断类决策，界面渲染时动态计算最新差异、显性化所有状态避免误判。
- 支持两种运行模式切换：人工管控模式下所有Agent自迭代提案需人工审批，自主模式下提案仅过代码校验即可生效，搭配回撤断路器，超标自动切回人工管控。

### 关键结果
在实盘模拟美股交易账户连续运行7.5周：前2.5周人工管控模式下，6个Agent提案有2个被人工否决，决策中位数延迟8.8小时；后5周自主模式下，56个Agent提案全部通过代码校验自动生效，后续人工事后审核删除了其中11条新增规则，中位数滞后8天；共记录20个仅上线后才会出现的生产故障，全部对应可落地的设计规则。

> 最值得记住的一句话：对于动作不可逆的Agent系统，校验不是事后加的一层补丁，是从设计阶段就完成的权责拆解，没有任何技术层可以替代人工的判断类决策。
