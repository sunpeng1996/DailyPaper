---
title: 'EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models'
title_zh: EvoWorld：面向生成式视频模型的视野外世界演化
authors:
- Yequan Bie
- Dengyang Jiang
- Zhixuan Chen
- Xiaozhuan Liang
- Haoxuan Che
- Quande Liu
- Xi Chen
- Hao Chen
affiliations:
- The Hong Kong University of Science and Technology
- Tencent
- The Chinese University of Hong Kong
arxiv_id: '2611.06748'
url: https://arxiv.org/abs/2611.06748
pdf_url: https://arxiv.org/pdf/2611.06748
published: '2026-11-04'
collected: '2026-11-09'
category: Multimodal
direction: 多模态生成 · 世界模型因果演化
tags:
- Generative Video
- World Model
- Causal Reasoning
- Vision-Language Model
- Video Diffusion
one_liner: 提出脑-渲染器协作的EvoWorld框架，解决生成视频视野外因果演化逻辑不一致问题
practical_value: '- 开发仿真环境交互Agent时，可复用「推理大脑+渲染器解耦」架构，用多模态大模型维护世界状态、做因果推理，降低交互逻辑矛盾

  - 生成电商商品动态展示视频、虚拟主播场景内容时，可借鉴显式世界状态维护设计，避免多轮生成的前后因果不一致问题

  - 长序列多轮生成任务可参考分段自回归生成+状态校验的模式，平衡生成视觉质量与逻辑一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有生成视频模型仅擅长输出视觉合理的像素，缺乏显式世界状态维护与事件因果推理机制，常生成视觉可信但行为静态、因果矛盾的内容，无法支撑视野外的世界演化仿真需求。

### 方法关键点
1. 定义Out-of-Sight Causal Evolution新问题，要求模型即使在对象移出视野后仍能推理事件因果影响，生成逻辑自洽的演化结果
2. 推出脑-渲染器协作的EvoWorld框架：用Vision-Language Model作为世界大脑，观察已生成片段、维护动态世界状态、推理合理状态转移；用分段自回归视频渲染器完成可视化输出
3. 配套发布EvoWorld-Data训练集与EvoWorld-Bench评测集，覆盖事件实现、因果反应、重访一致性三个核心评测维度

### 关键结果
相比同期SOTA生成视频模型，EvoWorld在事件条件因果演化指标上实现大幅提升，同时完全保留原有视觉质量与时空一致性表现
