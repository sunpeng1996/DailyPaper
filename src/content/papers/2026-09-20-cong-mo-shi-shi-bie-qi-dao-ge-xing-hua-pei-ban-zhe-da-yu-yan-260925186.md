---
title: 'From Pattern Recognizers to Personalized Companions: A Survey of Large Language
  Models in Mental Health'
title_zh: 《从模式识别器到个性化陪伴者：大语言模型心理健康应用综述》
authors:
- He Hu
- Yucheng Zhou
- Qianning Wang
- Yingjian Zou
- Chiyuan Ma
- Juzheng Si
- Jianzhuang Liu
- Zitong Yu
- Laizhong Cui
- Fei Ma
arxiv_id: '2609.25186'
url: https://arxiv.org/abs/2609.25186
pdf_url: https://arxiv.org/pdf/2609.25186
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: LLM+Agent 心理健康领域应用综述
tags:
- LLM
- Mental Health
- Agent Architecture
- Survey
- Longitudinal Personalization
one_liner: 将心理健康领域LLM应用划分为三阶段演进框架，系统梳理核心技术、Agent架构与基准资源
practical_value: '- 三阶段演进框架可迁移到个性化用户陪伴Agent的迭代规划，从工具→即时交互→长期陪伴的路径可直接复用

  - Agent的Profile/Memory/Reasoning/Planning四模块架构，可套用到电商专属导购Agent、会员陪伴Agent的设计

  - 纵向个性化建模思路可借鉴到长周期用户兴趣建模、复购唤醒、高价值用户留存等推荐场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
全球心理健康患病率持续上升，传统医疗存在资源有限、成本高、隐私顾虑等壁垒，当前LLM在心理健康领域的研究碎片化，缺乏统一的演进脉络梳理，难以明确发展方向。
### 方法关键点
将LLM在心理健康领域的应用划分为三个递进演化阶段：
1. 阶段1：作为被动信息工具与模式识别器，用于心理健康评估诊断
2. 阶段2：作为共情对话者，提供无状态的即时情绪支持交互
3. 阶段3：作为纵向个性化陪伴者，以有状态认知Agent实现长期陪伴
系统梳理各阶段核心技术、Agent四模块（Profile、Memory、Reasoning、Planning）架构、数据集与评测基准。
### 关键结果
输出了负责任、以人为中心的心理健康AI发展路线图，同时开源了整理好的领域资源库，覆盖相关研究、数据集等核心资源
