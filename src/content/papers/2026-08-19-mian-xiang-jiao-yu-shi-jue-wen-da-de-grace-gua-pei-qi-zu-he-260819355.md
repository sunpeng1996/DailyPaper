---
title: 'GRACE: Grounded Reasoning via Adapter Composition and Evidence-Aware Calibration
  for Educational Visual Question Answering'
title_zh: 面向教育视觉问答的GRACE：适配器组合与证据校准的接地推理框架
authors:
- Xinjin Li
- Yudi Xia
- Xi Zhao
- Yiliu Xu
- Yining Liu
- Cheng Lu
- Yujian Long
- Yu Ma
- Jinghan Cao
- Liang Fan
affiliations:
- Columbia University
- Carnegie Mellon University
- University of California, Berkeley
- Georgetown University
- Texas A&M University
arxiv_id: '2608.19355'
url: https://arxiv.org/abs/2608.19355
pdf_url: https://arxiv.org/pdf/2608.19355
published: '2026-08-19'
collected: '2026-08-21'
category: Multimodal
direction: 多模态大模型 · 高效适配与推理校准
tags:
- Multimodal LLM
- Parameter Efficient Fine-Tuning
- Adapter
- VQA
- Calibration
one_liner: 基于结构化教学状态路由，通过轻量适配器组合与证据校准提升冻结多模态大模型教育VQA效果
practical_value: '- 电商多模态场景（商品图问答、直播内容理解）可复用「结构化场景特征（类目、用户等级、意图等）作为路由信号，组合多维度轻量Adapter」的方案，无需全量微调即可快速适配垂类场景，降低适配成本

  - 多选类任务（搜索query意图匹配、广告候选打分、推荐结果排序）可借鉴证据感知校准逻辑，在共享上下文下统一打分，减少语义相近候选的误判

  - 冻结基座的高效适配思路可直接迁移至多模态Agent的场景感知模块，降低基座迭代后的业务迁移成本，提升迭代效率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
教育VQA需结合图文证据解决结构化选题，语义相近选项、图文混排内容易引发模型推理捷径，现有共享Adapter方案泛化性不足，全量微调多模态大模型成本极高。
### 方法关键点
1. 引入结构化教学状态（科目、技能点、年级、视觉上下文等6类可推理特征）作为路由信号；
2. 对冻结多模态基座采用因子特定Prompt+轻量视觉Adapter的参数高效适配方案；
3. 新增证据感知选项校准模块，在共享多模态上下文下统一给所有候选打分，减少语义相近候选的误判。
### 关键结果
在ScienceQA数据集上，整体准确率较共享Adapter基线从90.5%提升至93.1%，带图像上下文题目的准确率从88.7%提升至91.2%；消融实验显示移除教学状态组合、选项校准、视觉Adapter分别掉点1.4、1.0、1.5个百分点。
