---
title: 'Beyond Information Seeking: Severity-Aware Question Supervision for Proactive
  Medical Dialogue'
title_zh: 超越信息检索：面向主动医疗对话的严重度感知问题监督方法
authors:
- Chenxuan Li
- Xinrong Chen
- Luyan Zhang
- Peidong Jia
- Zhongyu Zhao
- Xuecheng Shang
- Peixing Wan
affiliations:
- Peking University
- Northeastern University, Boston
arxiv_id: '2608.24521'
url: https://arxiv.org/abs/2608.24521
pdf_url: https://arxiv.org/pdf/2608.24521
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 主动交互决策优化
tags:
- Proactive Dialogue
- Risk-Aware Optimization
- Knowledge Distillation
- LoRA
- Medical Agent
one_liner: 提出严重度感知的ESR问诊目标，蒸馏训练后将医疗对话重症漏诊率降低29.5%
practical_value: '- 风险不对称业务场景可直接复用ESR框架逻辑：比如电商高退货率品类推荐、广告高价值转化场景，将决策损失权重引入用户信息采集/query询问策略，替代仅优化信息增益的传统方案

  - 离线复杂策略可通过蒸馏转换为轻量前缀策略：部署时无需调用教师侧的风险计算、答案预测模块，仅靠对话前缀即可实时输出决策，大幅降低推理成本，适合高并发Agent交互场景

  - 未知用户反馈的决策排序可复用人群统计边际化方案：训练阶段用历史人群的答案分布模拟未观测的用户反馈，无需实时用户回答即可完成最优决策排序，适合冷启动交互策略设计'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有主动交互Agent多基于信息增益选择采集的信息，优先降低决策不确定性，但忽略了高风险场景的错误后果不对称性——漏诊重症等严重错误的代价远高于普通决策误差，需要同时考虑证据的信息价值和对下游决策的风险影响。
### 方法关键点
- 设计ESR（Expected-Severity-Risk）目标函数：为每类决策结果分配严重度权重，量化每个候选信息采集动作预期降低的严重度加权终端决策风险
- 训练阶段用历史人群的答案统计分布，边际化未观测的用户回答，无需实时用户反馈即可完成候选动作的价值排序
- 将ESR排序结果作为监督信号，用LoRA微调Qwen3-4B得到轻量前缀策略，部署时无需调用教师侧的复杂计算模块，仅根据对话前缀即可输出最优动作
### 关键结果
在DDxPlus医疗诊断数据集子集上训练，对比基于信息增益的E-ENTROPY基线：三个随机种子下，ESR将高重症漏诊率从0.0645降至0.0455（降幅29.5%），诊断准确率从0.9123提升至0.9320，单轮对话仅增加0.14个提问；固定提问预算的实验显示，提问数超过10轮时ESR的重症漏诊优势更显著。

高风险决策场景下，信息增益最大的证据不一定是决策价值最高的证据，引入不对称后果权重能在几乎不增加交互成本的前提下大幅优化核心风险指标
