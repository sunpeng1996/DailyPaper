---
title: 'MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing'
title_zh: 《MTEdit：基于打包轨迹的多轮图像编辑数据集与评测基准》
authors:
- Houyuan Chen
- Fanzhou Wang
- Xiangyu Fan
- Songlin Yang
- Zhitao Yang
- Lvmin Zhang
- Pei Yang
- Hao Zhao
- Lei Yang
- Anyi Rao
affiliations:
- SenseTime Research
- HKUST MMLab
- Stanford University
- AIR, Tsinghua University
arxiv_id: '2610.23751'
url: https://arxiv.org/abs/2610.23751
pdf_url: https://arxiv.org/pdf/2610.23751
published: '2026-10-15'
collected: '2026-10-20'
category: Multimodal
direction: 多模态生成 · 多轮图像编辑
tags:
- Multimodal Generation
- Multi-turn Editing
- Dataset Construction
- Benchmark
- LLM Fine-tuning
one_liner: 提出500K规模低漂移多轮图像编辑数据集MTEdit与配套基准，微调开源模型性能登顶
practical_value: '- 多轮交互类数据集构建可复用PTC范式，替代传统逐轮rollout方案降低状态漂移，适配电商多轮素材生成、Agent多步任务轨迹数据集构造场景

  - 多轮生成任务评测可参考MTEdit-Bench的维度设计，从指令遵从、上下文一致性、质量漂移抵抗三个核心维度评估，适配电商多轮文案/素材生成的评测需求

  - 多模态大模型微调时，采用高密度长轨迹多轮数据（单轨迹平均5.38轮）可有效提升长上下文交互能力，可迁移到电商智能美工Agent、导购Agent的微调'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多轮图像编辑训练数据多采用逐轮rollout生成，存在误差累积、跨轮视觉质量漂移问题，难以支撑人-AI协同创作类场景的多轮交互需求。
### 方法关键点
1. 提出打包轨迹画布（PTC）生成流水线，在统一视觉上下文内联合生成多轮编辑状态，大幅降低跨轮质量漂移；
2. 构建500K规模MTEdit多轮编辑数据集，覆盖分步编辑、上下文感知编辑两类场景，单轨迹最多8轮、平均5.38轮，为当前规模最大的多轮图像编辑数据集之一；
3. 配套MTEdit-Bench评测基准，从指令遵从、内容一致性、抗质量漂移、历史上下文利用4个维度评估模型能力；
4. 基于MTEdit微调Qwen-Image-Edit-Causal得到Qwen-Image-MTEdit模型。
### 关键结果
Qwen-Image-MTEdit在MTEdit-Bench上取得所有参评开源模型中的最优性能，验证了数据集的有效性。
