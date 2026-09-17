---
title: Single-Token Expected-Value Scoring for Cold-Start Candidate Ranking
title_zh: 面向冷启动候选排序的单Token期望分值方法
authors:
- Qihang Wang
- Jinwei Tan
- Mengyuan Shi
- Mayank Sharma
- Shuai Zhao
- Fuxian Li
- Ryan Yan
- Alexander P. Kreuzer
- Mohit Jain
- Dheeraj Toshniwal
affiliations:
- Indeed, Inc.
arxiv_id: '2609.18188'
url: https://arxiv.org/abs/2609.18188
pdf_url: https://arxiv.org/pdf/2609.18188
published: '2026-09-16'
collected: '2026-09-17'
category: RecSys
direction: 冷启动排序 · 小模型微调
tags:
- Cold-Start
- Ranking
- SLM
- Ordinal Regression
- Low-Latency
one_liner: 提出基于单Token期望打分的冷启动排序框架，仅需少量标注即可实现低延迟高准确率排序
practical_value: '- 冷启动排序场景可直接复用单Token期望打分方案：将排序目标转化为1-5分的序数分类，取首个token概率分布的期望作为分值，省去生成后解析步骤，大幅降低推理延迟，适配高吞吐在线服务

  - 少量标注场景下的SLM微调可采用MSE+交叉熵的混合序数回归损失：MSE保留序关系距离，交叉熵锐化类别边界，无需依赖海量用户交互日志即可完成模型适配

  - 电商冷启动新品/新商家/广告排序场景可直接迁移该范式：仅需十万级人工标注即可完成排序模型上线，大幅降低冷启动阶段的数据依赖'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
冷启动排序场景存在两大痛点：零样本LLM排序结果不稳定、准确率不足；传统深度排序模型依赖百万级交互日志，低流量细分场景无法满足，仅能获取十万级序数相关性标注
### 方法关键点
- 单Token期望打分范式：将候选-查询相关性转化为{1,2,3,4,5}的序数分类任务，取首个解码Token概率分布的数学期望作为排序分值，仅需单步解码，无需后解析，确定性高、延迟低
- 微调SLM采用MSE+分类交叉熵的混合序数回归损失：MSE保留序数间距离关系，交叉熵锐化类别边界，仅需标注数据即可学习异质性排序规则
### 关键结果
离线效果优于启发式基线与零样本LLM，端到端模拟实现求职者侧NDCG@10提升54.2%、低相关率下降46.7%；线上实验实现雇主侧低相关率下降27.3%、留存率提升7.07%
