---
title: 'MP-Bench: Evaluating Voice Agents as a Multiparty Conversation Participant'
title_zh: MP-Bench：面向多方对话参与者的语音Agent评估基准
authors:
- Yi-Jen Shih
- Shih-Yun Shan Kuan
- Guan-Ting Lin
- Kai-Wei Chang
- Siddhant Arora
- Shu-wen Yang
- Abdelrahman Mohamed
- Shinji Watanabe
- Hung-yi Lee
- David Harwath
affiliations:
- The University of Texas at Austin
- National Taiwan University
- Massachusetts Institute of Technology
- Carnegie Mellon University
- Meta AI
arxiv_id: '2609.13076'
url: https://arxiv.org/abs/2609.13076
pdf_url: https://arxiv.org/pdf/2609.13076
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: Agent 多方对话场景性能评估
tags:
- Voice Agent
- Multi-party Conversation
- Benchmark
- Turn-taking
- Response Evaluation
one_liner: 首个面向多方对话场景的语音Agent专用评估基准，覆盖轮次感知、响应合理性等维度，测试12款系统暴露显著短板
practical_value: '- 电商线下/直播场景的语音导购Agent可复用该基准的轮次感知评估维度，优化多人咨询场景下的应答时机、插话规则策略

  - 多坐席协同智能客服场景可参考该基准的响应合理性评估框架，提升多人对话上下文语义理解与应答生成准确率

  - 可迁移该基准的多轮上下文QA评估思路，优化直播场景下智能助手对多观众提问的响应优先级排序逻辑'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有语音Agent评估体系普遍聚焦双人对话、被动音频理解任务，遗漏了大量真实存在的多方对话场景，该场景下对话复杂度指数级提升，要求Agent同时具备上下文理解、轮次接管判断、响应适配能力，现有基准无法覆盖评估需求。
### 方法关键点
提出MP-Bench，是首个专门针对多方对话主动参与场景的语音Agent评估基准，核心评估三个维度：1. 轮次感知意识 2. 响应适配合理性 3. 上下文理解QA任务，实现客观量化评估。
### 关键结果
测试12款主流实时语音Agent，多方对话上下文理解准确率最高仅33%，轮次接管判断性能接近随机水平，暴露出实时语音Agent在多方场景下的显著性能短板。
