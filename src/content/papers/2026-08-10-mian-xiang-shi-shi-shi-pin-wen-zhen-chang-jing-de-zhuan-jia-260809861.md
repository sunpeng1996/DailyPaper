---
title: Towards Expert-level Medical AI for Real-time Video Consultations
title_zh: 面向实时视频问诊场景的专家级医疗AI系统
authors:
- Mahvish Nagda
- Jihyeon Lee
- Matthew Thompson
- Chunjong Park
- Tim Strother
- Valentin Liévin
- Roma Ruparel
- Akshay Goel
- Teya Bergamaschi
- Suhana Bedi
affiliations:
- Google Research
- Google DeepMind
arxiv_id: '2608.09861'
url: https://arxiv.org/abs/2608.09861
pdf_url: https://arxiv.org/pdf/2608.09861
published: '2026-08-10'
collected: '2026-08-11'
category: MultiAgent
direction: 多Agent 实时音视频医疗交互
tags:
- Multi-Agent System
- Multimodal
- Real-time AI
- LLM
- Clinical AI
one_liner: 基于Gemini构建多Agent医疗系统AMIE(Video)，视频问诊实测达基层医师同等及以上诊疗水平
practical_value: '- 多Agent模块化架构可直接复用：将低延迟对话、领域推理、实时多模态感知拆分独立模块的设计，适配电商实时音视频导购、直播场智能客服等场景的Agent开发

  - 跨模态效果评估方法可迁移：通过模态消融对比不同交互形态（纯文本/音视频）的用户偏好、任务效果差异，指导产品交互方案选型

  - 领域定制化评估体系搭建思路可参考：先定义场景专属感知特征分类体系再落地自动化评测，可复用在直播内容审核、实时导购效果量化等场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文本医疗AI丢弃音视频非语言感知信息，无法覆盖无法用文字表述症状的用户，此前音视频医疗AI均未达到临床医师水平

### 方法关键点
1. 基于Gemini构建多Agent系统AMIE(Video)，融合低延迟对话、临床推理、实时音视频感知三大独立模块
2. 定义远程医疗场景下临床音视频提示词分类体系，配套搭建自动化评估框架指导模型迭代

### 关键结果
在30名基层医师、15名模拟患者、100个临床场景的随机OSCE测试中：
- AMIE(Video)在病史采集、诊断、处置、体格观察维度评分与医师相当或更优
- 模拟患者在沟通效率、便捷度、被理解感上更偏好视频版方案，仅在医患信任关系构建上医师更有优势
