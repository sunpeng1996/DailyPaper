---
title: 'MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with
  Deep Graph Reinforcement Learning'
title_zh: MPFlow：面向闪电网络的深度图强化学习预算最大流优化框架
authors:
- Harrison Rush
- Vincent Davis
- Simone Antonelli
- Vikash Singh
- Jesse Shrader
- Emanuele Rossi
affiliations:
- Amboss Technologies
- CISPA Helmholtz Center for Information Security
- Stillmark
- Sapienza University of Rome
arxiv_id: '2607.08703'
url: https://arxiv.org/abs/2607.08703
pdf_url: https://arxiv.org/pdf/2607.08703
published: '2026-07-09'
collected: '2026-07-12'
category: Agent
direction: 图强化学习Agent · 预算约束组合优化
tags:
- GraphRL
- PPO
- GNN
- CombinatorialOptimization
- ProductionDeployment
one_liner: 提出结合消息传递GNN与PPO的轻量Agent，解决图上预算约束最大流组合优化问题，已落地生产
practical_value: '- 图上预算约束选点/选边场景（如广告流量分配、达人种草选号、渠道开户）可复用「消息传递GNN+PPO+action masking」的轻量Agent架构，参数少易落地

  - 训练阶段引入hub-exclusion课程学习，可避免模型只拟合头部热门节点，提升长尾场景优化效果，适配流量冷启动、新用户冷启推荐等场景

  - 组合优化问题可拆解为序列决策MDP，单步奖励用边际收益替代全局收益，能大幅降低训练难度，提升收敛速度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
闪电网络流动性配置属于预算约束下的图组合优化问题：给定固定开户预算选择节点开通通道最大化路由容量，传统启发式方法泛化性差、优化上限低。
### 方法关键点
1. 将问题建模为序列决策MDP，单步奖励设为开通通道后的边际最大流增益；
2. 轻量Agent由2层消息传递GNN、actor-critic模块构成，结合PPO算法与action masking训练；
3. 训练阶段采用hub-exclusion课程学习，移除训练子图头部hub节点，强制模型学习容量感知选点策略，避免盲目绑定热门节点。
### 关键结果
真实闪电网络快照实验效果全面优于启发式基线；已上线生产用于节点开户推荐，累计执行4640次开户决策，分配267.3BTC（超1600万美元）覆盖30个托管节点。
