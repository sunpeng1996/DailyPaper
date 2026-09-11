---
title: 'The Convention Gap: Towards Measuring Implicit Communication in Cooperative
  AI Evaluation'
title_zh: 合作AI评估中隐式通信的「惯例差」度量方法
authors:
- Makoto Fukushima
- Hua-Dong Xiong
- Ehsan Moradi Pari
affiliations:
- Honda Research Institute Japan
- Honda Research Institute USA
arxiv_id: '2609.11489'
url: https://arxiv.org/abs/2609.11489
pdf_url: https://arxiv.org/pdf/2609.11489
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: 协作Agent · 人机适配评估
tags:
- Cooperative AI
- Implicit Communication
- Agent Evaluation
- Human-AI Collaboration
- Convention Gap
one_liner: 提出「惯例差」指标量化协作场景隐式沟通效率，可更准确评估AI与人协作的适配性
practical_value: '- 电商导购/客服Agent迭代时，可引入惯例差指标替代纯AI侧效果指标，更准确衡量人机协作效率

  - 推荐系统人机交互模块（如猜你想问、智能助手）可通过测量惯例差优化隐式需求理解精度，降低用户表达成本

  - 多Agent协作场景的评估框架可复用该指标设计思路，区分字面信息与隐式共识的贡献'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前合作AI多基于AI-AI基准评估，无法捕捉人类协作依赖的隐式共识（超越字面信息的共享协议），难以准确衡量AI与人协作的适配性。
### 方法关键点
提出「惯例差」指标，定义为基于通信字面内容预测的失败概率与实际观测失败率的差值，在Hanabi卡牌游戏场景中可精确计算；对10.1万条来自人-人、AI-AI、人-AI对局的操作数据做回测验证。
### 关键结果
人-人对局惯例差为+26.2pp，AI-AI仅为-0.7pp，人-AI为+16.4pp；无提示卡牌操作场景下人-人对局差达+46pp；人-AI对局中惯例差越大的AI搭档，人类操作失败率越低，该指标比游戏得分更能区分人机协作适配性；可控实验下Off-Belief Learning Agent的惯例差可从无共识场景的+1.6pp随共识增加单调升至+21.7pp。
