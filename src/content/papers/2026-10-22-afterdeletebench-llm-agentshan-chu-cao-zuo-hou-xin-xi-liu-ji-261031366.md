---
title: 'AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents'
title_zh: AfterDeleteBench：LLM Agent删除操作后信息留存审计基准
authors:
- Ehsan Saleh
- Roozbeh Nahavandi
- Sama Salarian
- Raef Bassily
- Andrew Perrault
affiliations:
- The Ohio State University
arxiv_id: '2610.31366'
url: https://arxiv.org/abs/2610.31366
pdf_url: https://arxiv.org/pdf/2610.31366
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: LLM Agent · 隐私审计与信息删除
tags:
- LLM-Agent
- Privacy-Audit
- Memory-Management
- Forgetting
- Benchmark
one_liner: 提出固定权重LLM Agent删除后信息残留的行为审计基准，量化衍生状态的泄漏风险
practical_value: '- 开发带持久记忆的电商导购/客服Agent时，用户删除隐私数据（地址、手机号、消费记录等）不能仅删除源交互记录，需基于provenance追溯所有衍生的summary、关联记忆片段一并清理，避免合规风险

  - 做Agent隐私合规审计时，不能仅排查存储层的敏感数据残留，需增加黑盒行为探测环节，构造多轮查询试探是否能恢复已删除信息，同时需对齐响应格式与解析规则，避免漏判实际泄漏

  - 可落地两类互补的删除防护机制：全链路provenance跟踪的衍生数据联动删除（彻底清除现有残留）、写入阶段的敏感内容精确过滤（防止已泄漏信息被回写入持久内存）'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
带持久记忆的LLM Agent会基于用户交互生成摘要、关联特征等衍生状态，用户删除原始交互记录时，衍生状态中的残留信息仍可能被恢复泄漏，现有删除校验仅验证存储层源记录是否移除，无法覆盖这类合规风险，缺乏统一可控的行为审计方法。
### 方法关键点
- 采用成对对照实验范式：同一份数据分别在「暴露秘密后删除源记录的forget组」和「从未暴露秘密的clean组」运行，两组信息恢复率的差值直接归因于删除后的残留泄漏
- 拆分三个独立生命周期度量：Reconstruction（单次查询能否直接恢复已删信息）、Commitment（恢复的信息是否会被回写入持久内存）、Activation（全新会话能否再次召回已删信息）
- 测试两类互补干预方案：基于完整provenance追溯的衍生状态联动删除、写入阶段的精确敏感字面量过滤
### 关键结果
- 单条直接查询可从Qwen2.5-7B-Instruct恢复68%的已删秘密，对照组恢复率为0；即使无完整秘密串，仅留存分散组件+公开拼接规则时，Qwen/Mistral/Phi-3的恢复率仍达62%~99%
- 全链路provenance联动删除可将恢复率降至0，写入过滤仅能阻止泄漏信息回写，无法消除已存在的内存残留
- 请求格式与解析器不匹配会导致70%以上的实际泄漏被漏判，如模型已返回秘密但解析器未读取对应字段时会被误记为无泄漏
### 核心结论
LLM Agent的删除有效性必须在系统行为层面审计，不能仅验证存储层源记录的删除
