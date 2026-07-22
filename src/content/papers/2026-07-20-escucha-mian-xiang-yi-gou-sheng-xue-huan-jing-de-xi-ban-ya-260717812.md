---
title: 'ESCUCHA: A Spanish Speech Benchmark for Heterogeneous Acoustic Conditions'
title_zh: ESCUCHA：面向异构声学环境的西班牙语语音评测基准
authors:
- Fernando López
- Ana Ayala
- Guillermo Segovia
- Fernando Ibáñez
- Ana Martínez
- Pablo Gómez
- Jordi Luque
affiliations:
- Telefónica Innovación Digital
- Universidad Autónoma de Madrid
- Universidad Complutense de Madrid
arxiv_id: '2607.17812'
url: https://arxiv.org/abs/2607.17812
pdf_url: https://arxiv.org/pdf/2607.17812
published: '2026-07-20'
collected: '2026-07-22'
category: Eval
direction: 大音频模型 · 西班牙语语音评测基准
tags:
- Speech Benchmark
- Large Audio Language Model
- Multimodal Evaluation
- Spanish Speech
- Acoustic Robustness
one_liner: 首个面向异构声学环境的西班牙语语音理解基准，覆盖多口音与多类推理评测任务
practical_value: '- 布局西语区语音搜索、语音导购、智能客服等业务时，可参考该基准的真实场景声学数据构建逻辑，覆盖多口音、嘈杂环境等真实case，提升语音理解模块鲁棒性

  - 评测语音大模型在业务场景的表现时，可复用其「感知层+推理层」双层任务设计框架，兼顾基础识别准确率和复杂业务场景的理解需求

  - 业务涉及开放域语音问答（如西语用户语音咨询商品信息）时，可参考该基准的开放式问答标注规则，优化业务效果评测指标设计'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
大音频语言模型（LALMs）迭代速度快，但真实异构声学环境下的西班牙语语音理解评测资源严重匮乏，缺乏覆盖复杂推理能力的标准化基准。
### 方法关键点
1. 采集162.9小时真实场景（非现有数据集二次采样）语音数据，覆盖数秒到80分钟时长，配对1000条人工标注的问答对
2. 任务覆盖9类感知任务、10类推理任务，纳入多西班牙口音、非规范语音，同时支持多音频问答、口语提问、音频指令等多种任务形式，标注支持开放式评测的样本
### 关键结果
对多个SOTA多模态/语音模型的基准测试显示，现有模型性能与经过训练的人类水平存在显著差距。
