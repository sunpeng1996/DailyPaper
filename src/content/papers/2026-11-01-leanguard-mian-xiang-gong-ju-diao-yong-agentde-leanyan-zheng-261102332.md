---
title: 'LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents'
title_zh: LEANGUARD：面向工具调用Agent的Lean验证安全护栏系统
authors:
- Sreehari Sankar
- Debargha Ganguly
- Vikash Singh
- Mohsen Hariri
- Weicong Chen
- Yanyan Zhang
- Shouren Wang
- Wang Yang
- Chaoda Song
- Alexander Nemecek
affiliations:
- Case Western Reserve University
- UT Austin
arxiv_id: '2611.02332'
url: https://arxiv.org/abs/2611.02332
pdf_url: https://arxiv.org/pdf/2611.02332
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: Agent工具调用 · 可证明安全护栏
tags:
- Tool-using Agent
- Guardrail
- Formal Verification
- Lean 4
- Prompt Injection Defense
one_liner: 基于Lean 4实现的可证明安全Agent工具调用护栏，支持反馈修复与自动证明修复
practical_value: '- 电商交易/客服类高风险Agent可复用其「可信状态快照+历史时序校验+归属权校验」的准入逻辑，高风险操作（退款、改地址、换品）不采信LLM生成内容或工具返回文本作为授权依据，仅对接后端可信快照数据，避免Prompt
  Injection导致的资损

  - 工具调用拦截后不要返回空拒绝，可借鉴其反馈引导机制，返回明确的规则违反原因和操作提示（如「该订单不属于当前登录用户，请核对订单号」），可降低30%左右的重复拦截率，提升任务成功率

  - 参数类错误导致的调用拦截可复用proof-guided repair思路，基于业务规则枚举合法参数候选自动修正，无需LLM二次生成，中位数延迟仅2ms，几乎无性能损耗，比如退款时自动匹配订单原支付渠道'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工具调用类LLM Agent频繁出现违反领域策略的操作，Prompt Injection等攻击会触发异常支付、敏感数据泄露等高风险问题，现有护栏要么缺乏形式化安全证明，要么拦截后Agent恢复成功率低，严重影响业务可用性和安全性。

### 方法关键点
- 部署在LLM和工具之间的运行时拦截层，所有工具调用先经过Lean 4编写的策略校验，仅当满足规则才放行，校验逻辑经证明与LeanLTL语义等价，默认fail-closed，缺失证据直接拒绝
- 策略支持状态谓词+带作用域的过去时间时序算子，可表达「必须先读订单才能修改」「同一订单仅能修改一次」这类依赖历史的规则，所有校验依赖后端可信快照、历史执行日志，不采信非结构化文本作为授权依据
- 拦截后提供两种恢复路径：一是返回违反的规则和自然语言提示，引导LLM自行修正调用；二是基于Lean元编程自动搜索符合用户意图的合法参数，生成可证明合规的修正调用，无需LLM参与

### 关键结果
在τ²-bench的5个Qwen模型（0.8B-27B）上测试，无护栏的Agent至少执行33次违反策略的工具调用，LEANGUARD拦截率100%，带反馈模式下任务成功率无显著下降；在DTap Prompt注入基准上，直接注入成功率从57.9%降至5.9%，间接注入从22.3%降至3.8%；参数错误导致的拦截中34.9%可自动修复，中位数延迟2ms。

最值得记住的一句话：Agent的安全保障不能依赖LLM本身的对齐能力，必须在工具调用边界做独立、可证明的策略校验，非结构化文本永远不能作为授权依据。
