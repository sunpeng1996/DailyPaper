---
title: 'What to Delegate, What to Preserve: Human Preferences for Agentic AI Across
  Everyday Life and Work'
title_zh: 生活与工作全场景下人类对Agentic AI的任务委托偏好研究
authors:
- Sarah Wheeler
- Veronica Rammouz
- Yaoyao Qian
- Zexuan Liu
- Mengyi Wei
- Anthony Rios
- Tianzhi He
- Kyrie Zhou
affiliations:
- University of Illinois Urbana-Champaign
- University of Texas at San Antonio
- Northeastern University
- Technical University of Munich
arxiv_id: '2611.09730'
url: https://arxiv.org/abs/2611.09730
pdf_url: https://arxiv.org/pdf/2611.09730
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 人机协作任务委托偏好研究
tags:
- Agentic AI
- Human-AI Collaboration
- Task Delegation
- User Preference
- HCI
one_liner: 通过9领域45场景的289人调研，明确Agentic AI任务委托的影响因素与用户偏好边界
practical_value: '- 做消费端AI Agent产品时优先落地差旅、通信、家居管理类高接受度场景，规避心理健康、医疗、创意类低接受度场景，降低冷启动阻力

  - Agent产品设计需遵循「有界自治」原则：AI负责执行重复/事务性工作，人类保留最终决策权、监督权，可显著提升用户接受度

  - 商业化定价可参考调研数据：工具类Agent单次服务中位数定价$10、月度订阅中位数定价$5，职场类Agent可适当上浮30%-50%

  - 影响用户使用意愿的核心因素是AI信任度、既往同类任务AI使用经验、预期经济收益，隐私顾虑在控制其他变量后无显著独立影响，资源投入可向信任建设倾斜'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM驱动的AI Agent已可独立完成多步任务，但用户愿意委托的任务边界、影响委托意愿的核心因素尚不清晰。过往研究多集中于职场场景或单一领域，缺乏覆盖生活与工作的全场景跨域对比，也未同时量化信任、隐私、经济收益等多维度因素的影响权重，无法支撑C端Agent产品的设计与商业化。

### 方法关键点
- 调研设计：289名有AI使用经验的美国成年人，采用重复测量设计，每人随机评估9个领域各1个场景，共覆盖45个用例、9个核心领域（家居、职场、差旅、医疗、心理健康、学习、创意、通信、财务）
- 测量维度：包含自动化偏好、多主体信任度、协作需求、隐私顾虑、付费意愿等指标，同时采集开放式反馈分析用户对AI参与形式的偏好
- 分析模型：采用广义估计方程（GEE）控制用户个体差异与领域固定效应，识别委托意愿的独立影响因素

### 关键结果数字
- 委托意愿从高到低排序：差旅>通信>学习>家居>财务>职场>医疗>创意>心理健康，其中通信场景25.3%用户愿意完全委托，心理健康场景仅10%用户愿意完全委托
- 核心正向影响因素：AI信任度（每提升1分，委托意愿提升0.47分）、预期AI主导权、同类任务AI使用经验、预期经济收益；核心负向影响因素：担心失去任务带来的个人成就感
- 付费意愿：单次服务中位数$10，月度订阅中位数$5，职场类服务定价中位数最高，单次$15、月度$8.99

### 核心结论
用户对AI Agent的核心偏好是「有界自治」，即AI可承担大部分执行工作，但人类必须保留参与、监督与最终决策权。
