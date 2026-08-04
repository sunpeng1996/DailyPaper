---
title: Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch
title_zh: 基于代理增强自主研究的智能体贝叶斯优化框架
authors:
- Paul Brunzema
- Louis Tiao
- Nhat Le
- Kevin De Angeli
- Yao Xuan
- Djordje Gligorijevic
affiliations:
- Meta
- RWTH Aachen University
arxiv_id: '2608.00316'
url: https://arxiv.org/abs/2608.00316
pdf_url: https://arxiv.org/pdf/2608.00316
published: '2026-07-31'
collected: '2026-08-04'
category: Agent
direction: Agent 驱动贝叶斯优化自适应调优
tags:
- Bayesian Optimization
- LLM Agent
- Hyperparameter Tuning
- Surrogate Model
- Autoresearch
one_liner: 提出LLM智能体主导贝叶斯优化循环的框架，兼顾BO可靠性与LLM先验利用、自适应能力
practical_value: '- 推荐/广告系统的超参数调优（如排序模型的lr、正则系数，流量分配权重）可复用该架构：把BO后端封装为工具给LLM Agent调用，既利用LLM接收自然语言业务先验的能力（如大促前指令调高探索权重），又保留BO的样本效率，避免纯LLM调优的不稳定

  - 动态业务场景（如电商库存约束调整、广告出价规则变更）可借鉴自适应重配置逻辑：Agent可根据实时业务信号自动调整优化目标、约束边界、探索策略，无需人工重写优化逻辑，响应速度大幅提升

  - LLM Agent工具调用设计可复用：将专业计算模块（BO引擎、A/B测试统计模块、召回排序引擎）封装为简单CLI/API，通过系统prompt要求Agent优先调用工具做精确计算，避免纯LLM直接输出的校准误差，同时保留Agent决策控制权'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统贝叶斯优化（BO）策略预定义后固定，难以编码自然语言形式的领域先验；现有LLM+BO方法要么将LLM限定为固定组件，要么完全替换BO丢弃不确定性支撑，样本效率低、可靠性差，无法适配动态变化的优化需求。

### 方法关键点
- 提出智能体BO范式：LLM Agent作为BO循环核心决策者，贝叶斯后端提供不确定性感知的优化基底，两者分工互补
- 实现Sara智能体+lenz BO后端：lenz基于BoTorch开发，暴露CLI接口支持**探测**（获取surrogate诊断、预测结果）、**重配置**（调整搜索边界、acquisition函数、目标/约束）、**候选生成**三类操作，所有历史评估数据独立存储，重配置不会失效
- Sara的系统prompt明确行为规则：要求其主导优化决策，每轮评估前先推理，根据先验选择初始化策略，优先调用lenz完成精确计算，避免直接输出不可靠的候选解

### 关键结果
实验覆盖合成BO基准、LCBench超参调优、化学反应产率优化三类场景，对比Ax（SOTA BO）、LLAMBO（纯LLM优化）、Centaur（CMA-ES+LLM混合）等基线：
1. 无先验场景下，Sara与Ax性能持平，简单regret比LLAMBO、Centaur低30%以上
2. 有自然语言先验的化学反应优化场景，Sara收敛速度比Ax快40%，最终产率比LLAMBO高15~25pp
3. 动态需求场景下，Sara可在1轮迭代内完成优化目标重配置（如把算力从约束升级为第二优化目标），无需重启或丢弃历史数据

### 核心结论
LLM Agent做优化的最优范式不是替代专业计算引擎，而是作为决策中枢调用专业工具，兼顾语义先验利用、自适应能力和专业计算的可靠性、样本效率。
