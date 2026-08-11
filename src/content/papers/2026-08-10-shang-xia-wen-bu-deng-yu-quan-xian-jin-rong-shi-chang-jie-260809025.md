---
title: 'Context Is Not Authority: Structured Runtime Governance for Financial Market
  Agents'
title_zh: 上下文不等于权限：金融市场Agent的结构化运行时管控框架
authors:
- Rui Tang
- Qiangqiang Liu
- Yichi Zhang
- Youwei Wang
- Xi Chen
- Chen Dong
affiliations:
- OpenAsk
- Binance
- New York University
- Xiamen University
- Bank of Hebei
arxiv_id: '2608.09025'
url: https://arxiv.org/abs/2608.09025
pdf_url: https://arxiv.org/pdf/2608.09025
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent运行时权限管控 · 金融场景适配
tags:
- Agent Governance
- Runtime Control
- Financial AI
- Agent Safety
- Auditability
one_liner: 提出SAGE-Fin金融Agent运行时权限管控机制，隔离上下文与操作权限，防范非授权金融动作
practical_value: '- 可复用「上下文≠权限」设计思路，在电商导购Agent、客服Agent、理财Agent场景中，将RAG检索结果、会话上下文与最终输出权限解耦，避免将检索到的规则直接作为对用户的承诺，降低合规风险

  - 可借鉴Typed Candidate+Coverage Debt机制，在生成式推荐、Agent输出环节将候选输出做结构化分类，明确每个类型所需的校验条件，缺失校验条件时自动降级输出（如从具体折扣承诺降级为「请咨询人工客服」）

  - 可复用非可替换Receipt设计，在多Agent协作、多流程节点的业务中，不同阶段的流程凭证不可跨阶段复用，例如推荐Agent的用户偏好匹配凭证不能直接作为交易Agent的下单权限凭证，必须单独走交易权限校验'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前金融Agent即使获取到正确的上下文，也存在将软信号硬化为交易指令、过期报价直接作为用户承诺、重复输出违规内容等风险，本质是误将上下文等同于操作权限，自然语言输出跨越权限边界引发合规、资金损失，通用Agent管控机制缺乏针对金融等高合规场景的权限传递规则。

### 方法关键点
- 核心管控对象为Agent拟产生的实际效果而非输出文本，所有候选输出先编译为带类型的结构化Candidate，明确每个类型对应的校验条件
- 引入Coverage Debt机制，缺失、过期的校验条件会显性化，自动收缩可用权限范围，避免隐性假设带来的风险
- 设计不可跨类型复用的Receipt凭证机制，仅对应类型的有效凭证（commit用于用户响应、execAuth用于交易执行、deploy用于策略发布）可触发对应操作，状态变更后自动重新校验权限
- 消费侧各Adapter（响应/执行/策略发布）会统一校验凭证有效性、候选类型、Coverage Debt、当前系统状态，不满足条件则直接拦截或降级

### 关键结果数字
- 616个人工构造的测试用例上，5个确定性规则生成3080个输出，原型与参考标准的二分类校验一致性达616/616，覆盖3个指定响应门控用例，22个专项路径测试全部通过
- 已在某数字资产平台生产环境处理用户请求，独立运营团队的正式评估对实用性和流程适配性给出强正面结论，用户反馈同样强正面
- 历史上3起未被旧系统拦截的生产故障，可被100%拦截

**最值得记住的一句话：上下文可以为权限判断提供信息支撑，但上下文本身绝非权限**
