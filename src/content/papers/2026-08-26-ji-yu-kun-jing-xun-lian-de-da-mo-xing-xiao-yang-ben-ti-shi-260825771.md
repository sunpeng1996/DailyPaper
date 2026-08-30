---
title: Large Language Model Few-Shot Prompting with Dilemma Training Outperforms Human
  Surrogates in Predicting Patient Preferences
title_zh: 基于困境训练的大模型小样本提示预测患者偏好优于人类代理人
authors:
- Natasha Ureyang
- Sebastian Porsdam Mann
- Yuxin Liu
- Zuriel Hassirim
- Melanie Almonte
- Wenhao Chen
- Joyce Ng
- Thant Nay Lin
- Aung Thiha
- Gerald CH Koh
affiliations:
- National University of Singapore
- University of Copenhagen
- Imperial College London
arxiv_id: '2608.25771'
url: https://arxiv.org/abs/2608.25771
pdf_url: https://arxiv.org/pdf/2608.25771
published: '2026-08-26'
collected: '2026-08-30'
category: Agent
direction: Agent 个性化偏好预测
tags:
- LLM
- Agent
- Preference-Prediction
- Few-shot-Prompting
- Context-Aware
one_liner: 提出融合困境训练的个性化偏好预测Agent P4-DT 医疗场景偏好预测准确率显著超越人类代理人
practical_value: '- 做用户个性化偏好建模时，可替换静态问卷/标签为「两难场景问答」的双向交互方式，获取更贴近真实决策的用户偏好，提升偏好预测准确率

  - 小样本prompt设计时，融合用户上下文决策行为和开放式回复文本，可比仅用静态属性打分提升15pct左右的预测效果，可迁移到用户意愿预测、个性化推荐场景

  - 偏好预测Agent训练可参考困境训练范式，通过多样化场景决策任务拟合用户决策逻辑，而非仅拟合静态标签，适合高风险决策类推荐（如金融、大额消费）'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
重疾场景下人类代理预测患者治疗偏好准确率仅约68%，过往个性化偏好预测Agent将用户价值观视为静态评分，忽略决策的上下文依赖性，易产生决策冲突。
### 方法关键点
提出基于「关怀逻辑」的P4-DT Agent，通过向用户推送多样化医疗两难场景完成双向训练，引导用户输出个性化偏好推理逻辑，构建用户专属决策策略；小样本prompt融合上下文场景决策数据与用户开放式文本回复。
### 关键结果数字
12组患者-代理配对实验中，P4-DT预测患者治疗选择准确率达81.7%，显著优于无辅助人类代理的55.0%、有P4-DT辅助人类代理的61.7%；相比仅用静态值评分的方案，准确率提升15.0个百分点。
