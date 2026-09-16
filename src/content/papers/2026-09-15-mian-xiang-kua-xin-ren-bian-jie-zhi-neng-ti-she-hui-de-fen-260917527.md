---
title: Agentic Societies Need a Social Harness
title_zh: 面向跨信任边界智能体社会的分层Social Harness治理架构
authors:
- Tapan Chugh
- Vidushi Singh
- Krish Jain
- Arvind Krishnamurthy
- Ratul Mahajan
affiliations:
- University of Washington
arxiv_id: '2609.17527'
url: https://arxiv.org/abs/2609.17527
pdf_url: https://arxiv.org/pdf/2609.17527
published: '2026-09-15'
collected: '2026-09-16'
category: MultiAgent
direction: 多智能体协作 · 跨信任边界治理
tags:
- MultiAgent
- Social Harness
- Cross Trust Collaboration
- Agent Communication
- MultiAgent Security
one_liner: 提出5层Social Harness架构，解决跨信任多智能体协作的效率、可靠性与安全问题
practical_value: '- 电商多Agent协作场景（用户导购Agent、商家运营Agent、平台治理Agent的售后/优惠协商）可直接复用分层架构：L1身份校验防仿冒官方消息，L3规则防火墙拦截商家虚假承诺、用户恶意索赔请求，降低欺诈率

  - 多Agent任务协调（大促跨部门Agent调度、广告投放多角色Agent协同）可引入L4任务级协作契约，约定发言顺序、有效消息格式、协商终止条件，避免消息风暴与协商死锁，实测可将消息量降低3~25倍

  - Agent交互安全设计可复用信任分层思路：优先在Harness层而非LLM推理层实现校验规则，避免prompt注入绕过防护，同时降低推理开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前跨信任边界的多智能体协作存在普遍问题：即使所有Agent均诚实可信，也会因上下文隔离、消息时序冲突、协商策略不一致出现协作失败；恶意Agent可利用通信漏洞实施拖延、欺骗、隐私窃取等攻击，现有多Agent框架（CrewAI、AutoGen等）均面向单主体设计，跨主体通信协议仅解决连通性问题，无协作治理能力，无法满足电商、企业协作等场景下多利益主体的Agent协作需求。

### 方法关键点
提出与Agent个人Harness解耦的5层Social Harness架构，专门处理跨主体通信治理：
1. L1不可伪造身份层：所有消息签名校验，防仿冒、Sybil攻击
2. L2可靠有序通信层：支持组播、汇聚等集体通信原语，可选悲观并发控制避免消息时序冲突
3. L3个人防火墙层：按信任规则校验入站消息的结构、语义合法性，拦截胁迫、欺骗类消息
4. L4协作规范层：通过任务级契约约定发言顺序、有效消息格式、协商终止条件，支持活跃度、安全性预校验
5. L5社会制度层：基于不可篡改通信日志实现事后溯源、问责，对违规Agent实施权限封禁等处罚

### 关键实验
基于会议调度场景测试，覆盖1~7个参与Agent、全GPT-5.4/混合Claude Opus 4.8两种模型配置、3种通信模式：
- 诚实Agent场景下，7人组会议调度，p2p隔离上下文下Claude配置成功率为0%，切换为共享上下文后成功率提升至90%，组播模式可将消息量降低3~25倍
- 存在1个恶意Agent场景下，欺骗攻击成功率最高达100%，社会压力攻击成功率最高达30%，单Agent无法检测合谋类攻击

### 核心结论
仅靠LLM能力优化无法解决跨信任多智能体协作的失效与安全问题，必须在通信治理层构建系统性防护架构。
