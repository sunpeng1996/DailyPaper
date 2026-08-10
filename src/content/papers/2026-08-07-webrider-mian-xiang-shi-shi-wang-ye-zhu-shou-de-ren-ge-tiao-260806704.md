---
title: 'WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance'
title_zh: WebRider：面向实时网页助手的人格条件化意图控制器
authors:
- Zhi Li
- Tao Zhou
- Yeqing Li
- Eugene Ie
- Demetri Terzopoulos
affiliations:
- University of California, Los Angeles
- Google
arxiv_id: '2608.06704'
url: https://arxiv.org/abs/2608.06704
pdf_url: https://arxiv.org/pdf/2608.06704
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: 网页Agent · 人格条件化意图控制
tags:
- WebAgent
- Persona Conditioning
- Intent Tracking
- Hierarchical Control
- Agent Evaluation
one_liner: 提出意图契约与分层控制架构，解决网页Agent执行的用户委托策略保真度不足问题
practical_value: '- 电商导购Agent可复用「意图契约」设计：将用户偏好、校验要求（如验正品、看售后政策）、停止条件固化为可审计的结构化契约，避免推荐结果符合表层要求但违反隐性策略

  - 分层控制架构可直接迁移：上层维护契约状态做长周期决策，下层仅做当前页动作生成，分工明确易迭代，下层动作模块可单独用小模型SFT优化，无需修改上层逻辑

  - Agent评估可增加轨迹级校验：不要仅看最终结果，需加契约门控校验和步级人工舒适度评分，避免搜品Agent仅最终商品价格符合要求，但跳过验卖家信誉等用户要求的步骤

  - 同任务反事实构造方法可复用：同一个搜索请求搭配不同用户策略生成测试case，验证推荐/导购Agent的个性化策略是否真正生效，而非输出通用结果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有网页Agent仅以最终任务完成率为评估目标，忽略用户委托时隐含的策略约束（如搜品需校验卖家信誉、不确定时需主动询问），强基线Full-Pro任务完成率达99.2%，但完全符合所有策略约束的占比仅38.8%，任务完成不代表符合用户真实预期，亟需可审计、高保真的网页Agent架构。

### 方法关键点
- 提出**意图契约**：将用户目标、硬约束、证据举证要求、回答格式、任务级人格控制策略固化为可审计的稳定记录，仅当用户明确澄清时才允许修改
- 三层分层控制架构：上层维护契约状态，决策浏览、询问、停止、回答等长周期行为；中间层将上层意图转换为带安全校验的原子JSON动作AST，禁止做证据充足性判断；下层执行器调用浏览器、搜索等工具执行动作
- 构建RiderBench基准：包含768个基础任务，搭配15种人格策略生成4096个意图契约，覆盖42个公开网站，同时支持契约门控自动评估和步级人工可接受度评估

### 关键结果
- 基线Full-Pro任务完成率99.2%，但契约门控成功率（CGS）仅38.8%，验证了任务完成率和策略保真度的巨大gap
- 分层架构的IntentCore相比纯prompt注入人格+意图的方案，CGS提升5.6pp，人格一致性得分（PCS）达86%，人工委托偏好（HCP）领先基线42.5%
- 仅替换中间层动作策略的MidSFT-8B模型，在固定上层控制器的情况下CGS达50.8%，超过Exec-Pro基线19.6pp，验证了分层架构的可训练性

### 核心结论
对于网页Agent，执行路径本身就是任务的一部分，显性的意图契约是验证路径是否符合用户委托的核心依据
