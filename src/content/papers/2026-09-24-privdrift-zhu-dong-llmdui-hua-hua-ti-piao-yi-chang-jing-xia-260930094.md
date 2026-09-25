---
title: 'PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations'
title_zh: PrivDrift：主动LLM对话话题漂移场景下的用户隐私泄露审计
authors:
- Luciano Maldonado
affiliations:
- West Virginia University
arxiv_id: '2609.30094'
url: https://arxiv.org/abs/2609.30094
pdf_url: https://arxiv.org/pdf/2609.30094
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: LLM会话隐私风险评估
tags:
- Privacy
- LLM Security
- Benchmark
- Multi-turn Conversation
- Information Leakage
one_liner: 提出PrivDrift基准，审计多轮LLM对话话题漂移后用户敏感信息的泄露风险
practical_value: '- 部署电商导购、客服类Agent时，需新增话题漂移后的敏感信息泄露检测环节，避免用户此前提交的地址、支付信息等被恶意prompt提取

  - 多轮会话的隐私防护不能依赖话题跳转自动脱敏，需主动对KV cache中存储的PII类信息做定向擦除或加密处理

  - 上线面向C端的LLM助手前，可参考PrivDrift的构造逻辑生成专项测试用例，全链路评估会话周期内的隐私风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM广泛作为持久化助手应用于多轮会话场景，现有隐私评估仅覆盖训练数据记忆、即时越狱两类场景，未覆盖会话内话题漂移后早期提交的敏感信息仍可被后续探测提取的风险。
### 方法关键点
构建PrivDrift审计基准，包含1000组可控多轮对话，植入预设敏感信息、设置内容密集的话题漂移轮次、配套标准化的诱导式提取探针，可量化不同LLM的会话隐私泄露水平。
### 关键结果
3款长上下文LLM的会话级混合泄露率达38.7%~54.6%，泄露率与模型选型、敏感信息类型、探测诱导强度强相关；测试范围内增加话题漂移轮次无法有效降低泄露率，活跃会话的隐私风险属于持续的行为级故障，而非仅偶发的越狱或训练记忆问题。
