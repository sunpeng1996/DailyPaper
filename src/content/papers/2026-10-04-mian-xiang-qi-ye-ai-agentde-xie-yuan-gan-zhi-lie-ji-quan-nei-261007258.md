---
title: 'Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving
  Column-Level Access Control in Enterprise AI Agents'
title_zh: 面向企业AI Agent的血缘感知列级权限管控内存治理框架
authors:
- Venkata M Sangaraju
- Sudhir Vissa
affiliations:
- Independent Researcher
- SAGE7 AI
arxiv_id: '2610.07258'
url: https://arxiv.org/abs/2610.07258
pdf_url: https://arxiv.org/pdf/2610.07258
published: '2026-10-04'
collected: '2026-10-09'
category: Agent
direction: 企业多Agent 共享内存隐私治理
tags:
- AI Agent
- Memory Governance
- Access Control
- Data Lineage
- Privacy Preservation
one_liner: 提出附血缘图谱的AMU内存模型与派生门控策略，消除跨部门共享内存的敏感数据泄露
practical_value: '- 企业级多Agent共享内存架构可直接复用AMU的血缘追踪方案，在数据库驱动层拦截SQL自动提取列级血缘，无需修改Agent业务逻辑即可避免低权限Agent通过缓存结果泄露用户隐私、交易数据等敏感信息

  - 复用定义哈希冲突检测逻辑，解决电商多部门（运营/广告/财务）同名KPI定义不一致的语义漂移问题，自动识别GMV、复购率、用户生命周期价值等核心指标的计算逻辑差异

  - 落地时可参考90%血缘完整度的保守部署阈值，采用血缘提取失败时默认标记为最高敏感、拒绝访问的fail-closed策略，在保障安全的前提下尽可能降低工程改造量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
企业多Agent共享内存普遍采用内容/角色级访问控制，存在两大核心风险：一是合法计算的缓存结果隐含敏感列，低权限Agent访问时会造成数据泄露，AgentLeak基准显示跨Agent消息泄露率达68.8%，远超最终输出的27.2%；二是多部门同名KPI计算逻辑不一致导致语义漂移，且现有方案无法适配EU AI Act的可解释性要求。

### 方法关键点
- 设计Analytical Memory Unit（AMU）内存元组，每个缓存结果附完整派生血缘图谱，预计算敏感列集合S(a)与定义哈希H(a)
- 血缘门控检索算法：仅当请求方权限覆盖缓存结果的所有敏感列时才返回结果，复杂度最坏O(n)、最优O(1)
- 写入冲突检测逻辑：比对不同部门同名指标的定义哈希，自动识别KPI语义漂移，仅告警不阻塞写入

### 关键实验
对比无内存、原生共享内存、血缘感知内存三类方案，在5表合成数据集与8表TPC-H基准数据集上测试：原生方案跨部门泄露率达18.8%~25.5%，血缘感知方案泄露率为0（理论安全保证），保留81.5%~82.6%的内存复用率，最坏检索开销仅13.8μs；血缘完整度达75%~90%时即可完全消除泄露，LangChain+Ollama的真实Agent PoC测试9轮交互零泄露，自动识别2次KPI定义冲突。

### 核心结论
内存治理不能只管控「谁能访问什么内容」，更要校验「请求方是否有权限获取生成该内容的所有源数据」
