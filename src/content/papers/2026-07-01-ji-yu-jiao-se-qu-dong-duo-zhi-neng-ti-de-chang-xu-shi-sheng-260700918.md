---
title: 'From Personas to Plot: Character-Grounded Multi-Agent Story Generation for
  Long-Form Narratives'
title_zh: 基于角色驱动多智能体的长叙事生成与图驱动幻觉检测框架
authors:
- Aayush Aluru
- Chloe Ho
- Muhammad Hammouri
- Kerry Luo
- Myra Malik
- Ryan Lagasse
- Arjun Bahuguna
- Vasu Sharma
affiliations:
- Pocket FM
- Princeton University
- University of Michigan
- University of Maryland
- Universitat Pompeu Fabra
arxiv_id: '2607.00918'
url: https://arxiv.org/abs/2607.00918
pdf_url: https://arxiv.org/pdf/2607.00918
published: '2026-07-01'
collected: '2026-07-02'
category: MultiAgent
direction: 多智能体长叙事生成 · 一致性评估
tags:
- MultiAgent
- Long-Form Generation
- Hallucination Detection
- World State Tracking
- DPO
one_liner: 提出多智能体叙事生成引擎Magnet与图驱动幻觉检测管线Atlas，显著提升长文本叙事一致性
practical_value: '- 多智能体分工+共享结构化世界状态的架构，可直接迁移到电商长文案生成（如系列商品故事、品牌内容连载），解决长文本前后信息不一致、人设冲突问题

  - 15步未完成换目标、40步切换内容方向的动态目标管理规则，可复用在智能导购/客服Agent的多轮对话流设计，避免对话卡顿、重复应答

  - Atlas图驱动幻觉检测管线可直接改造用于电商AIGC内容（商品详情页、营销文案）的事实一致性校验，比纯LLM-as-Judge方案F1高4.8%，误判率更低

  - 仅用1k偏好样本对角色Agent做LoRA DPO微调即可大幅提升动作符合人设的比例，可复用在各垂类业务Agent的人设对齐优化，实现低成本快速迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在长文本叙事生成中普遍存在角色设定冲突、情节前后矛盾的问题，现有多智能体生成方案依赖纯文本记忆，缺乏结构化全局状态跟踪，且没有可解释的长文本幻觉检测工具，无法支撑数百页级的连贯内容生产。
### 方法关键点
- Magnet生成框架采用四层多智能体分工：角色Agent基于人设、当前目标、共享世界状态生成动作；Critic校验动作合理性并输出世界状态更新；叙事者整合有效动作生成流畅正文；目标生成器动态更新目标，15步未完成则替换目标、40步切换故事域避免内容重复
- 共享世界状态用有向图存储全局实体、关系、属性，仅同步被叙事者选中的动作对应的状态更新，避免无效信息污染全局状态
- Atlas幻觉检测管线分三次从文本中抽取事件、实体、关系构建场景级世界图，对比前后场景的图属性冲突检测幻觉，输出结果可解释
### 关键结果
对比单模型prompting、IBSEN基线，100页长文本场景下，Magnet的编辑标注量比单模型低41%、比IBSEN低34%，幻觉数量比单模型低50%、比IBSEN低45%；Atlas幻觉检测的F1值达0.853，比纯LLM-as-Judge方案高4.8个百分点。
### 核心洞见
长文本的全局一致性无法仅依赖prompt工程实现，结构化全局状态跟踪+动态目标管理是提升长序列生成质量的核心抓手。
