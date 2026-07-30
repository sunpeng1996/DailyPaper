---
title: 'Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online
  Advertising'
title_zh: 面向在线广告的决策感知用户模拟器：超越单一行为模仿
authors:
- Zipeng Chen
- Jiaer Zheng
- Xiangyang Xu
- Xinyu Lin
- Zhaobin Wang
- Zhaohui Liu
- Qianjin Xiang
- Xiaoyu Zhao
- Zhuozhen Yu
- Guangshuo Wang
affiliations:
- Tencent Inc.
- National University of Singapore
arxiv_id: '2607.26893'
url: https://arxiv.org/abs/2607.26893
pdf_url: https://arxiv.org/pdf/2607.26893
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 推荐系统 · LLM用户行为仿真
tags:
- User Simulator
- LLM4Rec
- Online Advertising
- RLHF
- Context Compression
one_liner: 基于跨域行为的三阶段框架，联合生成用户决策轨迹与行为，提升广告仿真保真度与诊断性
practical_value: '- 跨域用户行为压缩技巧可直接复用：低信息行为（如skip）仅保留类目，高信息行为（点击/转化/负反馈）保留全属性，再分域分配context配额，大幅降低长序列推理成本同时保留核心信号

  - 小模型蒸馏用户模拟器的SFT+RL范式可迁移：用大模型生成思考轨迹做SFT，再用rubric-based多维度奖励（形式/内容/逻辑+行为准确度）做GRPO训练，35B小模型效果超过通用397B大模型，兼顾性能和推理成本

  - 仿真评估的双维度指标可直接用于业务离线评测：除常规行为预测F1外，新增思考路径的形式/内容/逻辑打分，仿真结果不仅能测策略效果还能定位失败原因，可用于新广告/推荐策略的预筛，降低线上A/B测试成本

  - 闭环prompt优化方法可迁移到所有LLM落地场景：基于错误case自动迭代prompt，能显著提升事实一致性和行为分布对齐度，减少人工调prompt成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM用户模拟器多基于单域行为、仅预测点击/转化等显性动作，存在偏好建模不全、模型易走捷径（过拟合特定动作）问题，仿真保真度低，且无法输出决策原因无诊断价值；而线上A/B测试广告策略成本高、易伤害用户体验，急需高保真带诊断能力的离线用户模拟器。

### 方法关键点
- 阶段1 Context Engineering：分层压缩跨域用户行为，item层按动作价值分配保留粒度，stream层给用户画像/广告历史/内容历史分别分配5K/20K/7K配额，总context控制在32K；再通过闭环自动优化prompt，引导模型按focus-draft-verify-finalize步骤推理，减少幻觉
- 阶段2 SFT：用397B大模型做教师，生成匹配真实行为的思考轨迹，错判样本注入真实行为后重生成做hard sample，再用评审LLM过滤低质量轨迹，仅用4K高质量样本蒸馏35B学生模型
- 阶段3 RL：设计混合奖励，行为正确得1分，思考质量按形式/内容/逻辑多维度rubric打分，用GRPO算法训练，兼顾行为准确率和思考路径合理性

### 关键结果数字
基于腾讯5域跨域真实广告数据测试，DASH（35B小模型）的加权F1达62.15%，比最优通用大模型Qwen3.5-397B高2.6个百分点，思考质量得分92.01，也超过所有通用大模型；消融实验显示去掉Context Engineering后F1下降10.22个点，是影响最大的组件；仅用4K SFT样本加RL的效果比12K SFT样本更好，训练成本降低70%。

用户仿真的核心不是模仿行为，而是还原决策逻辑，小模型通过针对性蒸馏和RL对齐，完全可以在垂直场景超过通用大模型的效果，同时满足工业级 latency 要求。
