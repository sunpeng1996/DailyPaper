---
title: 'Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation,
  and Accountability Architecture for Cross-Organization Autonomous AI Agents'
title_zh: 《ATI：跨组织自治AI代理的联邦身份信任与问责架构》
authors:
- Viet K. Nguyen
- Mohammad I. Husain
affiliations:
- California State Polytechnic University, Pomona
arxiv_id: '2611.23202'
url: https://arxiv.org/abs/2611.23202
pdf_url: https://arxiv.org/pdf/2611.23202
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent跨组织协作安全架构
tags:
- Agent-Security
- Federated-Identity
- Zero-Trust
- Remote-Attestation
- Multi-Agent-System
one_liner: 提出独立于Agent框架的5层信任安全架构，将跨组织攻击拦截率从43%提升至84%
practical_value: '- 跨平台Agent协作可直接复用ATI的5层安全校验设计，在Agent入口侧加独立于模型的安全代理层，无需修改现有Agent逻辑，即可快速实现跨主体身份验证、权限管控

  - 电商跨品牌/跨平台Agent协作场景，可参考AgentCA的联邦证书机制，无需统一根证书，通过对等交换CA公钥即可建立跨组织信任，适配去中心化协作需求

  - 内部Agent系统可落地Attestation层校验逻辑，对Agent的加载模型、工具集、系统prompt做哈希校验，100%拦截模型替换、工具投毒、系统prompt篡改攻击，校验开销仅0.2µs

  - 跨Agent调用的审计可复用hash链式签名日志方案，所有工具调用留痕且不可篡改，解决多Agent协作的责任溯源问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前跨组织AI Agent协作场景中，传统网络认证、API鉴权仅能验证调用方身份，无法校验Agent实际运行的模型、工具、系统prompt合法性，主流Agent框架无通用跨组织信任机制，且模型自带安全防护效果不稳定，同一种攻击在不同模型上的拦截率差异可达93%，无法满足合规与安全要求。
### 方法关键点
- 设计5层独立于Agent框架的安全平面：Identity层基于公钥哈希生成全局唯一Agent身份，所有请求必须签名；Trust层通过对等组织级AgentCA建立联邦信任，无需统一根证书；Attestation层在模型运行前校验模型、工具、系统prompt哈希与备案的一致性；Policy层对每一次工具调用做细粒度权限校验；Accountability层通过签名哈希链式日志记录所有操作，防篡改。
- 所有校验逻辑在独立安全代理层运行，无需修改现有Agent框架代码，适配CrewAI、AutoGen、LangGraph等6种主流Agent框架。
### 关键结果
在8个组织、6种Agent框架的模拟联邦环境中测试14种攻击场景、6种正常任务，对比无防护基线：总攻击拦截率从43%提升至84%，其中身份伪造、证书盗用、模型替换、系统prompt篡改等10种定向攻击拦截率达100%，正常任务成功率从91%微升至92%，单请求校验总开销仅约174µs，几乎不增加链路耗时。
> 最值得记住的结论：仅依赖Agent模型自带的安全防护不可靠，独立于模型的确定性安全校验是跨组织Agent协作的必备基础。
