---
title: 'Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents'
title_zh: TokenFlow防火墙：面向持久化AI Agent的语义运行时审计框架
authors:
- Puji Wang
- Yingchen Zhang
- Ruqing Zhang
- Jiafeng Guo
- Xueqi Cheng
affiliations:
- State Key Laboratory of AI Safety
- Institute of Computing Technology, CAS
- University of Chinese Academy of Sciences
arxiv_id: '2607.08395'
url: https://arxiv.org/abs/2607.08395
pdf_url: https://arxiv.org/pdf/2607.08395
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 持久化AI Agent · 运行时安全审计
tags:
- Agent Security
- Runtime Auditing
- Semantic Firewall
- Token Flow
- Persistent Agent
one_liner: 提出层级语义审计框架TokenWall，拦截AI Agent跨边界token流，兼顾安全效用与低延迟
practical_value: '- 层级审计架构可复用：优先轻量规则过滤明显风险，再用小尺寸本地模型做语义判断，仅高风险/模糊案例触发大模型仲裁，能大幅降低安全模块的运行成本与延迟，适合电商Agent、导购Agent的落地

  - 跨边界token流抽象可借鉴：将Agent的内存更新、工具调用参数、组件通信等交互统一抽象为source-sink token流，在数据落盘/工具执行前做审计，比事后行为检测的拦截效率更高，可用于防范推荐系统Agent的prompt注入、数据泄露风险

  - 支持可恢复重写的安全策略：对风险可隔离的token流做局部改写而非全量拦截，能大幅提升正常业务请求的通过率，避免安全模块过度拦截影响用户体验，适合电商场景下客服Agent、订单处理Agent的安全管控'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
持久化AI Agent支持跨会话状态留存、工具调用、能力复用，相比普通对话助手，恶意内容可通过内存、技能、组件通信等路径长期传播，攻击面大幅扩大。现有规则审计方案粒度粗，无法识别隐式语义攻击；远程大模型审计方案延迟高、需上传敏感上下文，存在隐私风险，且难以覆盖全量预执行场景。

### 方法关键点
- 提出跨边界token流抽象：将Agent所有安全相关的状态转移（内存写入、工具参数、上下文更新、权限变更等）统一建模为携带source、sink、元数据的token流，在内容落地/执行前的安全节点拦截审计
- 三层级审计流水线：1）轻量规则预检查：过滤明确规则违反的请求，降低后续语义审计负担；2）本地小模型语义审计：基于边界类型判断风险，支持允许、重写、人工审核、拦截四类决策，可对可分离的风险片段做局部改写；3）大模型 fallback 仲裁：仅高风险、高不确定性、高影响的模糊案例触发大模型终审
- 结构化审计输出：小模型输出包含风险、不确定性、可利用性、影响范围等5个[0,1]评分，结合边界类型的升级规则自动判断是否需要触发大模型仲裁

### 关键实验
在CIK-Bench持久化Agent安全基准上测试，对比7种现有Agent防御方案。TokenWall将攻击成功率降至12.5%，优于最优基线的14.7%；正常业务请求通过率达97.4%，无人工干预的正常案例新增延迟仅0.69秒，攻击案例平均延迟16.9秒，远低于大模型全量审计方案的64.3秒。

### 核心结论
持久化Agent的安全防护需从静态接口防御转向对跨边界语义信息流的自适应运行时管控
