---
title: 'SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using
  Agents against Prompt Injection'
title_zh: SPILLWAY：分离目标准入与净化的工具调用Agent提示注入防御方案
authors:
- Woosang Lim
- Yeseul Chang
- Jaewoo Lee
affiliations:
- SAINT Machines
- KAIST
- Chung-Ang University
arxiv_id: '2611.07222'
url: https://arxiv.org/abs/2611.07222
pdf_url: https://arxiv.org/pdf/2611.07222
published: '2026-11-03'
collected: '2026-11-17'
category: Agent
direction: Agent安全 · 提示注入防御
tags:
- Prompt Injection
- Agent Security
- Tool Calling
- LLM Defense
- Runtime Guard
one_liner: 基于工具结构化返回做目标准入，结合规则净化，实现低开销高鲁棒的Agent提示注入防御
practical_value: '- 做电商Agent（自动客服、订单处理、智能导购）安全防护时，可复用分层思路：先做无模型的结构化参数准入（如支付账号、收件地址仅允许来自系统返回的结构化字段，禁止从用户/第三方文本中提取），再做前置规则过滤指令类文本，最后仅对异常请求调用小模型复核，兼顾成本与安全性

  - 现有业务Agent的工具调用模块可快速接入该方案：仅需给工具返回的敏感字段（用户ID、支付ID、联系地址）打上identity标签，复用规则库做准入校验，无需修改Agent逻辑，改造工作量极低

  - 针对电商高风险操作（退款、优惠券发放、用户信息修改），可叠加授权规则：仅用户初始指令明确提到的操作允许执行，其余一律拦截或二次确认，避免注入引发资损'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工具调用Agent已广泛用于支付、办公、电商订单处理等场景，间接提示注入（攻击者在网页、文档、邮件中嵌入恶意指令）可劫持Agent执行转账、泄露数据、违规发放优惠券等高风险操作。现有防御方案要么依赖每步LLM校验导致开销极高，要么需要预先路由规划泛用性差，且普遍存在攻击漏判、正常业务效用下降的问题，亟需低开销、高鲁棒的生产级防御方案。
### 方法关键点
- 双层分离架构：将目标准入和内容净化解耦，分别在工具调用出口、工具返回入口做校验，无额外骨干LLM调用
- 出口准入层：直接从工具返回的结构化身份字段（如用户ID、支付账户、收件地址）构建准入索引，仅允许调用目标属于用户初始指令、准入索引或固定授权规则的请求，全程为集合查找，无模型开销
- 入口净化层：用固定规则移除工具返回中的伪造对话轮次、针对Agent的指令类文本、账号变更声明等风险内容，保留移除片段作为证据，被移除片段中提到的目标直接拦截，不进入后续复核
- 仅当请求被准入层拦截且目标不在移除片段中时，才调用本地小模型做双视图复核，确认符合用户意图才放行
### 关键结果
在AgentDojo、AgentDyn共7个测试集、3个骨干模型（gpt-4o-mini、qwen3:8b、qwen3-coder:30b）上对比ROPE、MELON、Progent等7种SOTA防御方案：
1. 标准模板注入下攻击成功率（ASR）为0，是唯一在所有测试集+骨干组合下实现零漏判的方案，保留99.8%的无防御Agent的良性效用，攻击下效用达0.489，为所有方案最高
2. 对抗ChatInject伪造对话模板、AutoDojo优化注入攻击时ASR仍为0，对抗RL生成的PISmith攻击时ASR仅0.005
3. 单episode平均额外开销<0.5s，额外模型调用<0.15次，远低于MELON、DRIFT等方案的2~13次额外调用
### 核心结论
Agent安全防御的核心是用结构化规则锁死核心操作的参数来源，而不是靠LLM去识别恶意指令，后者永远存在被绕过的可能
