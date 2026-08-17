---
title: 'AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator
  and Tool Coevolution'
title_zh: AdsWorldEngine：编排器与工具协同进化的自迭代对话式广告Agent
authors:
- Simiao Zuo
- Chenhui Xu
- Yimeng Jia
- Qiang Lou
- Jian Jiao
- Denis Charles
affiliations:
- Microsoft
arxiv_id: '2608.13833'
url: https://arxiv.org/abs/2608.13833
pdf_url: https://arxiv.org/pdf/2608.13833
published: '2026-08-13'
collected: '2026-08-17'
category: Agent
direction: Agent 对话式广告投放优化
tags:
- Conversational Advertising
- LLM Agent
- GRPO
- Tool Coevolution
- Reinforcement Learning
one_liner: 提出生产级对话广告Agent框架，实现编排器与广告工具协同迭代优化
practical_value: '- 对话类广告/推荐场景可复用Opportunity Gate设计：结合规则+成本敏感GRPO训练的触发模型，优先控制负向体验（误插广告）的同时保障营收，适合对用户体验敏感的智能助手、客服对话场景

  - 借鉴编排器-工具协同迭代框架：先SFT让Agent学会工具调用流程，再用GRPO优化Agent策略，用高/低奖励轨迹自动构建偏好数据更新检索、排序工具，无需额外人工标注即可实现推荐全链路迭代

  - 生产场景的判断模型可复用标签grounded训练流程：基于人工标注+引导生成思考链+反射过滤不一致样本+成本敏感GRPO，可解决搜索推荐中误推比漏推代价更高的不对称错误成本分类问题

  - 商业化优化逻辑可参考：对话广告场景同时优化广告相关性与多样性，可实现用户体验与商业化双赢，同时提升RPM和广告覆盖率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话式广告需要从多轮对话历史、助手回复中隐式推断用户商业意图，还要判断广告是否会打扰用户，现有方案大多只优化单个模块，缺乏端到端生产级框架；同时Agent与下游检索、排序工具割裂，无法协同优化，常规判断模型也难以适配生产场景不对称的错误成本（比如误插广告比漏插对用户体验伤害大）。

### 方法关键点
- 核心框架分4模块：Opportunity Gate（规则+触发模型判断当前轮次是否适合插广告）、Orchestrator（对话状态解析、商业意图生成、工具调用、筛选Top3广告slate）、广告工具集（检索、相关性、排序、定价等）、Evaluator（离线从用户/广告主/平台三方维度打分，提供训练奖励）
- 标签grounded判断建模流程：基于生产规则人工标注样本，引导LLM生成对应标签的思考链，通过反射步骤过滤与标签矛盾的样本，用成本敏感GRPO训练（关闭组标准差缩放，保留不对称奖励gap），适配错误成本不对称的分类任务
- 编排器与工具协同迭代算法：先SFT训练编排器的基础工具调用能力，固定工具用GRPO优化编排器策略，再用编排器的高/低奖励轨迹构建偏好对(intent, a+, a-)，用DPO类损失更新下游工具，循环迭代实现二者协同进化

### 关键实验
离线对比微软现有生产广告系统，多样性提升60%、相关性提升80%；线上A/B测试在Microsoft Copilot部署20天，RPM提升22%，广告覆盖率提升74%；触发模型对比prompted GPT-5，FPR下降39%同时TPR不变，平衡准确率提升2.5%。

最值得记住的一句话：Agent系统优化不能仅把下游工具当作固定基础设施，通过奖励轨迹让编排器与工具协同迭代，能同时提升用户体验与商业化收益。
