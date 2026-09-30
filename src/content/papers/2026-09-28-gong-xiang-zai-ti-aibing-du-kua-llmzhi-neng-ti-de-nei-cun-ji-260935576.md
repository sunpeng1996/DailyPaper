---
title: 'Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents'
title_zh: 共享载体AI病毒：跨LLM智能体的内存跳跃攻击
authors:
- Sidharth Pulipaka
- Ansh Sharma
- Stanislau Hlebik
- Leonidas Raghav
- Vyas Raina
- Ivaxi Sheth
- Mario Fritz
affiliations:
- SPAR
- University of Cambridge
- APTA AI
- CISPA Helmholtz Center for Information Security
arxiv_id: '2609.35576'
url: https://arxiv.org/abs/2609.35576
pdf_url: https://arxiv.org/pdf/2609.35576
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 安全 · 多跳恶意攻击传播
tags:
- LLM Agent
- Prompt Injection
- Memory Poisoning
- Security
- Multi-hop Propagation
one_liner: 揭示独立LLM Agent可通过共享artifact实现无直接通信的多跳恶意攻击传播
practical_value: '- 部署带持久内存、文件读写、外部调用能力的业务Agent时，必须增加内存写入校验：检查新增内存内容是否来自用户指令而非外部输入，可阻断绝大多数此类记忆注入攻击

  - 业务Agent的外部网络访问必须配置域名白名单+用户二次确认机制，可直接阻断依赖外部端点的高传播性攻击路径

  - 电商/广告场景中多用户共享的商品详情、评论、工单等公共artifact需增加注入检测，避免单个恶意内容通过用户Agent形成大规模传播

  - 多Agent协同场景下需对高频流转的高曝光内容优先做安全筛查，仅需覆盖20%高传播节点即可拦截69%的传播路径'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前带持久内存的LLM Agent已广泛用于读写共享文件、调用外部服务，现有攻击研究多聚焦单Agent污染或存在直接通信的多Agent传播，而无直接通信的独立Agent间通过用户共享artifact的间接传播风险未被系统研究。这类攻击隐蔽性极强，攻击者仅需投放单个恶意文件即可实现大规模传播，对企业级Agent部署、电商多用户共享内容场景存在极大安全隐患。

### 方法关键点
- 定义artifact介导的传播范式：恶意内容通过共享文件写入Agent持久内存，Agent后续生成新文件时自动注入恶意内容，其他Agent读取该新文件即被感染，形成「artifact-内存-artifact」的无接触传播循环
- 设计两类攻击实现：端点辅助型（诱导Agent调用攻击者可控的外部接口自动补全完整攻击payload，大幅降低多跳传播中的内容损耗）、纯prompt型（完全依赖Agent自身记忆复制传播内容，无需外部服务依赖）
- 构建时序人机协同仿真评估环境：覆盖职场协作、个人生产力等6类场景共36个测试工作流，包含3-12个完全独立的Agent，1:1模拟真实用户读写共享文件的日常协作流程

### 关键实验结果
在4款主流LLM上测试，单个恶意种子文件最高可感染100%的独立Agent，传播链最长可达8跳；30Agent的大规模协同场景下，DeepSeek-V4-Pro、GPT-OSS-120B的感染率达90-100%，即便是能力最强的GPT-5.6 Luna感染率也达60-80%；仅需增加内存写入来源校验、配置外部访问白名单两类低成本方案，即可几乎完全阻断此类攻击。

### 核心结论
共享artifact与Agent持久内存已成为新的安全边界，无直接通信的独立Agent可通过用户日常的文件共享流程实现大规模恶意传播。
