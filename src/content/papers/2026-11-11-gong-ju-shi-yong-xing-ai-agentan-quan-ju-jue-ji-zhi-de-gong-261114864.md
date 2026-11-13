---
title: 'When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using
  AI Agents'
title_zh: 工具使用型AI Agent安全拒绝机制的攻击面与防御研究
authors:
- Charles Xiao
arxiv_id: '2611.14864'
url: https://arxiv.org/abs/2611.14864
pdf_url: https://arxiv.org/pdf/2611.14864
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent安全攻防 · 拒绝机制优化
tags:
- Agent Safety
- Indirect Prompt Injection
- Over-Abstention
- Provenance Verification
- Tool-using Agent
one_liner: 揭示工具型Agent安全拒绝机制的攻击面，提出来源感知的先验证后拒绝防御方法
practical_value: '- 涉及商品上下架、订单审核、内容分发的业务Agent，禁止单纯使用「谨慎优先」安全提示，避免被恶意植入的伪造合规警告诱导拒绝正常业务操作，实测该策略会让Gemini的过度拒绝率从9.8%飙升到86.3%

  - 可直接复用「Verify-Before-Abstain」协议，对风险警告增加来源校验逻辑：仅当风险来自官方可信来源/经过权威记录佐证才触发拒绝，实测该策略可将虚假警告下的任务完成率从13%恢复到100%（Gemini场景）

  - 业务Agent的风险识别不要只匹配“警告、冻结、禁止”等敏感词，需结合内容事实判断，部分模型对事实表述的风险识别率比显性警告低47%-100%，易漏判真实风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前工具型LLM Agent的安全设计多优先鼓励谨慎拒绝风险操作，但攻击者可在低信任内容（如用户评论、第三方文档、商品描述）中植入伪造的风险警告，诱导Agent拒绝执行合法任务，属于间接Prompt注入的可用性攻击，现有安全策略完全未覆盖该攻击场景。

### 方法关键点
- 基于AgentAbstain基准构建51组可注入伪造警告的配对任务，覆盖21个仿真业务环境，包含干净任务、虚假警告任务、敏感内容任务、显性/隐性风险表述对比任务四类变体
- 对比三类提示策略：原生基线、谨慎优先、来源感知+Verify-Before-Abstain协议（要求Agent仅采信经过权威来源佐证的风险警告）
- 测试三类主流大模型：deepseek-v4-pro、gpt-5.4、gemini-3-flash

### 关键实验结果
基线条件下三类模型的过度拒绝率为9.8%~27.5%，使用谨慎优先提示后，过度拒绝率最高飙升至86.3%（gemini-3-flash），且干净任务完成率无明显下降，说明安全提示直接放大了攻击效果；引入Verify-Before-Abstain策略后，虚假警告下的任务完成率最高从13%恢复到100%（deepseek-v4-pro、gemini-3-flash），仅带内来源伪造场景下会出现最多20%的过度拒绝，若权威记录被篡改则防御完全失效；额外测试显示模型对显性警告的识别率比事实表述的同等级风险高29%~100%，存在明显的词汇过拟合问题。

### 核心结论
Agent安全评估不能只看拒绝有害操作的比例，还要区分拒绝的依据是真实风险还是攻击者伪造的虚假信号，单纯提高安全阈值反而会成为新的攻击面。
