---
title: Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent
  Context Compaction
title_zh: Agent上下文压缩场景下的规则合规性评估基准ARCBench
authors:
- Yiwei Zha
- Qingyu Meng
- Herbert Bos
- Min Chen
affiliations:
- Vrije Universiteit Amsterdam, VUSec
arxiv_id: '2611.03223'
url: https://arxiv.org/abs/2611.03223
pdf_url: https://arxiv.org/pdf/2611.03223
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 规则合规性评估基准
tags:
- LLM Agent
- Context Compaction
- Rule Compliance
- Benchmark
- Agent Safety
one_liner: 基于pi Agent构建可配置基准ARCBench，定位上下文压缩后的规则违规来源并分析影响因素
practical_value: '- 电商/运营类Agent部署时，高风险规则（如发券、退款、用户信息披露规则）不要进入通用上下文压缩流程，做单独固定挂载，避免规则被压缩弱化或忽略

  - 上下文压缩策略优先选择带规则保留优化的生成式压缩方案，避免FIFO等选择性压缩策略，后者规则丢失率达84%，违规率是生成式方案的2倍以上

  - 压缩token预算不要低于750，300及以下预算下95%的规则会被丢弃，违规率上升至50%

  - 工具调用环节增加独立的规则校验层，不要依赖上下文规则留存保障合规，攻防场景下就算规则100%留存，违规率仍高于无攻击基线'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent长会话需压缩上下文适配窗口限制、降低推理成本，但现有研究仅发现压缩后规则违规率上升，未在完整Agent运行链路中评估合规性，也无法定位违规来源（是规则被删除还是Agent主动忽略），不同压缩配置、攻防场景对违规的影响也不清晰。

### 方法关键点
- 基于开源pi Agent框架构建ARCBench，覆盖17个对应OWASP风险类的任务场景，支持规则投递方式、压缩策略、压缩预算、攻防配置自定义
- 设计双判定机制：规则状态judge判定压缩后规则的状态（完全保留/部分保留/丢失）；Agent行为judge定位规则留存时的违规原因（将后续请求当许可/范围误判/未感知规则/明知故犯）
- 核心指标采用violation@k，统计至少出现1次违规的任务占比，对齐安全场景的风险评估逻辑

### 关键结果
- 全上下文基线违规率为9.6%，压缩后违规率升至37.8%；70.1%的压缩上下文仍完全保留规则，但这类场景的违规率是全上下文的2.6倍
- 选择性压缩（如FIFO）违规率达50.2%，84.1%的规则被完全丢失；生成式压缩违规率为21.8%，91.2%的规则被保留
- 针对性注入攻击使违规率升至46.3%，规则保留率降至42.5%；最强防御可将规则保留率恢复至99%，但违规率仍高于无攻击基线

### 核心结论
规则在压缩上下文中存在，完全不等于Agent会遵守该规则，规则保留不能作为合规的充分指标
