---
title: 'MoP-JEPA: Hard-Assigned Predictor Mixtures for Stochastic JEPA World Models'
title_zh: MoP-JEPA：基于硬分配预测器混合的随机JEPA世界模型
authors:
- Zhi Song
- Ximing Xing
- Zhenchao Tang
- hanbo Huang
- Tianxu Lv
- minghao Yang
- Zhongzheng Niu
- He Bing
- Lusheng Wang
- Jianhua Yao
affiliations:
- City University of Hong Kong
- Tencent
arxiv_id: '2607.05238'
url: https://arxiv.org/abs/2607.05238
pdf_url: https://arxiv.org/pdf/2607.05238
published: '2026-07-06'
collected: '2026-07-08'
category: Agent
direction: Agent世界模型 · JEPA随机分支预测
tags:
- JEPA
- World Model
- Stochastic Dynamics
- Hard Assignment
- Planning
one_liner: 针对JEPA世界模型在随机环境下的均值坍缩问题，提出硬分配多预测头实现分支模式枚举
practical_value: '- 遇到一对多回归场景（如用户多兴趣召回、广告多候选生成）可借鉴硬分配winner-take-all机制，避免均值坍缩产生无效中间结果

  - 多输出模型评估可复用论文的验证协议：引入上下文无关对照、乱序上下文测试、精度guard，避免coverage虚高

  - 多专家结构无需盲目加soft gating，硬分配加路由权重的设计在分支场景下可直接输出可枚举候选，适配下游搜索/规划逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有JEPA世界模型采用单确定性预测头做隐空间回归，在随机分支环境下存在结构性缺陷：回归最优解会输出后继隐状态的条件均值，落在多个真实状态之间的无效区域，即使采用门控MoE结构，加权求和后仍输出单向量，同样存在坍缩问题，导致下游规划完全失效。

### 方法关键点
- 替换单预测头为K个独立预测头，每个头输出一个候选后继隐状态，新增仅依赖上下文的路由模块输出各头的权重
- 采用硬分配训练机制：每个样本的目标隐状态仅分配给距离最近的预测头更新，其余头无梯度
- 损失函数由三部分组成：最优头的JEPA回归损失、路由预测最优头的交叉熵损失、预测头负载均衡的KL散度正则项
- 提出多预测模型验证协议：包括上下文无关码本对照、乱序上下文测试、路由门控输出、转移精度guard、验证路径准则，避免覆盖率注水

### 关键实验
在OGBench离线数据集上对比单头JEPA、门控MoE版M3-JEPA、变分Var-JEPA、混合密度网络MDN等基线：
1. 单头、门控MoE、变分JEPA的规划成功率仅0.02~0.09，MoP-JEPA最高达0.85
2. 验证路径指标下，MoP-JEPA在三类迷宫任务上比最强基线MDN高2~5倍
3. 真实环境执行上，MoP-JEPA在最难迷宫任务的7个公开基线中排名第二

**最值得记住的一句话**：一对多回归场景下，独立多专家不解决多样性问题，硬分配才是避免均值坍缩、得到可枚举有效分支的核心设计。
