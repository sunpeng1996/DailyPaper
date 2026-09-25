---
title: Agentic Detection of Online Conspiracies
title_zh: 基于智能体的网络阴谋论言论检测方法
authors:
- Lior Biton
- Oren Tsur
affiliations:
- Ben-Gurion University of the Negev, Israel
- Department of Computer and Information Science
arxiv_id: '2609.30250'
url: https://arxiv.org/abs/2609.30250
pdf_url: https://arxiv.org/pdf/2609.30250
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 语境推理·内容风险识别
tags:
- Agent
- Intent Recognition
- Social Context Reasoning
- Text Classification
- Misinformation Detection
one_liner: 提出配备社交查询工具的Agent框架，结合自适应语境推理识别社交媒体阴谋论发言意图
practical_value: '- 内容/评论风险审核场景可借鉴「按需调用工具获取社交上下文」的Agent推理范式，替代全量上下文投喂，降低token消耗的同时提升识别准确率

  - 意图识别类任务中，相同文本匹配不同用户历史行为/社交关系语境的思路，可迁移到推荐系统用户意图推断、评论情感极性判别等场景

  - 标注稀缺的adversarial分类任务中，可优先验证context-aware的Agent方案相比纯文本分类基线的效果优势'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
社交媒体阴谋论言论无稳定lexical标记，相同文本可对应支持、批评、讽刺等多元意图，纯文本分类无法推断发言者真实意图，现有方案忽略社交语境的自适应调用逻辑。
### 方法关键点
提出内置社交查询工具集的Agent框架，可根据当前推理步骤按需调用对应社交上下文（如用户历史发言、同内容互动数据等），无需全量投喂所有可用上下文。
### 关键结果
- 覆盖2018-2023年80%~90%希伯来语公开推文的数据集测试，人工标注对抗集下context-aware方案效果显著优于纯文本分类
- Agent框架效果明显优于接入相同全量上下文的非Agent基线，同时可通过工具按需调用平衡识别效果与token消耗
