---
title: Environment Evolution for Terminal Agents
title_zh: 面向终端Agent的环境演化训练范式
authors:
- Zhiyuan Fan
- Tinghao Yu
- Yuanjun Cai
- Jiang Zhou
- Jiangtao Guan
- Jincheng Liu
- Yun Yang
- Dingxin Hu
- Zhuo Han
- Xing Wu
affiliations:
- Hunyuan Team, Tencent
arxiv_id: '2609.04128'
url: https://arxiv.org/abs/2609.04128
pdf_url: https://arxiv.org/pdf/2609.04128
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent训练 · 环境自动演化
tags:
- Terminal Agent
- Reinforcement Learning
- Environment Evolution
- Off-policy
- Curriculum Learning
one_liner: 提出无需依赖目标Agent rollout的off-policy环境演化范式，持续生成递增难度训练环境提升终端Agent性能
practical_value: '- 电商/推荐Agent训练可直接复用场景新颖性、技能稀有度、执行长度三个难度维度，无需on-policy rollout即可自动生成难度递增的模拟交互任务，降低标注与真实环境交互成本

  - 双闭环多Agent难例生成框架可迁移到推荐系统的难负样本构造：Proposer生成难样本、Reviewer做规则校验、Verifier做有效性检查，自动扩充训练样本池提升排序模型鲁棒性

  - 演化谱系（EL）调度器可直接复用进推荐模型课程学习流程，按模型当前能力阈值逐步引入更难训练样本，避免过早接触过难样本浪费算力，提升训练效率

  - 环境演化思路可用于构建搜索推荐的仿真测试环境，自动生成用户行为/流量分布的演化场景，提前验证推荐策略在未知场景下的适配性'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有终端Agent RL训练环境普遍难度不足，无法为前沿模型提供有效学习信号；传统协同演化方法依赖on-policy rollout生成环境，泛化性差，随着模型能力提升无法持续输出学习信号，制约Agent能力上限。
### 方法关键点
- 从多轮学习目标推导模型无关的环境难度公式，拆解为场景新颖性、技能稀有度、执行长度三个可控演化维度，实现off-policy难度评估
- 设计双闭环多Agent框架实现环境演化：第一环完成演化方案规划与规则评审，第二环基于方案修改环境，依次通过可执行性、验证系统有效性、质量三类校验，确保生成环境可用
- 提出EL调度器，根据当前模型在当前代环境的通过率阈值，按顺序逐步引入更高代难环境，避免过难样本无有效学习信号的问题
### 关键结果
基于Qwen3.6-27B、Qwen3.6-35B-A3B做200步RL训练，对比环境集成、Agent-环境协同演化baseline，在Terminal-Bench 2.1上性能分别提升14.4、18.0个百分点，峰值准确率达71.5%、64.9%，较最优baseline分别高8.6、9.8个百分点。
> 最值得记住：Agent训练的瓶颈已经从算法转向训练环境的难度与多样性，off-policy环境自动演化是持续提升Agent能力的可扩展路径。
