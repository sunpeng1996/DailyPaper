---
title: 'A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate
  Information Sharing'
title_zh: 上下文完整性生成模型：区分信息共享的适当与不适当场景
authors:
- Omer Ebead
- Claude Formanek
- Joel Z. Leibo
affiliations:
- Cooperative AI Foundation
- Cape Institute for Safe AI
- African Institute for Mathematical Sciences, South Africa
- Google DeepMind
arxiv_id: '2611.08284'
url: https://arxiv.org/abs/2611.08284
pdf_url: https://arxiv.org/pdf/2611.08284
published: '2026-11-05'
collected: '2026-11-08'
category: Agent
direction: Agent 多角色交互隐私规范研究
tags:
- LLM-Agent
- Contextual Integrity
- Privacy Compliance
- Multi-Agent Simulation
- Information Sharing
one_liner: 基于双LLM对话模拟构建上下文完整性生成模型，可研究不同场景下的信息共享规律
practical_value: '- 电商客服Agent、用户隐私交互场景可复用双Agent模拟框架，提前测试隐私泄露风险，优化敏感信息回复的合规性

  - 可借鉴上下文规范判定逻辑，优化推荐/广告系统的用户敏感信息采集、使用规则，避免违规获取或使用用户隐私

  - 多Agent交互的合规性测试方法可复用，用于业务对外输出Agent的安全测评，比如客服话术、直播带货话术合规校验'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
上下文完整性（CI）理论指出信息流动的适当性高度依赖场景规范，现有隐私合规方法大多基于静态规则，无法适配动态交互场景下的边界判定需求，也缺乏高效的模拟测试框架来验证智能体的信息共享行为合规性。
### 方法关键点
1. 构建双LLM驱动的多角色对话模拟框架，分别由两个智能体扮演私有信息持有者、信息索取方，复现真实信息交互流程
2. 以CI理论为判定基准，控制变量测试场景类型、持有者决策逻辑、性格倾向、底座LLM选型等因素对信息共享/拒绝行为的影响
3. 覆盖合规索取、诈骗伪装等多类典型场景，全程追踪对话过程中的信息披露行为演变规律
### 关键结果
实验验证智能体可准确响应合法索取者的信息需求，同时存在超30%的概率向无权限的伪装索取者不当披露隐私信息，框架可有效支撑不同场景下的信息共享规范研究
