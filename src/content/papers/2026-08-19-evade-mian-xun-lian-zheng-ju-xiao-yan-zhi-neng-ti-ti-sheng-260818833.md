---
title: 'EVADE: Evidence-Verified Agentic Diagnosis with Escape'
title_zh: EVADE：免训练证据校验智能体，提升医疗VLM推理可靠性
authors:
- Mohaimenul Azam Khan Raiaan
- Nur Mohammad Fahad
affiliations:
- Monash University
- Murdoch University
arxiv_id: '2608.18833'
url: https://arxiv.org/abs/2608.18833
pdf_url: https://arxiv.org/pdf/2608.18833
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent 多模态推理可靠性优化
tags:
- Agentic Reasoning
- Vision-Language Model
- Calibration
- Selective Prediction
- Medical VQA
one_liner: 提出免训练跨视图一致性校验Agent框架，不损失精度下最多降低VLM预期校准误差45%
practical_value: '- 多模态商品属性校验场景可复用跨视角一致性校验逻辑：对同一个商品分别用全局图、细节放大图查询VLM属性，回答不一致直接触发人工复审，避免错误属性推荐引发客诉

  - LLM/多模态模型打分环节可直接复用置信度融合方法：将生成token的概率均值与模型输出的口头置信加权融合，无需微调即可缓解模型过自信问题，提升召回/排序的校准度

  - 推理成本管控可复用动态算力分配策略：简单样本直接返回结果，仅低置信度样本走多步校验流程，在生成式推荐、Query改写等场景平衡效果与推理成本

  - 避免单模型自校验的验证幻象：不要用同一份输入让模型校验自身输出，可通过改写Query、切分输入片段等方式改变输入视角再做一致性校验，大幅降低误报率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前医疗VLM存在三大顽疾：一是系统性过自信、校准能力差，模型缩放或CoT等常规Prompt策略均无法解决；二是测试时推理（如CoT）在医疗场景反而会降低精度、加剧过自信；三是单模型自校验存在「验证幻象」，同输入下模型容易同意自己的错误答案，无法有效检测幻觉。现有方案要么需要微调、依赖外部工具，要么没有围绕校准和弃权机制设计，无法在不损失精度的前提下提升可靠性。

### 方法关键点
- 完全免训练的推理侧Agent流程，仅依赖单个冻结VLM，无需外部工具或微调
- 置信度融合：将回答token的几何平均概率与模型输出的口头置信度加权融合，作为单视图回答的置信度
- 智能体视觉缩放：低置信度样本触发VLM自主定位最相关诊断区域，裁剪放大后重新回答
- 跨视图一致性校验门控：仅当全局图和放大区域图的回答一致且置信度达标时才输出，不一致时融合双视图再判断，最终仍不确定则弃权

### 关键实验
基于Qwen2.5-VL-7B在VQA-RAD、SLAKE、PathVQA三个医疗VQA数据集测试，对比零样本、CoT、自一致性、自校验、置信度阈值弃权等基线。EVADE是唯一同时提升校准、降低选择风险且保持精度的方法：相比零样本，ECE在VQA-RAD降23%、SLAKE降28%、PathVQA降45%；单样本平均仅需2.1-2.4次前向传播，远低于自一致性的5次。消融实验表明可靠性收益主要来自一致性门控和校准弃权，7B VLM还无法利用定位到的区域修改答案。

最值得记住的一句话：单模型自校验的验证幻象本质是同输入下的偏差耦合，通过改变输入视角（而非重复读取同一份输入或自身输出）做一致性校验，是免训练提升大模型可靠性的有效路径。
