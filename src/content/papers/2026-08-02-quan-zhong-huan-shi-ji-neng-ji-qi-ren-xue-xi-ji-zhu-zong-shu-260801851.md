---
title: 'Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting
  Weights to Robots that Write their Own Skills'
title_zh: 权重还是技能？机器人学习技术综述：从动作预测权重到自编写技能机器人
authors:
- Gaytri Jena
- Kapil Wanaskar
- Vinija Jain
- Aman Chadha
- Vasu Sharma
- Amitava Das
affiliations:
- UC Berkeley
- San Jose State University
- Meta
- Apple
- BITS Pilani Goa
arxiv_id: '2608.01851'
url: https://arxiv.org/abs/2608.01851
pdf_url: https://arxiv.org/pdf/2608.01851
published: '2026-08-02'
collected: '2026-08-08'
category: Agent
direction: Agent 自主技能迭代与分类体系研究
tags:
- Robot Learning
- Code-as-Policy
- Self-Improvement
- VLA Model
- Skill Library
one_liner: 沿权重/技能轴梳理机器人学习领域，给出代码即策略自改进分类体系与技能经济开放问题
practical_value: '- 可复用「按自改进程度划分能力层级」的分类思路，给业务Agent的工具调用/策略迭代能力做分级评估，明确迭代边界

  - 代码即技能的无梯度自优化方案可迁移到推荐系统的规则生成/调整场景，避免频繁小样本微调的成本

  - 静态技能库+动态反馈修复的架构可复用给电商客服Agent/营销话术生成Agent，降低规则维护成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前机器人学习领域存在VLA模型（能力固化在冻结权重）、代码即技能Agent（自主编写优化可执行技能）两大并行范式，缺乏统一框架梳理技术边界与演进路径。
### 方法关键点
1. 沿「权重vs技能」核心轴梳理领域，将代码即策略方法按自改进程度分层：零样本程序合成→闭环自修复→持久化技能记忆→结合执行反馈、记忆、进化搜索的开放循环四层；
2. 明确技能的5种定义，仅代码形态的技能可实现无梯度更新的自改进；
3. 覆盖6大技术族共77个代表性系统，明确各技术族的能力边界与不足。
### 关键结果
识别出当前商用机器人技能市场仅支持静态技能分发，存在适配性、跨载体迁移、安全验证等6类核心开放问题；仅ASPIRE、ENPIRE、RoboClaw等极少数系统实现了最高级的开放自改进循环。
