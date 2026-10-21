---
title: 'DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems'
title_zh: DecisionPivot：面向LLM系统决策模型的诊断基准
authors:
- Xialie Zhuang
- Mingcong Lei
- Zunhai Su
- Ri Liu
- Jianjin Li
- Peixian Ma
- Jia Pan
- Ngai Wong
- Guanhua Chen
- Chuan-Wei Kuo
affiliations:
- StartLux
arxiv_id: '2610.28522'
url: https://arxiv.org/abs/2610.28522
pdf_url: https://arxiv.org/pdf/2610.28522
published: '2026-10-19'
collected: '2026-10-21'
category: Eval
direction: LLM决策模型诊断评估基准
tags:
- Decision Model
- LLM Evaluation
- Benchmark
- Contrastive Testing
- Confidence Calibration
- Agent Decision Making
one_liner: 构建双轨对照诊断基准，细粒度评估LLM决策模型的正确性、鲁棒性与置信度可靠性
practical_value: '- 评估自研的LLM路由、内容审核、商品匹配、Agent目标校验等决策模块时，可引入对照样本（仅修改关键决策特征，其余上下文不变），避免仅用整体准确率掩盖细粒度缺陷

  - 部署置信度驱动的分级决策链路（如低置信走人工审核/多步推理）时，可参考论文的选择性覆盖、高置信准确率指标评估链路实际可用率，而非仅看整体准确率

  - 针对电商商品属性校验、营销规则匹配这类对关键参数敏感的决策场景，可参考核心轨的样本生成方法构造边界测试用例，提前发现阈值附近的决策错误

  - 多模型选型时不要仅看公开测试集的聚合得分，需补充业务场景相关的对照测试，避免选到泛化性差、依赖数据捷径的模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM系统决策模型（路由、护栏、输出校验、Agent目标判断等）的评估仅依赖聚合准确率，无法识别模型是否依赖数据捷径、能否稳定响应关键特征变化、置信度是否可靠，还易受训练集污染干扰，导致选型结果与上线实际表现差距显著。
### 方法关键点
- 双轨基准设计：核心轨含7800个自动生成、独立求解器校验的样本，覆盖13个任务族，构造仅修改关键决策特征的对照实验组，消除标注误差与训练污染；参考轨含32233个来自35个公开测试集的样本，兼容现有评估指标
- 多维度评估体系：除常规准确率外，新增要求对照组成员全部判断正确的Pair Accuracy、概率排序正确性、5%错误率下的选择性覆盖率、高置信准确率等指标，全面定位决策缺陷
- 覆盖7类核心决策场景：包含请求路由、风控护栏、输出校验、Agent目标校验、推理分类、数据对账、搜索匹配全链路决策角色
### 关键结果
- 测试40个决策模型后发现，公开测试集得分仅差2.6分的两个27B模型，对照组合格率分别为70.1%和44.2%，差距显著
- Perplexity Decider在2400个二分类对照对中概率排序正确率达92.3%，但仅74.1%的对照对两个样本都判断正确，暴露概率排序与实际决策正确性的gap
- GLM-5.3开启高推理模式后对照组合格率从81.5%提升至93.5%，但推理token量提升超1倍

仅看聚合准确率的决策模型评估存在严重盲区，针对关键特征扰动、置信度可靠性的细粒度诊断才能选出实际落地稳定的决策模型。
