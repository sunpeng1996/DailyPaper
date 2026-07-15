---
title: 'KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving
  Memory and Skill'
title_zh: KnowAct-GUIClaw：具备自进化记忆与技能的个人GUI自动化助手
authors:
- Yunxin Li
- Jinchao Li
- Shibo Su
- Zhenran Xu
- Chenrui Zhao
- Tongshu Bian
- Xiaoman Liang
- Meishan Zhang
- Baotian Hu
- Min Zhang
arxiv_id: '2607.12625'
url: https://arxiv.org/abs/2607.12625
pdf_url: https://arxiv.org/pdf/2607.12625
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: GUI Agent 跨平台自进化优化
tags:
- GUI Agent
- Self-Evolution
- Cross-Platform
- Memory System
- Skill Library
one_liner: 提出带自进化记忆与技能库的GUI Agent框架，解决现有方案跨平台适配差、无自进化机制的问题
practical_value: '- 可插拔GUI子Agent设计可直接复用，适配电商多端（APP/PC/小程序）自动化运营任务，如批量商品上架、客诉自动处理

  - 经验可归因记忆+自进化技能库架构可迁移到推荐系统用户偏好记忆模块，提升跨session购物车补全等长周期任务准确率

  - 基于用户反馈迭代任务分解逻辑的思路，可用于搜索推荐Agent的query理解与执行链路优化，降低人工规则配置成本'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有主流Agent框架OpenClaw跨平台GUI交互支持不足，缺乏自进化机制，无法适配多设备生态、难以通过执行经验持续优化性能。
### 方法关键点
基于认知-执行统一范式提出Know-Route-Act-Reflect架构：1. 主Agent基于积累的交互经验与任务相关知识完成长周期任务分解与分配；2. 可插拔GUI子Agent搭配经验可归因记忆系统与自进化技能库，支持无缝跨平台迁移与快速能力集成；3. 框架持续存储用户画像与反馈，迭代优化任务分解与工具调用准确率。
### 关键结果数字
在Android、iOS、HarmonyOS、Windows多平台实验中效果领先；基于开源Kimi-2.6的版本在长周期MobileWorld基准上准确率达64.1%，超过Seed-2.0-Pro、GPT-5.5等所有闭源Agent模型；记忆与技能模块可跨基座迁移，对Kimi-2.6的性能提升达8.5%
