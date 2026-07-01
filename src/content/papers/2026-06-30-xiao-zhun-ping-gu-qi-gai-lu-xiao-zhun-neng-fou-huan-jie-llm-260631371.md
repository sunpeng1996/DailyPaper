---
title: 'Calibrating the Evaluator: Does Probability Calibration Mitigate Preference
  Coupling in LLM Agent Feedback Loops?'
title_zh: 校准评估器：概率校准能否缓解LLM Agent反馈回路的偏好耦合
authors:
- Zewen Liu
affiliations:
- 齐鲁理工学院软件工程学院
arxiv_id: '2606.31371'
url: https://arxiv.org/abs/2606.31371
pdf_url: https://arxiv.org/pdf/2606.31371
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent反馈回路偏好耦合缓解
tags:
- LLM Agent
- Probability Calibration
- Preference Coupling
- TTRL
- LLM-as-Judge
one_liner: 提出置信度校准的TTRL协议，缓解LLM Agent反馈回路中的评估器偏好耦合
practical_value: '- 电商/广告场景的LLM-as-judge评估链路可直接替换二元判断为置信度 elicitation，用置信度加权更新排序/召回策略，降低评估偏好导致的马太效应

  - 推荐系统在线实验评估阶段，可加入滑动窗口等距回归校准评估器置信度，无需改动召回/排序模型即可降低偏好传导，提升策略多样性

  - Agent闭环迭代场景可复用校准TTRL协议，通过置信度门控过滤低置信度评估信号，减少无效策略更新，降低偏好崩塌风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多Agent LLM系统普遍依赖评估器反馈指导策略迭代，但评估器自带的系统偏好会通过反馈回路持续传导，导致Agent策略分布被扭曲、出现偏好崩塌，现有研究仅能诊断该问题，未提出可落地的缓解方案，因此探索概率校准对偏好耦合的抑制价值很高。

### 方法关键点
- 改进标准TTRL（测试时间强化学习）协议，修改评估prompt要求评估器输出0-1的偏好置信度，而非二元胜负判断
- 采用滑动窗口等距回归对最近10轮的（置信度、实际胜负）对做实时后校准，修正评估器置信度偏差
- 策略权重更新采用置信度加权机制：置信度为0.5时无更新，置信度为1时更新幅度等于原二元判断的赢局更新幅度，避免弱偏好累积

### 关键实验
以DeepSeek-V4-Pro为执行Agent、GLM5.2为评估器，做5组被试内对照实验，对比标准二元TTRL：耦合系数γ在T→V方向降低20%、V→T方向降低49%；策略分布的Jensen-Shannon散度在T→V方向降低45%、V→T方向降低67%；对称学习率、输出长度归一化两组控制实验均验证效果不是来自更新不对称或输出格式偏差。

最值得记住的一句话：仅需调整评估器输出格式和更新规则的轻量化校准方案，就能大幅降低LLM-as-judge闭环系统的偏好耦合，无需改动执行模型。
