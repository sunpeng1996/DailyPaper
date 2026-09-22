---
title: 'CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning'
title_zh: CTRL：基于LLM引导残差学习的可控时间序列预测框架
authors:
- Minkyoung Kim
- Daeun Ji
- Yohan Lee
- Beomsoo Kim
- Beakcheol Jang
affiliations:
- Yonsei University
arxiv_id: '2609.23257'
url: https://arxiv.org/abs/2609.23257
pdf_url: https://arxiv.org/pdf/2609.23257
published: '2026-09-20'
collected: '2026-09-22'
category: MultiAgent
direction: 多智体时序预测 · 无标注自适应
tags:
- Time-Series-Forecasting
- LLM-Agent
- Residual-Learning
- Test-Time-Adaptation
- STL-Decomposition
one_liner: 将LLM作为多智体控制器生成控制信号修正时序主干误差，仅3-24次调用提升非平稳场景预测精度
practical_value: '- 电商销量、流量、广告CTR等非平稳时序预测场景，可直接复用「冻住现有主干模型+LLM Agent生成控制信号+轻量残差解码器修正」架构，无需微调LLM，部署成本极低，精度提升明显

  - 线上分布漂移场景可复用其无标注测试时自适应方案：缓存历史STL统计量，通过Z-score检测漂移后仅调用少量LLM更新对应分量的控制信号，无需重训主干模型

  - 多Agent分工设计可迁移到各类预测任务：按任务可拆分的特征维度（比如时序的趋势/周期/噪声，推荐的用户/物品/上下文）拆分专门Agent，每个仅输出语义明确的低维控制信号，大幅降低LLM推理难度和出错概率

  - 推荐系统长周期用户留存、复购预测团队，可直接把现有预测模型作为冻住的主干，加一层CTRL的修正模块，无侵入式提升非平稳场景的预测精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM-based时序预测方案存在两个核心缺陷：要么将LLM降格为纯数值预测器，浪费其语义推理与泛化能力；要么直接输出预测结果，在非平稳、分布漂移场景下稳定性差、噪声大。而电商、广告、推荐等业务的核心时序数据（销量、流量、CTR、用户活跃度）普遍存在非平稳、周期性波动、突发漂移的特性，现有方案要么精度不足，要么需要大量LLM调用/微调，部署成本过高。

### 方法关键点
- 架构解耦：冻住的时序预测主干（DLinear、PatchTST等）生成基础预测结果，3个专门化LLM Agent（趋势、季节、不规则）作为控制器，无需微调LLM，仅输出低维控制信号
- 控制信号生成：对主干的预测误差做STL时序分解，每个Agent对应分析一个分量的误差模式：趋势/季节Agent输出[scale, bias, gate, confidence]4维语义明确的控制信号，不规则Agent输出自然语言分析后通过冻住的GPT-2编码为向量
- 轻量残差解码器：仅约400K参数，接收拼接的控制信号生成修正量，叠加到基础预测结果上，是唯一需要训练的模块
- 无标注测试时自适应：缓存训练集的STL统计特征，测试时通过Z-score检测分布漂移，仅需最多3次额外LLM调用即可更新对应分量的控制信号，无需ground truth或重训

### 关键结果
在ETT、Weather、ECL、Exchange等7个公开时序基准上测试，对比TimeLLM、CALF、TEMPO等SOTA方案：非平稳数据集（如ETTh2、ETTm2）最高实现12%的MSE降低；比直接用GPT-4做逐样本预测的LLMTime方案，MSE最高降低44.3%；全流程仅需3-24次LLM调用，比逐样本调用的方案降低1000倍以上的调用成本。

最值得记住的一句话：LLM用于时序预测的核心价值是语义推理而非数值计算，作为控制器生成高层指导信号的投入产出比远高于直接做数值生成。
