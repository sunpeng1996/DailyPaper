---
title: 'CogEvol: Towards Efficient and Reliable Learning Environment Generation'
title_zh: CogEvol：面向高效可靠的学习环境生成模型
authors:
- Shangqing Tu
- Daniel Zhang-Li
- Yucheng Wang
- Shiyu Gan
- Yanpeng Wang
- Huiqiang Rong
- Mofei Chen
- Shen Yang
- Yini Chen
- Yinuo Duan
affiliations:
- CogEvol Inc.
- Tsinghua University
arxiv_id: '2608.30968'
url: https://arxiv.org/abs/2608.30968
pdf_url: https://arxiv.org/pdf/2608.30968
published: '2026-08-30'
collected: '2026-09-02'
category: LLM
direction: 大模型生成优化 · 低成本训练推理
tags:
- SFT
- GRPO
- Reward Model
- LLM Generation
- Cost Optimization
one_liner: 提出CogEvol系列模型，单轮生成结构化课件/交互式HTML学习资源，兼具高可靠低时延低成本
practical_value: '- 可复用「生产故障回流SFT数据集」的迭代机制，将业务badcase直接转化为标注样本，快速提升生成类Agent的可靠性

  - 混合规则+VLM奖励驱动GRPO训练的范式可迁移到电商详情页、活动文案等多模态生成场景，有效规避奖励黑客问题

  - 轻量化微调+脚手架编辑的成本优化方案可直接复用，能将生成类任务推理成本降低70%以上，适配大流量生产场景

  - 国产昇腾芯片全栈适配优化经验可复用，在大流量生成类业务中大幅降低算力采购与运营成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多轮Agent生成学习资源时延高、输出可靠性差，同时头部大模型推理成本高昂，难以支撑大规模落地，亟需高可靠、低时延、低成本的单轮生成方案。
### 方法关键点
1. 搭建生产数据回流pipeline，将真实业务故障转化为53687条经过验证的SFT样本；
2. 采用规则+VLM混合奖励驱动GRPO RL训练，提前修复奖励黑客问题（视觉达标但功能失效的输出）；
3. 配套脚手架编辑机制，完成国产昇腾加速器全栈适配优化。
### 关键结果
22万生产请求中，课件生成中位时延17s、交互式HTML生成中位时延59s，替代原有分钟级多轮方案；CogEvol-27B参数仅为头部编码模型的1/26.9，课件质量得分83.7、500例HTML基准得分63.7；脚手架编辑进一步降低约76%生成成本，昇腾运行效果与A800 GPU持平。
