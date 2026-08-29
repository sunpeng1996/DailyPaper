---
title: 'Cultural Moment Benchmark: Evaluating Video Cultural Reasoning and Grounding
  in Southeast Asia'
title_zh: 面向东南亚视频文化推理与定位的文化时刻基准（CMB）
authors:
- Burak Satar
- Zhixin Ma
- Cheng Yu-Tong
- Huy Hoang Tran
- Phuong Anh Nguyen
- Chong-Wah Ngo
affiliations:
- Singapore Management University
- UIT, VNU-HCM
arxiv_id: '2608.23065'
url: https://arxiv.org/abs/2608.23065
pdf_url: https://arxiv.org/pdf/2608.23065
published: '2026-08-24'
collected: '2026-08-29'
category: Eval
direction: 多模态文化理解 · 评测基准构建
tags:
- Multimodal
- Cultural Reasoning
- Benchmark
- Vision-Language
- Evaluation
one_liner: 构建分三阶段评估视频文化理解能力的东南亚多国基准，可精准定位模型能力瓶颈
practical_value: '- 做东南亚跨境内容/电商推荐时，需针对不同国家单独构建文化知识数据集，不要复用泛东南亚统一模型，邻国文化知识适配度极低

  - 多模态内容理解任务的评测可复用「能力分阶段拆解+语义相似干扰项」的设计，精准定位模型短板而非仅输出单一总分

  - 东南亚非拉丁字母国家的视频内容理解任务可优先测试去音频的效果，避免音频带来的不必要干扰'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频文化理解基准将符号识别、视觉匹配、时序定位三类能力打包评测，无法定位模型瓶颈，且缺乏东南亚细分国家的文化专项数据集。
### 方法关键点
构建CMB基准，覆盖东南亚7国5大类共306个专家标注文化概念，分三阶段独立评测：S1选择对应文化概念名、S2选择匹配视频片段、S3预测片段起止时间；引入语义相似干扰项、无标注视频片段、跨样本自由定位设计，保证各阶段评测的能力独立性。
### 关键结果数字
最强闭源多模态模型三阶段全对准确率<30%；三类能力无完全级联效应，视觉识别正确对时序定位无明显帮助；非拉丁字母国家场景中音频更多为干扰项，去掉音字幕对游戏、音乐类内容的理解效果影响最大；邻国专家对本地文化概念的答题正确率低于随机水平。
