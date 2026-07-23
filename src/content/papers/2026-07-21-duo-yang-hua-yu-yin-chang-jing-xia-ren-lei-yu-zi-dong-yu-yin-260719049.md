---
title: 'Benchmarking Human and Automatic Speech Recognition of Diverse Speech: Initial
  Results'
title_zh: 多样化语音场景下人类与自动语音识别性能基准测试初步结果
authors:
- Ilse Huisman
- Rares Popa
- Yuanyuan Zhang
- Odette Scharenborg
affiliations:
- Delft University of Technology
- Multimedia Computing Group
arxiv_id: '2607.19049'
url: https://arxiv.org/abs/2607.19049
pdf_url: https://arxiv.org/pdf/2607.19049
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 语音识别 · 人机性能基准测试
tags:
- ASR
- Speech Recognition
- Benchmark
- Human Performance
- Accent Robustness
one_liner: 对比SOTA ASR与荷兰本土听众的多样化语音识别能力，验证部分场景下ASR表现已超人类
practical_value: '- 电商语音客服、语音导购类Agent选型ASR能力时，可优先参考Google Telephony类SOTA方案，针对老人/儿童/方言口音场景做专项调优

  - 语音交互类业务设定效果基准时，无需默认将人类听力作为性能上限，可结合业务场景（口音、语句长度）定制合理阈值

  - 评估ASR落地效果时需规避测试集选择偏差，小范围抽样测试的结论不可直接泛化到全量业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
长期以来人类语音识别能力被视为ASR系统的性能上限，但现有研究缺乏针对不同年龄、地域口音等多样化语音场景的系统性人机性能对比。
### 方法关键点
选取多套SOTA ASR系统与荷兰本土听众为测试对象，针对荷兰儿童语音、老年人群语音、弗拉芒口音三类典型多样化语音做识别性能对比，同时验证测试子集与全量Jasmin-CGN测试集的结论差异。
### 关键结果
1. Google Telephony在所有参评ASR系统中表现最优
2. ASR整体表现与人类听众相当，特定场景下性能甚至超过人类
3. 人机性能差异与说话人年龄、地域口音、语句长度显著相关
4. 测试集选择偏差会显著影响人机性能对比的最终结论
