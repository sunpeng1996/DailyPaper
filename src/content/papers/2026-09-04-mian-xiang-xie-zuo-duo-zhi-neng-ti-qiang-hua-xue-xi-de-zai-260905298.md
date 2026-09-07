---
title: Online Change-point Detection for Cooperative Multi-Agent Reinforcement Learning
title_zh: 面向协作多智能体强化学习的在线变点检测算法
authors:
- Fatemeh Saberi Khomami
- Julita Vassileva
affiliations:
- University of Saskatchewan, Canada
arxiv_id: '2609.05298'
url: https://arxiv.org/abs/2609.05298
pdf_url: https://arxiv.org/pdf/2609.05298
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: 多智能体强化学习 · 非稳态变点检测
tags:
- MARL
- Change-point Detection
- Non-stationarity
- Online Drift Detection
- Reward Monitoring
one_liner: 提出轻量算法无关的PPR检测器，基于奖励信号识别协作MARL训练中的环境与任务漂移
practical_value: '- 电商多智能体协同场景（如直播间多Agent调度、搜推广多模块联动）可复用PPR的非侵入式监控思路，无需改造现有模型，直接监控业务回报（GMV、点击率、转化率）序列的漂移，精准触发策略更新

  - PPR的SMA平滑→EMV方差放大→KSWIN分布检验的信号处理pipeline可直接迁移到业务指标漂移检测场景，相比直接用原始指标漏检率降低60%+，相比仅用平滑指标误报率降低90%+

  - 设计Agent在线自适应系统时，可参考本文灵敏度-稳定性权衡逻辑，根据业务对误报、响应延迟的容忍度调整SMA窗口大小、EMV的β系数，适配不同场景需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
协作MARL已落地于仓储调度、流量分配、多角色Agent协同等场景，但现实环境天然非稳态：奖励规则、环境约束、智能体协作模式都可能动态变化，依赖历史经验训练的策略会快速失效。现有研究多聚焦漂移后的自适应策略，缺少轻量的前置漂移检测能力，无法精准判定策略更新时机：要么反应滞后导致业务效果下跌，要么过度频繁调整导致策略震荡。

### 方法关键点
- 提出PPR（Patterns of Past Rewards）检测pipeline，完全不侵入底层MARL算法，仅基于每轮episodic return信号处理，计算成本极低
- 第一阶段用SMA（简单滑动平均）平滑回报序列，过滤探索噪声、随机转移带来的短期波动
- 第二阶段用EMV（指数移动方差）转换平滑后的回报，放大突变信号、弱化渐变干扰，提升漂移辨识度
- 第三阶段用KSWIN滑动窗口KS检验，对比参考窗口与近期窗口的信号分布差异，输出漂移判定结果

### 关键实验
在自定义MPE Speaker-Listener双智能体协作环境下测试两类受控漂移场景（地标颜色映射变更、奖励函数目标变更），对比三个方案：
1. 原始回报+KSWIN：2/3的漂移完全漏检，仅1/3的检测延迟高达数千episode，几乎不可用
2. SMA平滑回报+KSWIN：检测延迟仅52~104 episode，但预漂移误报、重复报警高达300次左右，实用价值低
3. PPR：检测延迟250~262 episode，预漂移误报≤11次，重复报警≤11次，在速度和稳定性间取得最优平衡

### 核心结论
基于回报信号的漂移检测存在明确的灵敏度-稳定性权衡，轻量的两级信号转换可以在几乎不增加计算成本的前提下，实现工业场景可用的在线变点检测能力
