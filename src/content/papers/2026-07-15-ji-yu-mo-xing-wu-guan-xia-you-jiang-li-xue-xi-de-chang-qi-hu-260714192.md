---
title: Long-term User Engagement Optimization through Model-agnostic Downstream Rewards
  Learning
title_zh: 基于模型无关下游奖励学习的长期用户参与度优化
authors:
- Dingsu Wang
- Filip Ryzner
- Kelly He
- Armando Ordorica
- David Woo
- Aditya Mantha
- Liyao Lu
- Usha Amrutha Nookala
- Haoran Guo
- Jiacong He
affiliations:
- Pinterest
arxiv_id: '2607.14192'
url: https://arxiv.org/abs/2607.14192
pdf_url: https://arxiv.org/pdf/2607.14192
published: '2026-07-15'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统 · 长期用户留存优化
tags:
- Long-term Retention
- Downstream Reward
- Ranking Optimization
- Industrial Recommendation
- Multi-surface Recommendation
one_liner: 提出模型无关的通用下游奖励框架，低 overhead 优化推荐系统长期用户留存与参与度
practical_value: '- 复用离线筛选代理指标的三准则（与长期留存相关、会话内可观测、多变量下仍有增量预测性）+ 用户流行度（UP）归一化方案，快速定位业务里的长期价值代理信号，避免盲试

  - 三类下游奖励可直接嵌入现有多任务排序模型作为新增head：深度会话折扣累积奖励、分用户群的浅度互动负惩罚、跨兴趣簇互动的新场景采纳奖励，无需重构现有架构

  - 照搬DRv2工程架构：存储用户每日结构化行为序列，在dataloader层用UDF按需计算奖励，无需预计算全量 reward 表，可将新 reward 迭代周期从数周压缩到2天

  - 多目标权重采用HyperOPT离线调优，和模型训练解耦，可快速找到即时指标不降、长期指标最优的权重组合，降低线上风险'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统多优化短期点击、曝光等即时信号，易引发反馈循环同质化，伤害用户长期留存；但直接优化留存面临标签稀疏、延迟高、归因难三大痛点，传统RL方案需定制化 reward 工程、计算开销大，难以跨场景复用，亟需低门槛、通用的长期价值优化方案。
### 方法关键点
- 离线信号筛选框架：基于三准则筛选候选会话级信号，采用用户流行度（UP）归一化消除曝光偏差，最终筛选出P2P深度探索、收藏、跨品类深度参与为核心正信号，浅度高容量浏览为噪声信号。
- 三类模型无关下游奖励设计：1）深度会话奖励：对推荐触发的后续会话内高价值动作（收藏、下载、截图）做折扣加权求和；2）负反馈奖励：分用户群设定浅点击阈值（核心用户1s、非核心0.5s），惩罚无后续高价值动作的短停留点击；3）新场景采纳奖励：用户对超出历史兴趣簇的内容产生有效互动时给予正奖励，鼓励兴趣拓展。
- 工程架构优化：DRv2存储用户每日结构化行为序列，在dataloader层通过UDF按需计算奖励，无需预计算全量 reward 表，迭代周期从3周降至2天。
### 关键结果
在Pinterest全场景线上A/B测试：Homefeed下三类奖励分别带来Successful Sessions +0.36%、+0.16%、+0.1%，总使用时长最高提升+0.46%，WAU最高+0.1%；扩展到Search、Related Pins、Notifications场景，分别实现搜索满足率+0.25%、Successful Sessions +0.15%、+0.14%的提升。

最值得记住的一句话：用户如何参与内容，比用户接触了多少内容，对长期留存的预测性更强。
