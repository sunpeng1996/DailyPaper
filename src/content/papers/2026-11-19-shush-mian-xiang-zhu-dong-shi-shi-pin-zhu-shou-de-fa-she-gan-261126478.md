---
title: 'SHUSH: Emission-Aware Reward Design for Proactive Video Assistants'
title_zh: SHUSH：面向主动式视频助手的发射感知奖励设计
authors:
- Shawn Liang
- Soamar Homsi
- Gourav Datta
affiliations:
- Case Western Reserve University
- Air Force Research Laboratory
arxiv_id: '2611.26478'
url: https://arxiv.org/abs/2611.26478
pdf_url: https://arxiv.org/pdf/2611.26478
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 主动交互奖励优化
tags:
- Proactive Agent
- Reward Design
- Reinforcement Learning
- Video LLM
- F1 Reward
one_liner: 针对主动视频助手过度输出问题，设计发射感知F1奖励，降低回复量同时提升精度与F1
practical_value: '- 电商主动客服、直播智能助理、短视频主动互动Agent，可直接替换原有PAUC类奖励为发射感知F1奖励，避免过度骚扰用户，同时降低无效推理成本

  - 主动push、弹窗、个性化推荐场景，原有奖励仅优化点击/转化召回易导致过度推送，可复用一对一双边匹配的奖励设计，给无效推送增加显式成本，平衡用户体验与业务目标

  - RL优化交互系统时，可通过调整γ、β参数快速适配业务需求：需高召回（比如售后风险提醒）调大β，需低打扰（比如营销消息推送）调大γ'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
主动式交互助手需要自主决策何时回复，现有PAUC类奖励仅鼓励及时正确回复，不惩罚过量输出，会导致系统频繁发送无效回复，浪费用户注意力、消耗算力还降低用户信任；现有辅助惩罚项归一化后会随决策步数增加而失效，稀疏事件场景下过度发射问题尤其严重。

### 方法关键点
- 基于F1的发射感知奖励通过最大权重二分匹配将模型输出与黄金标注区间一一绑定，每个标注区间最多给1个回复计奖励，未匹配的回复直接计成本，新增回复必须带来足够价值才能覆盖成本，从底层避免无代价重试
- 设计区间边界连续加权函数，避免边界处奖励跳变，α控制区间内回复时效折扣，γ控制无效发射惩罚权重，β控制召回权重，可灵活适配不同业务需求

### 关键实验
在OmniPro视觉子集上对比MMDuet2基线：β=1.5配置下回复量降2.5倍，时序F1从0.259升至0.396，内容F1从0.103升至0.154；γ=1.5保守配置下回复量降82.5%，精度从0.161升至0.418。在ProactiveVideoQA数据集上验证原有PAUC指标完全不感知回复量，过度发射的模型可拿到高PAUC但F1极低，新奖励在多数子数据集上同时提升PAUC和F1。

### 核心结论
所有主动交互系统的奖励设计必须给每一次输出赋予明确的边际成本，否则必然会激励过度输出。
