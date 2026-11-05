---
title: 'AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java
  LLM Agents'
title_zh: AgentTrustCI：面向Java LLM Agent的构建时合规测试框架
authors:
- Sachin Gupta
affiliations:
- Independent Researcher, San Jose, California, USA
arxiv_id: '2611.06674'
url: https://arxiv.org/abs/2611.06674
pdf_url: https://arxiv.org/pdf/2611.06674
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: LLM Agent 构建时合规性测试
tags:
- LLM Agent
- Test Framework
- CI-CD
- Policy Compliance
- Trajectory Validation
one_liner: 提出Java/JUnit5的LLM Agent构建时测试框架，三层校验100%覆盖55个合成用例所有故障
practical_value: '- 可复用三层校验逻辑到电商/推荐Agent（导购、售后、运营Agent）的合规测试：政策层校验工具调用白名单、参数合规，规避私自调用改单、退款等高风险接口；grounding层校验回答是否基于工具返回，杜绝虚构商品信息、订单号、库存数；轨迹层校验执行流程符合业务规则（比如退款必须先查订单→走审批→打款，不能跳步）

  - 低成本落地技巧：优先用确定性正则、字符串匹配做grounding校验，无需LLM judge即可覆盖90%以上虚构信息、敏感字段泄露问题，延迟仅微秒级，可直接嵌入CI流程不拖慢发布速度

  - 轨迹校验双模式适配不同业务：严格匹配适合强合规流程（支付、退款、用户信息修改），宽松匹配允许额外合理调用（比如用户问商品参数时额外调用库存查询接口），平衡灵活性与合规性

  - 测试用例设计思路：按故障分层构造用例，每个用例仅触发一类校验失败，方便快速定位问题，同时设置关键故障零容忍阈值，上线前强制检测高风险违规行为'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基础设施安全仅能保障LLM Agent的运行环境可信，无法校验Agent是否调用了合规工具、回答是否基于工具返回结果、是否遵循指定工作流：比如售后Agent可能私自调用关单接口、虚构工单信息、跳过审批流程，仅校验最终回答正确性无法发现这类风险，需要在构建阶段就将业务行为约束转化为可自动化执行的测试规则。
### 方法关键点
- 三层校验架构：政策层校验工具调用白/黑名单、参数必填/禁止/枚举值合规；确定性grounding层通过正则提取回答中的ID、数字、引用内容，校验是否全部存在于工具返回结果，同时检测敏感字段泄露、未调用写工具就声称操作成功的问题；轨迹层支持严格匹配（工具调用序列完全一致）和宽松匹配（指定序列按顺序出现，允许插入其他合法调用），额外支持禁止中间工具、禁止重复调用规则
- 基于Java/JUnit5实现，可直接嵌入Java生态CI流程，无需调用LLM即可完成所有校验，支持故障原因分层打标，快速定位问题
- 预留LLM judge扩展接口，可对接语义校验能力处理paraphrase、上下文敏感的复杂校验场景
### 关键结果
基于覆盖7个企业域的55个合成用例（30个注入故障、12个关键故障、25个正常用例含10个边缘正常用例）测试：三层全链路校验准确率100%，30个故障全部检出，25个正常用例全部通过，12个关键故障零遗漏；单校验层各自准确率63.6%，仅覆盖对应层的10个故障；warm后全链路校验平均延迟3.369μs，P95延迟6.333μs，几乎不占用CI流程时间。

最值得记住的结论：LLM Agent的行为合规性不能只依赖最终回答正确性校验，必须同时覆盖工具权限、回答事实来源、执行流程合法性三个维度，三层确定性校验是低成本覆盖绝大多数常见Agent故障的有效方案。
