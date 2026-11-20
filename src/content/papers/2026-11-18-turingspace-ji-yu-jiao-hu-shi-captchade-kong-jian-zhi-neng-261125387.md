---
title: 'TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs'
title_zh: TuringSpace：基于交互式CAPTCHA的空间智能测评与训练框架
authors:
- Xuwei Ding
- Skylar Zhai
- Linxin Song
- Jiarui Feng
- Dongqi Fu
- Huajun Xi
- Junnan Li
- Jingcheng Liang
- Jieyu Zhao
- Yinglong Xia
affiliations:
- University of Pennsylvania
- University of Minnesota
- University of Southern California
- Meta
- MBZUAI
arxiv_id: '2611.25387'
url: https://arxiv.org/abs/2611.25387
pdf_url: https://arxiv.org/pdf/2611.25387
published: '2026-11-18'
collected: '2026-11-20'
category: Eval
direction: 多模态大模型 · 空间能力测评训练
tags:
- MLLM
- Spatial Intelligence
- CAPTCHA
- Benchmark
- Fine-tuning
- Embodied AI
one_liner: 提出覆盖5类空间能力的交互式CAPTCHA测评训练环境，可提升MLLM空间能力并迁移至真实场景
practical_value: '- 开发GUI交互Agent的团队可复用该交互式任务微调范式，提升模型对界面元素的空间推理、点击拖拽操作的准确率

  - 电商3D商品展示、虚拟试穿类交互Agent可借鉴该空间能力训练方法，优化对用户空间操作指令的响应效果

  - 构建业务场景模型评测基准时，可参考程序自动生成实例的方案，降低标注成本同时提升基准的泛化性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有CAPTCHA基准大多已被破解且极少涉及空间能力维度，现有空间能力基准普遍不要求动作交互，无法验证MLLM的空间感知-动作闭环能力。
### 方法关键点
构建TuringSpace合成Web环境，包含125种交互式CAPTCHA任务，覆盖5类空间能力，必须通过屏幕点击、拖拽操作完成；每个任务可程序化生成新实例，自带校验器与标准答案生成逻辑，可作为可扩展的训练gym。
### 关键结果
人类任务成功率达94.1%，GPT-6 Astra失败率为25.9%，开源最优模型Kimi K3失败率达68.0%；基于该gym微调Qwen3.5-9B，成功率从1.6%提升至33.1%，超过Kimi K3，7个OOD基准全部获得提升，其中真实室内视频数据集VSI-Bench上准确率提升9.9个百分点。
