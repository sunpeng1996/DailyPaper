---
title: A Self-Evolving Agent for Longitudinal Personal Health Management
title_zh: 面向长期个人健康管理的自进化Agent架构
authors:
- Haoran Li
- Jiebi Deng
- Tong Jin
- Jinghong Han
- Yuxin Wang
- Zexin Wang
- Qingyi Si
- Weikang Gong
- Xiahai Zhuang
- Jia You
affiliations:
- 复旦大学
- 京东
- 北京中医药大学
- 华中科技大学
arxiv_id: '2607.13940'
url: https://arxiv.org/abs/2607.13940
pdf_url: https://arxiv.org/pdf/2607.13940
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 长时记忆与自进化优化
tags:
- Agent
- Long-Term Memory
- Self-Evolving
- Privacy Protection
- Prompt Optimization
one_liner: 提出分离公共知识与私有分层记忆的自进化开源健康Agent，大幅提升长时响应准确率与隐私性
practical_value: '- 长时用户记忆可采用「公共规则/通用知识 + 私有分层记忆（静态画像/可复用流程/交互片段）」的拆分架构，既降低prompt长度又保留个性化信息，可直接迁移到电商用户长期偏好建模场景。

  - 每次交互结束后新增自动归纳步骤，动态判定记忆更新/淘汰规则，避免全量历史塞入prompt，可复用到搜索推荐的用户行为序列动态压缩、个性化Agent上下文管理场景。

  - 私有记忆与公共知识物理分离的设计，可直接复用在需要保护用户隐私的个性化服务场景（比如电商私域用户服务Agent），降低隐私泄露风险。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有个性化AI系统大多孤立处理单次请求，未基于用户长期状态迭代输出策略，无法适配长周期个性化服务需求，还存在上下文冗余、隐私泄露风险。
### 方法关键点
1. 开源Agent架构HealthClaw将共享安全规则、通用领域知识与用户私有长时记忆解耦，私有记忆拆分用户静态画像、可复用流程、交互片段三类；
2. 每次交互结束后新增归纳模块，自动判定记忆更新策略：更新画像、修订流程、留存片段或直接淘汰，无需人工介入。
### 关键结果
900组长时响应测试中，准确率从仅用当前query prompting的0.2%提升至45.7%，prompt上下文长度比全量历史prompt方案低71.7%；100组隐私测试中隐私合规表现优于所有基线；9组生物医学任务核心指标平均提升27个百分点。
