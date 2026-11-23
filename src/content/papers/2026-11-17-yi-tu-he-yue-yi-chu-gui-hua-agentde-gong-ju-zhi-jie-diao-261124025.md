---
title: 'Intent Contracts: Taking Tools Away from Agents'
title_zh: 意图合约：移除规划Agent的工具直接调用权限
authors:
- Ziyuan Wang
- Genliang Zhu
- Xiaobo Chen
- Chu Wang
affiliations:
- Independent Researcher
- Georgia Institute of Technology
- University of Massachusetts Amherst
- University of Illinois Urbana-Champaign
arxiv_id: '2611.24025'
url: https://arxiv.org/abs/2611.24025
pdf_url: https://arxiv.org/pdf/2611.24025
published: '2026-11-17'
collected: '2026-11-23'
category: Agent
direction: Agent 工具调用权限管控
tags:
- LLM Agent
- Tool Calling
- Authorization
- Intent Alignment
- Safety
one_liner: 提出意图合约机制，通过大小模型权限分离降低Agent工具调用越权风险
practical_value: '- 可复用Agent大小模型权限拆分架构：强LLM做复杂规划（如电商导购Agent的需求理解、路径规划），弱LLM仅做授权校验+工具调用生成，降低规划侧被prompt注入后的风险

  - 意图校验机制可直接迁移：要求规划侧输出操作目标、用户原句引用、操作范围三个字段，代码先做引用合法性校验，再由可信侧判断授权，可解决大促场景下导购Agent误操作用户订单、优惠券的问题

  - 操作全链路可审计方案：所有变更对象都要求规划侧提前在合约中明文声明，可用于电商Agent操作的事后审计、问题溯源，降低合规风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具调用Agent存在普遍的越权操作风险：当用户请求存在歧义时，规划模型可能自行扩大操作范围，而传统权限分类器仅能看到用户输入和最终命令，无法感知规划侧的真实意图，既容易漏过未授权操作，也无法处理同时包含合法/非法内容的组合请求。

### 方法关键点
- 架构拆分：完全移除强规划LLM的工具调用权限，仅允许其提交包含操作目标、用户原句引用、操作范围的短意图合约
- 三层校验流程：代码先校验用户引用真实性、操作范围合法性、目标格式合规性；再由小尺寸可信LLM独立判断用户授权范围，自行生成工具调用；工具执行结果仅返回给规划侧，可信侧仅获取执行状态回执
- 三类基准对比：盲审（可信侧仅看命令）、带意图审核（可信侧看命令+合约）、意图合约（可信侧仅看合约，自行生成调用）

### 关键实验结果
基于AmPermBench的3类DevOps任务共96个prompt，规划模型用gpt-6.1-terra，可信模型用GLM-5.3-Flash：
1. 意图合约模式下100%的变更对象都提前在合约中声明，对比带意图审核的12.5%、盲审的7.4%，实现操作全链路可审计
2. 当规划侧夹带未授权任务时，意图合约完成合法任务的比例达90%（27/30），远高于带意图审核的53.3%（16/30）
3. 所有模式处理歧义请求时错误率均达40%~49%，核心原因是可信侧无法访问环境校验规划侧选择的对象是否正确

### 最值得记住的一句话
仅靠意图校验无法解决歧义请求的对象选择错误，可信侧必须能够访问环境上下文才能从根源降低越权操作风险。
