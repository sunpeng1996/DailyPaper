---
title: 'Ask About the Right Moment: Training-Free Object Identity Reasoning for Video-Language
  Models'
title_zh: 无需训练的视频语言模型对象身份推理方法：选对询问时机
authors:
- Di Yang
- Xiaochang Li
- Muyang Liu
- Yufei Wang
- Yanhai Xiong
affiliations:
- College of William & Mary
- SparcAI Inc.
arxiv_id: '2610.31471'
url: https://arxiv.org/abs/2610.31471
pdf_url: https://arxiv.org/pdf/2610.31471
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态推理 · 视频语言模型
tags:
- Video-LM
- Object Tracking
- Identity Reasoning
- Training-Free
- Multimodal Agent
one_liner: 无需训练的Track Then Bind框架拆分语义绑定与时序跟踪，大幅提升Video-LM物体时序身份推理性能
practical_value: '- 多模态内容理解场景可复用「先绑定明确时刻的语义ID，再跟踪时序状态」的框架，规避大模型跨时序推理幻觉，可落地到电商直播商品跟踪、短视频带货商品识别场景

  - 无需训练的工具组合架构可直接落地，用现成tracker+冻结VLM即可提升时序类多模态任务性能，节省微调成本

  - 长时序多模态Agent开发可拆分语义绑定和时序维护模块，避免大模型重复解读原始视频/长序列内容，降低推理成本同时提升准确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有Video-LM可准确识别单帧物体，但无法跨时序维持身份一致性，在贝壳游戏等时序身份推理任务上，8B到235B参数的开源模型、RL工具Agent性能均接近随机水平。

### 方法关键点
无训练的Track Then Bind框架拆分语义身份绑定与时序身份维护任务：
1. 用可提示的视频跟踪器跟踪所有候选物体并标注轨道号
2. 调用冻结VLM回答证据可见时刻的静态问题，将目标物体绑定到对应轨道
3. 直接从轨道文本化状态推导答案，无需VLM重新解读原始视频

### 关键结果
搭配Qwen3-VL-32B时，VET-Bench两任务精度达92%、90%，远高于同模型16样本投票的30~32%；Perception Test杯子游戏准确率55.4%，较SOTA提升13.9pp；TOC-Bench准确率48.6%，较同模型直接回答提升11.5pp；真实贝壳游戏上较直接标注轨道提问的方法高12~19pp。
