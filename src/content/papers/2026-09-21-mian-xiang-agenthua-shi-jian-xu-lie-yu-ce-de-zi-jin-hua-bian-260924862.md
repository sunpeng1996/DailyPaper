---
title: 'When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series
  Forecasting'
title_zh: 面向Agent化时间序列预测的自进化编排策略框架TIMEVOLVE
authors:
- Yifan Hu
- Xilin Dai
- Zhiyuan Qu
- Yiding Liu
- Zewei Dong
- Jiang-ming Yang
- Qiang Xu
affiliations:
- Ant International
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2609.24862'
url: https://arxiv.org/abs/2609.24862
pdf_url: https://arxiv.org/pdf/2609.24862
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent时序预测 · 自进化编排策略
tags:
- Time Series Forecasting
- Agent Policy Evolution
- Delayed Feedback
- Online Learning
- Orchestration Policy
one_liner: 冻结底层预测组件，基于部署延迟反馈联合更新三类编排规则提升时序预测效果
practical_value: '- 电商销量、流量、库存等时序预测场景可直接复用predict-reveal-update延迟反馈范式，无需微调冻结的基础时序模型/LLM，仅更新轻量编排参数即可持续迭代效果，上线成本极低

  - 多模型融合场景可借鉴EvolveTrust的多维度权重计算逻辑，结合历史误差、当前数据特征、场景模式动态分配不同模型权重，替代固定融合规则适配分布漂移

  - LLM辅助业务决策场景可复用EvolveReason+EvolveIntervene组合：先通过可解释结构特征排序候选决策路径，再动态调整LLM推理结果对数值基线的修正幅度，降低幻觉风险

  - 策略冷启动阶段可复用warm-up权重+证据特征+动态ramp方案，上线初期无反馈数据时也能产出合理编排结果，随着反馈积累平滑过渡到自适应策略'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agent化时间序列预测系统仅通过反思、检索优化单次预测结果，未将部署后的真实观测值转化为持久的编排策略更新。随着时序分布漂移、模式切换，不同数值模型、推理策略、干预规则的有效性动态变化，静态编排规则无法充分发挥各组件的差异化优势，效果天花板明显。
### 方法关键点
- 设计时序合法的predict-reveal-update协议：预测前锁定所有专家输出、候选推理路径、决策链路结果，等待预测窗口真实值披露后，用天然生成的延迟标签更新策略，无额外标注成本
- 三个联动更新模块：EvolveTrust基于历史误差、当前证据、场景模式多维度动态计算数值专家权重生成基线预测；EvolveReason基于候选路径的连续性、平滑度等结构特征训练轻量排序模型，选择最优推理路径；EvolveIntervene动态学习当前路径对基线的修正幅度，平衡推理增益和幻觉风险
- 所有底层组件（数值预测模型、LLM、工具、Prompt）全程冻结，仅更新KB级别的编排参数，部署和迭代成本极低
### 关键实验
在8个Time-MMD多域时序数据集上，和15个基线（含KairosAgent、MemCast等Agent系统，Chronos-2、TimesFM-3等零样本时序基础模型，PatchTST等全监督时序模型）对比，TIMEVOLVE平均MSE/MAE排名为1.25/1.375，位列所有方法第一，7个域上双指标最优；相比固定编排策略的基线版本，平均MSE下降6.3%、MAE下降7.6%，其中经济域MSE下降17.7%，公益域MAE下降25%。
### 核心结论
在动态时序场景下，迭代轻量编排策略的投入产出比，远高于替换或微调单个底层预测模型。
