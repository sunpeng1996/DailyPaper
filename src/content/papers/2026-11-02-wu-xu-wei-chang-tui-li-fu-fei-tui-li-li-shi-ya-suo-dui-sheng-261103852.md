---
title: Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning
  History Compaction on Future Generation and Agent Cost
title_zh: 无需为长推理付费：推理历史压缩对生成效果与Agent成本的因果影响
authors:
- Anton Hristov
affiliations:
- Technological School Electronic Systems
arxiv_id: '2611.03852'
url: https://arxiv.org/abs/2611.03852
pdf_url: https://arxiv.org/pdf/2611.03852
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 推理成本效率优化
tags:
- Reasoning Compaction
- Agent Efficiency
- Cost Reduction
- Inference Optimization
- Zero Retraining
one_liner: 无需重训，仅通过重写压缩推理历史即可降低20%-50%后续推理token量且基本不损任务成功率
practical_value: '- 电商导购Agent、多轮检索推荐Agent可直接复用该方案：在工具调用返回前压缩前序推理历史，可降低20%~50%的推理token成本，任务成功率波动不超过2%

  - 工程实现可复用轻量化规则：仅压缩超过12词的推理块，若压缩结果比原文更长则直接回退为原始内容，避免额外的压缩开销反超收益

  - 业务落地优先测试自压缩方案：用当前部署的LLM自身作为压缩器，相比第三方外部压缩器更适配自身推理风格，可降低信息丢失导致的效果下降风险

  - 对于多轮生成式推荐场景（如对话式选品、用户需求深挖），可每2~3轮做一次历史压缩，平衡压缩开销和推理成本收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM长推理链可显著提升复杂任务解决能力，但推理token占总生成token的53%~85%，直接推高API调用和推理成本；闭源模型推理记录不公开无法针对性优化，开源模型默认推理输出冗余，现有优化方案大多需要重训，落地成本高。
### 方法关键点
- 纯推理压缩：用压缩LLM将历史推理记录重写为精简状态记录，保留决策相关事实、数值、不确定性、结论、待执行动作，删除重复内容，系统/用户消息、工具调用/返回结果保持不变，无需修改目标模型权重
- 盲态时序设计：在Agent发起工具调用后、工具结果返回前完成推理重写，对比原始和压缩历史的后续生成效果，保证仅推理历史差异影响结果
- 准入校验：用GPT-5.6 Sol完成改写和信息完整性校验，仅通过校验的压缩历史进入后续实验
### 关键结果
- 受控对比实验覆盖6款主流LLM，172组有效配对中87.8%的场景后续推理token量下降，各模型中位数降幅20.2%~50.5%，整体任务成功率波动±1%
- 编码Agent部署实验在SWE-bench 50个代码任务上测试，6/8的压缩配置总支出下降，7/8的配置目标模型请求时间下降，最大总支出降幅46.5%，任务成功率波动不超过6%
> 最值得记住：推理历史压缩的收益必须结合具体模型、任务场景评估，仅靠压缩后的trace长度不能直接判断方案价值
