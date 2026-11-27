---
title: 'What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot
  Time-Series Models'
title_zh: 零样本时序预测榜单分辨率度量方法及Vernier工具
authors:
- Arya Sikder
- Sriram Pillutla
arxiv_id: '2611.31619'
url: https://arxiv.org/abs/2611.31619
pdf_url: https://arxiv.org/pdf/2611.31619
published: '2026-11-22'
collected: '2026-11-27'
category: Eval
direction: 时序大模型 · 榜单评估
tags:
- Time-Series-Forecasting
- Leaderboard-Evaluation
- Zero-Shot
- Foundation-Model
- Evaluation-Metric
one_liner: 提出时序预测榜单分辨率度量指标，推出Vernier工具量化榜单排名可信度
practical_value: '- 业务端做销量/流量等时序预测模型选型时，不要盲目采信榜单排名，需先计算榜单分辨率，低于分辨率的排名差无参考价值

  - 内部搭建时序模型评估榜单时，可引入分辨率指标，通过提升独立测试样本量降低分辨率，避免无效排名波动

  - 零样本时序大模型落地时必须对齐输入历史长度变量，历史长度缩短可能导致最高15%的误差上升，需匹配业务实际可用历史长度测试'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
零样本时序大模型评估高度依赖公开榜单，但现有榜单均未披露可检测的最小性能差（分辨率），排名可信度无法校验，也未对齐输入历史长度等关键变量。

### 方法关键点
1. 定义榜单分辨率为榜单可稳定检测的最小性能差异，开发Vernier工具可基于现有榜单已发布的数据集级分数直接计算分辨率；
2. 支持识别与榜首性能无统计学差异的模型条目，可判断排名是否受其他无关提交的影响，兼容依赖提交池/独立排名两类榜单规则。

### 关键结果
GIFT-Eval等4个主流时序榜单分辨率是相邻排名性能差的3.6~19倍，TOP10排名中可区分的步长不足2个，仅BOOM榜单因2554条独立时序可完整区分TOP10；依赖提交池的排名规则每7次更新就有43对TOP10排名在模型未重跑的情况下反转；输入历史缩短会导致3/4开源时序模型误差上升，最高达15%。
