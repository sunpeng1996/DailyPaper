---
title: 'Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool
  Calls'
title_zh: 面向LLM工具调用的角色分层共形风险控制方法
authors:
- Md Ashikur Rahman
- Md Arifur Rahman
- Niamul Hassan Samin
- Khandaker Rifah Tasnia
- Sifat Rahman Ahona
- Juena Ahmed Noshin
arxiv_id: '2607.24343'
url: https://arxiv.org/abs/2607.24343
pdf_url: https://arxiv.org/pdf/2607.24343
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent工具调用风险管控
tags:
- LLM Agent
- Tool Call
- Conformal Risk Control
- Risk Management
- Prompt Injection
one_liner: 为LLM工具调用各语义角色参数设置独立风险预算，解决聚合控制掩盖高风险字段违规的问题
practical_value: '- 电商场景的Agent（如智能客服下单、自动营销推送、财务对账工具）可直接复用分层校准逻辑：对收件人、支付账户、优惠券面额、活动预算等高风险字段单独设置风险预算，避免聚合校验漏过高危违规

  - 可作为插件层搭配任意现有字段级违规检测器使用，无需替换现有安全基建，仅需新增校准层即可获得有限样本下的可证明风险保证，工程改造成本极低

  - 针对出现率极低的高风险字段（如电商场景的银行卡号、API密钥），可采用多高风险角色池化校准的方案，在样本不足时仍能拿到全局风险保证，解决小样本风险管控难题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent工具调用风险控制存在两类缺陷：确定性硬规则防护仅支持黑白名单判定，无灵活可调的风险预算与残留违规统计边界；聚合级Conformal Risk Control（CRC）以整个工具调用为单位校验风险，大量低风险字段（如邮件正文、商品描述）的合规表现会稀释高风险字段（如收款账户、收件人、优惠券码）的违规率，导致罕见高风险字段的实际违规率远超预设阈值，带来重大业务损失。
### 方法关键点
- 为工具调用的每个参数分配语义角色（target/credential/command/content等），对每个角色单独设置风险阈值与预算，通过类条件共形校准实现有限样本下的角色级风险保证
- 对样本量不足无法单独校准的罕见高风险角色，池化为统一高风险组进行校准，在小样本场景下仍能保证整体风险可控
- 运行时仅拦截/回退违规字段而非拒绝整个工具调用，最大化正常业务可用性
### 关键结果
在AgentDojo、InjecAgent两个基准，覆盖GPT-4o、Gemini 2.5、Llama3.3等6个主流大模型测试：
1. 针对1%高风险角色违规预算，聚合CRC的目标字段违规率最高达21.2%，本方法仅0.0%-0.3%，同时保留9.4%-14.9%的业务效用
2. 8种分布漂移场景下，本方法的预算合规率达100%±0%，远高于PACT类基线的61%±33%、FIDES类基线的48%±48%
3. 未知工具套件测试的24个模型-套件场景全部合规，最坏目标字段违规率仅1.5%

最值得记住的一句话：结构化工具调用的风险校验粒度应当匹配语义角色的风险等级，而非整个调用动作。
