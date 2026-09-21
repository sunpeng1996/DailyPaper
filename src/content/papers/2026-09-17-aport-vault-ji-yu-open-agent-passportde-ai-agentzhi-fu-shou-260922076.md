---
title: 'APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent
  Passport'
title_zh: APort Vault：基于Open Agent Passport的AI Agent支付授权基准
authors:
- Uchi Uchibeke
affiliations:
- APort Technologies Inc.
arxiv_id: '2609.22076'
url: https://arxiv.org/abs/2609.22076
pdf_url: https://arxiv.org/pdf/2609.22076
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: Agent 安全授权与基准测试
tags:
- AI Agent
- Payment Authorization
- Benchmark
- Open Agent Passport
- Security
one_liner: 基于4371条人类真实攻击测试，证明工具调用前加OAP检查可完全拦截Agent非法支付
practical_value: '- 做电商Agent自动支付、广告投放、代下单等高资金风险场景时，必须在工具调用和实际执行之间加独立的确定性授权层，不要依赖LLM本身的安全能力，14款主流模型都存在一定概率的非法支付请求漏过

  - Agent效果/安全评估时，优先用可直接观测的状态变化（如实际转账是否发生、订单是否生成）作为核心指标，不要完全依赖LLM Judge，本文中LLM Judge在Level3场景下kappa仅0.167，可靠性极低

  - 高风险Agent的风险统计要按攻击来源会话聚类计算置信区间，不要直接用总样本数算，本文47.9%的非法转账来自同一个攻击会话，直接用总样本算会严重低估风险

  - 涉及高风险操作的Agent基准测试，尽可能用真实人类对抗攻击数据而非合成样本，本文中多轮攻击的效果几乎都集中在伪造工具返回这一种真实攻击类型，合成样本容易漏测'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent安全基准大多仅测试LLM本身的抗攻击能力，不考虑部署架构的防护效果，且多用合成攻击、依赖LLM Judge打分，结果可靠性低，无法给实际部署者提供明确的剩余风险参考，尤其支付类高风险Agent亟需可落地的安全架构验证和真实对抗基准。

### 方法关键点
- 收集公开CTF赛事中1128名参赛者提交的4371条真实人类支付攻击请求，覆盖权限宣称、直接转账、JSON注入等9类攻击类型
- 对比两种架构：无防护的纯模型架构，和工具调用前加Open Agent Passport（OAP）确定性授权检查的架构
- 测试覆盖8家机构的14款主流LLM、5级支付权限策略、单轮/多轮两种回放模式，共完成225964次评测
- 核心指标采用可直接观测的实际转账结果，无需LLM Judge介入，避免主观打分误差

### 关键结果
- 纯模型架构下，Level2-4的限制权限场景共出现140次非法转账，占比0.182%；加OAP授权层的相同场景下，69297次评测中非法转账次数为0，95%置信区间下的风险上限仅0.38%
- OAP层并未降低合法支付的通过率：合法转账请求的处理差异仅为0.084个百分点，且单次授权检查延迟仅53ms，几乎不影响整体链路性能
- 14款LLM的非法支付请求率差异很小，且没有一款模型能完全避免非法请求，攻击跨模型迁移率极低，靠更换模型无法解决根本安全问题

**最值得记住的一句话**：高风险Agent的安全不要依赖LLM本身的能力，在工具执行路径上加独立的确定性授权层，是目前可落地的、能100%拦截已知非法操作的有效方案
