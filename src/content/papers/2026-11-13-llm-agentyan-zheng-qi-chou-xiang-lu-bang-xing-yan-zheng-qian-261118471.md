---
title: Do Verifier Judgments Survive Abstraction? Measuring Verification Transport
  for LLM Agent Evaluation
title_zh: LLM Agent验证器抽象鲁棒性：验证迁移效应的量化评估
authors:
- Disha Sheshanarayana
- Sai Linisha Reddy Goli
affiliations:
- Manipal University Jaipur
arxiv_id: '2611.18471'
url: https://arxiv.org/abs/2611.18471
pdf_url: https://arxiv.org/pdf/2611.18471
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: Agent验证 · 执行抽象鲁棒性评估
tags:
- LLM Agent
- Verification
- Trajectory Evaluation
- Abstraction Robustness
- Provenance Recovery
one_liner: 提出Verification Transport指标，量化执行抽象对Agent验证器判断稳定性的影响
practical_value: '- 电商/推荐Agent轨迹质检、奖励建模场景，不能仅测完整原生轨迹准确率，必须覆盖实际部署的工具封装、子Agent调用、长历史压缩等抽象场景，避免上线后验证失效

  - 验证场景可按需选协议：低误判需求优先选V-LLM直接验证，低漏判需求优先选证据对齐协议，证据不足时主动弃权而非乱判

  - Agent执行链路需保留可还原的全量provenance，抽象导致的验证错误85.5%可通过还原原始执行证据恢复，成本低收益高

  - 验证器选型不要只看原生场景准确率，需加测不同抽象程度下的稳定性，隐藏执行信息越多验证失效概率越高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM验证器广泛用于Agent轨迹的过程级评估，但现有验证可靠性测试都基于完整原生执行视图，实际部署中Agent执行会经过工具封装（宏抽象）、子Agent委托、长历史压缩等处理，验证器可见的执行证据被裁剪，原生场景下的准确判断是否会失效缺乏量化研究，直接影响线上Agent监控、奖励建模、安全审计的可靠性。

### 方法关键点
- 提出Verification Transport Failure Rate（VTFR）指标，衡量原生视图下判断正确的样本，经过抽象后出现误判或无有效输出的比例；配套Restoration Recovery Rate（RRR）衡量还原原始执行证据后的故障恢复比例
- 严格控制变量：固定任务、实际执行轨迹、真值、验证器、评估标准，仅改变验证器可见的执行证据，覆盖宏抽象、委托抽象、历史压缩3种工业界常见抽象边界
- 对比4类主流验证协议：直接验证（V-LLM）、证据对齐验证（V-EVIDENCE）、主动溯源验证（V-AGENTIC）、多轮审议验证（V-DELIBERATIVE）

### 关键实验
基于4个主流Agent轨迹基准（AgentProcessBench、ATBench、PlanRewardBench、AgentDojo）、7款主流大模型作为验证器骨干测试：宏/委托抽象下VTFR达31%左右，历史压缩下为20.3%；还原原始provenance可恢复85.5%的验证错误，仅5.2%的原正确判断会被降级；抽象程度越高VTFR越高，provenance保真度越高恢复效果越好。

原生视图下的验证准确率不足以表征线上部署的验证器可靠性，必须结合实际部署的抽象边界做鲁棒性测试。
