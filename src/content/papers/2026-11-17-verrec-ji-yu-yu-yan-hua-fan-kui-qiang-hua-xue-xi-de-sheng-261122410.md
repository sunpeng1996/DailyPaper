---
title: 'More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative
  Recommendation'
title_zh: VerRec：基于语言化反馈强化学习的生成式推荐框架
authors:
- Zipeng Chen
- Xinyu Lin
- Yuliang Sun
- Sheng Zhang
- Zeyu Wang
- Xiaowen Shi
- Junwei Pan
- Chengguo Yin
affiliations:
- Tencent Inc.
- National University of Singapore
- The Chinese University of Hong Kong
arxiv_id: '2611.22410'
url: https://arxiv.org/abs/2611.22410
pdf_url: https://arxiv.org/pdf/2611.22410
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式推荐 · 语言化反馈RL优化
tags:
- Generative Recommendation
- Reinforcement Learning
- User Simulator
- GRPO
- Semantic ID
one_liner: 通过LLM用户模拟器生成个性化语言反馈，结合GRPO联合优化提升生成式推荐性能
practical_value: '- 生成式推荐RL训练阶段可快速复用该框架：仅需新增LLM用户模拟器生成个性化反馈，基于反馈做候选精炼后联合优化，在增加47%训练成本的前提下，推荐准确率、多样性均有明显提升，且不影响线上推理速度

  - 奖励设计可直接复用：采用「二进制命中奖励+排序感知负样本惩罚」的组合，解决纯二进制奖励对不同错误负样本区分度不足的问题，显著提升排序效果

  - 电商场景用户模拟器可直接复用其prompt模板：基于用户历史交互的正负评价、物品的公共评价生成高对齐度的语言反馈，无需额外标注数据即可落地

  - 针对RL训练中refine样本的概率偏移问题，可复用其Policy Shaping操作，稳定训练过程，避免分布偏移导致的训练波动'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的RL训练依赖标量奖励，仅能判断推荐结果好坏，无法揭示偏好错配、重复推荐等具体错误原因，导致策略需盲目试错，训练效率低、优化方向模糊，相同低奖励的不同问题无法得到针对性修正。
### 方法关键点
- 搭建LLM用户模拟器：输入用户历史交互的正负偏好总结、待评估物品的公共评价，输出包含评分+自然语言点评的个性化语言化反馈
- 候选扩增流程：先基于用户历史生成G个初始候选，再结合每个候选对应的反馈生成G个优化候选，组成2G大小的扩增样本组
- 联合优化策略：奖励采用「二进制正确性奖励+排序感知奖励」组合提升负样本区分度，基于GRPO做联合优化，对初始候选用CLIP操作稳定训练，对优化候选用Policy Shaping解决上下文概率偏移问题
- 推理轻量化：用户模拟器仅在训练阶段使用，推理阶段无额外开销，可直接嵌入现有GenRec流水线
### 关键结果
在Amazon的Book、Baby、Cell Phones三个数据集上，基于MiniOneRec、LETTER两个主流生成式推荐骨干测试，相比最优基线：Baby数据集H@10相对提升13%，Cell Phones数据集N@10相对提升6.7%；训练阶段奖励收敛速度是纯标量奖励RL的1.9倍，候选类别多样性提升60%。
### 核心洞察
语言化反馈为RL训练补充了显式可解释的优化方向，在仅增加少量训练成本的前提下大幅提升探索效率，且完全不影响线上推理性能。
